# ADR 004 — Idempotency and ordering for webhooks

## Status
Accepted

## Context
Webhooks can arrive duplicated or out of order. State must not corrupt under these conditions.

## Decision
- Enforce **idempotency** by rejecting duplicate event IDs.
- Support **ordering policies**: `strict` (reject out-of-order) and `relaxed` (accept with audit).
- Persist unprocessable events to a **dead‑letter** state for replay.

## Consequences
- **Pros:** Safe retries, auditable anomalies, operator control over replay.
- **Cons:** Requires careful key design and monitoring of dead‑letters.
- **Migration path:** Add nonce/window tracking for advanced replay protection later.

## References
- `src/events/engine.py` (idempotency, ordering)
- `tests/test_events_engine.py`
- `docs/known_limitations.md` (replay protection limits)
