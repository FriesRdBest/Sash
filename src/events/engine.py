"""Webhook receiver, normalization, signature validation, idempotency, ordering, replay, dead-letter."""

import hashlib
import hmac
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal

from src.domain.models import AuditRecord, EventStatus
from src.events.errors import (
    DuplicateEventError,
    InvalidPayloadError,
    OutOfOrderEventError,
    SignatureValidationError,
)
from src.persistence.sqlite_repo import audit_repo

logger = logging.getLogger(__name__)


@dataclass
class NormalizedEvent:
    """Provider-independent normalized event."""

    id: str
    correlation_id: str
    event_type: str  # e.g., "message.sent", "message.delivered", "message.failed"
    provider: str  # e.g., "sinch", "twilio", "mock"
    raw_payload: dict[str, Any]
    timestamp: datetime
    sequence: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)
    status: EventStatus = EventStatus.PENDING


@dataclass
class IdempotencyRecord:
    """Track processed event IDs for idempotency."""

    event_id: str
    correlation_id: str
    processed_at: datetime
    status: str  # processed, failed, dead_letter
    attempts: int = 1
    last_error: str | None = None


@dataclass
class DeadLetterEntry:
    """Dead-letter store entry."""

    event_id: str
    correlation_id: str
    reason: str
    attempts: int
    raw_payload: dict[str, Any]
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


# In-memory stores for demo (could be SQLite-backed)
_idempotency_store: dict[str, IdempotencyRecord] = {}
_dead_letter_store: list[DeadLetterEntry] = []
_event_sequence: dict[str, int] = {}  # correlation_id -> last processed sequence


def validate_webhook_payload(payload: dict[str, Any]) -> None:
    """Validate required fields in webhook payload."""
    required = ["event_id", "event_type", "correlation_id", "timestamp"]
    for f in required:
        if f not in payload:
            raise InvalidPayloadError(f"Missing required field: {f}", field=f)
    if not isinstance(payload.get("timestamp"), str):
        raise InvalidPayloadError("Timestamp must be ISO string", field="timestamp")


def verify_signature(payload_bytes: bytes, signature: str | None, secret: str = "mock-secret") -> bool:
    """Verify webhook signature (HMAC-SHA256). Mockable for tests."""
    if not signature:
        raise SignatureValidationError("Missing signature header")
    expected = hmac.new(secret.encode(), payload_bytes, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature, expected):
        raise SignatureValidationError("Signature mismatch")
    return True


