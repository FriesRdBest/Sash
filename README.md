# Sash

**Sash: a production-readiness and deployment accelerator for programmable customer communications.**

It demonstrates how an engineer can qualify an engagement, design an API-driven architecture, build resilient communication workflows, test failure modes, instrument operations, and produce a customer handoff package. Built for the Senior Forward Deployed Engineer role at Sinch.

## For reviewers (start here)

- **Evidence index:** [`docs/EVIDENCE_INDEX.md`](docs/EVIDENCE_INDEX.md) — tests, ADRs, release notes, known limitations, case study, interview pack.
- **Demo in 5 minutes:** see section below.
- **Interview walkthrough:** [`docs/interview_readiness.md`](docs/interview_readiness.md).

## Demo in 5 minutes

```bash
# Clone and run (no credentials required)
git clone https://github.com/FriesRdBest/Sash.git && cd Sash
docker compose up --build
# Open http://localhost:8501
```

**Suggested flow:**
1) Qualification → 2) Workflow → 3) Run Workflow → 4) Event Timeline → 5) Failure Lab → 6) Observability → 7) Scorecard → 8) Security & AI Review → 9) Handoff Package → 10) Deployment.
See `docs/interview_readiness.md` for a scripted 5‑minute walkthrough.

## What’s real vs simulated

- **Real:** Domain models, workflow engine, event normalization, idempotency/ordering, dead-letter handling, resilience scenarios, scorecard logic, security/AI checks, handoff generator, deployment packaging.
- **Simulated (demo mode):** Provider responses, latency/retry/fallback metrics, some security controls (e.g., retention automation), external monitoring/tracing.
See `docs/known_limitations.md` for details and migration paths.

## Problem

A customer may say:
> When a user signs up, send a verification message. If SMS fails, use another channel. Record the result in our CRM, alert operations when delivery degrades, and make the whole workflow auditable.

The hard part is not sending one API request. The hard part is making the workflow reliable inside a real enterprise environment.

Sash answers:
- Is this engagement technically feasible?
- Which communication channel should be used?
- What happens when delivery fails?
- How are retries and duplicate events handled?
- Where are consent, identity, secrets, and regional requirements addressed?
- How does the customer know a message was delivered?
- What does the customer team need to own after handoff?
- How can Sinch learn from implementation evidence?

## Target user

- Forward Deployed Engineers and solution architects who need to move a customer from ambiguity to production.
- Customer engineering teams who need a clear architecture, runbook, and ownership model.
- Product and security reviewers who need evidence of reliability, security, and operational readiness.

## Flagship scenario

A fictional enterprise, **Aurora Marketplace**, wants to verify new users using:
1. SMS as the primary channel
2. WhatsApp or email as a fallback
3. Delivery-status webhooks
4. An internal customer database
5. An operations dashboard
6. Fraud and abuse controls
7. A supportable production deployment

See `docs/case_study_aurora.md` for the full narrative.

## Architecture

See `docs/architecture_description.md` for components, data flow, and trust boundaries.

## Local setup (no Docker)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Optional Sinch integration (advanced): set `PROVIDER_API_KEY`, `WEBHOOK_SECRET`, and `DATABASE_URL` in your environment. Mock mode remains the default.

## Test strategy

```bash
python -m pytest tests/ -q
```

Coverage includes domain, events, integration, resilience, observability, security, AI review, handoff, workflow, timeline, qualification, and E2E Aurora scenario.

## Failure modes

See `docs/decisions/` for architecture decision records and `docs/known_limitations.md` for production gaps and next steps.

## Security considerations

- No secrets committed; use environment variables or a secret manager.
- Sensitive fields are redacted in logs; see Security Review in the UI.
- Webhook signature verification and idempotency are implemented; advanced replay protection is a roadmap item.

## Production limitations

- Demo uses mock providers and synthetic metrics.
- Retention/deletion jobs and external monitoring are not automated.
- Some security controls are partial; see `docs/known_limitations.md`.

## Customer handoff example

Use the **Handoff Package** page in the UI to generate architecture, runbook, ownership, rollback, training, and risks. See `docs/handoff/` (generated at runtime) for exports.

## License

MIT (see `LICENSE`).
