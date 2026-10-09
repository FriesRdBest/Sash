"""Typed errors for integration layer."""


class IntegrationError(Exception):
    """Base class for integration errors."""

    pass


class ProviderTimeoutError(IntegrationError):
    """Raised when a provider call exceeds its timeout."""

    pass


class ProviderApiError(IntegrationError):
    """Raised when a provider returns an API error response."""

    def __init__(self, status_code: int, message: str, raw_response: dict | None = None):
        self.status_code = status_code
        self.message = message
        self.raw_response = raw_response or {}
        super().__init__(f"Provider API error {status_code}: {message}")


class ProviderConfigurationError(IntegrationError):
    """Raised when provider configuration is invalid or missing."""

    pass


class ProviderRateLimitError(IntegrationError):
    """Raised when provider rate limit is exceeded."""

    def __init__(self, retry_after_seconds: int, message: str = "Rate limit exceeded"):
        self.retry_after_seconds = retry_after_seconds
        self.message = message
        super().__init__(f"{message} (retry after {retry_after_seconds}s)")


class MessageDeliveryError(IntegrationError):
    """Raised when a message fails to deliver after retries."""

    def __init__(self, channel: str, reason: str, last_error: Exception | None = None):
        self.channel = channel
        self.reason = reason
        self.last_error = last_error
        super().__init__(f"Message delivery failed on {channel}: {reason}")
