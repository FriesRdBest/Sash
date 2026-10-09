"""Typed errors for event/webhook engine."""


class EventProcessingError(Exception):
    """Base class for event processing errors."""


class InvalidPayloadError(EventProcessingError):
    """Raised when webhook payload is malformed or missing required fields."""

    def __init__(self, message: str, field: str | None = None):
        self.message = message
        self.field = field
        super().__init__(f"Invalid payload: {message}" + (f" (field: {field})" if field else ""))


class SignatureValidationError(EventProcessingError):
    """Raised when webhook signature validation fails."""

    def __init__(self, message: str = "Invalid signature"):
        self.message = message
        super().__init__(message)


class DuplicateEventError(EventProcessingError):
    """Raised when a duplicate event is detected (idempotency)."""

    def __init__(self, event_id: str):
        self.event_id = event_id
        super().__init__(f"Duplicate event detected: {event_id}")


class OutOfOrderEventError(EventProcessingError):
    """Raised when an event arrives out of expected order."""

    def __init__(self, event_id: str, expected_sequence: int, actual_sequence: int):
        self.event_id = event_id
        self.expected_sequence = expected_sequence
        self.actual_sequence = actual_sequence
        super().__init__(f"Out-of-order event {event_id}: expected seq {expected_sequence}, got {actual_sequence}")


class DeadLetterEventError(EventProcessingError):
    """Raised when an event is moved to dead-letter due to repeated failures."""

    def __init__(self, event_id: str, reason: str, attempts: int):
        self.event_id = event_id
        self.reason = reason
        self.attempts = attempts
        super().__init__(f"Event {event_id} dead-lettered after {attempts} attempts: {reason}")
