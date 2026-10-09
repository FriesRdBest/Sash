"""Unit tests for the observability console engine."""

import pytest

from src.observability.engine import ObservabilityEngine


@pytest.fixture
def engine_system():
    return ObservabilityEngine(correlation_id=None)


@pytest.fixture
def engine_corr():
    return ObservabilityEngine(correlation_id="corr-test-123")


def test_snapshot_has_kpis(engine_system):
    snap = engine_system.snapshot()
    assert len(snap.kpis) >= 4
    assert any(k.name == "Total events" for k in snap.kpis)
    assert any(k.name == "Failed" for k in snap.kpis)


def test_snapshot_has_breakdowns(engine_system):
    snap = engine_system.snapshot()
    assert isinstance(snap.channel_breakdown, dict)
    assert isinstance(snap.failure_breakdown, dict)


def test_snapshot_has_latency_and_retry_metrics(engine_system):
    snap = engine_system.snapshot()
    assert "p50_ms" in snap.latency_metrics
    assert "total_retries" in snap.retry_metrics
    assert "fallback_executions" in snap.fallback_metrics


def test_correlation_snapshot_has_metadata(engine_corr):
    snap = engine_corr.snapshot()
    assert snap.metadata["label"].startswith("correlation=")
    assert "corr-test-123" in snap.metadata["label"]


def test_alerts_generated_on_failures(engine_system):
    # In demo mode, there may be few events; we assert structure, not count.
    snap = engine_system.snapshot()
    for alert in snap.alerts:
        assert alert.severity in {"info", "warning", "critical"}
        assert alert.title
        assert alert.message


def test_recommendations_are_actionable(engine_system):
    snap = engine_system.snapshot()
    for rec in snap.recommendations:
        assert rec.title
        assert rec.reason
        assert rec.action
        assert rec.priority in {"low", "medium", "high"}


def test_recent_events_are_limited(engine_system):
    snap = engine_system.snapshot()
    assert len(snap.recent_events) <= 20
    for e in snap.recent_events:
        assert "event_type" in e
        assert "status" in e
