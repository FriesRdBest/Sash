"""End-to-end Aurora happy path: registration → consent → verification → audit."""

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from src.domain.models import AuditRecord, Customer, WorkflowExecution
from src.integration.lab import ExecutionResult, IntegrationLab
from src.persistence.sqlite_repo import (
    audit_repo,
    customer_repo,
    event_repo,
    execution_repo,
)
from src.workflow.designer import WorkflowConfig

logger = logging.getLogger(__name__)


@dataclass
class AuroraSession:
    """Represents one end-to-end verification session."""

    correlation_id: str
    customer: Customer
    workflow: WorkflowConfig
    execution_result: ExecutionResult
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
    status: str = "running"  # running, completed, failed


def register_customer(
    phone_number: str, email: str | None = None, external_id: str | None = None
) -> Customer:
    """Register a new customer and persist."""
    customer = Customer(phone_number=phone_number, email=email, external_id=external_id)
    customer_repo.save(customer.id, customer.model_dump(mode="json"))
    logger.info(
        f"[AURORA] Registered customer {customer.id} with phone {customer.phone_number}"
    )
    return customer


def record_consent(
    customer: Customer,
    granted: bool,
    channel: str = "sms",
    correlation_id: str | None = None,
) -> AuditRecord:
    """Record consent audit entry."""
    audit = AuditRecord(
        entity_type="customer",
        entity_id=customer.id,
        action="consent_recorded",
        old_state=None,
        new_state={"granted": granted, "channel": channel},
        actor="user",
        correlation_id=correlation_id or customer.correlation_id,
    )
    audit_repo.record(audit.model_dump(mode="json"))
    logger.info(
        f"[AURORA] Consent recorded for customer {customer.id}: granted={granted}"
    )
    return audit


def run_verification(
    customer: Customer,
    workflow: WorkflowConfig,
    correlation_id: str | None = None,
    mode: str = "mock",
) -> ExecutionResult:
    """Run verification workflow and persist events/execution."""
    lab = IntegrationLab(mode=mode)
    result = lab.execute_workflow(
        workflow, customer_phone=customer.phone_number, correlation_id=correlation_id
    )

    # Persist execution
    execution = WorkflowExecution(
        workflow_id=workflow.id,
        customer_id=customer.id,
        status="completed" if result.success else "failed",
        metadata={
            "correlation_id": result.correlation_id,
            "total_latency_ms": result.total_latency_ms,
        },
    )
    execution_repo.save(execution.id, execution.model_dump(mode="json"))

    # Persist events
    for event in result.events:
        event_repo.save(event.id, event.model_dump(mode="json"))

    # Audit: verification completed
    audit = AuditRecord(
        entity_type="workflow_execution",
        entity_id=execution.id,
        action="verification_completed",
        old_state=None,
        new_state={"success": result.success, "events_count": len(result.events)},
        actor="system",
        correlation_id=result.correlation_id,
    )
    audit_repo.record(audit.model_dump(mode="json"))

    logger.info(
        f"[AURORA] Verification completed for customer {customer.id} with success={result.success}"
    )
    return result


def create_aurora_session(
    phone_number: str,
    workflow: WorkflowConfig,
    email: str | None = None,
    external_id: str | None = None,
    mode: str = "mock",
) -> AuroraSession:
    """Run the full Aurora happy path and return a session object."""
    from uuid import uuid4

    correlation_id = str(uuid4())

    # 1. Register customer
    customer = register_customer(
        phone_number=phone_number, email=email, external_id=external_id
    )

    # 2. Record consent
    record_consent(
        customer,
        granted=True,
        channel=workflow.steps[0].channel,
        correlation_id=correlation_id,
    )

    # 3. Run verification
    result = run_verification(
        customer, workflow, correlation_id=correlation_id, mode=mode
    )

    session = AuroraSession(
        correlation_id=correlation_id,
        customer=customer,
        workflow=workflow,
        execution_result=result,
        completed_at=datetime.now(timezone.utc),
        status="completed" if result.success else "failed",
    )

    logger.info(
        f"[AURORA] Session completed: {session.correlation_id} status={session.status}"
    )
    return session


def get_audit_timeline(correlation_id: str) -> list[dict[str, Any]]:
    """Get audit timeline for a correlation ID."""
    records = audit_repo.get_by_correlation(correlation_id)
    timeline = []
    for r in records:
        timeline.append(
            {
                "timestamp": r["timestamp"],
                "entity_type": r["entity_type"],
                "entity_id": r["entity_id"],
                "action": r["action"],
                "actor": r["actor"],
                "summary": f"{r['action']} on {r['entity_type']} ({r['entity_id'][:8]}...)",
            }
        )
    return timeline


def get_session_details(correlation_id: str) -> dict[str, Any]:
    """Get detailed session summary for a correlation ID."""
    # Find execution by metadata correlation_id (simple scan for demo)
    executions = execution_repo.get_all()
    execution = None
    for ex in executions:
        if ex.get("metadata", {}).get("correlation_id") == correlation_id:
            execution = ex
            break

    if not execution:
        return {"error": "Execution not found"}

    events = event_repo.find_by(
        execution_id=execution["workflow_id"]
    )  # approximate for demo
    audit = get_audit_timeline(correlation_id)

    return {
        "execution": execution,
        "events": events,
        "audit": audit,
    }
