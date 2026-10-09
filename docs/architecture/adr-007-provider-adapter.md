# ADR 007: Provider adapter pattern for Sinch integration

## Status

Accepted

## Context

Sash must integrate with communications providers:
- Sinch (primary target)
- Potentially other providers in future

Requirements:
- Isolate provider-specific logic
- Support mock provider for demo
- Enable testing without real API calls
- Allow future provider swaps

## Decision

Implement a provider adapter pattern with:
1. Abstract interface (Protocol)
2. Mock implementation (for demo)
3. Sinch implementation (for production)

## Rationale

**Adapter pattern benefits:**
- Domain logic is provider-agnostic
- Easy to test with mock
- Can swap providers without changing domain
- Clear separation of concerns

**Interface design:**

```python
class ProviderAdapter(Protocol):
    def send(self, request: SendRequest) -> SendResponse: ...
    def status(self, message_id: str) -> StatusResponse: ...
    def validate_webhook(self, payload: dict, signature: str) -> bool: ...
```

**Mock implementation:**

- Simulates success, failure, timeout scenarios
- Configurable behavior for testing
- No external dependencies

**Sinch implementation:**

- Calls real Sinch APIs
- Handles Sinch-specific error codes
- Validates Sinch webhook signatures

**Why this matters:**

The Forward Deployed Engineer role requires integrating with customer systems and third-party providers. The adapter pattern demonstrates this capability while keeping the domain logic clean and testable.

## Consequences

- Additional abstraction layer
- Must maintain two implementations (mock, Sinch)
- Interface must be stable
- Testing is easier with mock

## References

- Component diagram: component.md
- Provider capability matrix: ../research/provider_capability_matrix.md
- Sinch product surface: ../research/sinch_product_surface.md
