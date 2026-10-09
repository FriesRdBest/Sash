# ADR 005: Event processing and normalization strategy

## Status

Accepted

## Context

Sash receives events from:
- Sinch webhooks (delivery reports, inbound messages)
- Internal workflow engine (state transitions)
- User actions (code submission)

Events arrive:
- Out of order
- With duplicates
- In provider-specific formats

## Decision

Implement an event normalization layer that:
1. Validates incoming events
2. Converts to normalized schema
3. Checks for duplicates via idempotency store
4. Persists to event store
5. Triggers workflow state transitions

## Rationale

**Normalization benefits:**
- Provider-agnostic domain logic
- Consistent event schema
- Easier testing and debugging
- Simplifies multi-provider support

**Idempotency benefits:**
- Duplicate webhooks do not corrupt state
- Retries are safe
- Audit trail is accurate

**Why this matters:**

Reliability is a core requirement. The system must handle real-world conditions: network issues, duplicate events, out-of-order delivery. Event normalization and idempotency are essential for production credibility.

**Implementation:**

```python
class EventNormalizer:
    def normalize(self, raw_event: RawEvent) -> NormalizedEvent:
        # Map provider fields to standard schema
        # Validate required fields
        # Enrich with metadata
        return normalized_event

class IdempotencyStore:
    def check_and_record(self, event_id: str) -> bool:
        # Return True if new, False if duplicate
        # Store event_id atomically
```

## Consequences

- Additional processing layer
- Must maintain idempotency store
- Event schema must be stable
- Testing must cover duplicate and out-of-order scenarios

## References

- Event model: ../research/event_model.md
- Workflow states: ../research/workflow_states.md
- Idempotency store: component.md
