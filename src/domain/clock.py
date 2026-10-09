"""Deterministic clock for testable time-dependent logic."""

from datetime import datetime
from typing import Optional


class Clock:
    """Abstract clock interface for time operations."""
    
    def now(self) -> datetime:
        """Return current datetime."""
        raise NotImplementedError


class SystemClock(Clock):
    """Real system clock."""
    
    def now(self) -> datetime:
        return datetime.utcnow()


class DeterministicClock(Clock):
    """Fixed-time clock for deterministic tests."""
    
    def __init__(self, fixed_time: Optional[datetime] = None):
        self._fixed_time = fixed_time or datetime.utcnow()
    
    def now(self) -> datetime:
        return self._fixed_time
    
    def advance(self, seconds: int):
        """Advance the clock by specified seconds."""
        from datetime import timedelta
        self._fixed_time += timedelta(seconds=seconds)


# Global clock instance (default to system clock)
_clock: Clock = SystemClock()


def get_clock() -> Clock:
    """Get the current clock."""
    return _clock


def set_clock(clock: Clock):
    """Set the clock (for testing)."""
    global _clock
    _clock = clock


def now() -> datetime:
    """Get current time from the configured clock."""
    return _clock.now()
