# ADR 003 — Normalized communication event model

## Status
Accepted

## Context
Multiple providers and webhooks produce heterogeneous payloads. We need a stable internal event model for reliability and observability.

## Decision
- Define a **normalized event schema** with: `event_id`, `correlation_id`, `execution_id`, `event_type`, `status`, `channel`, `timestamp`, `metadata`.
- Normalize inbound webhooks and provider responses into this model before persistence.

## Consequences
- **Pros:** Uniform queries, simpler idempotency/ordering, consistent observability.
- **Cons:** Extra normalization step; must keep schema in sync with provider capabilities.
- **Migration path:** Extend metadata for new provider fields without breaking consumers.

## References
- `src/domain/models.py` (Event)
- `src/events/engine.py` (normalize_event)
- `docs/architecture_description.md` (event flow)
