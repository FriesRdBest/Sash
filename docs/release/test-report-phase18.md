# Phase 18 Test Report

## Environment and scope

Results below are copied from user-provided Codespaces terminal output after restoring the Phase 18 snapshot. Environment reported Python 3.14.2 and Pydantic 2.14.0.

## Results

| Check | Result |
|---|---|
| `ruff check .` | Passed |
| `ruff format --check .` | Passed; 88 files already formatted after cleanup |
| `python -m pytest -q` | 143 passed |
| `git diff --check` | Passed before cleanup commit |
| Visual review | User reported passed |

The pytest run completed in 0.67 seconds in the latest reported run.

## Warnings

Pytest emitted six `PydanticDeprecatedSince20` warnings from class-based `Config` declarations in `src/domain/models.py`, at the Customer, Workflow, WorkflowExecution, Event, Engagement, and AuditRecord models. These are warnings, not failed tests.

## Boundaries

This report records the checks run locally in Codespaces. It is not a hosted CI report, formal accessibility audit, load-test report, security certification, or confirmation of the deployed Streamlit app. Re-run these checks against the exact release candidate before publishing.
