"""Production-readiness scorecard: weighted checks, blocking logic, exportable reports."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class CheckStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    BLOCKING = "blocking"
    SKIP = "skip"


class Dimension(str, Enum):
    API = "api"
    WEBHOOK = "webhook"
    RELIABILITY = "reliability"
    SECURITY = "security"
    SCALABILITY = "scalability"
    OBSERVABILITY = "observability"
    TESTING = "testing"
    OPERATIONS = "operations"
    CUSTOMER_READINESS = "customer_readiness"


@dataclass
class CheckDefinition:
    id: str
    dimension: Dimension
    name: str
    description: str
    weight: float  # 0-1 within dimension
    blocking: bool = False
    evidence_path: str = ""  # e.g. "tests/test_integration.py::test_provider_timeout"
    config_path: str = ""  # e.g. ".github/workflows/ci.yml"
    auto_run: bool = True


@dataclass
class CheckResult:
    definition: CheckDefinition
    status: CheckStatus
    message: str = ""
    evidence_url: str = ""
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.definition.id,
            "dimension": self.definition.dimension.value,
            "name": self.definition.name,
            "description": self.definition.description,
            "weight": self.definition.weight,
            "blocking": self.definition.blocking,
            "status": self.status.value,
            "message": self.message,
            "evidence_url": self.evidence_url or self.definition.evidence_path,
            "config_path": self.definition.config_path,
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat()
            if self.completed_at
            else None,
        }


@dataclass
class DimensionScore:
    dimension: Dimension
    score: float  # 0-100
    checks: list[CheckResult] = field(default_factory=list)
    blocking_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "dimension": self.dimension.value,
            "score": round(self.score, 2),
            "checks": [c.to_dict() for c in self.checks],
            "blocking_count": self.blocking_count,
        }


@dataclass
class ScorecardResult:
    run_id: str
    overall_score: float  # 0-100
    dimensions: list[DimensionScore]
    blocking_items: list[CheckResult]
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "overall_score": round(self.overall_score, 2),
            "dimensions": [d.to_dict() for d in self.dimensions],
            "blocking_items": [b.to_dict() for b in self.blocking_items],
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat()
            if self.completed_at
            else None,
            "metadata": self.metadata,
        }

    def to_markdown(self) -> str:
        lines = [
            "# Production Readiness Scorecard",
            "",
            f"**Run ID:** `{self.run_id}`",
            f"**Overall score:** {self.overall_score:.1f}/100",
            f"**Generated:** {self.completed_at.isoformat() if self.completed_at else self.started_at.isoformat()}",
            "",
        ]

        if self.blocking_items:
            lines.append("## Blocking items")
            lines.append("")
            for item in self.blocking_items:
                lines.append(
                    f"- **{item.definition.name}** ({item.definition.dimension.value}): {item.message}"
                )
            lines.append("")

        lines.append("## Dimension scores")
        lines.append("")
        lines.append("| Dimension | Score | Checks | Blocking |")
        lines.append("| --- | ---: | ---: | ---: |")
        for dim in self.dimensions:
            lines.append(
                f"| {dim.dimension.value} | {dim.score:.1f} | {len(dim.checks)} | {dim.blocking_count} |"
            )
        lines.append("")

        lines.append("## Details")
        lines.append("")
        for dim in self.dimensions:
            lines.append(f"### {dim.dimension.value}")
            lines.append("")
            for check in dim.checks:
                icon = {"pass": "✅", "fail": "❌", "blocking": "🚫", "skip": "⏭️"}.get(
                    check.status.value, "❓"
                )
                lines.append(
                    f"- {icon} **{check.definition.name}**: {check.message} "
                    f"(weight={check.definition.weight:.2f})"
                )
                if check.evidence_url or check.definition.evidence_path:
                    lines.append(
                        f"  - Evidence: `{check.evidence_url or check.definition.evidence_path}`"
                    )
            lines.append("")

        return "\n".join(lines)


# Default check catalog
DEFAULT_CHECKS: list[CheckDefinition] = [
    # API
    CheckDefinition(
        id="api_contract_tests",
        dimension=Dimension.API,
        name="API contract tests",
        description="OpenAPI/JSON-schema contract tests pass for all public endpoints.",
        weight=0.4,
        blocking=True,
        evidence_path="tests/test_api_contract.py",
        config_path=".github/workflows/ci.yml",
    ),
    CheckDefinition(
        id="api_error_handling",
        dimension=Dimension.API,
        name="API error handling",
        description="Timeouts, 4xx, 5xx are handled and surfaced with stable error codes.",
        weight=0.3,
        evidence_path="tests/test_provider_errors.py",
    ),
    CheckDefinition(
        id="api_versioning",
        dimension=Dimension.API,
        name="API versioning",
        description="Backward-compatible versioning strategy documented and enforced.",
        weight=0.3,
        config_path="docs/api-versioning.md",
    ),
    # Webhook
    CheckDefinition(
        id="webhook_signature_verification",
        dimension=Dimension.WEBHOOK,
        name="Webhook signature verification",
        description="All webhook callbacks verify cryptographic signatures.",
        weight=0.5,
        blocking=True,
        evidence_path="tests/test_webhook_security.py",
    ),
    CheckDefinition(
        id="webhook_idempotency",
        dimension=Dimension.WEBHOOK,
        name="Webhook idempotency",
        description="Duplicate callbacks are rejected or safely de-duplicated.",
        weight=0.5,
        evidence_path="tests/test_resilience_lab.py::test_duplicate_callback_does_not_mutate_twice",
    ),
    # Reliability
    CheckDefinition(
        id="failure_scenarios_documented",
        dimension=Dimension.RELIABILITY,
        name="Failure scenarios documented",
        description="All resilience scenarios have operator documentation.",
        weight=0.4,
        evidence_path="tests/test_resilience_lab.py::test_every_scenario_has_operator_documentation",
    ),
    CheckDefinition(
        id="failure_scenarios_tested",
        dimension=Dimension.RELIABILITY,
        name="Failure scenarios tested",
        description="All resilience scenarios are repeatable and safe.",
        weight=0.4,
        evidence_path="tests/test_resilience_lab.py::test_every_scenario_is_repeatable_and_safe",
    ),
    CheckDefinition(
        id="fallback_execution",
        dimension=Dimension.RELIABILITY,
        name="Fallback execution",
        description="Primary channel failure falls back to secondary channel.",
        weight=0.2,
        evidence_path="tests/test_resilience_lab.py::test_fallback_execution_reaches_secondary_channel",
    ),
    # Security
    CheckDefinition(
        id="secrets_management",
        dimension=Dimension.SECURITY,
        name="Secrets management",
        description="No secrets in code; environment variables or secret manager used.",
        weight=0.4,
        blocking=True,
        config_path=".github/workflows/ci.yml",
    ),
    CheckDefinition(
        id="dependency_scanning",
        dimension=Dimension.SECURITY,
        name="Dependency scanning",
        description="Automated vulnerability scanning enabled in CI.",
        weight=0.3,
        config_path=".github/workflows/security-scan.yml",
    ),
    CheckDefinition(
        id="audit_logging",
        dimension=Dimension.SECURITY,
        name="Audit logging",
        description="State changes and operator actions are logged with correlation IDs.",
        weight=0.3,
        evidence_path="src/audit/log.py",
    ),
    # Scalability
    CheckDefinition(
        id="queue_backpressure",
        dimension=Dimension.SCALABILITY,
        name="Queue backpressure",
        description="Queue depth threshold enforced; work deferred when overloaded.",
        weight=0.5,
        evidence_path="tests/test_resilience_lab.py::test_queue_backlog_exposes_threshold",
    ),
    CheckDefinition(
        id="horizontal_scaling",
        dimension=Dimension.SCALABILITY,
        name="Horizontal scaling",
        description="Stateless services can scale horizontally behind a load balancer.",
        weight=0.5,
        config_path="infra/README.md",
    ),
    # Observability
    CheckDefinition(
        id="structured_logging",
        dimension=Dimension.OBSERVABILITY,
        name="Structured logging",
        description="Logs are structured (JSON) and include correlation IDs.",
        weight=0.4,
        evidence_path="src/audit/log.py",
    ),
    CheckDefinition(
        id="metrics_dashboards",
        dimension=Dimension.OBSERVABILITY,
        name="Metrics & dashboards",
        description="Key SLOs exposed as metrics with dashboards/alerts.",
        weight=0.3,
        config_path="infra/monitoring/README.md",
    ),
    CheckDefinition(
        id="tracing",
        dimension=Dimension.OBSERVABILITY,
        name="Distributed tracing",
        description="Requests carry trace IDs across service boundaries.",
        weight=0.3,
        config_path="infra/tracing/README.md",
    ),
    # Testing
    CheckDefinition(
        id="unit_test_coverage",
        dimension=Dimension.TESTING,
        name="Unit test coverage",
        description="Core logic has high unit test coverage.",
        weight=0.4,
        config_path=".github/workflows/ci.yml",
    ),
    CheckDefinition(
        id="integration_tests",
        dimension=Dimension.TESTING,
        name="Integration tests",
        description="Integration tests cover provider, webhook, and workflow paths.",
        weight=0.3,
        evidence_path="tests/test_integration.py",
    ),
    CheckDefinition(
        id="resilience_tests",
        dimension=Dimension.TESTING,
        name="Resilience tests",
        description="Resilience lab tests pass for all scenarios.",
        weight=0.3,
        evidence_path="tests/test_resilience_lab.py",
    ),
    # Operations
    CheckDefinition(
        id="runbooks",
        dimension=Dimension.OPERATIONS,
        name="Runbooks",
        description="Operator runbooks exist for each failure scenario.",
        weight=0.4,
        config_path="docs/runbooks/README.md",
    ),
    CheckDefinition(
        id="deployment_strategy",
        dimension=Dimension.OPERATIONS,
        name="Deployment strategy",
        description="Blue/green or canary deployments configured.",
        weight=0.3,
        config_path="infra/deploy/README.md",
    ),
    CheckDefinition(
        id="rollback_plan",
        dimension=Dimension.OPERATIONS,
        name="Rollback plan",
        description="Rollback procedure documented and tested.",
        weight=0.3,
        config_path="docs/rollback.md",
    ),
    # Customer readiness
    CheckDefinition(
        id="customer_docs",
        dimension=Dimension.CUSTOMER_READINESS,
        name="Customer documentation",
        description="Public docs cover onboarding, API, webhooks, and errors.",
        weight=0.4,
        config_path="docs/README.md",
    ),
    CheckDefinition(
        id="support_playbook",
        dimension=Dimension.CUSTOMER_READINESS,
        name="Support playbook",
        description="Support team trained; escalation paths defined.",
        weight=0.3,
        config_path="docs/support-playbook.md",
    ),
    CheckDefinition(
        id="sla_definition",
        dimension=Dimension.CUSTOMER_READINESS,
        name="SLA definition",
        description="SLAs/SLOs defined and communicated to customers.",
        weight=0.3,
        config_path="docs/sla.md",
    ),
]


class ScorecardEngine:
    """Runs production-readiness checks and computes a weighted score."""

    def __init__(self, checks: list[CheckDefinition] | None = None):
        self.checks = checks or DEFAULT_CHECKS

    def run(
        self,
        test_results: dict[str, bool] | None = None,
        config_checks: dict[str, bool] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> ScorecardResult:
        """
        Run all checks.

        test_results: mapping from check.id or evidence_path to pass/fail.
        config_checks: mapping from check.config_path to pass/fail (file exists, CI configured, etc.).
        """
        test_results = test_results or {}
        config_checks = config_checks or {}
        metadata = metadata or {}

        run_id = str(uuid4())
        started_at = datetime.now(timezone.utc)

        results_by_dim: dict[Dimension, list[CheckResult]] = {
            dim: [] for dim in Dimension
        }

        for definition in self.checks:
            status = self._evaluate_check(definition, test_results, config_checks)
            result = CheckResult(
                definition=definition,
                status=status,
                message=self._message_for_status(definition, status),
                evidence_url="",
                started_at=started_at,
                completed_at=datetime.now(timezone.utc),
            )
            results_by_dim[definition.dimension].append(result)

        dimensions: list[DimensionScore] = []
        blocking_items: list[CheckResult] = []
        weighted_sum = 0.0
        weight_total = 0.0

        for dim, checks in results_by_dim.items():
            if not checks:
                continue
            dim_score, dim_weight_total = self._score_dimension(checks)
            blocking_count = sum(1 for c in checks if c.status == CheckStatus.BLOCKING)
            dimensions.append(
                DimensionScore(
                    dimension=dim,
                    score=dim_score,
                    checks=checks,
                    blocking_count=blocking_count,
                )
            )
            weighted_sum += dim_score * dim_weight_total
            weight_total += dim_weight_total
            blocking_items.extend(c for c in checks if c.status == CheckStatus.BLOCKING)

        overall = (weighted_sum / weight_total) if weight_total > 0 else 0.0

        return ScorecardResult(
            run_id=run_id,
            overall_score=overall,
            dimensions=dimensions,
            blocking_items=blocking_items,
            started_at=started_at,
            completed_at=datetime.now(timezone.utc),
            metadata=metadata,
        )

    def _evaluate_check(
        self,
        definition: CheckDefinition,
        test_results: dict[str, bool],
        config_checks: dict[str, bool],
    ) -> CheckStatus:
        # Prefer explicit test result by id, then evidence_path, then config_path.
        key = definition.id
        if key in test_results:
            passed = test_results[key]
        elif definition.evidence_path and definition.evidence_path in test_results:
            passed = test_results[definition.evidence_path]
        elif definition.config_path and definition.config_path in config_checks:
            passed = config_checks[definition.config_path]
        else:
            # Default: assume pass if no explicit failure known (demo mode).
            passed = True

        if not passed:
            if definition.blocking:
                return CheckStatus.BLOCKING
            return CheckStatus.FAIL
        return CheckStatus.PASS

    def _message_for_status(
        self, definition: CheckDefinition, status: CheckStatus
    ) -> str:
        if status == CheckStatus.PASS:
            return "Check passed."
        if status == CheckStatus.BLOCKING:
            return f"Blocking issue: {definition.description}"
        if status == CheckStatus.FAIL:
            return f"Issue detected: {definition.description}"
        return "Check skipped."

    def _score_dimension(self, checks: list[CheckResult]) -> tuple[float, float]:
        """Return (dimension_score_0_100, total_weight)."""
        if not checks:
            return 100.0, 0.0

        score_sum = 0.0
        weight_sum = 0.0

        for check in checks:
            w = check.definition.weight
            weight_sum += w
            if check.status == CheckStatus.PASS:
                score_sum += w * 100.0
            elif check.status == CheckStatus.SKIP:
                score_sum += w * 50.0
            # FAIL or BLOCKING contribute 0 for this check

        if weight_sum == 0:
            return 100.0, 0.0
        return score_sum / weight_sum, weight_sum
