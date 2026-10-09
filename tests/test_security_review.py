"""Unit tests for the security and compliance review module."""

import pytest

from src.security.review import (
    ControlStatus,
    SecurityReviewResult,
    run_security_review,
)


@pytest.fixture
def review():
    return run_security_review()


def test_review_has_threats_and_controls(review):
    assert len(review.threats) > 0
    assert len(review.controls) > 0
    assert len(review.pii_classes) > 0


def test_findings_derived_from_control_gaps(review):
    missing_or_partial = [
        c for c in review.controls if c.status in {ControlStatus.MISSING, ControlStatus.PARTIAL}
    ]
    assert len(missing_or_partial) > 0
    assert len(review.findings) >= len(missing_or_partial)


def test_recommendations_present_for_gaps(review):
    assert len(review.recommendations) > 0
    for rec in review.recommendations:
        assert rec["title"]
        assert rec["action"]
        assert rec["priority"] in {"low", "medium", "high"}


def test_result_to_dict_is_complete(review):
    data = review.to_dict()
    assert "run_id" in data
    assert "generated_at" in data
    assert "threats" in data
    assert "controls" in data
    assert "pii_classes" in data
    assert "findings" in data
    assert "recommendations" in data


def test_markdown_report_contains_key_sections(review):
    md = review.to_markdown()
    assert "# Security & Compliance Review" in md
    assert "## Threat model" in md
    assert "## Controls" in md
    assert "## PII classification" in md
