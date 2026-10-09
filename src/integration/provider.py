"""Provider interface and mock Sinch adapter."""

import json
import logging
import os
import re
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Protocol

from src.domain.models import EventStatus
from src.integration.errors import (
    ProviderApiError,
    ProviderConfigurationError,
    ProviderRateLimitError,
    ProviderTimeoutError,
)

logger = logging.getLogger(__name__)

# Patterns to redact PII and secrets
PHONE_PATTERN = re.compile(r'"phone_number"\s*:\s*"[^"]+"')
EMAIL_PATTERN = re.compile(r'"email"\s*:\s*"[^"]+"')
API_KEY_PATTERN = re.compile(r'"api_key"\s*:\s*"[^"]+"')
AUTH_HEADER_PATTERN = re.compile(r"(Authorization|api-key)\s*:\s*[^\n]+", re.IGNORECASE)


@dataclass
class ProviderRequest:
    """Outbound request to a provider."""

    channel: str
    to: str
    content: dict[str, Any]
    correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timeout_seconds: float = 30.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ProviderResponse:
    """Inbound response from a provider."""

    success: bool
    message_id: str | None = None
    status: EventStatus = EventStatus.PENDING
    error_code: str | None = None
    error_message: str | None = None
    raw_response: dict[str, Any] = field(default_factory=dict)
    latency_ms: float = 0.0


def redact_sensitive_data(text: str) -> str:
    """Redact PII and secrets from log text."""
    text = PHONE_PATTERN.sub('"phone_number": "[REDACTED]"', text)
    text = EMAIL_PATTERN.sub('"email": "[REDACTED]"', text)
    text = API_KEY_PATTERN.sub('"api_key": "[REDACTED]"', text)
    text = AUTH_HEADER_PATTERN.sub(r"\1: [REDACTED]", text)
    return text


class Provider(Protocol):
    """Interface for communication providers."""

    def send(self, request: ProviderRequest) -> ProviderResponse:
        """Send a message and return a response."""
        ...


class MockSinchProvider:
    """Mock Sinch provider for integration laboratory."""

    def __init__(self, mode: str = "mock"):
        self.mode = mode
        self._api_key = os.getenv("SINCH_API_KEY", "mock-key")
        self._api_secret = os.getenv("SINCH_API_SECRET", "mock-secret")
        if not self._api_key and mode == "real":
            raise ProviderConfigurationError("SINCH_API_KEY required for real mode")

    def send(self, request: ProviderRequest) -> ProviderResponse:
        start = time.perf_counter()

        # Simulate timeout
        if request.timeout_seconds <= 0:
            raise ProviderTimeoutError("Request timeout exceeded")

        # Simulate rate limit for testing
        if request.metadata.get("simulate_rate_limit"):
            raise ProviderRateLimitError(retry_after_seconds=5)

        # Simulate API error
        if request.metadata.get("simulate_api_error"):
            raise ProviderApiError(
                status_code=400,
                message="Invalid phone number format",
                raw_response={"error": "INVALID_PHONE"},
            )

        # Successful mock send
        message_id = f"msg-{uuid.uuid4().hex[:12]}"
        latency_ms = (time.perf_counter() - start) * 1000

        # Log request/response with redaction
        req_log = redact_sensitive_data(
            json.dumps(
                {
                    "channel": request.channel,
                    "to": request.to,
                    "content": request.content,
                }
            )
        )
        resp_log = redact_sensitive_data(
            json.dumps(
                {"message_id": message_id, "status": "sent", "latency_ms": latency_ms}
            )
        )
        logger.info(f"[MOCK_SINCH] Request: {req_log}")
        logger.info(f"[MOCK_SINCH] Response: {resp_log}")

        return ProviderResponse(
            success=True,
            message_id=message_id,
            status=EventStatus.SENT,
            raw_response={"message_id": message_id, "status": "sent"},
            latency_ms=latency_ms,
        )


class RealSinchProvider:
    """Real Sinch provider (optional, requires credentials)."""

    def __init__(self):
        self._api_key = os.getenv("SINCH_API_KEY")
        self._api_secret = os.getenv("SINCH_API_SECRET")
        if not self._api_key or not self._api_secret:
            raise ProviderConfigurationError(
                "SINCH_API_KEY and SINCH_API_SECRET required"
            )

    def send(self, request: ProviderRequest) -> ProviderResponse:
        # Placeholder: real HTTP integration would go here
        # For now, raise to indicate unimplemented in demo
        raise NotImplementedError("Real Sinch integration not implemented in demo")


def create_provider(mode: str = "mock") -> Provider:
    """Factory to create provider instance."""
    if mode == "mock":
        return MockSinchProvider(mode="mock")
    elif mode == "real":
        return RealSinchProvider()
    else:
        raise ProviderConfigurationError(f"Unknown provider mode: {mode}")
