# Product Case Study – Aurora Marketplace

## Context

Aurora Marketplace is a fictional enterprise that wants to verify new users during onboarding. Their requirement:

> When a user signs up, send a verification message. If SMS fails, use another channel. Record the result in our CRM, alert operations when delivery degrades, and make the whole workflow auditable.

The hard part is not sending one API request. It is making the workflow reliable inside a real enterprise environment.

## Approach with Sash

Sash demonstrates how a Forward Deployed Engineer can take this ambiguous requirement and produce a production-ready pattern.

### 1. Feasibility & qualification

- Used **Qualification** to assess channel support, volume, timeline, and readiness.
- Produced a score and signals (e.g., webhook capability, API client availability) to confirm feasibility.

### 2. Workflow design

- Defined a simple multi-step workflow: SMS primary, email fallback.
- Captured templates, channels, and order in a versioned `WorkflowConfig`.

### 3. Resilience & failure handling

- Used the **Failure & Resilience Laboratory** to simulate:
  - Provider timeout
  - Rate limiting
  - Webhook outage
  - Duplicate callbacks
  - Out-of-order events
  - CRM/database failures
  - Queue backlog
  - Fallback execution
- Each scenario includes detection, expected behavior, impact, alert, recovery, and residual risk.

### 4. Observability & operations

- Instrumented events with correlation IDs.
- Built an **Observability Console** showing:
  - KPIs (total, sent, delivered, failed)
  - Failure breakdown
  - Latency, retry, and fallback metrics
  - Alerts and actionable recommendations
- Defined a runbook and alert guide for common incidents.

### 5. Security, AI, and readiness

- Ran a **Security & Compliance Review** with:
  - Threat model (secrets, PII, webhook integrity, auth, retention, residency)
  - Control catalog (secret management, redaction, signatures, auth, retention, regional controls)
  - PII classification and redaction rules
- Ran an **AI Engineering Review** to detect secrets, unsafe imports, and long functions, with sanitized AI-use logging.
- Produced a **Production Readiness Scorecard** with weighted checks and blocking items.

### 6. Handoff & deployment

- Generated a **Handoff Package** containing:
  - Architecture overview
  - Workflow definition
  - Configuration guide
  - Deployment instructions
  - Runbook, alert guide, ownership matrix, rollback plan
  - Training checklist and open-risk register
- Packaged the solution with Docker, health checks, and a demo reset script.

## Outcomes

Aurora’s engineering and operations teams receive:

- A clear architecture and workflow definition.
- Evidence that failure modes are understood and tested.
- An operational console and runbook for day-2 operations.
- A security and AI review with explicit limitations and next steps.
- A handoff package that lets them operate and extend the solution independently.

This case study shows how Sash turns an ambiguous customer narrative into a repeatable, auditable, production-ready pattern.
