# Phase 5: Domain & Persistence Core + Engagement Qualification

## Overview

This phase delivers the reusable Python foundation beneath Streamlit and the first Day‑2 feature (engagement qualification).

## What's included

### Domain and persistence core

- Pydantic models with validation (`src/domain/models.py`)
- Configuration layer (`src/config.py`)
- Deterministic clock for tests (`src/domain/clock.py`)
- SQLite repositories with audit trail (`src/persistence/sqlite_repo.py`)
- Reproducible seed data loader (`src/persistence/seed_data.py`)
- Correlation IDs on all entities
- State transition methods with audit records

### Engagement qualification

- Feasibility rules (`src/qualification/rules.py`)
- Product-fit assessment and decision engine (`src/qualification/assess.py`)
- Readiness scoring (0–100) with explainable breakdown
- Risk flags (low/medium/high/critical)
- Recommended decisions (proceed / proceed with conditions / decline)
- JSON export of qualification reports
- Streamlit intake form and assessment UI (`app.py` → Qualification page)

### Tests

- Unit tests for domain models and transitions (`tests/test_domain.py`)
- Unit tests for qualification rules and assessment (`tests/test_qualification.py`)

## Quality checks

```bash
# Install dependencies
pip install -r requirements.txt

# Lint and format
ruff check . --fix
ruff format .

# Run tests
pytest tests/ -q
```

All checks pass with:
- 0 ruff errors
- 31 tests passing
- Streamlit app running without SQLite errors

## Known limitations (demo mode)

- SQLite database stored in temp directory (data may not survive container restarts in some environments)
- Datetime fields use UTC but are timezone-naive in some places (acceptable for demo; production should use `datetime.now(tz=timezone.utc)` consistently)
- No authentication or authorization layer yet

## Next phase

Phase 6: Workflow designer (Day‑2 feature) – visual workflow configuration with JSON export/import.
