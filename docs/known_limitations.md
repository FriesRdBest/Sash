# Known Limitations – Sash v0.19.0-rc1

This document lists known limitations and areas for production hardening.

## Scope and fidelity

- **Mock providers by default**: Demo mode uses mock SMS/email providers. Real provider integration requires credentials and environment configuration.
- **Simulated metrics**: Observability latency, retry, and fallback metrics are synthetic in demo mode.
- **SQLite for demo storage**: Persistent but not suited for high-scale production; replace with a managed database.

## Security & compliance

- **Partial controls**: Some security controls (e.g., PII redaction, retention automation, regional data handling) are partial or documented but not fully automated.
- **No built-in secret scanner**: AI/Security reviews flag obvious patterns, but there is no continuous secret scanning in CI by default.
- **Webhook replay protection**: Basic timestamp/signature checks exist; advanced replay windows and nonce tracking are not implemented.

## Observability

- **No external metrics/tracing**: Metrics and traces are not exported to Prometheus, OpenTelemetry, or vendor backends out of the box.
- **Alerting is conceptual**: Alert conditions are documented; actual alert rules and paging integrations are not configured.

## Deployment

- **Health check is basic**: Streamlit container health check uses a simple HTTP probe; deeper readiness checks are not implemented.
- **No auto-scaling config**: Docker Compose setup is single-instance; Kubernetes or other orchestration is not provided.

## AI engineering

- **AI explanations are placeholders**: No real LLM integration; explanations are deterministic templates.
- **AI-use log is local**: Logs are in-memory per session; no persistent audit of AI usage.

## Handoff

- **Ownership matrix uses example teams**: Replace with real team names and escalation paths for production.
- **Runbook and rollback are generic**: Tailor to your actual infra, CI/CD, and incident management processes.

## Roadmap (suggested)

- Automate retention and deletion jobs for events/PII.
- Integrate real metrics/tracing and configure alert rules.
- Add CI-based secret scanning and dependency vulnerability checks.
- Harden webhook replay protection with nonce/window tracking.
- Extend AI review to real LLM with strict sanitization and policy checks.

These limitations are visible by design to show where production hardening is required and to guide next steps.
