# Component diagram

This document describes the component architecture for Sash.

```
┌─────────────────────────────────────────────────────────────────┐
│                      Streamlit UI Layer                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │   Landing   │ │ Qualification│ │  Workflow   │               │
│  │    Page     │ │    Page     │ │  Designer   │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │Observability│ │   Failure   │ │  Handoff    │               │
│  │   Console   │ │  Simulator  │ │  Generator  │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ uses
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                       Domain Core                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   Workflow Engine                        │   │
│  │  - create_workflow()                                     │   │
│  │  - transition_state()                                    │   │
│  │  - validate_transition()                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Event Processor                       │   │
│  │  - normalize_event()                                     │   │
│  │  - validate_event()                                      │   │
│  │  - correlate_events()                                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   Retry Manager                          │   │
│  │  - should_retry()                                        │   │
│  │  - calculate_backoff()                                   │   │
│  │  - track_attempts()                                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                Idempotency Manager                       │   │
│  │  - check_duplicate()                                     │   │
│  │  - record_event_id()                                     │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ↓               ↓               ↓
┌───────────────────┐ ┌─────────────┐ ┌───────────────────┐
│ Provider Adapter  │ │ Persistence │ │   Observability   │
│                   │ │   Layer     │ │                   │
│ ┌───────────────┐ │ │ ┌─────────┐ │ │ ┌───────────────┐ │
│ │   Interface   │ │ │ │Workflow │ │ │ │  Structured   │ │
│ │ - send()      │ │ │ │Repository│ │ │ │   Logging     │ │
│ │ - status()    │ │ │ └─────────┘ │ │ └───────────────┘ │
│ └───────────────┘ │ │ ┌─────────┐ │ │ ┌───────────────┐ │
│ ┌───────────────┐ │ │ │ Event   │ │ │ │   Metrics     │ │
│ │ Mock Provider │ │ │ │Repository│ │ │ │  (in-memory)  │ │
│ └───────────────┘ │ │ └─────────┘ │ │ └───────────────┘ │
│ ┌───────────────┐ │ │ ┌─────────┐ │ │                   │
│ │ Sinch Provider│ │ │ │ Audit   │ │ │                   │
│ │   (future)    │ │ │ │Repository│ │ │                   │
│ └───────────────┘ │ │ └─────────┘ │ │                   │
└───────────────────┘ └─────────────┘ └───────────────────┘
```

## Components

### Workflow Engine

- **Purpose:** Orchestrate verification workflows
- **Responsibilities:** State transitions, validation, lifecycle management
- **Dependencies:** Event processor, persistence layer

### Event Processor

- **Purpose:** Normalize and validate events from all sources
- **Responsibilities:** Schema validation, correlation, enrichment
- **Dependencies:** Provider adapter, observability

### Retry Manager

- **Purpose:** Manage retry logic for transient failures
- **Responsibilities:** Backoff calculation, attempt tracking, retry decisions
- **Dependencies:** Event processor, persistence

### Idempotency Manager

- **Purpose:** Prevent duplicate event processing
- **Responsibilities:** Event ID tracking, duplicate detection
- **Dependencies:** Persistence layer

### Provider Adapter

- **Purpose:** Abstract communications provider
- **Responsibilities:** API calls, response handling, error mapping
- **Implementations:** Mock, Sinch

### Persistence Layer

- **Purpose:** Store workflows, events, audit trail
- **Responsibilities:** CRUD operations, transactions, queries
- **Implementations:** SQLite (demo), PostgreSQL (future)

### Observability

- **Purpose:** Provide visibility into system behavior
- **Responsibilities:** Logging, metrics, traces
- **Consumers:** Operations dashboard, debugging

## Component interactions

1. UI calls Workflow Engine to create/modify workflows
2. Workflow Engine calls Event Processor to handle events
3. Event Processor calls Provider Adapter for external calls
4. All components call Observability for logging
5. All components call Persistence Layer for state

## References

- Container diagram: `container.md`
- Data flow diagram: `dataflow.md`
