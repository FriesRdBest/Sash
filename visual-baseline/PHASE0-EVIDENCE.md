# Phase 0 — Visual-refresh baseline evidence

## Scope

This is a visual-only refresh baseline. No application copy, navigation labels,
widget order, functional behavior, routing, or feature scope may change during
the visual-refresh work.

## Protected baseline

- Repository: `FriesRdBest/Sash`
- Branch: `main`
- Baseline commit: `3b7eff1eed0298894526828ba258ced3f77cd62c`
- Baseline commit message: `docs: add Sinch token references and contrast findings`
- Local backup branch: `backup/phase0-visual-baseline`
- Local annotated tag: `phase0-visual-baseline`
- Pre-theme rollback commit: `ea7d82b54d574e0fad7bbb1a132d026497766f90`
- Current theme commit: `76c68577c400a002a1725d627a68baeb0ad725aa`

## Source fingerprints

- `app.py`: `8e7dc6944f1e8fa1dfc4d0d5efe44d251af8a9249892b5bba60e4ba31668f849`
- `src/styles.py`: `1e0c7772135e582d631972e2ecd6d352c83b67d430b043865fbfe4dd42cba5ba`

## Application scope

The visual baseline covers the 13 pages reachable through the sidebar:

1. Home
2. Domain Models
3. Qualification
4. Engagements
5. Workflows
6. Run Workflow
7. Event Timeline
8. Failure Lab
9. Scorecard
10. Observability
11. Security Review
12. AI Review
13. Handoff Package

The `Deployment` code block at `app.py:1461` is not reachable through sidebar
navigation. It is intentionally excluded from the visual-refresh baseline and
must not be styled, deleted, or altered as part of this work.

## Screenshot inventory

### Default states

| File | Page / state |
|---|---|
| `01-home-default.png` | Home |
| `02-domain-models-default.png` | Domain Models |
| `03-qualification-default.png` | Qualification |
| `04-engagements-default.png` | Engagements |
| `05-workflows-default.png` | Workflows |
| `06-run-workflow-default.png` | Run Workflow |
| `07-event-timeline-default.png` | Event Timeline |
| `08-failure-lab-default.png` | Failure Lab |
| `09-scorecard-default.png` | Scorecard |
| `10-observability-default.png` | Observability |
| `11-security-review-default.png` | Security Review |
| `12-ai-review-default.png` | AI Review |
| `13-handoff-package-default.png` | Handoff Package |

### Interaction states

| File | Page / state |
|---|---|
| `14-qualification-assessment.png` | Qualification assessment result |
| `15-engagements-seeded.png` | Engagements after loading seed data |
| `16-run-workflow-result.png` | Run Workflow completed mock verification |
| `17-event-timeline-populated.png` | Event Timeline populated from completed run |
| `18-event-timeline-metrics-expanded.png` | Event Timeline metrics expander expanded |
| `19-scorecard-results.png` | Scorecard completed |
| `20-observability-refreshed.png` | Observability snapshot refreshed |
| `21-security-review-results.png` | Security Review completed |
| `22-ai-review-results.png` | AI Review completed |
| `23-handoff-package-generated.png` | Handoff Package generated |

## Coverage notes

- All 10 attempted interaction-state captures passed.
- The Failure Lab is represented by its default screenshot only because its
  interactive control was not identified in the automated Phase 0 inventory.
- No interaction was attempted against the unreachable Deployment page.
- The temporary SQLite database, `/tmp/sash.db`, was backed up before each
  capture session and restored afterward.

## Visual-refresh constraints

- Preserve all existing copy, emoji, navigation labels, navigation order,
  widgets, information sequence, and functional behavior.
- Do not add features, remove controls, reorder navigation, or alter routing.
- Treat the existing palette and theme as the starting point, subject to the
  approved visual-refresh specification and accessibility verification.
- Do not use blue `#3A6FF3` as normal-size body-text color on white or
  `#F6F7FB`; it is below the 4.5:1 WCAG AA normal-text contrast threshold.
- Preserve semantic success, warning, and error color meanings.

## Non-blocking finding

Streamlit emitted a deprecation warning recommending replacement of
`use_container_width` with `width='stretch'` or `width='content'`. This is
out of scope for the visual refresh and must be handled separately.

## Phase 0 status

**Complete.** The baseline is protected, all 13 reachable pages have default
screenshots, and 10 principal interaction states have captured evidence.
