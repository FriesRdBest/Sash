"""Unit tests for event and webhook engine."""

import hashlib
import hmac
import json

import pytest

from src.events import engine
from src.events.engine import (
    DeadLetterEntry,
    check_idempotency,
    check_ordering,
    get_dead_letters,
    move_to_dead_letter,
    normalize_event,
    process_webhook,
    replay_dead_letter,
    simulate_failed_event,
    validate_webhook_payload,
    verify_signature,
)
from src.events.errors import (
    DuplicateEventError,
    InvalidPayloadError,
    OutOfOrderEventError,
    SignatureValidationError,
)


class TestValidateWebhookPayload:
    def test_valid_payload(self):
        payload = {
            "event_id": "evt-123",
            "event_type": "message.sent",
            "correlation_id": "corr-abc",
            "timestamp": "2026-10-09T01:00:00Z",
        }
        validate_webhook_payload(payload)  # should not raise

    def test_missing_field(self):
        payload = {"event_id": "evt-123"}
        with pytest.raises(InvalidPayloadError):
            validate_webhook_payload(payload)

    def test_invalid_timestamp(self):
        payload = {
            "event_id": "evt-123",
            "event_type": "message.sent",
            "correlation_id": "corr-abc",
            "timestamp": 12345,
        }
        with pytest.raises(InvalidPayloadError):
            validate_webhook_payload(payload)


class TestVerifySignature:
    def test_valid_signature(self):
        payload = {"event_id": "evt-123"}
        payload_bytes = json.dumps(payload, sort_keys=True).encode()
        secret = "test-secret"
        signature = hmac.new(secret.encode(), payload_bytes, hashlib.sha256).hexdigest()
        assert verify_signature(payload_bytes, signature, secret) is True

    def test_missing_signature(self):
        payload = {"event_id": "evt-123"}
        payload_bytes = json.dumps(payload, sort_keys=True).encode()
        with pytest.raises(SignatureValidationError):
            verify_signature(payload_bytes, None)

    def test_invalid_signature(self):
        payload = {"event_id": "evt-123"}
        payload_bytes = json.dumps(payload, sort_keys=True).encode()
        with pytest.raises(SignatureValidationError):
            verify_signature(payload_bytes, "bad-signature")


class TestNormalizeEvent:
    def test_normalize_valid_event(self):
        payload = {
            "event_id": "evt-123",
            "event_type": "message.delivered",
            "correlation_id": "corr-abc",
            "timestamp": "2026-10-09T01:00:00Z",
            "provider": "sinch",
            "status": "delivered",
        }
        event = normalize_event(payload)
        assert event.id == "evt-123"
        assert event.event_type == "message.delivered"
        assert event.status.value == "delivered"

    def test_normalize_failed_status(self):
        payload = {
            "event_id": "evt-456",
            "event_type": "message.failed",
            "correlation_id": "corr-xyz",
            "timestamp": "2026-10-09T02:00:00Z",
            "status": "failed",
        }
        event = normalize_event(payload)
        assert event.status.value == "failed"


class TestIdempotency:
    def test_duplicate_event_rejected(self):
        # Ensure clean store for this test
        engine._idempotency_store.clear()

        payload = {
            "event_id": "evt-idempotency-test",
            "event_type": "message.sent",
            "correlation_id": "corr-idempotency-test",
            "timestamp": "2026-10-09T03:00:00Z",
        }
        event = normalize_event(payload)
        check_idempotency(event.id)  # first time OK
        with pytest.raises(DuplicateEventError):
            check_idempotency(event.id)  # second time raises


class TestOrdering:
    def test_strict_ordering_rejects_out_of_order(self):
        engine._event_sequence.clear()
        payload1 = {
            "event_id": "evt-seq1",
            "event_type": "message.sent",
            "correlation_id": "corr-seq",
            "timestamp": "2026-10-09T04:00:00Z",
            "sequence": 1,
        }
        payload2 = {
            "event_id": "evt-seq0",
            "event_type": "message.sent",
            "correlation_id": "corr-seq",
            "timestamp": "2026-10-09T04:00:01Z",
            "sequence": 0,
        }
        event1 = normalize_event(payload1)
        event2 = normalize_event(payload2)
        check_ordering(event1, policy="strict")  # seq 1 OK
        with pytest.raises(OutOfOrderEventError):
            check_ordering(event2, policy="strict")  # seq 0 after 1 rejected

    def test_relaxed_ordering_accepts_out_of_order(self):
        engine._event_sequence.clear()
        payload1 = {
            "event_id": "evt-seq1",
            "event_type": "message.sent",
            "correlation_id": "corr-seq2",
            "timestamp": "2026-10-09T04:00:00Z",
            "sequence": 1,
        }
        payload2 = {
            "event_id": "evt-seq0",
            "event_type": "message.sent",
            "correlation_id": "corr-seq2",
            "timestamp": "2026-10-09T04:00:01Z",
            "sequence": 0,
        }
        event1 = normalize_event(payload1)
        event2 = normalize_event(payload2)
        check_ordering(event1, policy="relaxed")  # OK
        check_ordering(event2, policy="relaxed")  # also OK in relaxed mode


class TestDeadLetter:
    def test_move_to_dead_letter(self):
        engine._dead_letter_store.clear()
        payload = {
            "event_id": "evt-dl",
            "event_type": "message.failed",
            "correlation_id": "corr-dl",
            "timestamp": "2026-10-09T05:00:00Z",
        }
        event = normalize_event(payload)
        move_to_dead_letter(event, reason="Test failure", attempts=3)
        dead = get_dead_letters("corr-dl")
        assert len(dead) == 1
        assert dead[0].event_id == "evt-dl"
        assert dead[0].reason == "Test failure"

    def test_replay_dead_letter(self):
        engine._dead_letter_store.clear()
        payload = {
            "event_id": "evt-replay",
            "event_type": "message.failed",
            "correlation_id": "corr-replay",
            "timestamp": "2026-10-09T05:00:00Z",
        }
        event = normalize_event(payload)
        move_to_dead_letter(event, reason="Test", attempts=1)
        replayed = replay_dead_letter("evt-replay")
        assert replayed is not None
        assert replayed.id == "evt-replay"
        dead = get_dead_letters("corr-replay")
        assert len(dead) == 0  # removed after replay


class TestProcessWebhook:
    def test_process_valid_webhook(self):
        engine._idempotency_store.clear()
        payload = {
            "event_id": "evt-webhook",
            "event_type": "message.sent",
            "correlation_id": "corr-webhook",
            "timestamp": "2026-10-09T06:00:00Z",
            "provider": "mock",
            "status": "sent",
        }
        event = process_webhook(payload, verify_sig=False)
        assert event.id == "evt-webhook"
        assert event.status.value == "sent"

    def test_process_duplicate_webhook_rejected(self):
        engine._idempotency_store.clear()
        payload = {
            "event_id": "evt-dup2",
            "event_type": "message.sent",
            "correlation_id": "corr-dup2",
            "timestamp": "2026-10-09T06:00:00Z",
        }
        process_webhook(payload, verify_sig=False)  # first OK
        with pytest.raises(DuplicateEventError):
            process_webhook(payload, verify_sig=False)  # duplicate rejected


class TestSimulateFailedEvent:
    def test_simulate_failed_event_creates_dead_letter(self):
        engine._dead_letter_store.clear()
        entry = simulate_failed_event(correlation_id="corr-sim-fail")
        assert isinstance(entry, DeadLetterEntry)
        assert entry.reason == "Simulated failure"
        dead = get_dead_letters("corr-sim-fail")
        assert len(dead) >= 1
