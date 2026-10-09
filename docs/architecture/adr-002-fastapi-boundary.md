# ADR 002: Keep FastAPI as optional future boundary

## Status

Accepted

## Context

The domain core could be:
1. Directly called by Streamlit (current)
2. Exposed via FastAPI service (future)

## Decision

Start with direct in-process calls. Design domain core with clean interfaces so FastAPI can be added later without refactoring.

## Rationale

**Current approach (direct calls):**
- Simpler deployment (single app)
- Faster development
- No network overhead
- Sufficient for demo

**Future approach (FastAPI):**
- Better separation of concerns
- Independent scaling
- Can be called by external systems
- Required for production

**Why defer:**

The demo needs to prove domain understanding and reliability patterns, not distributed system complexity. FastAPI adds deployment and testing overhead without proportional value for the initial demonstration.

## Consequences

- Domain core must have clean interfaces
- FastAPI layer can be added in a single commit later
- Current deployment is simpler
- Production deployment will require extraction

## References

- Container diagram: container.md
- Component diagram: component.md
