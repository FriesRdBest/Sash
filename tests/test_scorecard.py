"""Unit tests for the production-readiness scorecard engine."""

import pytest

from src.scorecard.engine import (
    CheckDefinition,
    CheckStatus,
    Dimension,
    ScorecardEngine,
)


@pytest.fixture
def engine():
    checks = [
        CheckDefinition(
            id="api_contract_tests",
            dimension=Dimension.API,
            name="API contract tests",
            description="Contract tests pass.",
            weight=0.6,
            blocking=True,
            evidence_path="tests/test_api.py",
        ),
        CheckDefinition(
            id="api_error_handling",
            dimension=Dimension.API,
            name="API error handling",
            description="Errors handled.",
            weight=0.4,
        ),
        CheckDefinition(
            id="webhook_signature_verification",
            dimension=Dimension.WEBHOOK,
            name="Webhook signature verification",
            description="Signatures verified.",
            weight=1.0,
            blocking=True,
        ),
    ]
    return ScorecardEngine(checks=checks)


def test_all_pass_yields_high_score(engine):
    result = engine.run(test_results={})
    assert result.overall_score > 80
    assert not result.blocking_items


def test_blocking_failure_marks_item_and_lowers_score(engine):
    result = engine.run(test_results={"api_contract_tests": False})
    assert any(c.definition.id == "api_contract_tests" for c in result.blocking_items)
    assert result.overall_score < 100


def test_dimension_scores_reflect_weights(engine):
    result = engine.run(test_results={"api_contract_tests": False})
    api_dim = next(d for d in result.dimensions if d.dimension == Dimension.API)
    # One blocking fail (weight 0.6) and one pass (weight 0.4)
    expected_api_score = (0.4 * 100.0) / (0.6 + 0.4)
    assert abs(api_dim.score - expected_api_score) < 0.01


def test_webhook_blocking_failure_is_recorded(engine):
    result = engine.run(test_results={"webhook_signature_verification": False})
    webhook_dim = next(d for d in result.dimensions if d.dimension == Dimension.WEBHOOK)
    assert webhook_dim.blocking_count == 1
    assert any(
        c.definition.id == "webhook_signature_verification" and c.status == CheckStatus.BLOCKING
        for c in webhook_dim.checks
    )


def test_result_to_dict_is_complete(engine):
    result = engine.run(test_results={})
    data = result.to_dict()
    assert "run_id" in data
    assert "overall_score" in data
    assert "dimensions" in data
    assert "blocking_items" in data
    assert "started_at" in data
    assert "completed_at" in data


def test_markdown_report_contains_key_sections(engine):
    result = engine.run(test_results={"api_contract_tests": False})
    md = result.to_markdown()
    assert "# Production Readiness Scorecard" in md
    assert "## Blocking items" in md
    assert "## Dimension scores" in md
    assert "api_contract_tests" in md
