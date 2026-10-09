# ADR 006: Observability approach using structured logs and in-memory metrics

## Status

Accepted

## Context

Sash needs observability for:
- Debugging workflow issues
- Monitoring delivery rates
- Alerting on failures
- Demonstrating operational maturity

## Decision

Use structured logging (Python logging with JSON formatter) and in-memory metrics for the demo. Design for future integration with Prometheus, Grafana, and distributed tracing.

## Rationale

**Structured logging benefits:**
- Machine-parseable
- Easy to query and filter
- Supports correlation IDs
- Works with any log aggregator

**In-memory metrics benefits:**
- Simple to implement
- No external dependencies
- Sufficient for demo
- Can be exported to Prometheus later

**Why not full observability stack now:**

The demo needs to show observability thinking, not a complete production monitoring setup. Structured logs and basic metrics demonstrate the right mindset without the complexity of deploying Prometheus, Grafana, Jaeger, etc.

**Implementation:**

```python
import logging
import json

logger = logging.getLogger(__name__)

def log_event(event: NormalizedEvent):
    logger.info(
        "event_processed",
        extra={
            "event_id": event.event_id,
            "event_type": event.event_type,
            "workflow_id": event.workflow_id,
            "correlation_id": event.correlation_id,
        }
    )
```

Metrics (in-memory):

```python
class Metrics:
    def __init__(self):
        self.counters = defaultdict(int)
    
    def increment(self, name: str, value: int = 1):
        self.counters[name] += value
    
    def get(self, name: str) -> int:
        return self.counters[name]
```

## Consequences

- Demo shows observability thinking
- Production requires external monitoring stack
- Log aggregation must be configured separately
- Metrics are lost on restart (acceptable for demo)

## References

- Observability console: ../README.md
- Threat model: threat_model.md
