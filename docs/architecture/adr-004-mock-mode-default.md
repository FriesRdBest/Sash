# ADR 004: Use mock provider mode by default

## Status

Accepted

## Context

Sash integrates with Sinch APIs for communications. Options:

1. Require real Sinch credentials (production mode)
2. Use mock provider by default (demo mode)
3. Support both with configuration

## Decision

Use mock provider mode by default. Support optional Sinch integration via environment variables.

## Rationale

**Mock mode benefits:**
- No credentials required for demo
- Works on Streamlit Community Cloud free tier
- Predictable behavior for testing
- No cost exposure
- Faster iteration (no API rate limits)

**Real Sinch benefits:**
- Demonstrates actual integration
- Validates against real API behavior
- More credible for production discussions

**Why mock by default:**

The goal is to demonstrate engineering capability, domain understanding, and reliability patterns. These can be proven without real API credentials. Real integration can be added as an optional mode.

**Implementation:**

```python
class ProviderAdapter(Protocol):
    def send(self, request: SendRequest) -> SendResponse: ...
    def status(self, message_id: str) -> StatusResponse: ...

class MockProvider(ProviderAdapter):
    # Simulates Sinch behavior

class SinchProvider(ProviderAdapter):
    # Calls real Sinch API
```

Configuration via environment variable:

```bash
SASH_PROVIDER=mock  # default
SASH_PROVIDER=sinch  # optional
```

## Consequences

- Demo works without credentials
- Real Sinch integration requires additional development
- Must ensure mock behavior is realistic
- Documentation must clarify mock vs. real modes

## References

- Assumptions register: ../research/assumptions_register.md
- Provider capability matrix: ../research/provider_capability_matrix.md
