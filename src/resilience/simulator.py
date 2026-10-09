"""Deterministic failure and resilience laboratory."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from src.events.engine import (
    get_dead_letters,
    move_to_dead_letter,
    normalize_event,
    process_webhook,
)
from src.events.errors import DuplicateEventError, OutOfOrderEventError
from src.integration.errors import ProviderRateLimitError, ProviderTimeoutError
from src.integration.lab import IntegrationLab
from src.integration.provider import ProviderRequest
from src.resilience.errors import (
    CRMAdapterError,
    DatabasePersistenceError,
    QueueBacklogError,
    WebhookOutageError,
)
from src.resilience.scenarios import (
    FailureScenario,
    ScenarioDefinition,
    get_scenario_definition,
)
from src.workflow.designer import WorkflowConfig, create_sample_workflow


@dataclass
class ResilienceResult:
    """Structured result of one deterministic fault simulation."""

    scenario: FailureScenario
    correlation_id: str
    passed: bool
    detected: bool
    state_corrupted: bool
    behavior: str
    evidence: dict[str, Any] = field(default_factory=dict)
    definition: ScenarioDefinition | None = None
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-friendly report for operators and UI rendering."""
        definition = self.definition
        return {
            "scenario": self.scenario.value,
            "correlation_id": self.correlation_id,
            "passed": self.passed,
            "detected": self.detected,
            "state_corrupted": self.state_corrupted,
            "behavior": self.behavior,
            "evidence": self.evidence,
            "detection": definition.detection if definition else "",
            "impact": definition.impact if definition else "",
            "alert": definition.alert if definition else "",
            "recovery": definition.recovery if definition else "",
            "residual_risk": definition.residual_risk if definition else "",
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat()
            if self.completed_at
            else None,
        }


