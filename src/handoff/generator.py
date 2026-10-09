"""Handoff package generator: operator-ready documentation and artifacts."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class HandoffPackage:
    run_id: str
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    architecture_md: str = ""
    workflow_definition: dict[str, Any] = field(default_factory=dict)
    configuration_guide_md: str = ""
    deployment_instructions_md: str = ""
    runbook_md: str = ""
    test_evidence_md: str = ""
    alert_guide_md: str = ""
    ownership_matrix_md: str = ""
    rollback_plan_md: str = ""
    training_checklist_md: str = ""
    open_risk_register_md: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "generated_at": self.generated_at.isoformat(),
            "architecture_md": self.architecture_md,
            "workflow_definition": self.workflow_definition,
            "configuration_guide_md": self.configuration_guide_md,
            "deployment_instructions_md": self.deployment_instructions_md,
            "runbook_md": self.runbook_md,
            "test_evidence_md": self.test_evidence_md,
            "alert_guide_md": self.alert_guide_md,
            "ownership_matrix_md": self.ownership_matrix_md,
            "rollback_plan_md": self.rollback_plan_md,
            "training_checklist_md": self.training_checklist_md,
            "open_risk_register_md": self.open_risk_register_md,
            "metadata": self.metadata,
        }


def _architecture_md() -> str:
    return """# Architecture Overview

Sash is a production-readiness accelerator for programmable customer communications.
It provides workflow design, deterministic failure injection, observability, security review,
and AI-assisted code review capabilities.

## High-level components

- **Domain models**: Customer, Workflow, Engagement, Event, AuditRecord.
- **Workflow engine**: Executes multi-step communication workflows (SMS, email, etc.).
- **Integration layer**: Mock and real provider integrations with retry/backoff.
- **Resilience lab**: Deterministic failure scenarios (timeout, rate limit, webhook outage, etc.).
- **Observability console**: KPIs, alerts, recommendations, and event timeline.
- **Security & compliance review**: Threat model, controls, PII classification.
- **AI engineering review**: Deterministic static checks with optional AI explanations.
- **Scorecard**: Weighted production-readiness score with blocking items.

## Data flow (simplified)

1. Operator designs a workflow in the Streamlit UI.
2. Workflow is executed against a provider (mock or real) via the integration layer.
3. Events are stored and correlated by `correlation_id`.
4. Observability and scorecard components read events to produce health and readiness views.
5. Security and AI reviews analyze code and configuration to produce findings and recommendations.

## Trust boundaries

- **UI (Streamlit)**: Trusted internal tool; not exposed directly to customers.
- **API/Integration layer**: Authenticated by service credentials; secrets managed externally.
- **Event store**: Internal persistence; access controlled; PII redaction applied where possible.
- **Webhook receiver**: Public endpoint; signature verification and replay protection required.
"""


def _workflow_definition() -> dict[str, Any]:
    # Derive a sample workflow from the existing designer.
    # In a real handoff, this would be exported from the live system.
    return {
        "name": "Onboarding sequence (sample)",
        "description": "Demo workflow used across tests and UI examples.",
        "steps": [
            {
                "channel": "sms",
                "template": "Welcome to Sash!",
                "order": 0,
            },
            {
                "channel": "email",
                "template": "Your Sash onboarding email.",
                "order": 1,
            },
        ],
        "notes": "Replace templates and channels with production values before go-live.",
    }


def _configuration_guide_md() -> str:
    return """# Configuration Guide

This document describes required configuration and secrets for running Sash.

## Environment variables

Required (example names; adjust to your environment):

- `PROVIDER_API_KEY`: API key for the primary SMS/email provider.
- `WEBHOOK_SECRET`: Shared secret for verifying webhook signatures.
- `DATABASE_URL`: Connection string for the event/audit database.
- `ENVIRONMENT`: `dev`, `staging`, or `prod`.

## Secrets management

- Do not commit secrets to version control.
- Use your platform's secret manager (e.g., GitHub Secrets, AWS Secrets Manager).
- Rotate secrets on a regular cadence and after any suspected leakage.

## Feature flags (optional)

- `ENABLE_AI_EXPLANATIONS`: Toggle AI-assisted explanations in AI Review.
- `ENABLE_MOCK_PROVIDER`: Use mock provider for demos and tests.
"""


def _deployment_instructions_md() -> str:
    return """# Deployment Instructions

## Prerequisites

- Python 3.11+
- Access to a secret manager and database service
- CI/CD system (e.g., GitHub Actions)

## Steps

1. **Clone the repository** and ensure you are on the desired release tag/commit.
2. **Configure secrets** in your CI/CD and runtime environment (see Configuration Guide).
3. **Run tests**:
   ```bash
   python -m pytest tests/
   ```
4. **Deploy**: Use your existing pipeline (e.g., GitHub Actions, Kubernetes manifests).
   - Ensure database migrations are applied.
   - Verify health checks and readiness probes.
5. **Validate**:
   - Run a sample workflow from the UI.
   - Check the Observability console for events.
   - Confirm alerts are firing as expected.

## Rollback

See the Rollback Plan document for detailed steps.
"""


def _runbook_md() -> str:
    return """# Operational Runbook

This runbook covers common incidents and responses.

## Elevated failure rate

- **Symptom**: Observability shows increased `Failed` events.
- **Actions**:
  1. Open the Observability console and inspect the Failure breakdown.
  2. Check provider status page and logs for rate limits or outages.
  3. If needed, enable fallback channels or throttle traffic.
  4. Document the incident and update the open-risk register if systemic.

## Webhook failures

- **Symptom**: Dead-letter queue growing; callbacks not processed.
- **Actions**:
  1. Verify webhook signature configuration and clock skew.
  2. Inspect dead-letter entries for correlation IDs.
  3. Replay failed callbacks after fixing root cause.

