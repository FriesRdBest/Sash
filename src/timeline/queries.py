"""Event timeline and audit query utilities."""

import logging
from typing import Any

from src.events.engine import get_dead_letters
from src.persistence.sqlite_repo import audit_repo, event_repo, execution_repo

logger = logging.getLogger(__name__)


def get_events_by_correlation(correlation_id: str) -> list[dict[str, Any]]:
    """Get all events for a correlation ID (approximate via execution metadata)."""
    # Scan executions for matching correlation_id
    executions = execution_repo.get_all()
    matching_exec_ids = [
        ex["id"]
        for ex in executions
        if ex.get("metadata", {}).get("correlation_id") == correlation_id
    ]

    events = []
    for exec_id in matching_exec_ids:
        exec_events = event_repo.find_by(execution_id=exec_id)
        events.extend(exec_events)

    # Sort by created_at
    events.sort(key=lambda e: e.get("created_at", ""))
    return events


def get_audit_by_correlation(correlation_id: str) -> list[dict[str, Any]]:
    """Get audit records for a correlation ID."""
    records = audit_repo.get_by_correlation(correlation_id)
    records.sort(key=lambda r: r.get("timestamp", ""))
    return records


def build_timeline(correlation_id: str) -> list[dict[str, Any]]:
    """Build combined timeline of events + audit for a correlation ID."""
    events = get_events_by_correlation(correlation_id)
    audit = get_audit_by_correlation(correlation_id)
    dead_letters = get_dead_letters(correlation_id)

    timeline = []

    # Add events
    for e in events:
        timeline.append(
            {
                "type": "event",
                "timestamp": e.get("created_at"),
                "summary": f"Event {e.get('channel', 'unknown')} {e.get('status', 'unknown')}",
                "details": e,
            }
        )

    # Add audit
    for a in audit:
        timeline.append(
            {
                "type": "audit",
                "timestamp": a.get("timestamp"),
                "summary": f"{a.get('action', 'unknown')} on {a.get('entity_type', 'unknown')}",
                "details": a,
            }
        )

    # Add dead-letters
    for dl in dead_letters:
        timeline.append(
            {
                "type": "dead_letter",
                "timestamp": dl.created_at.isoformat(),
                "summary": f"Dead-letter: {dl.reason}",
                "details": {
                    "event_id": dl.event_id,
                    "reason": dl.reason,
                    "attempts": dl.attempts,
                    "raw_payload": dl.raw_payload,
                },
            }
        )

    # Sort by timestamp
    timeline.sort(key=lambda x: x["timestamp"] or "")
    return timeline


def compute_metrics(correlation_id: str) -> dict[str, Any]:
    """Compute metrics for a correlation ID (demo includes some simulated values)."""
    events = get_events_by_correlation(correlation_id)
    audit = get_audit_by_correlation(correlation_id)
    dead_letters = get_dead_letters(correlation_id)

    total_events = len(events)
    sent_events = sum(1 for e in events if e.get("status") == "sent")
    delivered_events = sum(1 for e in events if e.get("status") == "delivered")
    failed_events = sum(1 for e in events if e.get("status") == "failed")

    avg_latency_ms = 0.0
    latencies = [
        e.get("metadata", {}).get("latency_ms", 0)
        for e in events
        if e.get("metadata", {}).get("latency_ms")
    ]
    if latencies:
        avg_latency_ms = sum(latencies) / len(latencies)

    return {
        "correlation_id": correlation_id,
        "total_events": total_events,
        "sent_events": sent_events,
        "delivered_events": delivered_events,
        "failed_events": failed_events,
        "dead_letter_count": len(dead_letters),
        "audit_record_count": len(audit),
        "avg_latency_ms": round(avg_latency_ms, 2),
        # Simulated metrics (labelled)
        "simulated": {
            "delivery_rate_pct": round(
                (delivered_events / max(total_events, 1)) * 100, 1
            ),
            "first_response_time_ms": 150.0,  # simulated
            "end_to_end_time_ms": 1250.0,  # simulated
        },
    }


def get_state_transitions(correlation_id: str) -> list[dict[str, Any]]:
    """Get state transition history for a correlation ID."""
    audit = get_audit_by_correlation(correlation_id)
    transitions = []

    last_state: dict[str, Any] | None = None
    for a in audit:
        new_state = a.get("new_state")
        if new_state:
            transitions.append(
                {
                    "timestamp": a["timestamp"],
                    "action": a["action"],
                    "from_state": last_state,
                    "to_state": new_state,
                    "actor": a.get("actor", "unknown"),
                }
            )
            last_state = new_state

    return transitions


def search_events(
    query: str | None = None,
    event_type: str | None = None,
    status: str | None = None,
    limit: int = 50,
) -> list[dict[str, Any]]:
    """Search events with simple filters (demo: scans all events)."""
    all_events = event_repo.get_all()
    results = []

    for e in all_events:
        if event_type and e.get("channel") != event_type:
            continue
        if status and e.get("status") != status:
            continue
        if query:
            text = f"{e.get('execution_id', '')} {e.get('content', {})}".lower()
            if query.lower() not in text:
                continue
        results.append(e)
        if len(results) >= limit:
            break

    results.sort(key=lambda x: x.get("created_at", ""))
    return results
