# Interview Readiness Pack – Sash (v0.19.0-rc1)

This pack prepares you to present Sash as a professional case study for the Senior Forward Deployed Engineer role.

## 1. Five‑minute demo script

**Goal:** Show end‑to‑end value, not every feature.

**Flow (target ~5:00):**

- **0:00–0:30 — Problem & audience**
  - “Aurora Marketplace needs reliable user verification: send SMS, fallback to another channel, record in CRM, alert on degradation, and keep it auditable.”
  - Open `README.md` and point to the problem statement and target user.

- **0:30–1:15 — Qualification + Workflow**
  - Open **Qualification**, enter a sample customer, click “Qualify customer.”
  - Highlight score, verdict, and signals (webhook, API client).
  - Open **Workflows**, show the sample two‑step workflow (SMS → email).

- **1:15–2:15 — Run + Timeline + Resilience**
  - Open **Run Workflow**, execute with default phone; copy correlation ID.
  - Open **Event Timeline**, paste ID; show events, metrics, state transitions.
  - Open **Failure Lab**, run “Provider timeout” or “Run all”; show one result with detection, impact, recovery.

- **2:15–3:15 — Observability + Scorecard**
  - Open **Observability**, refresh; show KPIs, one alert, one recommendation.
  - Open **Scorecard**, run; point to overall score and at least one blocking item.

- **3:15–4:15 — Security + AI + Handoff**
  - Open **Security Review**, run; show one threat, one partial control, one PII class.
  - Open **AI Review**, run (AI explanations optional); show one finding and the AI‑use log.
  - Open **Handoff Package**, generate; open Architecture, Runbook, Ownership, Rollback tabs.

- **4:15–5:00 — Deployment + Close**
  - Open **Deployment**, show `docker compose up` and health status.
  - Point to `CHANGELOG.md`, `RELEASE_NOTES_v0.19.0.md`, `docs/evidence/test_report_v0.19.0.md`, and `docs/known_limitations.md`.
  - Close: “Sash turns an ambiguous requirement into an auditable, production‑ready pattern with a clear handoff.”

**Tips:**
- Keep clicks deliberate; pre‑open tabs if needed.
- Narrate outcomes (“This shows we can detect and recover from X”) rather than UI mechanics.

## 2. Fifteen‑minute technical walkthrough

**Goal:** Show depth without getting lost in code.

**Structure:**

- **0–2 min — Architecture overview**
  - Reference `docs/architecture_description.md`.
  - Layers: UI → Domain → Workflow Engine → Integration → Events/Webhooks → Observability/Security/Scorecard → Handoff/Deployment.
  - Trust boundaries: UI (internal), API/Integration (authenticated), Event store (controlled), Webhook receiver (public, signed).

- **2–6 min — Critical paths**
  - **Workflow execution:** `src/workflow/engine.py` → `src/integration/lab.py` → event store.
  - **Resilience:** `src/resilience/simulator.py` and `tests/test_resilience_lab.py` (operator docs + repeatability).
  - **Observability:** `src/observability/engine.py` (KPIs, alerts, recommendations from event data).
  - **Security/AI:** `src/security/review.py` and `src/ai_review/engine.py` (threat→control mapping; deterministic checks + sanitized AI prompts).

- **6–10 min — Data & reliability**
  - Correlation IDs end‑to‑end; idempotency and ordering in `src/events/engine.py`.
  - Dead‑letter handling and replay (`move_to_dead_letter`, `get_dead_letters`).
  - Scorecard logic: weighted dimensions, blocking items (`src/scorecard/engine.py`).

- **10–13 min — Operations & handoff**
  - Docker setup, health check, demo reset (`Dockerfile`, `docker-compose.yml`, `scripts/reset_demo.sh`).
  - Handoff generator: architecture, runbook, ownership, rollback, training, risks (`src/handoff/generator.py`).
  - Known limitations and next steps (`docs/known_limitations.md`).

- **13–15 min — Trade‑offs & roadmap**
  - Why mock‑first, why deterministic checks before AI, why Streamlit for demo.
  - Short roadmap: real metrics/tracing, retention automation, enhanced webhook replay protection, CI secret scanning.

## 3. Architecture defense (talking points)

- **Mock‑first integration:** Accelerates learning and testing; real providers can be swapped behind the same interface.
- **Deterministic failure lab:** Repeatable, auditable evidence of resilience without flaky infra.
- **Event‑centric design:** Correlation IDs, idempotency, and dead‑lettering make debugging and ops tractable.
- **Weighted scorecard:** Converts engineering quality into a delivery decision with explicit blocking risks.
- **Handoff focus:** Architecture, runbook, ownership, and rollback are first‑class artifacts, not afterthoughts.

## 4. Failure‑mode discussion prompts

Be ready to discuss:

- **Provider timeout / rate limit:** Detection, backoff, user impact, fallback channel.
- **Webhook outage / duplicates / out‑of‑order:** Signature verification, idempotency keys, ordering policies, dead‑letter replay.
- **CRM / DB failures:** Isolation from communication path, partial‑write avoidance, retry strategy.
- **Queue backlog:** Thresholds, deferral behavior, alerting.
- **Secret leakage:** Redaction, environment‑based secrets, AI/Security review findings.

Map each to a test: e.g., `test_provider_timeout_documents_safe_failure`, `test_duplicate_callback_does_not_mutate_twice`.

## 5. Trade‑off answers (sample Q&A)

- **Why Streamlit instead of a custom UI?**
  - Speed to value, focus on backend reliability and handoff; UI is a means to demonstrate operability.
- **Why deterministic checks before AI?**
  - Deterministic checks are authoritative and reproducible; AI is advisory and must not auto‑approve code.
- **Why weighted scorecard instead of pass/fail?**
  - Real systems have partial readiness; weighting and blocking items give a nuanced go/no‑go signal.
- **Why mock providers in demo?**
  - Removes external dependencies for evaluators; production pattern is identical with real credentials.

## 6. Next‑roadmap (short, defensible)

- **Observability hardening:** Export real metrics/traces; configure alert rules in a monitoring system.
- **Security automation:** CI secret scanning, DLP, automated retention/deletion jobs.
- **Webhook hardening:** Nonce/window‑based replay protection.
- **AI integration:** Optional LLM explanations with strict sanitization and policy guardrails.
- **Scale & HA:** Multi‑instance deployment, managed database, orchestration (K8s) patterns.

## 7. FDE role mapping

Map Sash features to Senior FDE responsibilities:

- **Ambiguous problem → structured solution:** Qualification + workflow design.
- **Reliability engineering:** Resilience lab, dead‑lettering, fallback execution.
- **Operational excellence:** Observability console, runbook, alert guide, rollback plan.
- **Security & compliance:** Threat model, controls, PII classification, AI governance.
- **Customer independence:** Handoff package, deployment packaging, training checklist.
- **Evidence & communication:** Test report, release notes, case study, known limitations.

Use this pack to frame Sash as a deliberate, defensible body of work aligned to the FDE mandate: turn ambiguous customer needs into reliable, operable, and handoff‑ready solutions.
