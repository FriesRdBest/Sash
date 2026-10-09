# Container diagram

This document describes the container architecture for Sash.

```
┌─────────────────────────────────────────────────────────────────┐
│                         Sash Application                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Streamlit UI (app.py)                        │  │
│  │  - Landing page                                           │  │
│  │  - Engagement qualification (future)                      │  │
│  │  - Workflow designer (future)                             │  │
│  │  - Observability console (future)                         │  │
│  │  - Handoff generator (future)                             │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              │ calls                            │
│                              ↓                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   Domain Core                              │  │
│  │  - Workflow engine                                         │  │
│  │  - State machine                                           │  │
│  │  - Event normalizer                                        │  │
│  │  - Retry policy                                            │  │
│  │  - Idempotency store                                       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│              ┌───────────────┼───────────────┐                 │
│              │               │               │                 │
│              ↓               ↓               ↓                 │
│  ┌─────────────────┐ ┌─────────────┐ ┌─────────────────┐      │
│  │ Provider Adapter│ │ Persistence │ │  Observability  │      │
│  │                 │ │  Layer      │ │                 │      │
│  │ - Mock provider │ │ - SQLite    │ │ - Structured    │      │
│  │ - Sinch adapter │ │ - Repositories│   logs          │      │
│  │   (future)      │ │             │ │ - In-memory     │      │
│  │                 │ │             │ │   metrics       │      │
│  └─────────────────┘ └─────────────┘ └─────────────────┘      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Containers

### Streamlit UI

- **Technology:** Streamlit (Python)
- **Responsibility:** User interface for demo and operations
- **Interfaces:** Calls domain core directly (in-process)
- **Deployment:** Streamlit Community Cloud

### Domain Core

- **Technology:** Python modules
- **Responsibility:** Workflow orchestration, state management, event processing
- **Interfaces:** Provider adapter, persistence layer, observability
- **Deployment:** Bundled with Streamlit app

### Provider Adapter

- **Technology:** Python interface + implementations
- **Responsibility:** Abstract Sinch API calls
- **Implementations:**
  - Mock provider (default)
  - Sinch provider (optional, future)
- **Deployment:** In-process

### Persistence Layer

- **Technology:** SQLite (demo), PostgreSQL-ready interfaces
- **Responsibility:** Store workflows, events, audit trail
- **Interfaces:** Repository pattern
- **Deployment:** Local file (demo), database server (production)

### Observability

- **Technology:** Python logging, in-memory metrics
- **Responsibility:** Structured logs, metrics, traces
- **Interfaces:** Called by domain core and adapters
- **Deployment:** In-process

## Communication patterns

- **UI → Domain:** Direct function calls (in-process)
- **Domain → Provider:** Interface calls with retry logic
- **Domain → Persistence:** Repository pattern
- **Domain → Observability:** Structured logging

## Future evolution

- Extract Domain Core into FastAPI service
- Replace SQLite with PostgreSQL
- Add Redis for caching and queues
- Deploy to container orchestration (Kubernetes)

## References

- Component diagram: `component.md`
- Deployment diagram: `deployment.md`
