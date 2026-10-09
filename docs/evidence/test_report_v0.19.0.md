# Test & Evidence Report – Sash v0.19.0-rc1

**Generated:** 2026-10-09  
**Commit:** `e50eebd` (Phase 18 polish) → `v0.19.0-rc1`  
**Test command:** `python -m pytest tests/ -v --tb=short`

## Test summary

- **Total tests:** 143
- **Passed:** 143
- **Failed:** 0
- **Warnings:** 6 (Pydantic v2 deprecation; non-blocking)

## Coverage by area

| Area                  | Test module(s)                              | Notes                                      |
|-----------------------|---------------------------------------------|--------------------------------------------|
| Domain models         | `tests/test_domain.py`                      | Customer, Workflow, Event, Engagement      |
| Events & webhooks     | `tests/test_events_engine.py`               | Validation, signature, idempotency, ordering|
| Integration lab       | `tests/test_integration_lab.py`             | Mock provider, redaction, error handling   |
| Resilience lab        | `tests/test_resilience_lab.py`              | 9 failure scenarios + operator docs        |
| Observability         | `tests/test_observability.py`               | KPIs, alerts, recommendations              |
| Security review       | `tests/test_security_review.py`             | Threats, controls, PII classes             |
| AI review             | `tests/test_ai_review.py`                   | Secret/unsafe import/long-function checks  |
| Scorecard             | `tests/test_scorecard.py`                   | Weighted scoring, blocking logic           |
| Handoff generator     | `tests/test_handoff.py`                     | Document completeness and structure        |
| Workflow engine       | `tests/test_workflow.py`                    | Retry policy, step validation, config      |
| Timeline & queries    | `tests/test_timeline.py`                    | Event/audit queries, metrics, search       |
| Qualification         | `tests/test_qualification.py`               | Channel/volume/timeline feasibility, score |
| E2E Aurora scenario   | `tests/test_e2e_aurora.py`                  | Register, consent, workflow, audit timeline|
| Placeholders          | `tests/test_placeholder.py`                 | Basic import checks                        |

## Representative evidence

- **Resilience:** Each scenario in `FailureScenario` has operator documentation and is repeatable/safe (`test_resilience_lab.py`).
- **Security:** Threats map to controls; findings and recommendations are generated (`test_security_review.py`).
- **AI:** Deterministic checks detect secrets, unsafe imports, and long functions; AI-use log is sanitized (`test_ai_review.py`).
- **Handoff:** All 11 documents are generated with metadata (`test_handoff.py`).

## How to reproduce

```bash
cd /workspaces/Sash
pip install -r requirements.txt
python -m pytest tests/ -v --tb=short
```

Attach the pytest output and this report to any release artifact or review package.
