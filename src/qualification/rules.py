"""Feasibility rules and readiness scoring for engagement qualification."""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class RuleResult:
    """Result of a single feasibility rule check."""

    rule_name: str
    passed: bool
    score_impact: int
    message: str
    risk_level: RiskLevel = RiskLevel.LOW


SUPPORTED_CHANNELS = {"sms", "whatsapp", "email", "voice"}
HIGH_VOLUME_THRESHOLD = 50000
CRITICAL_VOLUME_THRESHOLD = 100000
MIN_TIMELINE_DAYS = 7
SHORT_TIMELINE_DAYS = 14


def check_channel_support(channels: list[str]) -> RuleResult:
    """Check if all requested channels are supported."""
    unsupported = set(channels) - SUPPORTED_CHANNELS

    if unsupported:
        return RuleResult(
            rule_name="Channel Support",
            passed=False,
            score_impact=-30,
            message=f"Unsupported channels: {', '.join(unsupported)}",
            risk_level=RiskLevel.CRITICAL,
        )

    return RuleResult(
        rule_name="Channel Support",
        passed=True,
        score_impact=0,
        message="All channels supported",
        risk_level=RiskLevel.LOW,
    )


def check_volume_feasibility(expected_volume: int) -> RuleResult:
    """Check if expected volume is feasible."""
    if expected_volume >= CRITICAL_VOLUME_THRESHOLD:
        return RuleResult(
            rule_name="Volume Feasibility",
            passed=False,
            score_impact=-40,
            message=f"Volume {expected_volume:,} exceeds critical threshold ({CRITICAL_VOLUME_THRESHOLD:,})",
            risk_level=RiskLevel.CRITICAL,
        )

    if expected_volume >= HIGH_VOLUME_THRESHOLD:
        return RuleResult(
            rule_name="Volume Feasibility",
            passed=True,
            score_impact=-10,
            message=f"High volume ({expected_volume:,}) - requires capacity planning",
            risk_level=RiskLevel.HIGH,
        )

    return RuleResult(
        rule_name="Volume Feasibility",
        passed=True,
        score_impact=0,
        message=f"Volume {expected_volume:,} is within normal range",
        risk_level=RiskLevel.LOW,
    )


def check_timeline_feasibility(timeline_days: int) -> RuleResult:
    """Check if timeline is feasible."""
    if timeline_days < MIN_TIMELINE_DAYS:
        return RuleResult(
            rule_name="Timeline Feasibility",
            passed=False,
            score_impact=-50,
            message=f"Timeline {timeline_days} days is below minimum ({MIN_TIMELINE_DAYS} days)",
            risk_level=RiskLevel.CRITICAL,
        )

    if timeline_days <= SHORT_TIMELINE_DAYS:
        return RuleResult(
            rule_name="Timeline Feasibility",
            passed=True,
            score_impact=-15,
            message=f"Short timeline ({timeline_days} days) - accelerated delivery required",
            risk_level=RiskLevel.HIGH,
        )

    return RuleResult(
        rule_name="Timeline Feasibility",
        passed=True,
        score_impact=0,
        message=f"Timeline {timeline_days} days is feasible",
        risk_level=RiskLevel.LOW,
    )


def check_priority_alignment(priority: str) -> RuleResult:
    """Check if priority aligns with resource availability."""
    if priority == "critical":
        return RuleResult(
            rule_name="Priority Alignment",
            passed=True,
            score_impact=-5,
            message="Critical priority - dedicated resources required",
            risk_level=RiskLevel.MEDIUM,
        )

    return RuleResult(
        rule_name="Priority Alignment",
        passed=True,
        score_impact=0,
        message=f"Priority '{priority}' is manageable",
        risk_level=RiskLevel.LOW,
    )


def check_use_case_clarity(use_case: str) -> RuleResult:
    """Check if use case is clearly defined."""
    if not use_case or len(use_case) < 10:
        return RuleResult(
            rule_name="Use Case Clarity",
            passed=False,
            score_impact=-20,
            message="Use case is not clearly defined",
            risk_level=RiskLevel.HIGH,
        )

    return RuleResult(
        rule_name="Use Case Clarity",
        passed=True,
        score_impact=0,
        message="Use case is clearly defined",
        risk_level=RiskLevel.LOW,
    )


def run_all_checks(engagement_data: dict[str, Any]) -> list[RuleResult]:
    """Run all feasibility checks on an engagement."""
    checks = [
        check_channel_support(engagement_data.get("channels", [])),
        check_volume_feasibility(engagement_data.get("expected_volume", 0)),
        check_timeline_feasibility(engagement_data.get("timeline_days", 30)),
        check_priority_alignment(engagement_data.get("priority", "medium")),
        check_use_case_clarity(engagement_data.get("use_case", "")),
    ]
    return checks


def calculate_readiness_score(rule_results: list[RuleResult]) -> int:
    """Calculate overall readiness score (0-100)."""
    base_score = 100

    for result in rule_results:
        base_score += result.score_impact

    return max(0, min(100, base_score))


def get_risk_flags(rule_results: list[RuleResult]) -> list[dict[str, Any]]:
    """Extract risk flags from rule results."""
    flags = []

    for result in rule_results:
        if result.risk_level in (RiskLevel.HIGH, RiskLevel.CRITICAL):
            flags.append(
                {
                    "rule": result.rule_name,
                    "level": result.risk_level.value,
                    "message": result.message,
                }
            )

    return flags
