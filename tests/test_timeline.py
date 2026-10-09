"""Unit tests for event timeline and audit view."""

from src.events.engine import simulate_failed_event
from src.persistence.sqlite_repo import audit_repo, event_repo, execution_repo
from src.timeline.queries import (
    build_timeline,
    compute_metrics,
    get_audit_by_correlation,
    get_events_by_correlation,
    get_state_transitions,
    search_events,
)


class TestGetEventsByCorrelation:
    def test_returns_events_for_correlation(self):
        # Simulate an Aurora session to create events
        from src.e2e.aurora_happy_path import create_aurora_session
        from src.workflow.designer import create_sample_workflow

        session = create_aurora_session(
            phone_number="+1234567890",
            workflow=create_sample_workflow(),
            mode="mock",
        )
        events = get_events_by_correlation(session.correlation_id)
        assert len(events) >= 1


class TestGetAuditByCorrelation:
    def test_returns_audit_for_correlation(self):
        from src.e2e.aurora_happy_path import create_aurora_session
        from src.workflow.designer import create_sample_workflow

        session = create_aurora_session(
            phone_number="+1234567890",
            workflow=create_sample_workflow(),
            mode="mock",
        )
        audit = get_audit_by_correlation(session.correlation_id)
        assert len(audit) >= 1
        actions = {a["action"] for a in audit}
        assert "consent_recorded" in actions


class TestBuildTimeline:
    def test_builds_combined_timeline(self):
        from src.e2e.aurora_happy_path import create_aurora_session
        from src.workflow.designer import create_sample_workflow

        session = create_aurora_session(
            phone_number="+1234567890",
            workflow=create_sample_workflow(),
            mode="mock",
        )
        timeline = build_timeline(session.correlation_id)
        assert len(timeline) >= 2  # at least events + audit
        types = {t["type"] for t in timeline}
        assert "event" in types or "audit" in types


class TestComputeMetrics:
    def test_computes_metrics_with_simulated_flag(self):
        from src.e2e.aurora_happy_path import create_aurora_session
        from src.workflow.designer import create_sample_workflow

        session = create_aurora_session(
            phone_number="+1234567890",
            workflow=create_sample_workflow(),
            mode="mock",
        )
        metrics = compute_metrics(session.correlation_id)
        assert metrics["correlation_id"] == session.correlation_id
        assert "total_events" in metrics
        assert "simulated" in metrics
        assert "delivery_rate_pct" in metrics["simulated"]


class TestGetStateTransitions:
    def test_returns_transitions(self):
        from src.e2e.aurora_happy_path import create_aurora_session
        from src.workflow.designer import create_sample_workflow

        session = create_aurora_session(
            phone_number="+1234567890",
            workflow=create_sample_workflow(),
            mode="mock",
        )
        transitions = get_state_transitions(session.correlation_id)
        assert len(transitions) >= 1
        assert all("from_state" in t and "to_state" in t for t in transitions)


class TestSearchEvents:
    def test_search_with_filters(self):
        # Just ensure function runs without error
        results = search_events(limit=10)
        assert isinstance(results, list)

    def test_search_by_status(self):
        results = search_events(status="sent", limit=10)
        assert isinstance(results, list)
