# Known Limitations

This is a portfolio/reference demonstration. Do not treat it as a production messaging gateway or as evidence of live Sinch delivery.

## Provider and data

- The demonstrated Aurora workflow is intended for deterministic mock-mode evaluation.
- Simulated provider responses, delivery metrics, latency, and failure scenarios are not Sinch production telemetry.
- Real provider credentials and live-channel behavior have not been established by the local test results.
- SQLite and demo persistence are not a validated multi-instance production data architecture.

## Operations

- The Streamlit app is a demonstration interface, not a hardened multi-tenant operations console.
- Production authentication, authorization, rate limiting, durable queue operations, high availability, and on-call ownership require deployment-specific design and verification.
- Customer CRM, identity-provider, alerting, and downstream integrations must be validated against the actual customer systems.
- Regional processing, consent, sender registration, country/channel eligibility, retention, and compliance requirements need customer- and jurisdiction-specific review.

## Verification gaps

- The 143 passing tests and Ruff checks were reported from a local Codespace run.
- Six Pydantic class-based `Config` deprecation warnings remain.
- The user reported a visual review passed. Keyboard-only navigation, visible focus, measured contrast, screen-reader behavior, and formal accessibility conformance are not verified here.
- Current deployed-app equivalence, screenshots, a recorded demo, load-test evidence, and hosted CI evidence remain release tasks until attached and reviewed.
- An architecture diagram in this repo is explanatory documentation, not proof that every depicted production component is deployed.
