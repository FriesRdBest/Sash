# ADR 002 — Mock‑first integration with optional Sinch adapter

## Status
Accepted

## Context
Evaluators must be able to run the demo without credentials. Production deployments will require real providers (e.g., Sinch).

## Decision
- Default to **mock providers** (SMS/email) with realistic error modes.
- Design an adapter boundary so a real Sinch client can be swapped in via environment variables.

## Consequences
- **Pros:** Zero‑friction demo, deterministic tests, no secret leakage risk in CI.
- **Cons:** Metrics are synthetic until real providers are configured.
- **Migration path:** Add `SINCH_API_KEY` etc. behind a feature flag; keep mock as fallback.

## References
- `src/integration/lab.py` (mock provider)
- `DEPLOYMENT.md` (environment configuration)
- `docs/known_limitations.md` (simulated metrics)
