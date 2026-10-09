"""Unit tests for integration laboratory and mock provider."""

import pytest
from src.domain.models import WorkflowConfig, WorkflowStep
from src.integration.errors import (
    ProviderApiError,
    ProviderConfigurationError,
    ProviderRateLimitError,
    ProviderTimeoutError,
)
from src.integration.lab import IntegrationLab, RetryConfig, run_workflow
from src.integration.provider import (
    MockSinchProvider,
    ProviderRequest,
    ProviderResponse,
    create_provider,
    redact_sensitive_data,
)


class TestRedactSensitiveData:
    def test_redact_phone(self):
        text = '{"phone_number": "+1234567890", "email": "test@example.com"}'
        redacted = redact_sensitive_data(text)
        assert '"phone_number": "+1234567890"' not in redacted
        assert '"phone_number": "[REDACTED]"' in redacted

    def test_redact_email(self):
        text = '{"email": "user@example.com"}'
        redacted = redact_sensitive_data(text)
        assert '"email": "[REDACTED]"' in redacted

    def test_redact_api_key(self):
        text = '{"api_key": "sk-1234567890abcdef"}'
        redacted = redact_sensitive_data(text)
        assert '"api_key": "[REDACTED]"' in redacted


class TestMockSinchProvider:
    def test_successful_send(self):
        provider = MockSinchProvider(mode="mock")
        request = ProviderRequest(channel="sms", to="+1234567890", content={"body": "Hello"})
        response = provider.send(request)
        assert response.success is True
        assert response.message_id is not None
        assert response.latency_ms >= 0

    def test_timeout_error(self):
        provider = MockSinchProvider(mode="mock")
        request = ProviderRequest(channel="sms", to="+1234567890", content={}, timeout_seconds=0)
        with pytest.raises(ProviderTimeoutError):
            provider.send(request)

    def test_rate_limit_error(self):
        provider = MockSinchProvider(mode="mock")
        request = ProviderRequest(
            channel="sms",
            to="+1234567890",
            content={},
            metadata={"simulate_rate_limit": True},
        )
        with pytest.raises(ProviderRateLimitError):
            provider.send(request)

    def test_api_error(self):
        provider = MockSinchProvider(mode="mock")
        request = ProviderRequest(
            channel="sms",
            to="+1234567890",
            content={},
            metadata={"simulate_api_error": True},
        )
        with pytest.raises(ProviderApiError):
            provider.send(request)


class TestCreateProvider:
    def test_mock_provider(self):
        provider = create_provider(mode="mock")
        assert isinstance(provider, MockSinchProvider)

    def test_invalid_mode(self):
        with pytest.raises(ProviderConfigurationError):
            create_provider(mode="invalid")


class TestIntegrationLab:
    def test_execute_simple_workflow(self):
        step = WorkflowStep(name="Test SMS", channel="sms", template="Hello {{name}}")
        workflow = WorkflowConfig(name="Test", steps=[step])
        lab = IntegrationLab(mode="mock")
        result = lab.execute_workflow(workflow, customer_phone="+1234567890")
        assert result.success is True
        assert len(result.events) == 1
        assert result.events[0].status.value == "sent"

    def test_workflow_with_fallback(self):
        step1 = WorkflowStep(
            name="Primary SMS",
            channel="sms",
            template="Verify: {{code}}",
            metadata={"simulate_api_error": True},
        )
        step2 = WorkflowStep(
            name="Fallback Email",
            channel="email",
            template="Verify: {{code}}",
        )
        step1.fallback_to = step2.id
        workflow = WorkflowConfig(name="Fallback Test", steps=[step1, step2])
        lab = IntegrationLab(mode="mock")
        result = lab.execute_workflow(workflow, customer_phone="+1234567890")
        assert result.success is True
        assert len(result.events) >= 2


class TestRunWorkflow:
    def test_run_workflow_helper(self):
        step = WorkflowStep(name="SMS", channel="sms", template="Hi")
        workflow = WorkflowConfig(name="Quick", steps=[step])
        result = run_workflow(workflow, customer_phone="+1234567890", mode="mock")
        assert result.success is True
        assert result.correlation_id is not None
