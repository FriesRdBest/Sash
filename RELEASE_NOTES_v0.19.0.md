# Release Notes – Sash v0.19.0-rc1

**Release candidate** for evaluation and feedback. This version demonstrates a complete path from ambiguous customer requirement to production-ready handoff.

## What’s new

- **End-to-end readiness flow**: Qualification → Workflow design → Execution → Resilience testing → Observability → Security & AI review → Scorecard → Handoff → Deployment.
- **Failure & Resilience Lab**: Nine deterministic failure scenarios with operator documentation and evidence.
- **Production Readiness Scorecard**: Weighted checks across API, webhook, reliability, security, scalability, observability, testing, operations, and customer readiness.
- **Observability Console**: Operator view with KPIs, alerts, recommendations, and correlation journey.
- **Security & AI Governance**: Threat model, control catalog, PII classification, and responsible AI review with sanitized prompts.
- **Handoff Package**: One-click generation of architecture, runbook, ownership matrix, rollback plan, training checklist, and risk register.
- **Deployment Packaging**: Dockerfile, docker-compose, health checks, demo reset, and clear startup instructions.

## How to run

```bash
# Demo (no secrets required)
docker compose up --build
# Open http://localhost:8501
```

Or locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Evidence

- **Tests**: 143 passing tests covering domain, events, integration, resilience, observability, security, AI review, handoff, workflow, timeline, qualification, and E2E.
- **Reports**: Scorecard, Security Review, AI Review, and Handoff Package can be generated from the UI and exported as Markdown.
- **Documentation**: `README.md`, `DEPLOYMENT.md`, `CHANGELOG.md`, and `docs/` provide architecture, operations, and limitations.

## Known limitations

See `docs/known_limitations.md`. Highlights:
- Demo uses mock providers and simulated metrics.
- Retention and deletion jobs are not automated.
- Some security controls are partial and require production hardening.

## Next steps

- Gather feedback on clarity, completeness, and operability.
- Harden security controls (secret scanning, DLP, retention automation).
- Extend observability to real metrics/tracing backends.
- Produce a short demo video following the provided script.

## Support

This repository is built as evidence for the Senior Forward Deployed Engineer role at Sinch. For questions, refer to the GitHub repository and included documentation.
