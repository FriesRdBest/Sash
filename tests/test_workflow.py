"""Unit tests for workflow designer."""

import pytest

from src.workflow.designer import (
    RetryPolicy,
    WorkflowConfig,
    WorkflowStep,
    create_sample_workflow,
    validate_workflow,
)


class TestRetryPolicy:
    def test_valid_retry_policy(self):
        policy = RetryPolicy(max_attempts=3, backoff_seconds=[5, 30, 120])
        assert policy.max_attempts == 3
        assert policy.backoff_seconds == [5, 30, 120]

    def test_invalid_max_attempts(self):
        with pytest.raises(ValueError):
            RetryPolicy(max_attempts=0)

    def test_invalid_backoff(self):
        with pytest.raises(ValueError):
            RetryPolicy(backoff_seconds=[])


class TestWorkflowStep:
    def test_valid_step(self):
        step = WorkflowStep(
            name="Test SMS",
            channel="sms",
            template="Hello {{name}}",
        )
        assert step.channel == "sms"
        assert step.timeout_seconds == 90

    def test_invalid_channel(self):
        with pytest.raises(ValueError):
            WorkflowStep(name="Test", channel="telegram", template="Hi")


class TestWorkflowConfig:
    def test_create_workflow(self):
        step = WorkflowStep(name="Step 1", channel="sms", template="Hello")
        wf = WorkflowConfig(
            name="Test Workflow",
            description="A test",
            steps=[step],
            owner="Tester",
        )
        assert wf.version == 1
        assert len(wf.steps) == 1

    def test_bump_version(self):
        step = WorkflowStep(name="Step 1", channel="sms", template="Hello")
        wf = WorkflowConfig(name="Test", steps=[step])
        original_version = wf.version
        wf.bump_version()
        assert wf.version == original_version + 1

    def test_json_roundtrip(self):
        step = WorkflowStep(name="Step 1", channel="sms", template="Hello")
        wf = WorkflowConfig(name="Test", steps=[step])
        json_str = wf.to_json()
        wf2 = WorkflowConfig.from_json(json_str)
        assert wf2.name == wf.name
        assert wf2.version == wf.version
        assert len(wf2.steps) == len(wf.steps)

    def test_invalid_no_steps(self):
        with pytest.raises(ValueError):
            WorkflowConfig(name="Empty", steps=[])

    def test_invalid_fallback_target(self):
        step = WorkflowStep(
            name="Step 1",
            channel="sms",
            template="Hello",
            fallback_to="nonexistent",
        )
        with pytest.raises(ValueError):
            WorkflowConfig(name="Bad fallback", steps=[step])


class TestValidateWorkflow:
    def test_valid_workflow(self):
        wf = create_sample_workflow()
        errors = validate_workflow(wf)
        assert len(errors) == 0

    def test_short_name(self):
        step = WorkflowStep(name="Step", channel="sms", template="Hello")
        wf = WorkflowConfig(name="AB", steps=[step])
        errors = validate_workflow(wf)
        assert any("name" in e for e in errors)

    def test_no_sms_or_email(self):
        step = WorkflowStep(name="Step", channel="whatsapp", template="Hello")
        wf = WorkflowConfig(name="Test", steps=[step])
        errors = validate_workflow(wf)
        assert any("SMS or Email" in e for e in errors)

    def test_short_template(self):
        step = WorkflowStep(name="Step", channel="sms", template="Hi")
        wf = WorkflowConfig(name="Test", steps=[step])
        errors = validate_workflow(wf)
        assert any("template" in e for e in errors)


class TestCreateSampleWorkflow:
    def test_sample_workflow_structure(self):
        wf = create_sample_workflow()
        assert "Aurora" in wf.name
        assert len(wf.steps) == 2
        assert wf.steps[0].channel == "sms"
        assert wf.steps[1].channel == "email"
        assert wf.consent_required is True
