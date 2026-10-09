"""Resilience laboratory scenario definitions and reporting contracts."""

from dataclasses import dataclass
from enum import Enum


class FailureScenario(str, Enum):
    """Repeatable failure scenarios supported by the resilience laboratory."""

    PROVIDER_TIMEOUT = "provider_timeout"
    RATE_LIMIT = "rate_limit"
    WEBHOOK_OUTAGE = "webhook_outage"
    DUPLICATE_CALLBACK = "duplicate_callback"
    OUT_OF_ORDER_EVENT = "out_of_order_event"
    CRM_FAILURE = "crm_failure"
    DATABASE_FAILURE = "database_failure"
    QUEUE_BACKLOG = "queue_backlog"
    FALLBACK_EXECUTION = "fallback_execution"


@dataclass(frozen=True)
class ScenarioDefinition:
    """Operator-facing explanation for a fault scenario."""

    scenario: FailureScenario
    title: str
    detection: str
    expected_behavior: str
    impact: str
    alert: str
    recovery: str
    residual_risk: str


SCENARIOS: dict[FailureScenario, ScenarioDefinition] = {
    FailureScenario.PROVIDER_TIMEOUT: ScenarioDefinition(
        scenario=FailureScenario.PROVIDER_TIMEOUT,
        title="Provider timeout",
        detection="ProviderTimeoutError and retry-attempt telemetry.",
        expected_behavior="Bounded retries occur; the execution fails safely after exhaustion.",
        impact="Verification is delayed or fails without a configured fallback.",
        alert="Provider timeout retry budget exhausted.",
        recovery="Retry after provider recovery or run a configured fallback channel.",
        residual_risk="The upstream provider can accept a late request after the client timed out.",
    ),
    FailureScenario.RATE_LIMIT: ScenarioDefinition(
        scenario=FailureScenario.RATE_LIMIT,
        title="Provider rate limit",
        detection="ProviderRateLimitError with a retry-after interval.",
        expected_behavior="Requests are deferred with bounded backoff; state remains unchanged.",
        impact="Delivery is delayed while capacity is constrained.",
        alert="Provider rate limit encountered.",
        recovery="Drain deferred work after retry-after or switch to an approved fallback.",
        residual_risk="Sustained throttling can breach delivery-time objectives.",
    ),
    FailureScenario.WEBHOOK_OUTAGE: ScenarioDefinition(
        scenario=FailureScenario.WEBHOOK_OUTAGE,
        title="Webhook receiver outage",
        detection="Receiver availability failure during callback processing.",
        expected_behavior="Callback is preserved as a dead-letter candidate rather than silently dropped.",
        impact="Final delivery status is temporarily unknown to operators.",
        alert="Webhook receiver unavailable; callback queued for recovery.",
        recovery="Restore receiver and replay the callback from the dead-letter store.",
        residual_risk="Delayed callbacks may arrive out of order after recovery.",
    ),
    FailureScenario.DUPLICATE_CALLBACK: ScenarioDefinition(
        scenario=FailureScenario.DUPLICATE_CALLBACK,
        title="Duplicate callback",
        detection="Idempotency key hit raises DuplicateEventError.",
        expected_behavior="Duplicate is rejected; no second audit mutation occurs.",
        impact="No customer impact; the callback is safely ignored.",
        alert="Duplicate callback detected for an existing event ID.",
        recovery="No replay required; inspect idempotency retention if duplicates persist.",
        residual_risk="Retention expiry can permit an old callback to be processed again.",
    ),
    FailureScenario.OUT_OF_ORDER_EVENT: ScenarioDefinition(
        scenario=FailureScenario.OUT_OF_ORDER_EVENT,
        title="Out-of-order event",
        detection="Sequence policy detects an event sequence lower than the processed sequence.",
        expected_behavior="Strict mode rejects it; relaxed mode records an explicit warning.",
        impact="Displayed message state can lag or require reconciliation.",
        alert="Out-of-order provider callback received.",
        recovery="Reconcile with provider state or replay in the correct order.",
        residual_risk="Providers may not supply a globally reliable ordering sequence.",
    ),
    FailureScenario.CRM_FAILURE: ScenarioDefinition(
        scenario=FailureScenario.CRM_FAILURE,
        title="CRM adapter failure",
        detection="Typed CRM adapter error from the integration boundary.",
        expected_behavior="Communication state remains traceable; customer-sync work fails independently.",
        impact="CRM can be temporarily stale while verification still completes.",
        alert="CRM synchronization failure.",
        recovery="Retry or replay the CRM update after the service recovers.",
        residual_risk="Customer-support agents may see stale CRM status until replay succeeds.",
    ),
    FailureScenario.DATABASE_FAILURE: ScenarioDefinition(
        scenario=FailureScenario.DATABASE_FAILURE,
        title="Database persistence failure",
        detection="Typed persistence failure before state is committed.",
        expected_behavior="Execution stops before unsafe partial persistence; no corrupt record is written.",
        impact="Journey status cannot be committed until persistence recovers.",
        alert="Database write failure detected.",
        recovery="Restore storage, retry the idempotent operation, and reconcile provider outcome.",
        residual_risk="A provider may have accepted a message while local persistence was unavailable.",
    ),
    FailureScenario.QUEUE_BACKLOG: ScenarioDefinition(
        scenario=FailureScenario.QUEUE_BACKLOG,
        title="Queue backlog",
        detection="Configured backlog threshold is exceeded.",
        expected_behavior="New work is deferred and backlog state is exposed to operators.",
        impact="Noncritical delivery is delayed; latency grows predictably.",
        alert="Queue backlog threshold exceeded.",
        recovery="Scale consumers, reduce ingress, then drain queued work in order.",
        residual_risk="Long queues can make time-sensitive verification codes expire.",
    ),
    FailureScenario.FALLBACK_EXECUTION: ScenarioDefinition(
        scenario=FailureScenario.FALLBACK_EXECUTION,
        title="Primary channel failure with fallback",
        detection="Primary provider failure exhausts its retry budget.",
        expected_behavior="Primary failure is audited and the configured fallback channel is attempted.",
        impact="Verification may be delayed but completes through the fallback when available.",
        alert="Primary channel failed; fallback execution initiated.",
        recovery="Confirm fallback delivery and retain primary failure for provider review.",
        residual_risk="Fallback channels may have different consent, reachability, or latency constraints.",
    ),
}


def get_scenario_definition(scenario: FailureScenario) -> ScenarioDefinition:
    """Return the documented contract for a supported scenario."""
    return SCENARIOS[scenario]
