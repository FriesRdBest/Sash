"""Unit tests for engagement qualification."""

from src.qualification.assess import assess_engagement
from src.qualification.rules import (
    RiskLevel,
    calculate_readiness_score,
    check_channel_support,
    check_priority_alignment,
    check_timeline_feasibility,
    check_use_case_clarity,
    check_volume_feasibility,
)


class TestChannelSupport:
    """Tests for channel support checks."""

    def test_supported_channels(self):
        result = check_channel_support(["sms", "email"])
        assert result.passed is True
        assert result.score_impact == 0

    def test_unsupported_channel(self):
        result = check_channel_support(["sms", "telegram"])
        assert result.passed is False
        assert result.risk_level == RiskLevel.CRITICAL


class TestVolumeFeasibility:
    """Tests for volume feasibility checks."""

    def test_normal_volume(self):
        result = check_volume_feasibility(1000)
        assert result.passed is True
        assert result.score_impact == 0

    def test_high_volume(self):
        result = check_volume_feasibility(60000)
        assert result.passed is True
        assert result.risk_level == RiskLevel.HIGH

    def test_critical_volume(self):
        result = check_volume_feasibility(150000)
        assert result.passed is False
        assert result.risk_level == RiskLevel.CRITICAL


class TestTimelineFeasibility:
    """Tests for timeline feasibility checks."""

    def test_normal_timeline(self):
        result = check_timeline_feasibility(30)
        assert result.passed is True
        assert result.score_impact == 0

    def test_short_timeline(self):
        result = check_timeline_feasibility(10)
        assert result.passed is True
        assert result.risk_level == RiskLevel.HIGH

    def test_impossible_timeline(self):
        result = check_timeline_feasibility(3)
        assert result.passed is False
        assert result.risk_level == RiskLevel.CRITICAL


class TestReadinessScore:
    """Tests for readiness score calculation."""

    def test_perfect_score(self):
        results = [
            check_channel_support(["sms"]),
            check_volume_feasibility(1000),
            check_timeline_feasibility(30),
            check_priority_alignment("medium"),
            check_use_case_clarity("User verification"),
        ]

        score = calculate_readiness_score(results)
        assert score == 100

    def test_reduced_score(self):
        results = [
            check_volume_feasibility(60000),  # -10
            check_timeline_feasibility(10),  # -15
        ]

        score = calculate_readiness_score(results)
        assert score == 75


class TestQualificationAssessment:
    """Tests for complete qualification assessment."""

    def test_proceed_decision(self):
        engagement = {
            "customer_name": "Alice",
            "company": "Acme",
            "use_case": "User verification",
            "channels": ["sms"],
            "expected_volume": 1000,
            "timeline_days": 30,
            "priority": "medium",
        }

        assessment = assess_engagement(engagement)

        assert assessment.decision == "proceed"
        assert assessment.score >= 80

    def test_decline_decision(self):
        engagement = {
            "customer_name": "Bob",
            "company": "BadFit",
            "use_case": "",
            "channels": ["telegram"],
            "expected_volume": 200000,
            "timeline_days": 2,
            "priority": "low",
        }

        assessment = assess_engagement(engagement)

        assert assessment.decision == "decline"

    def test_conditions_generated(self):
        engagement = {
            "customer_name": "Carol",
            "company": "HighVol",
            "use_case": "Mass notifications",
            "channels": ["sms", "whatsapp"],
            "expected_volume": 60000,
            "timeline_days": 10,
            "priority": "critical",
        }

        assessment = assess_engagement(engagement)

        assert len(assessment.conditions) > 0
        assert "Capacity planning review required" in assessment.conditions

    def test_export_json(self):
        engagement = {
            "customer_name": "Test",
            "company": "TestCo",
            "use_case": "Testing",
            "channels": ["sms"],
            "expected_volume": 1000,
            "timeline_days": 30,
            "priority": "medium",
        }

        assessment = assess_engagement(engagement)
        json_output = assessment.to_json()

        assert "score" in json_output
        assert "decision" in json_output
        assert "engagement" in json_output


class TestRiskFlags:
    """Tests for risk flag extraction."""

    def test_high_risk_flagged(self):
        engagement = {
            "customer_name": "Risk",
            "company": "RiskyCo",
            "use_case": "High volume alerts",
            "channels": ["sms"],
            "expected_volume": 150000,
            "timeline_days": 30,
            "priority": "medium",
        }

        assessment = assess_engagement(engagement)

        assert len(assessment.risk_flags) > 0
        assert any(f["level"] == "critical" for f in assessment.risk_flags)
