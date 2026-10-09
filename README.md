# Sash

Sash is a production readiness and deployment accelerator for programmable customer communications.

It demonstrates how an engineer can qualify an engagement, design an API driven architecture, build resilient communication workflows, test failure modes, instrument operations, and produce a customer handoff package.

This repository is built as evidence for the Senior Forward Deployed Engineer role at Sinch. It shows the ability to take an ambiguous customer problem, assess feasibility, design the integration, build the critical components, prove reliability, expose operational risk, and produce a handoff package.

## Problem

A customer may say:

When a user signs up, send a verification message. If SMS fails, use another channel. Record the result in our CRM, alert operations when delivery degrades, and make the whole workflow auditable.

The hard part is not sending one API request. The hard part is making the workflow reliable inside a real enterprise environment.

Sash answers:

- Is this engagement technically feasible
- Which communication channel should be used
- What happens when delivery fails
- How are retries and duplicate events handled
- Where are consent, identity, secrets, and regional requirements addressed
- How does the customer know a message was delivered
- What does the customer team need to own after handoff
- How can Sinch learn from implementation evidence

That matches the Sinch emphasis on supported APIs, repeatable patterns, measurable outcomes, production stabilization, and customer independence.

## Target user

- Forward Deployed Engineers and solution architects who need to move a customer from ambiguity to production
- Customer engineering teams who need a clear architecture, runbook, and ownership model
- Product and security reviewers who need evidence of reliability, security, and operational readiness

## Flagship scenario

A fictional enterprise, Aurora Marketplace, wants to verify new users using:

1. SMS as the primary channel
2. WhatsApp or email as a fallback
3. Delivery status webhooks
4. An internal customer database
5. An operations dashboard
6. Fraud and abuse controls
7. A supportable production deployment

The demo shows this flow:

User registration → Verification orchestration service → Sinch communication API → Delivery and inbound webhooks → Event normalization → State store and audit trail → Dashboard, alerts, and operational actions

Sinch Conversation API capabilities make this particularly relevant because the platform supports channel routing, delivery reports, inbound webhooks, predictable event structures, retries, and circuit breaker behavior.

Use mock mode by default so recruiters can run the application without credentials. Include an optional Sinch integration mode using environment variables.

## Success criteria

Sash is successful when:

- A new user can complete the verification journey in mock mode
- Every step is visible in the audit trail
- Final state is deterministic
- Errors are understandable
- The full path is covered by an end to end test
- The repository can be reviewed without verbal explanation
- The live demo works without secrets
- The README reflects reality

## Non goals

Sash is not:

- A basic SMS sender
- A chatbot that claims to integrate with Sinch
- A static architecture diagram
- A dashboard with fake KPIs but no event processing logic
- An AI code generator without validation
- A generic CRM or notification application
- A visually polished application that cannot demonstrate retries, webhooks, idempotency, or failure recovery
- A platform that pretends to replace Sinch APIs

The strongest project complements Sinch. It demonstrates the layer Sinch needs around its APIs: customer specific orchestration, integration, reliability, operational visibility, and deployment discipline.

## Risk register

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Scope creep | High | Medium | Fixed flagship scenario, phased delivery |
| Over engineering | Medium | Medium | Start simple, add complexity only when needed |
| Incomplete testing | High | Medium | Tests required for each phase, CI gates |
| Security gaps | High | Low | Threat model, secret management, redaction |
| Unclear narrative | Medium | Medium | README and demo follow customer story |
| Deployment friction | Medium | Low | One command startup, documented setup |

## Glossary

- **Forward Deployed Engineer**: An engineer who embeds with customer teams to make integrations work in production
- **Customer communications workflow**: A sequence of steps that sends messages via SMS, voice, email, or other channels
- **Mock mode**: A simulation environment that does not require real provider credentials
- **Provider adapter**: A service boundary that isolates provider specific logic
- **Event normalization**: Converting provider events into a consistent internal model
- **Idempotency**: Ensuring duplicate events do not change state more than once
- **Correlation ID**: A unique identifier that connects a send request to all later callbacks
- **Handoff package**: Documentation and runbooks that enable a customer to operate and extend the solution

## Initial delivery roadmap

