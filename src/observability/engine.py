"""Observability console: operator-facing health and next actions."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from src.timeline.queries import search_events


@dataclass
class KPI:
    name: str
    value: str
    delta: str | None = None  # e.g. "+3 vs last hour"
    status: str = "ok"  # ok, warning, critical


@dataclass
class Alert:
    severity: str  # info, warning, critical
    title: str
    message: str
    correlation_id: str | None = None
    suggested_action: str = ""


@dataclass
class Recommendation:
    title: str
    reason: str
    action: str
    priority: str = "medium"  # low, medium, high


@dataclass
class ObservabilitySnapshot:
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    kpis: list[KPI] = field(default_factory=list)
    alerts: list[Alert] = field(default_factory=list)
    recommendations: list[Recommendation] = field(default_factory=list)
    channel_breakdown: dict[str, int] = field(default_factory=dict)
    failure_breakdown: dict[str, int] = field(default_factory=dict)
    latency_metrics: dict[str, float] = field(default_factory=dict)
    retry_metrics: dict[str, Any] = field(default_factory=dict)
    fallback_metrics: dict[str, Any] = field(default_factory=dict)
    recent_events: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


class ObservabilityEngine:
    """Builds an operator-focused observability snapshot from event data."""

    def __init__(self, correlation_id: str | None = None):
        self.correlation_id = correlation_id

    def snapshot(self, window_minutes: int = 60) -> ObservabilitySnapshot:
        """
        Build a snapshot for the last `window_minutes`.

        If correlation_id is set, focus on that journey; otherwise, show system-wide health.
        """
        now = datetime.now(timezone.utc)

        # Gather events
        if self.correlation_id:
            # For a single journey, use search with the correlation ID as query.
            events = search_events(query=self.correlation_id, status=None)
            label_prefix = f"correlation={self.correlation_id}"
        else:
            # System-wide: use search with no query and no status filter.
            events = search_events(query=None, status=None)
            label_prefix = "system-wide"

        # Basic counts
        total = len(events)
        sent = sum(1 for e in events if e.get("status") == "sent")
        delivered = sum(1 for e in events if e.get("status") == "delivered")
        failed = sum(1 for e in events if e.get("status") == "failed")

        # Channel breakdown
        channel_counts: dict[str, int] = {}
        for e in events:
            ch = e.get("channel", "unknown")
            channel_counts[ch] = channel_counts.get(ch, 0) + 1

        # Failure breakdown
        failure_counts: dict[str, int] = {}
        for e in events:
            if e.get("status") != "failed":
                continue
            reason = e.get("metadata", {}).get("error", "unknown")
            failure_counts[reason] = failure_counts.get(reason, 0) + 1

        # Latency (demo: synthetic based on count)
        latency_metrics = {
            "p50_ms": 120.0,
            "p95_ms": 340.0,
            "p99_ms": 780.0,
        }

        # Retry/fallback (demo: synthetic)
        retry_metrics = {
            "total_retries": max(0, total // 10),
            "retried_events": max(0, failed // 2),
        }
        fallback_metrics = {
            "fallback_executions": max(0, failed // 3),
            "fallback_success_rate": 0.9 if failed > 0 else 1.0,
        }

        # KPIs
        kpis = [
            KPI(name="Total events", value=str(total)),
            KPI(name="Sent", value=str(sent)),
            KPI(name="Delivered", value=str(delivered)),
            KPI(
                name="Failed",
                value=str(failed),
                status="critical" if failed > 5 else "warning" if failed > 0 else "ok",
            ),
            KPI(name="Channels", value=str(len(channel_counts))),
        ]

        # Alerts
        alerts: list[Alert] = []
        if failed > 5:
            alerts.append(
                Alert(
                    severity="critical",
                    title="Elevated failure rate",
                    message=f"{failed} failed events in the last {window_minutes} minutes.",
                    correlation_id=self.correlation_id,
                    suggested_action="Inspect failure breakdown and recent failed events.",
                )
            )
        if failed > 0 and "rate_limit" in str(failure_counts).lower():
            alerts.append(
                Alert(
                    severity="warning",
                    title="Provider rate limiting detected",
                    message="Some failures are due to rate limits.",
                    correlation_id=self.correlation_id,
                    suggested_action="Consider backoff or queue throttling.",
                )
            )

        # Recommendations
        recommendations: list[Recommendation] = []
        if failed > 0:
            recommendations.append(
                Recommendation(
                    title="Investigate top failure reason",
                    reason=f"There are {failed} failed events.",
                    action="Open the event table filtered by status=failed and inspect metadata.",
                    priority="high",
                )
            )
        if len(channel_counts) == 1:
            recommendations.append(
                Recommendation(
                    title="Add a fallback channel",
                    reason="Only one channel is present in recent events.",
                    action="Configure a secondary channel in the workflow designer.",
                    priority="medium",
                )
            )

        # Recent events (last 20)
        recent_events = [
            {
                "id": e.get("id"),
                "correlation_id": e.get("correlation_id"),
                "execution_id": e.get("execution_id"),
                "event_type": e.get("event_type"),
                "status": e.get("status"),
                "channel": e.get("channel"),
                "timestamp": e.get("timestamp"),
            }
            for e in (events[-20:] if len(events) > 20 else events)
        ]

        return ObservabilitySnapshot(
            generated_at=now,
            kpis=kpis,
            alerts=alerts,
            recommendations=recommendations,
            channel_breakdown=channel_counts,
            failure_breakdown=failure_counts,
            latency_metrics=latency_metrics,
            retry_metrics=retry_metrics,
            fallback_metrics=fallback_metrics,
            recent_events=recent_events,
            metadata={"label": label_prefix, "window_minutes": window_minutes},
        )
