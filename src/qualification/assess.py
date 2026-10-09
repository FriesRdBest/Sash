"""Product-fit assessment and decision engine for engagement qualification."""

import json
from datetime import datetime, timezone
from typing import Any

from src.qualification.rules import (
    RiskLevel,
    calculate_readiness_score,
    get_risk_flags,
    run_all_checks,
)


class QualificationAssessment:
    """Complete qualification assessment for an engagement."""

    def __init__(self, engagement_data: dict[str, Any]):
        self.engagement = engagement_data
        self.rule_results = run_all_checks(engagement_data)
        self.score = calculate_readiness_score(self.rule_results)
        self.risk_flags = get_risk_flags(self.rule_results)
        self.decision = self._determine_decision()
        self.conditions = self._determine_conditions()

    def _determine_decision(self) -> str:
        """Determine qualification decision."""
        # Check for any critical failures
        critical_failures = [
            r
            for r in self.rule_results
            if not r.passed and r.risk_level == RiskLevel.CRITICAL
        ]

        if critical_failures:
            return "decline"

        if self.score >= 80:
            return "proceed"
        elif self.score >= 60:
            return "proceed_with_conditions"
        else:
            return "decline"

    def _determine_conditions(self) -> list[str]:
        """Determine conditions for proceeding."""
        conditions = []

        if self.engagement.get("expected_volume", 0) >= 50000:
            conditions.append("Capacity planning review required")

        if self.engagement.get("timeline_days", 30) <= 14:
            conditions.append("Accelerated delivery plan required")

        if "whatsapp" in self.engagement.get("channels", []):
            conditions.append("WhatsApp Business API approval required")

        if self.engagement.get("priority") == "critical":
            conditions.append("Dedicated engineering resources required")

        return conditions

    def to_dict(self) -> dict[str, Any]:
        """Convert assessment to dictionary."""
        return {
            "engagement": self.engagement,
            "score": self.score,
            "decision": self.decision,
            "conditions": self.conditions,
            "risk_flags": self.risk_flags,
            "rule_results": [
                {
                    "rule": r.rule_name,
                    "passed": r.passed,
                    "impact": r.score_impact,
                    "message": r.message,
                    "risk_level": r.risk_level.value,
                }
                for r in self.rule_results
            ],
            "assessed_at": datetime.now(timezone.utc).isoformat(),
        }

    def to_json(self, indent: int = 2) -> str:
        """Export assessment as JSON."""
        return json.dumps(self.to_dict(), indent=indent)

    def get_recommendation(self) -> str:
        """Get human-readable recommendation."""
        if self.decision == "proceed":
            return f"✅ PROCEED - Score {self.score}/100. No critical risks identified."
        elif self.decision == "proceed_with_conditions":
            conditions_str = "; ".join(self.conditions)
            return f"⚠️ PROCEED WITH CONDITIONS - Score {self.score}/100. Conditions: {conditions_str}"
        else:
            critical = [r for r in self.rule_results if not r.passed]
            reasons = "; ".join([r.message for r in critical])
            return f"❌ DECLINE - Score {self.score}/100. Critical issues: {reasons}"


def assess_engagement(engagement_data: dict[str, Any]) -> QualificationAssessment:
    """Assess an engagement and return qualification result."""
    return QualificationAssessment(engagement_data)


def assess_and_export(engagement_data: dict[str, Any]) -> str:
    """Assess engagement and return JSON report."""
    assessment = assess_engagement(engagement_data)
    return assessment.to_json()
