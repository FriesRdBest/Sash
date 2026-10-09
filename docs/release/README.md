# Phase 19 — Evidence and Release

Status: release candidate in progress. This document distinguishes verified evidence from work still requiring a human or live deployment check.

## Verified evidence

- Phase 18 local test run: 143 passed.
- Ruff lint: passed.
- Ruff format check: passed; 88 Python files already formatted after cleanup.
- `git diff --check`: passed before the formatting commit.
- User-reported visual review of the Phase 18 app: passed.
- The Phase 18 baseline is preserved by tag `phase18-restore-point`.
- Ruff cleanup commit: `b4ecfab`, on `chore/phase18-ruff-cleanup`; included in the documentation branch by cherry-pick.

These are local results reported from the Codespaces terminal. They are not a CI run or an independent reproduction by a release pipeline.

## Warnings

- Six Pydantic deprecation warnings remain for class-based model `Config` declarations in `src/domain/models.py`.
- These warnings did not fail the reported test run.
- Do not claim zero warnings until the migration is implemented and verified.

## Pending release evidence

- Confirm the live Streamlit Community Cloud app shows the restored Phase 18 version.
- Run browser-based keyboard navigation and focus-indicator checks.
- Measure text and control contrast; record method and results.
- Capture current screenshots from the deployed build.
- Render/export the architecture diagram and verify it against code.
- Record the five-minute customer scenario demo.
- Re-run tests, Ruff, and app-start smoke test on the exact release candidate commit.
- Review every README/release claim against implementation and evidence.
- Create a version tag and GitHub Release only after all required checks are complete.

## Release gate

Do not mark this release complete or publish a release while any required item above is pending. Keep the `phase18-restore-point` tag and recovery branches until the deployed build and release candidate are verified.