def normalize_event(payload: dict[str, Any]) -> NormalizedEvent:
    """Normalize provider-specific payload to NormalizedEvent."""
    validate_webhook_payload(payload)

    # Parse timestamp
    try:
        ts = datetime.fromisoformat(payload["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        raise InvalidPayloadError("Invalid timestamp format", field="timestamp")

    # Map provider status to EventStatus
    raw_status = payload.get("status", "pending").lower()
    status_map = {
        "sent": EventStatus.SENT,
        "delivered": EventStatus.DELIVERED,
        "failed": EventStatus.FAILED,
        "pending": EventStatus.PENDING,
    }
    status = status_map.get(raw_status, EventStatus.PENDING)

    return NormalizedEvent(
        id=payload["event_id"],
        correlation_id=payload["correlation_id"],
        event_type=payload["event_type"],
        provider=payload.get("provider", "unknown"),
        raw_payload=payload,
        timestamp=ts,
        sequence=payload.get("sequence", 0),
        metadata=payload.get("metadata", {}),
        status=status,
    )


def check_idempotency(event_id: str) -> None:
    """Check if event already processed; raise DuplicateEventError if so."""
    if event_id in _idempotency_store:
        raise DuplicateEventError(event_id)


def record_idempotency(event: NormalizedEvent, status: str, error: str | None = None) -> None:
    """Record event as processed in idempotency store."""
    _idempotency_store[event.id] = IdempotencyRecord(
        event_id=event.id,
        correlation_id=event.correlation_id,
        processed_at=datetime.now(timezone.utc),
        status=status,
        attempts=1,
        last_error=error,
    )


def check_ordering(event: NormalizedEvent, policy: Literal["strict", "relaxed"] = "relaxed") -> None:
    """Check event ordering; raise OutOfOrderEventError if violated (strict mode)."""
    last_seq = _event_sequence.get(event.correlation_id, 0)
    if event.sequence <= last_seq:
        if policy == "strict":
            raise OutOfOrderEventError(event.id, last_seq + 1, event.sequence)
        else:
            logger.warning(f"[WEBHOOK] Out-of-order event {event.id} (seq {event.sequence} <= {last_seq}), accepting in relaxed mode")
    _event_sequence[event.correlation_id] = max(last_seq, event.sequence)


def move_to_dead_letter(event: NormalizedEvent, reason: str, attempts: int = 3) -> None:
    """Move failed event to dead-letter store."""
    entry = DeadLetterEntry(
        event_id=event.id,
        correlation_id=event.correlation_id,
        reason=reason,
        attempts=attempts,
        raw_payload=event.raw_payload,
    )
    _dead_letter_store.append(entry)
    logger.error(f"[WEBHOOK] Event {event.id} moved to dead-letter: {reason}")


def replay_dead_letter(event_id: str) -> NormalizedEvent | None:
    """Replay a dead-letter event (returns normalized event or None if not found)."""
    entry = next((e for e in _dead_letter_store if e.event_id == event_id), None)
    if not entry:
        return None
    # Remove from dead-letter and re-normalize
    _dead_letter_store.remove(entry)
    return normalize_event(entry.raw_payload)


def get_dead_letters(correlation_id: str | None = None) -> list[DeadLetterEntry]:
    """Get dead-letter entries, optionally filtered by correlation_id."""
    if correlation_id:
        return [e for e in _dead_letter_store if e.correlation_id == correlation_id]
    return list(_dead_letter_store)


def process_webhook(
    payload: dict[str, Any],
    signature: str | None = None,
    verify_sig: bool = False,
    ordering_policy: Literal["strict", "relaxed"] = "relaxed",
) -> NormalizedEvent:
    """Process incoming webhook: validate, normalize, check idempotency/ordering, persist audit."""
    payload_bytes = json.dumps(payload, sort_keys=True).encode()

    # Signature validation (optional boundary)
    if verify_sig:
        verify_signature(payload_bytes, signature)

    # Normalize
    event = normalize_event(payload)

    # Idempotency
    check_idempotency(event.id)

    # Ordering
    check_ordering(event, policy=ordering_policy)

    # Audit: event received
    audit = AuditRecord(
        entity_type="webhook_event",
        entity_id=event.id,
        action="webhook_received",
        new_state={
            "event_type": event.event_type,
            "status": event.status.value,
            "correlation_id": event.correlation_id,
        },
        actor="webhook",
        correlation_id=event.correlation_id,
    )
    audit_repo.record(audit.model_dump(mode="json"))

    # Mark as processed
    record_idempotency(event, status="processed")

    logger.info(f"[WEBHOOK] Processed event {event.id} type={event.event_type} status={event.status.value}")
    return event


def simulate_failed_event(
    correlation_id: str,
    event_type: str = "message.failed",
    attempts: int = 3,
) -> DeadLetterEntry:
    """Simulate a failed event for dead-letter demo."""
    from uuid import uuid4

    payload = {
        "event_id": str(uuid4()),
        "event_type": event_type,
        "correlation_id": correlation_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "provider": "mock",
        "status": "failed",
        "sequence": _event_sequence.get(correlation_id, 0) + 1,
        "metadata": {"failure_reason": "Simulated failure"},
    }
    event = normalize_event(payload)
    move_to_dead_letter(event, reason="Simulated failure", attempts=attempts)
    return _dead_letter_store[-1]
