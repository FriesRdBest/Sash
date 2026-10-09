# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Design system and application shell
- Domain and persistence core
- Engagement qualification module
- Workflow designer
- Integration laboratory with mock provider
- Event and webhook engine
- End to end happy path for Aurora Marketplace scenario
- Failure and resilience laboratory
- Production readiness scorecard
- Observability console
- Security and compliance review
- AI engineering review
- Handoff package generator
- Deployment and operational packaging
- Quality, accessibility, and polish pass
- Evidence and release package
- Interview readiness materials

## [0.3.0] - 2026-10-09

### Added
- Phase 3 architecture and decision records completed
- docs/architecture/README.md — Architecture directory overview
- docs/architecture/context.md — System context diagram showing Aurora Marketplace, Sash, Sinch, and end users with trust boundaries
- docs/architecture/container.md — Container diagram showing Streamlit UI, domain core, provider adapter, persistence layer, and observability
- docs/architecture/component.md — Component diagram showing workflow engine, event processor, retry manager, idempotency manager, provider adapter, persistence, and observability
- docs/architecture/dataflow.md — Data flow diagram for verification workflow with Level 0 context flow and Level 1 internal flow
- docs/architecture/deployment.md — Deployment diagram for development, Streamlit Community Cloud, and future Kubernetes production deployment
- docs/architecture/threat_model.md — STRIDE threat model with 12 threats, security requirements, and trust boundaries
- docs/architecture/production_limitations.md — Explicit documentation of demo limitations vs. production requirements
- docs/architecture/adr-001-streamlit-for-ui.md — ADR for using Streamlit for demonstration UI
- docs/architecture/adr-002-fastapi-boundary.md — ADR for keeping FastAPI as optional future boundary
- docs/architecture/adr-003-sqlite-for-demo.md — ADR for SQLite with PostgreSQL-ready repository interfaces
- docs/architecture/adr-004-mock-mode-default.md — ADR for mock provider mode by default with optional Sinch integration
- docs/architecture/adr-005-event-processing.md — ADR for event normalization and idempotency strategy
- docs/architecture/adr-006-observability.md — ADR for structured logging and in-memory metrics
- docs/architecture/adr-007-provider-adapter.md — ADR for provider adapter pattern with mock and Sinch implementations

### Changed
- Updated changelog to reflect Phase 3 completion

## [0.2.0] - 2026-10-09

### Added
- Phase 2 research and domain model completed
- docs/research/README.md — Research directory overview
- docs/research/sinch_product_surface.md — Sinch API capabilities for verification, messaging, conversation, and voice
- docs/research/workflow_states.md — State machine for Aurora Marketplace verification workflow with states: pending, code_sent, verified, failed, expired, fallback_initiated
- docs/research/event_model.md — Normalized event schema for verification.requested, verification.sent, verification.delivered, verification.failed, verification.code_submitted, verification.completed, verification.expired
- docs/research/assumptions_register.md — Documented assumptions with validation status including mock mode sufficiency, Aurora realism, SQLite adequacy, Streamlit hosting, GitHub review depth, build timeline, and email outreach strategy
- docs/research/provider_capability_matrix.md — Comparison of SMS, WhatsApp, and email channels for delivery speed, reliability, cost, user friction, template approval, two-way communication, delivery reports, fallback suitability, regional restrictions, and opt-in requirements
- docs/research/customer_journey.md — Aurora Marketplace user verification journey with personas, stages, touchpoints, metrics, and pain points addressed
- docs/research/lifecycle_diagram.md — Event lifecycle from send request to final delivery status with state transitions, idempotency guarantees, and correlation model

### Changed
- Updated changelog to reflect Phase 2 completion

## [0.1.0] - 2026-10-09

### Added
- Phase 1 repository foundation completed
- CONTRIBUTING.md with contribution guidelines and pull request requirements
- SECURITY.md with vulnerability reporting and security expectations
- CODE_OF_CONDUCT.md adapted from Contributor Covenant
- .github/pull_request_template.md with required fields for purpose, scope, design, evidence, failure behavior, security, documentation, and known limitations
- .github/ISSUE_TEMPLATE/feature_request.md for new feature proposals
- .github/ISSUE_TEMPLATE/bug_report.md for defect tracking
- .github/ISSUE_TEMPLATE/research_task.md for investigation work
- .github/ISSUE_TEMPLATE/risk_or_decision.md for architectural decisions and risk assessment
- .github/workflows/ci.yml with linting, formatting, testing, and application startup checks
- Initial project board structure defined in README.md

### Changed
- Updated changelog to reflect Phase 1 completion

## [0.0.1] - 2026-10-09

### Added
- Project inception for Sash, a production readiness and deployment accelerator for programmable customer communications
- Phase 0 operating charter in README.md with product mission, problem statement, target users, flagship scenario, success criteria, non goals, risk register, glossary, and initial delivery roadmap
- Repository principles documenting commit style, pull request standards, project board structure, and minimum CI gates
- Clear positioning for the Senior Forward Deployed Engineer role at Sinch
- Flagship scenario definition for Aurora Marketplace user verification workflow
- Risk register covering scope creep, over engineering, incomplete testing, security gaps, unclear narrative, and deployment friction
- Glossary of key terms including Forward Deployed Engineer, customer communications workflow, mock mode, provider adapter, event normalization, idempotency, correlation ID, and handoff package
- Initial 20 phase delivery roadmap from operating charter through interview readiness

### Changed
- Initial repository setup with README, LICENSE, and .gitignore in place

### Notes
- This is the initial operating charter and project definition
- All subsequent phases will be documented here as they are completed
- Mock mode will be the default for all demonstrations
- Real Sinch integration is optional and will never be required to evaluate engineering quality
