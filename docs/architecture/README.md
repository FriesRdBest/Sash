# Architecture

This directory contains the architecture documentation for Sash, including diagrams, decision records, and operational models.

## Contents

### Diagrams

- `context.md` — System context diagram showing Sash, Aurora Marketplace, Sinch, and external dependencies
- `container.md` — Container diagram showing Streamlit UI, API layer, domain core, and persistence
- `component.md` — Component diagram showing services, repositories, and adapters
- `dataflow.md` — Data flow diagram for the verification workflow
- `deployment.md` — Deployment diagram for local development and Streamlit Community Cloud

### Models

- `threat_model.md` — Security threat model with STRIDE analysis
- `production_limitations.md` — Explicit limitations of the demo vs. production system

### Decisions

- `adr-001-streamlit-for-ui.md` — Why Streamlit was chosen for the demonstration interface
- `adr-002-fastapi-boundary.md` — Decision to keep FastAPI as an optional future boundary
- `adr-003-sqlite-for-demo.md` — Why SQLite is used for demo persistence with PostgreSQL-ready interfaces
- `adr-004-mock-mode-default.md` — Decision to use mock provider mode by default
- `adr-005-event-processing.md` — Event processing and normalization strategy
- `adr-006-observability.md` — Observability approach using structured logs and in-memory metrics
- `adr-007-provider-adapter.md` — Provider adapter pattern for Sinch integration

## Usage

Reference these documents when:

- Onboarding to the Sash architecture
- Making changes that affect system boundaries
- Evaluating trade-offs in implementation
- Preparing for production deployment

## Status

Phase 3 in progress. Architecture is stable for the demo scope.
