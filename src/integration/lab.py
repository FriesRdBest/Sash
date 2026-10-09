"""Integration laboratory: execute workflows with retry, timeout, and audit."""

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from src.domain.models import Event, EventStatus, WorkflowConfig, WorkflowStep
from src.integration.errors import (
    IntegrationError,
    MessageDeliveryError,
    ProviderRateLimitError,
    ProviderTimeoutError,
)
from src.integration.provider import Provider, ProviderRequest, ProviderResponse, create_provider

logger = logging.getLogger(__name__)


@dataclass
class ExecutionResult:
    """Result of executing a workflow."""

    workflow_id: str
    correlation_id: str
    success: bool
    events: list[Event] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    total_latency_ms: float = 0.0
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None


@dataclass
class RetryConfig:
    """Retry configuration for integration calls."""

    max_attempts: int = 3
    base_delay_seconds: float = 1.0
    max_delay_seconds: float = 30.0
    timeout_seconds: float = 10.0


class IntegrationLab:
    """Execute workflows against providers with retry, timeout, and audit."""

    def __init__(self, provider: Provider | None = None, mode: str = "mock"):
        self.provider = provider or create_provider(mode=mode)
        self.retry_config = RetryConfig()

    def execute_workflow(
        self,
        workflow: WorkflowConfig,
        customer_phone: str,
        correlation_id: str | None = None,
    ) -> ExecutionResult:
        """Execute a workflow for a given customer."""
        from uuid import uuid4

        correlation_id = correlation_id or str(uuid4())
        result = ExecutionResult(
            workflow_id=workflow.id,
            correlation_id=correlation_id,
            success=False,
        )

        logger.info(f"[INTEGRATION_LAB] Starting workflow {workflow.name} for {correlation_id}")

        for step in workflow.steps:
            try:
                event = self._execute_step(step, customer_phone, correlation_id)
                result.events.append(event)
                result.total_latency_ms += event.metadata.get("latency_ms", 0.0)

                if event.status == EventStatus.FAILED:
                    result.errors.append(f"Step {step.name} failed: {event.metadata.get('failure_reason', 'unknown')}")
                    if step.fallback_to:
                        logger.info(f"[INTEGRATION_LAB] Triggering fallback for step {step.name}")
                        fallback_step = next((s for s in workflow.steps if s.id == step.fallback_to), None)
                        if fallback_step:
                            fallback_event = self._execute_step(fallback_step, customer_phone, correlation_id)
                            result.events.append(fallback_event)
                            if fallback_event.status == EventStatus.SENT:
                                result.success = True
                                break
                    else:
                        break
            except IntegrationError as e:
                logger.error(f"[INTEGRATION_LAB] Integration error: {e}")
                result.errors.append(str(e))
                event = Event(
                    execution_id=correlation_id,
                    step_index=workflow.steps.index(step),
                    channel=step.channel,
                    status=EventStatus.FAILED,
                    metadata={"failure_reason": str(e)},
                )
                result.events.append(event)
                break

        result.completed_at = datetime.now(timezone.utc)
        result.success = result.success or all(e.status in {EventStatus.SENT, EventStatus.DELIVERED} for e in result.events)
        logger.info(f"[INTEGRATION_LAB] Completed workflow {workflow.name} with success={result.success}")
        return result

    def _execute_step(self, step: WorkflowStep, to: str, correlation_id: str) -> Event:
        """Execute a single workflow step with retry and timeout."""
        event = Event(
            execution_id=correlation_id,
            step_index=0,
            channel=step.channel,
            status=EventStatus.PENDING,
            content={"template": step.template},
        )

        last_error: Exception | None = None
        for attempt in range(self.retry_config.max_attempts):
            try:
                request = ProviderRequest(
                    channel=step.channel,
                    to=to,
                    content={"template": step.template},
                    correlation_id=correlation_id,
                    timeout_seconds=self.retry_config.timeout_seconds,
                    metadata={"step_name": step.name, "attempt": attempt + 1},
                )
                response = self.provider.send(request)
                event.status = response.status
                event.metadata.update(
                    {
                        "message_id": response.message_id,
                        "latency_ms": response.latency_ms,
                        "attempt": attempt + 1,
                    }
                )
                if response.success:
                    return event
                else:
                    last_error = Exception(response.error_message or "Unknown provider error")
            except ProviderTimeoutError as e:
                last_error = e
                logger.warning(f"[INTEGRATION_LAB] Timeout on attempt {attempt + 1} for step {step.name}")
            except ProviderRateLimitError as e:
                last_error = e
                delay = min(e.retry_after_seconds, self.retry_config.max_delay_seconds)
                logger.warning(f"[INTEGRATION_LAB] Rate limited, waiting {delay}s")
                time.sleep(delay)
            except IntegrationError as e:
                last_error = e
                logger.error(f"[INTEGRATION_LAB] Integration error: {e}")
                break

            if attempt < self.retry_config.max_attempts - 1:
                delay = min(self.retry_config.base_delay_seconds * (2 ** attempt), self.retry_config.max_delay_seconds)
                logger.info(f"[INTEGRATION_LAB] Retrying in {delay}s (attempt {attempt + 1}/{self.retry_config.max_attempts})")
                time.sleep(delay)

        event.status = EventStatus.FAILED
        event.metadata["failure_reason"] = str(last_error) if last_error else "Unknown error"
        raise MessageDeliveryError(channel=step.channel, reason=event.metadata["failure_reason"], last_error=last_error)


# Convenience function for simple usage
def run_workflow(
    workflow: WorkflowConfig,
    customer_phone: str,
    correlation_id: str | None = None,
    mode: str = "mock",
) -> ExecutionResult:
    """Run a workflow using the integration lab."""
    lab = IntegrationLab(mode=mode)
    return lab.execute_workflow(workflow, customer_phone, correlation_id)
