# ADR 001 — UI and API stack: Streamlit + FastAPI

## Status
Accepted

## Context
We need an interface that is fast to build, easy to run for evaluators, and credible for operations. We also need an optional API surface for health checks and automation.

## Decision
- Use **Streamlit** for the operator UI.
- Use **FastAPI** for an optional API service (health, simple workflow trigger).

## Consequences
- **Pros:** Rapid iteration, clear separation of UI vs service logic, easy Dockerization.
- **Cons:** Streamlit is not a general-purpose web framework; advanced UI customizations are limited.
- **Migration path:** UI can be replaced later; service logic lives in `src/` and is reusable.

## References
- `app.py` (Streamlit UI)
- `src/api/server.py` (FastAPI health + run endpoint)
