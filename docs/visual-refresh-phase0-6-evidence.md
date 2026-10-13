# Visual Refresh: Phase 0/6 Evidence

## Scope

This document records the verification evidence for the styling-only visual-refresh branch `visual-refresh-phase3-shell`.

The branch changes only `src/styles.py`. It does not change application copy, navigation labels or order, routing, domain logic, data models, tests, or functional sequences.

## Test and startup evidence

- Existing test suite: **143 passed**, with 6 pre-existing Pydantic deprecation warnings.
- Streamlit startup: successful on port 8501.
- Final branch diff: CSS-only additions in `src/styles.py`; no existing CSS rules removed.
- Rollback: reset the branch to `main` / `backup/phase0-visual-baseline` (`3b7eff1`) or revert the individual styling commits.

## Responsive evidence

Screenshots were captured for all 13 application pages at three viewport widths:

| Breakpoint | Viewport | Pages captured |
|---|---:|---:|
| Desktop | 1440 x 900 | 13 |
| Tablet | 834 x 1112 | 13 |
| Mobile | 390 x 844 | 13 |

Evidence location: `visual-baseline/phase0-6/desktop/`, `visual-baseline/phase0-6/tablet/`, and `visual-baseline/phase0-6/mobile/`.

## Pages covered

- Home
- Domain Models
- Qualification
- Engagements
- Workflows
- Run Workflow
- Event Timeline
- Failure Lab
- Scorecard
- Observability
- Security Review
- AI Review
- Handoff Package

## Accessibility evidence

Keyboard-focus evidence contains 12 sequential focus states captured after repeated `Tab` presses:

`visual-baseline/phase0-6/accessibility/keyboard-focus-01.png` through `keyboard-focus-12.png`.

Zoom and reflow evidence was captured at 200% zoom:

`visual-baseline/phase0-6/accessibility/zoom-200-percent-home.png`.

## Phase 5 page-specific evidence

Refined page-specific screenshots for all 13 pages are retained under:

`visual-baseline/phase5/`

Each file uses the naming pattern `phase5-<page-slug>-refined.png`.

## Known limitations

- The screenshots are local verification artifacts and are intentionally not committed to Git.
- Keyboard-focus evidence documents focus progression but does not replace a full screen-reader or automated accessibility audit.
- Contrast validation remains based on the existing palette and prior contrast research; a complete rendered-pair audit requires the approved private Sinch Brandfolder assets and usage rules.
- The formal token/component specification remains a separate Phase 2 deliverable and is not fully documented in this branch.