| Phase | Purpose | Key deliverables |
|---|---|---|
| 0 | Operating charter | Product brief, target user, flagship scenario, success criteria, non goals, risk register, glossary, initial roadmap |
| 1 | Repository foundation | Branch strategy, issue labels, project board, contribution guide, code of conduct, license, pull request template, issue templates, security policy, changelog, development setup |
| 2 | Research and domain model | Domain glossary, workflow states, normalized event model, lifecycle diagram, assumptions register, provider capability matrix, customer journey map |
| 3 | Architecture and decision record | Context diagram, container diagram, component diagram, data flow diagram, threat model, deployment diagram, ADRs |
| 4 | Design system and application shell | Sash visual identity, navigation, layout, typography, color semantics, status badges, empty states, error states, loading states, responsive behavior, demo reset controls |
| 5 | Domain and persistence core | Pydantic models, configuration layer, repository interfaces, SQLite implementation, seed data, audit records, correlation IDs, state transitions, deterministic clock |
| 6 | Engagement qualification | Intake form, feasibility rules, readiness scoring, product fit assessment, risk flags, recommended decision, conditions for approval, qualification report |
| 7 | Workflow designer | Workflow configuration, channel selection, fallback rules, retry policy, timeout policy, consent requirement, ownership fields, JSON export and import, workflow validation |
| 8 | Integration laboratory | Provider interface, mock Sinch adapter, optional Sinch adapter boundary, verification service, routing service, retry policy, CRM adapter stub, request and response logging with redaction |
| 9 | Event and webhook engine | Webhook receiver model, payload validation, event normalization, signature validation boundary, idempotency store, duplicate detection, ordering logic, replay capability, dead letter state |
| 10 | End to end happy path | Aurora Marketplace verification journey, registration, consent, verification request, provider response, delivery callback, final status, audit timeline |
| 11 | Failure and resilience laboratory | Failure simulator, provider timeout, rate limit, webhook outage, duplicate callback, out of order event, CRM failure, database failure, queue backlog, fallback execution, recovery actions |
| 12 | Production readiness scorecard | API, webhook, reliability, security, scalability, observability, testing, operations, and customer readiness checks, weighted score, blocking risk logic, recommendation engine |
| 13 | Observability console | KPI cards, event table, workflow timeline, correlation search, channel breakdown, failure breakdown, latency metrics, retry and fallback metrics, alert list, event detail view |
| 14 | Security and compliance review | Threat model, secret management guidance, PII classification, log redaction tests, consent controls, authentication boundary, replay protection, data retention assumptions, regional considerations |
| 15 | AI engineering review | Code review input, deterministic rule checks, optional model assisted explanation, findings by severity, evidence, remediation, required validation test, AI use log |
| 16 | Handoff package | Architecture document, workflow definition, configuration guide, deployment instructions, runbook, test evidence, alert guide, ownership matrix, rollback plan, training checklist, open risk register |
| 17 | Deployment and operational packaging | Streamlit deployment, Dockerfile, optional API service, health check, environment configuration, demo data reset, startup instructions, deployment notes |
| 18 | Quality, accessibility, and polish | Visual QA, keyboard and contrast review, error message review, performance review, test coverage report, dependency review, documentation review, recorded walkthrough |
| 19 | Evidence and release | Release candidate, tagged version, changelog, release notes, demo video, architecture image, test report, known limitations document, product case study, final issue closure |
| 20 | Interview readiness | Five minute demo, fifteen minute technical walkthrough, architecture defence, failure mode discussion, trade off answers, what I would do next roadmap, role mapping document |

## Repository principles

- Every meaningful capability is introduced through an issue, branch, pull request, test, documentation update, and intentional commit
- Every important architectural choice receives an Architecture Decision Record
- Every phase ends with demonstrable evidence, not merely completed code
- The mock environment is the default and must be fully functional without Sinch credentials
- Real Sinch integration is optional and must never be required to evaluate the engineering quality of the application
- The repository must clearly separate implemented, simulated, planned, and intentionally out of scope functionality
- Never use real customer data, real phone numbers, credentials, or unverified provider claims
- Never present simulated delivery metrics as real Sinch production metrics

Architecture Decision Records are especially important because they preserve the context, rationale, alternatives, and consequences of technical choices instead of showing only the final code.

## Commit style

Use commits that explain intent:

```
docs: define Sash product boundaries and flagship scenario
docs: record decision to use mock provider by default
feat: add qualification scoring rules
feat: add normalized communication event model
test: cover duplicate webhook idempotency
feat: add fallback routing for transient delivery failure
fix: preserve correlation ID across webhook processing
docs: add webhook outage recovery runbook
test: add resilience coverage for provider timeout
refactor: isolate provider adapter from orchestration service
release: prepare Sash version 0.3.0
```

Avoid commits such as:

```
updates
fixed stuff
more work
final
final final
changes
```

The commit history should tell a coherent story without requiring you to explain it verbally.

## Pull request standard

Every pull request should contain:

```
## Purpose
What customer or engineering problem does this solve

## Scope
What is included and intentionally excluded

## Design
What changed in the architecture or workflow

## Evidence
Which tests, screenshots, logs, or simulations prove it works

## Failure behavior
What happens when this fails

## Security and privacy
Does this affect secrets, PII, authentication, consent, or logging

## Documentation
Which README, ADR, runbook, or changelog entries changed

## Known limitations
What remains incomplete or simulated
```

An elite reviewer should be able to inspect a pull request and understand not only what you coded, but why it exists and how you proved it.

## Project board structure

Create GitHub Project views for:

- **Now** — actively committed work
- **Next** — prioritized work ready to begin
- **Blocked** — decisions or external information required
- **Evidence missing** — code exists but has not been adequately tested or documented
- **Risks** — security, reliability, scope, or deployment risks
- **Release readiness** — items required before a public demo or release
- **Later** — explicitly deferred work

Use issue labels such as:

```
type:feature
type:bug
type:research
type:decision
type:documentation
type:test

area:domain
area:ui
area:integration
area:webhooks
area:reliability
area:security
area:observability
area:operations

priority:p0
priority:p1
priority:p2

status:blocked
status:needs-evidence
```

This prevents the repository from looking like a random collection of tasks.

## Minimum CI gates

Every pull request should run:

1. Formatting check
2. Linting
3. Type checking
4. Unit tests
5. Integration tests
6. Security scan
7. Secret scan
8. Application startup check
9. Documentation link check if practical
10. Coverage report

Do not set an artificial coverage target simply to display a high percentage. Prioritize coverage of:

- State transitions
- Retry decisions
- Idempotency
- Event normalization
- Failure handling
- Authentication boundaries
- Redaction
- Qualification scoring

## What Brett should see

When a reviewer opens the repository, the first five minutes should reveal:

1. A clear README explaining the customer problem and the product purpose
2. A live demo that works without credentials
3. A visible architecture showing event flow and trust boundaries
4. A real test suite covering normal and failure paths
5. A decision history explaining trade offs
6. A changelog showing disciplined progression
7. A known limitations document that proves you understand the difference between a portfolio demonstration and production deployment
8. A short demo video showing qualification, happy path, failure injection, observability, readiness scoring, and handoff

The central impression should be:

This person does not merely build screens. They establish a reliable technical path from customer ambiguity to production operation.

That is the standard Sash should be built toward.
