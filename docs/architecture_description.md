# Architecture Description – Sash

This document describes the logical architecture of Sash. It can be used to create a diagram or as a standalone textual architecture reference.

## Logical components

1. **UI (Streamlit)**
   - Pages: Home, Domain Models, Qualification, Engagements, Workflows, Run Workflow, Event Timeline, Failure Lab, Scorecard, Observability, Security Review, AI Review, Handoff Package, Deployment.
   - Role: Operator interface for designing workflows, running simulations, inspecting events, and generating reports.

2. **Domain Layer**
   - Models: `Customer`, `Workflow`, `WorkflowExecution`, `Event`, `Engagement`, `AuditRecord`.
   - Role: Core business entities and invariants.

3. **Workflow Engine**
   - Executes `WorkflowConfig` against a provider.
   - Handles retries, fallbacks, and correlation IDs.
   - Produces `WorkflowExecutionResult` and events.

4. **Integration Layer**
   - Mock and real provider implementations (SMS, email).
   - Error handling: timeouts, rate limits, API errors.
   - Redaction of sensitive data in logs.

5. **Events & Webhooks**
   - Event normalization, validation, and storage.
   - Webhook signature verification, idempotency, and ordering policies.
   - Dead-letter queue for unprocessable events.

6. **Resilience Laboratory**
   - Deterministic failure scenarios (timeout, rate limit, webhook outage, duplicates, out-of-order, CRM/DB failures, queue backlog, fallback).
   - Operator documentation for each scenario.

7. **Observability**
   - KPI computation, alerts, recommendations.
   - Channel and failure breakdowns, latency/retry/fallback metrics.
   - Event search and correlation-journey view.

8. **Security & AI Review**
   - Threat model, control catalog, PII classification.
   - Deterministic static checks (secrets, unsafe imports, function length).
   - Optional AI-assisted explanations with sanitized prompts.

9. **Scorecard & Handoff**
   - Weighted readiness score with blocking items.
   - Handoff package generator (architecture, runbook, ownership, rollback, training, risks).

10. **Deployment & Operations**
    - Dockerfile and docker-compose for UI and optional API.
    - Health checks, environment configuration, demo reset.
    - Documentation: README, DEPLOYMENT.md, known limitations.

## Data flow (simplified)

1. Operator designs/chooses a workflow in the UI.
2. Workflow engine executes steps via the integration layer.
3. Events are stored with correlation IDs.
4. Observability and scorecard components read events to produce health/readiness views.
5. Security and AI reviews analyze code/configuration for risks.
6. Handoff generator assembles documentation for customer teams.

## Trust boundaries

- **UI**: Internal tool; not directly customer-facing.
- **API/Integration**: Authenticated by service credentials; secrets managed externally.
- **Event store**: Internal persistence; access controlled; PII redaction applied where possible.
- **Webhook receiver**: Public endpoint; signature verification and replay protection required.

This description matches the current codebase and can be rendered as a block diagram if desired.
