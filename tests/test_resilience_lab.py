"""Unit tests for the deterministic failure and resilience laboratory."""

import pytest

from src.resilience.scenarios import SCENARIOS, FailureScenario
from src.resilience.simulator import FailureSimulator
from src.workflow.designer import create_sample_workflow


@pytest.fixture
def simulator():
    """Provide a resilience simulator with deterministic thresholds."""
    return FailureSimulator(queue_threshold=3)


@pytest.mark.parametrize("scenario", list(FailureScenario))
def test_every_scenario_has_operator_documentation(scenario):
    definition = SCENARIOS[scenario]
    assert definition.detection
    assert definition.expected_behavior
    assert definition.impact
    assert definition.alert
    assert definition.recovery
    assert definition.residual_risk


@pytest.mark.parametrize("scenario", list(FailureScenario))
def test_every_scenario_is_repeatable_and_safe(simulator, scenario):
    result = simulator.run(scenario, workflow=create_sample_workflow())
    assert result.scenario == scenario
    assert result.detected is True
    assert result.state_corrupted is False
    assert result.completed_at is not None
    assert result.definition is not None


def test_provider_timeout_documents_safe_failure(simulator):
    result = simulator.run(FailureScenario.PROVIDER_TIMEOUT)
    assert result.passed is True
    assert result.evidence["exception"] == "ProviderTimeoutError"
    assert "Timeout" in result.behavior


def test_rate_limit_preserves_unsent_state(simulator):
    result = simulator.run(FailureScenario.RATE_LIMIT)
    assert result.passed is True
    assert result.evidence["retry_after_seconds"] == 5


def test_webhook_outage_creates_dead_letter(simulator):
    result = simulator.run(FailureScenario.WEBHOOK_OUTAGE)
    assert result.passed is True
    assert result.evidence["dead_letter_count"] >= 1


def test_duplicate_callback_does_not_mutate_twice(simulator):
    result = simulator.run(FailureScenario.DUPLICATE_CALLBACK)
    assert result.passed is True
    assert result.evidence["exception"] == "DuplicateEventError"


def test_out_of_order_callback_is_explicit(simulator):
    result = simulator.run(FailureScenario.OUT_OF_ORDER_EVENT)
    assert result.passed is True
    assert result.evidence["exception"] == "OutOfOrderEventError"


def test_crm_and_database_faults_are_isolated(simulator):
    crm = simulator.run(FailureScenario.CRM_FAILURE)
    database = simulator.run(FailureScenario.DATABASE_FAILURE)
    assert crm.evidence["sync_committed"] is False
    assert database.evidence["partial_write"] is False


def test_queue_backlog_exposes_threshold(simulator):
    result = simulator.run(FailureScenario.QUEUE_BACKLOG)
    assert result.passed is True
    assert result.evidence["depth"] > result.evidence["threshold"]


def test_fallback_execution_reaches_secondary_channel(simulator):
    result = simulator.run(FailureScenario.FALLBACK_EXECUTION)
    assert result.passed is True
    assert result.evidence["fallback_channel"] == "email"
    assert result.evidence["fallback_status"] == "sent"


def test_report_contains_all_operator_fields(simulator):
    report = simulator.run(FailureScenario.PROVIDER_TIMEOUT).to_dict()
    required = {
        "scenario",
        "correlation_id",
        "passed",
        "detected",
        "state_corrupted",
        "behavior",
        "detection",
        "impact",
        "alert",
        "recovery",
        "residual_risk",
    }
    assert required.issubset(report)
