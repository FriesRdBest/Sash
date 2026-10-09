# Deployment diagram

This document describes the deployment architecture for Sash.

## Development deployment

```
┌─────────────────────────────────────────────────────────────────┐
│                    Developer Workstation                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    Streamlit App                          │  │
│  │  - app.py                                                 │  │
│  │  - Domain Core                                            │  │
│  │  - Provider Adapter (Mock)                                │  │
│  │  - Persistence (SQLite file)                              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              │ runs on                          │
│                              ↓                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   Python 3.11                             │  │
│  │  - streamlit                                              │  │
│  │  - pydantic                                               │  │
│  │  - pytest                                                 │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Streamlit Community Cloud deployment

```
┌─────────────────────────────────────────────────────────────────┐
│                  Streamlit Community Cloud                       │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    Streamlit App                          │  │
│  │  - app.py                                                 │  │
│  │  - Domain Core                                            │  │
│  │  - Provider Adapter (Mock)                                │  │
│  │  - Persistence (SQLite in ephemeral storage)              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              │ deployed from                    │
│                              ↓                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    GitHub Repository                      │  │
│  │  - FriesRdBest/Sash                                       │  │
│  │  - Branch: main                                           │  │
│  │  - File: app.py                                           │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ accessed by
                              ↓
                ┌─────────────────────────┐
                │      Web Browser         │
                │  - Recruiter             │
                │  - Brett Scorza          │
                │  - Operations team       │
                └─────────────────────────┘
```

## Future production deployment

```
┌─────────────────────────────────────────────────────────────────┐
│                   Kubernetes Cluster                             │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  FastAPI    │  │  FastAPI    │  │  FastAPI    │             │
│  │   Service   │  │   Service   │  │   Service   │             │
│  │  (pod 1)    │  │  (pod 2)    │  │  (pod 3)    │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         │                │                │                     │
│         └────────────────┴────────────────┘                     │
│                          │                                      │
│                          ↓                                      │
│              ┌───────────────────────┐                         │
│              │   PostgreSQL Cluster   │                         │
│              └───────────────────────┘                         │
│                          │                                      │
│                          ↓                                      │
│              ┌───────────────────────┐                         │
│              │     Redis Cluster      │                         │
│              │  (cache + queues)      │                         │
│              └───────────────────────┘                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ↓                           ↓
      ┌─────────────────┐         ┌─────────────────┐
      │  Streamlit UI   │         │  Aurora Backend │
      │  (separate)     │         │                 │
      └─────────────────┘         └─────────────────┘
```

## Deployment requirements

### Current (demo)

- Python 3.11+
- Streamlit
- SQLite (file-based)
- No external services required

### Future (production)

- Python 3.11+
- FastAPI
- PostgreSQL 14+
- Redis 6+
- Kubernetes or container orchestration
- CI/CD pipeline
- Monitoring and alerting

## References

- Container diagram: `container.md`
- CI/CD workflow: ../../.github/workflows/ci.yml
