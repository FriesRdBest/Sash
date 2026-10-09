"""Typed errors and fault boundaries for resilience simulations."""


class ResilienceError(Exception):
    """Base exception for the resilience laboratory."""


class CRMAdapterError(ResilienceError):
    """Raised when a CRM synchronization boundary fails."""


class DatabasePersistenceError(ResilienceError):
    """Raised when persistence is unavailable before a state write commits."""


class QueueBacklogError(ResilienceError):
    """Raised when queue depth exceeds the configured threshold."""

    def __init__(self, depth: int, threshold: int):
        self.depth = depth
        self.threshold = threshold
        super().__init__(f"Queue backlog {depth} exceeds threshold {threshold}")


class WebhookOutageError(ResilienceError):
    """Raised when a webhook receiver is unavailable."""
