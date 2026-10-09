# Evidence Index — Sash v0.19.0-rc1

This page aggregates the key evidence artifacts for reviewers, hiring managers, and engineering stakeholders. Use it to validate claims, understand trade-offs, and assess production readiness.

## Quick links

| Artifact | Location | Purpose |
| --- | --- | --- |
| **Release notes** | [`RELEASE_NOTES_v0.19.0.md`](../RELEASE_NOTES_v0.19.0.md) | What’s new, how to run, known limitations, next steps. |
| **Changelog** | [`CHANGELOG.md`](../CHANGELOG.md) | Versioned progression of features, fixes, and notes. |
| **Test report** | [`docs/evidence/test_report_v0.19.0.md`](evidence/test_report_v0.19.0.md) | 143 passing tests, coverage by area, how to reproduce. |
| **Known limitations** | [`docs/known_limitations.md`](known_limitations.md) | Simulated vs real, security gaps, observability gaps, roadmap. |
| **Case study (Aurora)** | [`docs/case_study_aurora.md`](case_study_aurora.md) | End-to-end narrative from ambiguity to handoff. |
| **Architecture description** | [`docs/architecture_description.md`](architecture_description.md) | Components, data flow, trust boundaries. |
| **Interview readiness** | [`docs/interview_readiness.md`](interview_readiness.md) | 5‑min demo script, 15‑min walkthrough, Q&A, FDE mapping. |
| **ADRs** | [`docs/decisions/`](decisions/) | Rationale for UI+API, mock-first, event model, idempotency, observability. |

## Feature evidence map

| Feature | Evidence (tests/docs/UI) | Notes |
| --- | --- | --- |
| Qualification | `tests/test_qualification.py`; **Qualification** page | Feasibility/readiness scoring with explicit conditions. |
| Workflow designer | `tests/test_workflow.py`; **Workflows** + **Run Workflow** | Executable JSON workflow config; validation. |
| Integration lab (mock) | `tests/test_integration_lab.py`; mock provider | Timeouts, rate limits, API errors; redaction. |
| Events & webhooks | `tests/test_events_engine.py`; idempotency/ordering | Duplicate rejection, strict/relaxed ordering, dead-letter. |
| Resilience lab | `tests/test_resilience_lab.py`; **Failure Lab** | 9 scenarios with operator documentation. |
| Observability | `tests/test_observability.py`; **Observability** page | KPIs, alerts, recommendations; simulated metrics labelled. |
| Scorecard | `tests/test_scorecard.py`; **Scorecard** page | Weighted checks; blocking-risk logic; exportable report. |
| Security review | `tests/test_security_review.py`; **Security Review** page | Threats→controls, PII classes, findings/recommendations. |
| AI review | `tests/test_ai_review.py`; **AI Review** page | Deterministic checks; sanitized AI prompts; AI-use log. |
| Handoff package | `tests/test_handoff.py`; **Handoff Package** page | Architecture, runbook, ownership, rollback, training, risks. |
| Deployment | `Dockerfile`, `docker-compose.yml`, `scripts/reset_demo.sh`; **Deployment** page | One-command startup, health check, reset guidance. |
| Repository polish | ADRs, CI workflows, SECURITY.md, CONTRIBUTING.md | Decision history, gates, vulnerability process, contribution guide. |

## How to reproduce key evidence

```bash
# Clone and run tests
git clone https://github.com/FriesRdBest/Sash.git && cd Sash
pip install -r requirements.txt
python -m pytest tests/ -q

# Lint and security checks (CI mirrors these)
ruff check .
pip-audit || true
trufflehog . --only-verified || true

# Run the UI (demo mode)
streamlit run app.py
# Or with Docker
docker compose up --build
```

## What’s real vs simulated

- **Real:** Domain models, workflow engine, event normalization, idempotency/ordering, dead-letter handling, resilience scenarios, scorecard logic, security/AI checks, handoff generator, deployment packaging.
- **Simulated (demo mode):** Provider responses, latency/retry/fallback metrics, some security controls (e.g., retention automation), external monitoring/tracing.

See [`docs/known_limitations.md`](known_limitations.md) for details and migration paths.

## Next steps (roadmap)

- Real metrics/tracing exports and alert rule configuration.
- CI secret scanning/DLP and dependency vulnerability gates.
- Advanced webhook replay protection (nonce/window tracking).
- Real Sinch provider wiring behind a feature flag.
- HA/multi-instance deployment patterns.

## Contact & process

- Security issues: see [`SECURITY.md`](../SECURITY.md).
- Contributions: see [`CONTRIBUTING.md`](../CONTRIBUTING.md).
- Code owners: see [`CODEOWNERS`](../CODEOWNERS).

This index is intended to make the repository auditable without verbal explanation. If you need additional evidence, open an issue describing the gap and the decision context.