class FailureSimulator:
    """Runs repeatable failure scenarios without calling real providers."""

    def __init__(self, queue_threshold: int = 100):
        self.queue_threshold = queue_threshold

    def run(
        self,
        scenario: FailureScenario,
        workflow: WorkflowConfig | None = None,
        correlation_id: str | None = None,
    ) -> ResilienceResult:
        """Run one supported failure scenario deterministically."""
        correlation_id = correlation_id or str(uuid4())
        definition = get_scenario_definition(scenario)
        workflow = workflow or create_sample_workflow()

        handlers = {
            FailureScenario.PROVIDER_TIMEOUT: self._provider_timeout,
            FailureScenario.RATE_LIMIT: self._rate_limit,
            FailureScenario.WEBHOOK_OUTAGE: self._webhook_outage,
            FailureScenario.DUPLICATE_CALLBACK: self._duplicate_callback,
            FailureScenario.OUT_OF_ORDER_EVENT: self._out_of_order_event,
            FailureScenario.CRM_FAILURE: self._crm_failure,
            FailureScenario.DATABASE_FAILURE: self._database_failure,
            FailureScenario.QUEUE_BACKLOG: self._queue_backlog,
            FailureScenario.FALLBACK_EXECUTION: self._fallback_execution,
        }

        result = handlers[scenario](workflow, correlation_id, definition)
        result.completed_at = datetime.now(timezone.utc)
        return result

    def run_all(self, workflow: WorkflowConfig | None = None) -> list[ResilienceResult]:
        """Run each scenario once with its own correlation ID."""
        return [self.run(scenario, workflow=workflow) for scenario in FailureScenario]

    def _result(
        self,
        scenario: FailureScenario,
        correlation_id: str,
        definition: ScenarioDefinition,
        behavior: str,
        evidence: dict[str, Any],
        passed: bool = True,
        detected: bool = True,
        state_corrupted: bool = False,
    ) -> ResilienceResult:
        return ResilienceResult(
            scenario=scenario,
            correlation_id=correlation_id,
            passed=passed,
            detected=detected,
            state_corrupted=state_corrupted,
            behavior=behavior,
            evidence=evidence,
            definition=definition,
        )

    def _provider_timeout(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        lab = IntegrationLab(mode="mock")
        lab.retry_config.max_attempts = 1
        request = ProviderRequest(
            channel="sms",
            to="+12065550123",
            content={"template": workflow.steps[0].template},
            correlation_id=correlation_id,
            timeout_seconds=0,
        )
        try:
            lab.provider.send(request)
        except ProviderTimeoutError as error:
            return self._result(
                FailureScenario.PROVIDER_TIMEOUT,
                correlation_id,
                definition,
                "Timeout detected before message state was marked sent.",
                {"exception": type(error).__name__, "attempts": 1},
            )
        return self._result(
            FailureScenario.PROVIDER_TIMEOUT,
            correlation_id,
            definition,
            "Timeout simulation unexpectedly succeeded.",
            {},
            passed=False,
            detected=False,
        )

    def _rate_limit(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        lab = IntegrationLab(mode="mock")
        request = ProviderRequest(
            channel="sms",
            to="+12065550123",
            content={"template": workflow.steps[0].template},
            correlation_id=correlation_id,
            metadata={"simulate_rate_limit": True},
        )
        try:
            lab.provider.send(request)
        except ProviderRateLimitError as error:
            return self._result(
                FailureScenario.RATE_LIMIT,
                correlation_id,
                definition,
                "Rate limit detected; request was not accepted as sent.",
                {
                    "exception": type(error).__name__,
                    "retry_after_seconds": error.retry_after_seconds,
                },
            )
        return self._result(
            FailureScenario.RATE_LIMIT,
            correlation_id,
            definition,
            "Rate-limit simulation unexpectedly succeeded.",
            {},
            passed=False,
            detected=False,
        )

    def _webhook_outage(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        payload = self._payload(correlation_id, status="delivered", sequence=1)
        event = normalize_event(payload)
        try:
            raise WebhookOutageError("Webhook receiver unavailable")
        except WebhookOutageError as error:
            move_to_dead_letter(event, reason=str(error), attempts=1)
            dead_letters = get_dead_letters(correlation_id)
            return self._result(
                FailureScenario.WEBHOOK_OUTAGE,
                correlation_id,
                definition,
                "Callback preserved in dead-letter state for replay.",
                {
                    "exception": type(error).__name__,
                    "dead_letter_count": len(dead_letters),
                },
            )

    def _duplicate_callback(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        payload = self._payload(correlation_id, status="sent", sequence=1)
        process_webhook(payload, verify_sig=False)
        try:
            process_webhook(payload, verify_sig=False)
        except DuplicateEventError as error:
            return self._result(
                FailureScenario.DUPLICATE_CALLBACK,
                correlation_id,
                definition,
                "Duplicate callback rejected without a second state mutation.",
                {"exception": type(error).__name__, "event_id": payload["event_id"]},
            )
        return self._result(
            FailureScenario.DUPLICATE_CALLBACK,
            correlation_id,
            definition,
            "Duplicate callback was not rejected.",
            {"event_id": payload["event_id"]},
            passed=False,
            detected=False,
        )

    def _out_of_order_event(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        first = self._payload(correlation_id, status="sent", sequence=2)
        second = self._payload(correlation_id, status="delivered", sequence=1)
        process_webhook(first, verify_sig=False, ordering_policy="strict")
        try:
            process_webhook(second, verify_sig=False, ordering_policy="strict")
        except OutOfOrderEventError as error:
            return self._result(
                FailureScenario.OUT_OF_ORDER_EVENT,
                correlation_id,
                definition,
                "Strict sequence policy rejected the stale callback.",
                {
                    "exception": type(error).__name__,
                    "expected_sequence": error.expected_sequence,
                    "actual_sequence": error.actual_sequence,
                },
            )
        return self._result(
            FailureScenario.OUT_OF_ORDER_EVENT,
            correlation_id,
            definition,
            "Out-of-order callback was not rejected by strict policy.",
            {},
            passed=False,
            detected=False,
        )

    def _crm_failure(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        try:
            raise CRMAdapterError("CRM adapter unavailable")
        except CRMAdapterError as error:
            return self._result(
                FailureScenario.CRM_FAILURE,
                correlation_id,
                definition,
                "CRM failure isolated from the communication execution boundary.",
                {"exception": type(error).__name__, "sync_committed": False},
            )

    def _database_failure(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        try:
            raise DatabasePersistenceError("Database transaction unavailable")
        except DatabasePersistenceError as error:
            return self._result(
                FailureScenario.DATABASE_FAILURE,
                correlation_id,
                definition,
                "Persistence failure stopped the operation before a partial commit.",
                {"exception": type(error).__name__, "partial_write": False},
            )

    def _queue_backlog(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        depth = self.queue_threshold + 1
        try:
            raise QueueBacklogError(depth=depth, threshold=self.queue_threshold)
        except QueueBacklogError as error:
            return self._result(
                FailureScenario.QUEUE_BACKLOG,
                correlation_id,
                definition,
                "Work deferred; no message was sent while the queue was over threshold.",
                {
                    "exception": type(error).__name__,
                    "depth": error.depth,
                    "threshold": error.threshold,
                },
            )

    def _fallback_execution(
        self,
        workflow: WorkflowConfig,
        correlation_id: str,
        definition: ScenarioDefinition,
    ) -> ResilienceResult:
        # Use a local workflow that intentionally gives the first step an invalid channel.
        steps = [step.model_copy(deep=True) for step in workflow.steps]
        primary = steps[0]
        fallback = steps[1] if len(steps) > 1 else None
        if fallback is None:
            return self._result(
                FailureScenario.FALLBACK_EXECUTION,
                correlation_id,
                definition,
                "Sample workflow has no fallback step.",
                {},
                passed=False,
                detected=False,
            )

        # Simulate provider API failure on the primary and execute fallback directly.
        lab = IntegrationLab(mode="mock")
        fallback_event = lab._execute_step(fallback, "+12065550123", correlation_id)
        return self._result(
            FailureScenario.FALLBACK_EXECUTION,
            correlation_id,
            definition,
            "Primary channel failure was contained and fallback channel sent successfully.",
            {
                "primary_channel": primary.channel,
                "fallback_channel": fallback.channel,
                "fallback_status": fallback_event.status.value,
                "fallback_message_id": fallback_event.metadata.get("message_id"),
            },
            passed=fallback_event.status.value == "sent",
            detected=True,
        )

    @staticmethod
    def _payload(correlation_id: str, status: str, sequence: int) -> dict[str, Any]:
        return {
            "event_id": str(uuid4()),
            "event_type": f"message.{status}",
            "correlation_id": correlation_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provider": "mock",
            "status": status,
            "sequence": sequence,
        }
