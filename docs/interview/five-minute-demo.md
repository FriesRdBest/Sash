# Five-Minute Demo Script

## 0:00–0:30 — Customer problem

“Aurora Marketplace needs to verify new users, observe delivery outcomes, handle failures, and give operations a supportable workflow. Sash demonstrates the engineering path around that problem; it is not a replacement for Sinch APIs.”

## 0:30–1:00 — Qualify

Open Qualification. Explain which intake fields and rules are implemented. Point out assumptions and conditions rather than presenting the score as an authoritative customer decision.

## 1:00–1:40 — Define the workflow

Open Workflows. Show the sample workflow and exported JSON. State whether a displayed channel result is mock or real; default demo behavior is mock.

## 1:40–2:30 — Run the happy path

Open Run Workflow and execute with synthetic demo details only. Show the correlation ID, mock result, and audit trail. Do not use real customer PII or real phone numbers.

## 2:30–3:20 — Inject a failure

Open Failure Lab. Choose a scenario that is present in `src/resilience/scenarios.py`. Explain detection, simulated behavior, impact, and recovery. State explicitly that this is deterministic simulation.

## 3:20–4:05 — Inspect evidence

Use Event Timeline and Observability to follow the correlation ID. Distinguish stored demo events from production telemetry.

## 4:05–4:40 — Readiness and limits

Show Scorecard and Security Review. Explain blockers and limitations; do not imply the score certifies production readiness.

## 4:40–5:00 — Handoff

Show the handoff package and close with: “Sash makes a customer communication implementation understandable, testable, observable, and transferable.”

Before recording, verify all named sections exist and work in the deployed candidate. Capture the real current build; do not use screenshots from another version.
