"""Unit tests for Aurora happy path end-to-end."""

import pytest

from src.e2e.aurora_happy_path import (
    AuroraSession,
    create_aurora_session,
    get_audit_timeline,
    record_consent,
    register_customer,
    run_verification,
)
from src.workflow.designer import WorkflowConfig, WorkflowStep, create_sample_workflow


class TestRegisterCustomer:
    def test_register_customer_persists(self):
        customer = register_customer(phone_number="+1234567890", email="test@example.com")
        assert customer.phone_number == "+1234567890"
        assert customer.email == "test@example.com"
        assert customer.id is not None


class TestRecordConsent:
    def test_record_consent_creates_audit(self):
        customer = register_customer(phone_number="+1234567890")
        audit = record_consent(customer, granted=True, channel="sms")
        assert audit.entity_type == "customer"
        assert audit.action == "consent_recorded"
        assert audit.new_state["granted"] is True


class TestRunVerification:
    def test_run_verification_simple_workflow(self):
        step = WorkflowStep(name="SMS", channel="sms", template="Hi {{name}}")
        workflow = WorkflowConfig(name="Quick", steps=[step])
        customer = register_customer(phone_number="+1234567890")
        result = run_verification(customer, workflow, mode="mock")
        assert result.success is True
        assert len(result.events) >= 1


class TestCreateAuroraSession:
    def test_full_happy_path(self):
        workflow = create_sample_workflow()
        session = create_aurora_session(
            phone_number="+1234567890",
            workflow=workflow,
            email="user@example.com",
            mode="mock",
        )
        assert isinstance(session, AuroraSession)
        assert session.status == "completed"
        assert session.execution_result.success is True
        assert len(session.execution_result.events) >= 1

    def test_session_has_correlation_id(self):
        workflow = create_sample_workflow()
        session = create_aurora_session(phone_number="+1234567890", workflow=workflow, mode="mock")
        assert session.correlation_id is not None
        assert len(session.correlation_id) > 10


class TestAuditTimeline:
    def test_timeline_contains_entries(self):
        workflow = create_sample_workflow()
        session = create_aurora_session(phone_number="+1234567890", workflow=workflow, mode="mock")
        timeline = get_audit_timeline(session.correlation_id)
        assert len(timeline) >= 1
        actions = {e["action"] for e in timeline}
        assert "consent_recorded" in actions
        assert "verification_completed" in actions