## Secret leakage suspicion

- **Symptom**: AI/Security review flags hard-coded secrets.
- **Actions**:
  1. Rotate the affected secret immediately.
  2. Remove the secret from code/history (consult security team).
  3. Re-run Security Review to confirm resolution.
"""


def _test_evidence_md() -> str:
    return """# Test Evidence

Key test suites (run via `pytest`):

- **Resilience lab**: `tests/test_resilience_lab.py`
  - Validates failure scenarios and operator documentation.
- **Observability**: `tests/test_observability.py`
  - Validates KPIs, alerts, and recommendations.
- **Security review**: `tests/test_security_review.py`
  - Validates threat model, controls, and PII classification.
- **AI review**: `tests/test_ai_review.py`
  - Validates deterministic checks and AI-use logging.
- **Scorecard**: `tests/test_scorecard.py`
  - Validates weighted readiness scoring and blocking logic.

To generate evidence:

```bash
python -m pytest tests/ -v --tb=short
```

Attach the pytest output and any generated reports to your release artifact.
"""


def _alert_guide_md() -> str:
    return """# Alert Guide

This guide describes what to monitor and how alerts are raised.

## Key metrics

- Total events, Sent, Delivered, Failed (Observability KPIs)
- Failure breakdown by reason (e.g., timeout, rate limit)
- Dead-letter count
- Scorecard overall score and blocking items

## Alert channels

- Configure alerts in your monitoring system (e.g., Prometheus + Alertmanager, Datadog).
- Route critical alerts to on-call paging; non-critical to chat.

## Example alert conditions

- `failed_events > 5` in 5 minutes → Warning
- `failed_events > 20` in 5 minutes → Critical
- `scorecard_overall_score < 70` → Warning for release readiness
- `security_review_findings.critical > 0` → Block release
"""


def _ownership_matrix_md() -> str:
    return """# Ownership Matrix

Explicit ownership for key areas (update with real names/teams):

| Area                       | Owner (Team/Person) | Backup          |
|---------------------------|---------------------|-----------------|
| Workflow engine           | Platform Eng        | SRE             |
| Integration/provider layer| Integrations Eng    | Platform Eng    |
| Observability & alerts    | SRE                 | Platform Eng    |
| Security & compliance     | Security Eng        | Tech Lead       |
| AI engineering review     | Tech Lead           | Security Eng    |
| Handoff & documentation   | FDE / PM            | Tech Lead       |

Ensure on-call and escalation paths are documented in your internal wiki.
"""


def _rollback_plan_md() -> str:
    return """# Rollback Plan

This plan describes how to revert to a known-good state.

## When to roll back

- Critical production incidents tied to a recent change.
- Security findings that cannot be mitigated immediately.
- Data corruption or unrecoverable state issues.

## Steps

1. **Identify the last known-good release** (tag/commit).
2. **Freeze changes** to the affected service.
3. **Revert deployment**:
   - For blue/green: switch traffic to the previous blue/green slot.
   - For canary: reduce canary percentage to 0 and re-deploy stable version.
4. **Validate**:
   - Run smoke tests and a sample workflow.
   - Confirm Observability KPIs return to normal.
5. **Post-mortem**:
   - Document root cause and corrective actions.
   - Update the open-risk register and runbook as needed.
"""


def _training_checklist_md() -> str:
    return """# Training Checklist

Use this checklist to onboard new operators and engineers.

## For operators

- [ ] Understand the Architecture Overview.
- [ ] Can run a workflow from the UI and interpret events.
- [ ] Can read the Observability console and respond to alerts.
- [ ] Know how to use the Runbook for common incidents.
- [ ] Understand how to request access and secrets.

## For engineers

- [ ] Can run the full test suite and interpret results.
- [ ] Understand the Scorecard and Security Review outputs.
- [ ] Can add a new failure scenario to the Resilience Lab.
- [ ] Can extend the AI Review checks safely.
- [ ] Know the rollback and deployment procedures.
"""


def _open_risk_register_md() -> str:
    # In a real system, this would aggregate from security/ai reviews.
    return """# Open Risk Register

This register tracks known risks and their mitigation status.

## Example risks (update with real data)

- **R001**: PII redaction is partial (Security Review control C002).
  - **Status**: In progress
  - **Owner**: Security Eng
  - **Mitigation**: Enhance redaction rules and add tests.

- **R002**: Retention policy not automated (Security Review control C005).
  - **Status**: Planned
  - **Owner**: Platform Eng
  - **Mitigation**: Implement deletion jobs and document retention windows.

- **R003**: AI explanations are advisory only; operators might over-trust.
  - **Status**: Mitigated (UI labels, training)
  - **Owner**: Tech Lead
  - **Mitigation**: Reinforce training and UI warnings.
"""


def generate_handoff_package() -> HandoffPackage:
    """Generate a complete handoff package for Sash."""
    return HandoffPackage(
        run_id=str(uuid4()),
        architecture_md=_architecture_md(),
        workflow_definition=_workflow_definition(),
        configuration_guide_md=_configuration_guide_md(),
        deployment_instructions_md=_deployment_instructions_md(),
        runbook_md=_runbook_md(),
        test_evidence_md=_test_evidence_md(),
        alert_guide_md=_alert_guide_md(),
        ownership_matrix_md=_ownership_matrix_md(),
        rollback_plan_md=_rollback_plan_md(),
        training_checklist_md=_training_checklist_md(),
        open_risk_register_md=_open_risk_register_md(),
        metadata={
            "version": "0.16.0",
            "phase": "16 - Handoff Package Generator",
            "project": "Sash",
        },
    )
