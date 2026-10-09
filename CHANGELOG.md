# Changelog

All notable changes to this project will be documented in this file.

## [v0.19.0-rc1] - 2026-10-09

### Added
- Phase 11: Failure & Resilience Laboratory with deterministic scenarios and operator documentation.
- Phase 12: Production Readiness Scorecard with weighted checks and blocking-risk logic.
- Phase 13: Observability Console with KPIs, alerts, recommendations, and correlation journey view.
- Phase 14: Security & Compliance Review with threat model, controls, and PII classification.
- Phase 15: AI Engineering Review with deterministic checks and optional AI explanations.
- Phase 16: Handoff Package Generator (architecture, runbook, ownership, rollback, training, risks).
- Phase 17: Deployment & Operational Packaging (Dockerfile, docker-compose, health check, reset script).
- Phase 18: Quality, Accessibility & Polish pass (visual QA, error-message clarity, test coverage).
- Phase 19: Evidence & Release (this changelog, release notes, test report, known limitations, case study).

### Changed
- Updated navigation to include all Phase 11–19 pages.
- Clarified error messages and demo labels throughout the UI.
- Improved import formatting and minor lint issues.

### Fixed
- API server import order.
- Handoff generator unused imports.
- AI review secret detection pattern to allow underscores in values.

### Notes
- This is a release candidate (`v0.19.0-rc1`) intended for evaluation and feedback.
- Demo mode uses mock providers and simulated data; production deployment requires real credentials and infrastructure.
