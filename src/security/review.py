"""Security and compliance review: trust boundaries, privacy, secrets, and controls."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ControlStatus(str, Enum):
    IMPLEMENTED = "implemented"
    PARTIAL = "partial"
    MISSING = "missing"
    NOT_APPLICABLE = "not_applicable"


@dataclass
class Threat:
    id: str
    title: str
    description: str
    risk_level: RiskLevel
    affected_asset: str  # e.g. "PII in events", "API keys", "Webhook signatures"
    mitre_id: str | None = None  # optional MITRE ATT&CK mapping


@dataclass
class Control:
    id: str
    title: str
    description: str
    status: ControlStatus
    evidence_path: str = ""  # e.g. "src/integration/provider.py"
    linked_threats: list[str] = field(default_factory=list)  # threat IDs


@dataclass
class PIIClass:
    field_name: str
    category: str  # e.g. "contact", "identifier", "content"
    sensitivity: str  # low, medium, high
    redaction_rule: str  # e.g. "mask_all", "hash", "allow_with_consent"


@dataclass
class SecurityReviewResult:
    run_id: str
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    threats: list[Threat] = field(default_factory=list)
    controls: list[Control] = field(default_factory=list)
    pii_classes: list[PIIClass] = field(default_factory=list)
    findings: list[dict[str, Any]] = field(default_factory=list)
    recommendations: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "generated_at": self.generated_at.isoformat(),
            "threats": [
                {
                    "id": t.id,
                    "title": t.title,
                    "description": t.description,
                    "risk_level": t.risk_level.value,
                    "affected_asset": t.affected_asset,
                    "mitre_id": t.mitre_id,
                }
                for t in self.threats
            ],
            "controls": [
                {
                    "id": c.id,
                    "title": c.title,
                    "description": c.description,
                    "status": c.status.value,
                    "evidence_path": c.evidence_path,
                    "linked_threats": c.linked_threats,
                }
                for c in self.controls
            ],
            "pii_classes": [
                {
                    "field_name": p.field_name,
                    "category": p.category,
                    "sensitivity": p.sensitivity,
                    "redaction_rule": p.redaction_rule,
                }
                for p in self.pii_classes
            ],
            "findings": self.findings,
            "recommendations": self.recommendations,
            "metadata": self.metadata,
        }

    def to_markdown(self) -> str:
        lines = [
            "# Security & Compliance Review",
            "",
            f"**Run ID:** `{self.run_id}`",
            f"**Generated:** {self.generated_at.isoformat()}",
            "",
        ]

        lines.append("## Threat model")
        lines.append("")
        for t in self.threats:
            lines.append(
                f"- **{t.title}** (`{t.id}`, {t.risk_level.value}): {t.description} "
                f"(asset: {t.affected_asset})"
            )
        lines.append("")

        lines.append("## Controls")
        lines.append("")
        for c in self.controls:
            icon = {
                "implemented": "✅",
                "partial": "🟠",
                "missing": "❌",
                "not_applicable": "⚪",
            }.get(c.status.value, "❓")
            lines.append(
                f"- {icon} **{c.title}** (`{c.id}`): {c.description} "
                f"(status: {c.status.value})"
            )
        lines.append("")

        lines.append("## PII classification")
        lines.append("")
        for p in self.pii_classes:
            lines.append(
                f"- **{p.field_name}** ({p.category}, {p.sensitivity}): {p.redaction_rule}"
            )
        lines.append("")

        if self.findings:
            lines.append("## Findings")
            lines.append("")
            for f in self.findings:
                lines.append(f"- {f['title']}: {f['description']}")
            lines.append("")

        if self.recommendations:
            lines.append("## Recommendations")
            lines.append("")
            for r in self.recommendations:
                lines.append(f"- {r['title']}: {r['action']}")
            lines.append("")

        return "\n".join(lines)


def default_threats() -> list[Threat]:
    return [
        Threat(
            id="T001",
            title="Secret leakage via code or logs",
            description="API keys or credentials committed or logged in plaintext.",
            risk_level=RiskLevel.HIGH,
            affected_asset="API keys and secrets",
            mitre_id="T1552",
        ),
        Threat(
            id="T002",
            title="PII exposure in events or logs",
            description="Personal data stored or logged without redaction or minimization.",
            risk_level=RiskLevel.HIGH,
            affected_asset="PII in events and audit logs",
        ),
        Threat(
            id="T003",
            title="Webhook replay / tampering",
            description="Attacker replays or modifies webhook callbacks.",
            risk_level=RiskLevel.MEDIUM,
            affected_asset="Webhook integrity and ordering",
            mitre_id="T1557",
        ),
        Threat(
            id="T004",
            title="Unauthorized API access",
            description="Missing or weak authentication/authorization on API endpoints.",
            risk_level=RiskLevel.HIGH,
            affected_asset="API boundary",
        ),
        Threat(
            id="T005",
            title="Excessive data retention",
            description="Events and PII retained longer than necessary or policy.",
            risk_level=RiskLevel.MEDIUM,
            affected_asset="Event store and backups",
        ),
        Threat(
            id="T006",
            title="Cross-region data transfer without controls",
            description="PII transferred across regions without legal/technical controls.",
            risk_level=RiskLevel.MEDIUM,
            affected_asset="Data residency and compliance",
        ),
    ]


def default_controls() -> list[Control]:
    return [
        Control(
            id="C001",
            title="Secrets managed via environment / secret manager",
            description="No secrets committed; loaded from environment or managed service.",
            status=ControlStatus.IMPLEMENTED,
            evidence_path=".github/workflows/ci.yml",
            linked_threats=["T001"],
        ),
        Control(
            id="C002",
            title="PII redaction in logs and events",
            description="Sensitive fields are redacted or hashed before logging/storage.",
            status=ControlStatus.PARTIAL,
            evidence_path="src/audit/log.py",
            linked_threats=["T002"],
        ),
        Control(
            id="C003",
            title="Webhook signature verification",
            description="All webhook callbacks verify cryptographic signatures and timestamps.",
            status=ControlStatus.IMPLEMENTED,
            evidence_path="src/events/engine.py",
            linked_threats=["T003"],
        ),
        Control(
            id="C004",
            title="Authentication and authorization on API",
            description="API endpoints require valid auth and enforce least privilege.",
            status=ControlStatus.PARTIAL,
            evidence_path="src/api/README.md",
            linked_threats=["T004"],
        ),
        Control(
            id="C005",
            title="Retention policy and deletion jobs",
            description="Defined retention windows and automated deletion of old events/PII.",
            status=ControlStatus.MISSING,
            evidence_path="docs/retention.md",
            linked_threats=["T005"],
        ),
        Control(
            id="C006",
            title="Regional data handling and transfer controls",
            description="Data residency rules enforced; cross-region transfers documented.",
            status=ControlStatus.PARTIAL,
            evidence_path="docs/data-residency.md",
            linked_threats=["T006"],
        ),
    ]


def default_pii_classes() -> list[PIIClass]:
    return [
        PIIClass(
            field_name="phone_number",
            category="contact",
            sensitivity="medium",
            redaction_rule="mask_all",
        ),
        PIIClass(
            field_name="email",
            category="contact",
            sensitivity="medium",
            redaction_rule="mask_all",
        ),
        PIIClass(
            field_name="customer_external_id",
            category="identifier",
            sensitivity="low",
            redaction_rule="allow_with_consent",
        ),
        PIIClass(
            field_name="message_content",
            category="content",
            sensitivity="high",
            redaction_rule="hash",
        ),
    ]


def run_security_review() -> SecurityReviewResult:
    """Run a default security & compliance review for Sash."""
    threats = default_threats()
    controls = default_controls()
    pii_classes = default_pii_classes()

    findings: list[dict[str, Any]] = []
    recommendations: list[dict[str, Any]] = []

    # Derive findings from control gaps.
    for c in controls:
        if c.status == ControlStatus.MISSING:
            findings.append(
                {
                    "title": f"Missing control: {c.title}",
                    "description": c.description,
                    "risk": "high",
                    "linked_threats": c.linked_threats,
                }
            )
            recommendations.append(
                {
                    "title": f"Implement {c.title}",
                    "action": f"Add {c.description} and link to evidence.",
                    "priority": "high",
                }
            )
        elif c.status == ControlStatus.PARTIAL:
            findings.append(
                {
                    "title": f"Partial control: {c.title}",
                    "description": c.description,
                    "risk": "medium",
                    "linked_threats": c.linked_threats,
                }
            )
            recommendations.append(
                {
                    "title": f"Complete {c.title}",
                    "action": f"Strengthen {c.description} to fully mitigated.",
                    "priority": "medium",
                }
            )

    return SecurityReviewResult(
        run_id=str(uuid4()),
        threats=threats,
        controls=controls,
        pii_classes=pii_classes,
        findings=findings,
        recommendations=recommendations,
        metadata={"version": "0.14.0", "phase": "14 - Security & Compliance Review"},
    )
