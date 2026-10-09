# ADR 003: Use SQLite for demo with PostgreSQL-ready interfaces

## Status

Accepted

## Context

Persistence options:
1. SQLite (file-based, no setup)
2. PostgreSQL (production-grade, requires setup)
3. In-memory (fastest, no persistence)

## Decision

Use SQLite for the demo, but design repository interfaces to be database-agnostic so PostgreSQL can be swapped in later.

## Rationale

**SQLite benefits:**
- Zero setup (file-based)
- Works on Streamlit Community Cloud
- No external dependencies
- Sufficient for demo scale

**PostgreSQL benefits:**
- Concurrency support
- Durability guarantees
- Backup and replication
- Production-grade

**Why SQLite for demo:**

The demo needs to prove workflow orchestration and reliability patterns, not database scalability. SQLite is sufficient for demonstrating the concepts while keeping deployment simple.

**Repository pattern:**

All data access goes through repository interfaces:

```python
class WorkflowRepository(Protocol):
    def create(self, workflow: Workflow) -> None: ...
    def get_by_id(self, workflow_id: str) -> Workflow: ...
    def update(self, workflow: Workflow) -> None: ...
```

This allows swapping SQLite for PostgreSQL without changing domain logic.

## Consequences

- Demo deployment is simple
- Production requires database migration
- Repository interfaces must be defined upfront
- Test strategy must work with both databases

## References

- Deployment diagram: deployment.md
- Component diagram: component.md
