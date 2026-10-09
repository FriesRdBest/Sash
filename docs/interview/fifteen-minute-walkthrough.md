# Fifteen-Minute Technical Walkthrough

## 0:00–1:30 — Problem framing

Describe Aurora Marketplace's verification need, its asynchronous delivery callbacks, fallback expectations, and operator ownership. Clarify that the application is a reference/demo accelerator.

## 1:30–3:30 — Domain and workflow

Walk through the domain models, workflow definition, qualification logic, and the separation between workflow configuration and execution. Explain correlation IDs and consent/audit concepts based on current code.

## 3:30–6:00 — Integration boundary

Show the integration/provider modules and mock-mode path. Explain request/response validation, error boundaries, timeouts, retries, and redaction only to the degree directly supported by the code. The mock provider is not evidence of an active production Sinch integration.

## 6:00–8:30 — Asynchronous events

Explain event normalization, signature-validation boundary, idempotency, ordering policy, persistence, and timeline. Identify which pieces are implemented in-process and what would need durable infrastructure at scale.

## 8:30–10:30 — Failure behavior

Run a supported deterministic scenario from Failure Lab. Explain detection, state preservation, alerts/recovery as modeled. Do not describe simulated behavior as a live provider incident.

## 10:30–12:00 — Observability and security

Show correlation-based event inspection, metrics, security review, PII/redaction limitations, and the distinction between demonstration values and production instrumentation.

## 12:00–13:30 — Test evidence

Report the actual local result: 143 tests passed; Ruff checks passed; six Pydantic config deprecation warnings remain. Call this local evidence, not hosted CI or load-test evidence.

## 13:30–15:00 — Trade-offs and roadmap

Discuss Streamlit for demonstration, SQLite for local repeatability, provider abstraction, and mock-first evaluation. Next steps: confirm production requirements, validate a real provider sandbox safely, add deployment-specific durable queue/storage/security, run contract/load/resilience tests, and document ownership and rollback.
