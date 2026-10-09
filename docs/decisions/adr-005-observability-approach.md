# ADR 005 — Observability approach: KPIs, alerts, recommendations

## Status
Accepted

## Context
Operators need actionable insight, not just raw logs. We must derive KPIs and alerts from event data and label simulated values.

## Decision
- Implement an **ObservabilityEngine** that computes KPIs, alerts, and recommendations from stored events.
- Clearly label **simulated/demo** metrics in UI and docs.

## Consequences
- **Pros:** Actionable console, testable logic, clear demo vs production boundary.
- **Cons:** Demo metrics are synthetic until connected to real telemetry.
- **Migration path:** Replace synthetic metrics with real aggregations from your monitoring backend.

## References
- `src/observability/engine.py`
- `docs/known_limitations.md` (simulated metrics)
- `docs/architecture_description.md` (observability component)
