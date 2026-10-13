# Phase 2 — Sash visual system specification

## Scope

This specification governs a visual-only refresh of the existing Sash application.
It preserves every existing string, emoji, navigation label, navigation order,
widget, information sequence, interaction, route, and functional behavior.

The visual refresh covers the 13 pages reachable through the sidebar. The
`Deployment` code block at `app.py:1461` is unreachable through navigation and is
intentionally excluded from implementation and verification.

## Brand identity

- Product name: **Sash**
- Identity: text-only wordmark; no logo until approved Sinch Brandfolder assets
  and usage rules are available
- Wordmark: indigo `#1D2240`, bold, sentence case
- Visual direction: light, professional, operational, restrained, and evidence-led
- Iconography: retain existing functional emoji and symbols exactly as-is
- Private Sinch brand assets: not available; do not add or imply a Sinch logo

## Color tokens

| Token | Value | Approved use |
|---|---:|---|
| `--sash-page` | `#F6F7FB` | Application canvas |
| `--sash-surface` | `#FFFFFF` | Sidebar, cards, primary surfaces |
| `--sash-border` | `#CED5E8` | Borders, dividers, quiet selection surfaces |
| `--sash-text` | `#1D2240` | Headings, body text, primary controls |
| `--sash-muted` | `#564957` | Captions, secondary labels, supporting copy |
| `--sash-blue` | `#3A6FF3` | Links, focus, selected-state accent, non-text emphasis |
| `--sash-indigo` | `#1D2240` | Primary buttons and high-emphasis controls |
| `--sash-success` | `#26734D` | Success states |
| `--sash-warning` | `#805600` | Warning states |
| `--sash-error` | `#B42318` | Error states |
| `--sash-info` | `#1D2240` | Informational emphasis |

## Accessibility rules

- Normal text requires at least 4.5:1 contrast.
- Large text and meaningful non-text controls require at least 3:1 contrast.
- Blue `#3A6FF3` must not be used for normal-size body text on white or
  `#F6F7FB`.
- Do not place small status text directly on periwinkle `#CED5E8`.
- Keep all text opaque; never place body copy directly on translucent or blurred
  surfaces.
- Preserve semantic success, warning, and error meanings.
- Focus indicators must remain clearly visible and will be verified in Phase 6.

## Typography

| Role | Treatment |
|---|---|
| Page title | Indigo, bold, tight letter-spacing |
| Section heading | Indigo, bold, smaller than page title |
| Body text | Indigo, 1.6 line height |
| Caption / helper text | Plum, smaller size |
| Metric value | Indigo, large and bold |
| Metric label | Plum, small |
| Code / technical value | Existing monospace stack |

Do not introduce a new font, change font sizes arbitrarily, or alter text content.

## Spacing and layout

- Use the existing spacing rhythm: `0.25rem`, `0.5rem`, `1rem`, `1.5rem`, `2rem`.
- Retain the 1,440 px maximum content width.
- Retain all existing `st.columns` structures, ratios, and ordering.
- Group related material with cards only where a card already exists or a clear
  visual boundary improves scanning.
- Preserve clear separation between page sections, forms, results, tables, and
  notices.
- At 900 px and below, reduce page padding.
- At 640 px and below, allow horizontal groups to wrap and prevent clipping.

## Component treatments

| Component | Approved treatment |
|---|---|
| Sidebar | White surface, periwinkle right border, comfortable navigation spacing, subtle hover |
| Selected navigation | Clear accessible selected state using indigo; no small blue text on periwinkle |
| Page title | Indigo, bold, consistent top spacing |
| Section heading | Indigo, bold, consistent spacing |
| Card | 90% white translucent surface, periwinkle border, subtle shadow, restrained blur; opaque text only |
| Metric | Card-based; large indigo value and plum label |
| Primary button | Indigo background, white label, 2.75rem minimum height, 0.6rem radius |
| Secondary button | Light surface, indigo text, periwinkle border |
| Download button | Secondary-button family; preserve existing label and behavior |
| Form controls | Consistent height, spacing, labels, and focus treatment |
| Table | Full-width, horizontally scrollable when needed, readable dense rows |
| Expander | Periwinkle border, subtle hover, preserved label and content |
| Tabs | Consistent active/hover treatment; preserve labels and order |
| Status badge | Rounded pill; semantic color as text on white or very light surface |
| Empty state | Dashed periwinkle border, white surface, centered content |
| Notice | Retain Streamlit info/success/warning/error semantics; standardize spacing only |
| Timeline entry | Retain 10% color surface, left accent border, opaque indigo or plum text |
| Score gradient | Retain color-to-black gradient for success, warning, and error; exclude blue unless endpoint is darkened and re-verified |

## Page implementation priorities

### Home

Improve hierarchy of Purpose, Feature Roadmap, Quick Links, and Next Steps.
Retain the existing status banner, all copy, emoji, links, and four-column
quick-link layout.

### Domain Models

Align the four entity cards and persistence section. Retain the two-column
structure and all entity documentation.

### Qualification

Create clear separation between intake form and assessment results. Align the
three result metrics. Retain every input, validation behavior, rule result,
condition, and JSON export.

### Engagements

Improve empty-state and engagement-card density. Retain the seed-data action,
success message, and all engagement details.

### Workflows

Improve workflow summary and step-card hierarchy. Retain workflow JSON export
and the reset control.

### Run Workflow

Improve form and result separation. Retain validation, spinner, success/error
messages, event table, audit table, and operator guidance.

### Event Timeline

Align the five metrics, correlation search, timeline entries, expanders,
state-transition table, and global event search. Retain all labels and data.

### Failure Lab

Improve scenario selection, contract cards, simulation controls, results table,
and evidence expansion. Retain all scenario documentation and simulation
behavior.

### Scorecard

Improve run controls, overall score, dimension scores, details, and export.
Retain all checks, metrics, warnings, and export behavior.

### Observability

Improve KPI, alert, recommendation, channel/failure breakdown, latency/retry
metrics, and recent-event grouping. Retain view mode, correlation search,
refresh action, and all simulated-data disclosures.

### Security Review

Improve threat-model, controls, PII classification, findings, and
recommendation grouping. Retain review action, download action, and all copy.

### AI Review

Improve scope, findings, AI-use log, and advisory-language hierarchy. Retain
the explanation checkbox, review action, download action, and all copy.

### Handoff Package

Improve document tabs, generated-package result, and export hierarchy. Retain
generation action, document content, download action, and all copy.

## Implementation constraints

- Modify only styling, spacing, alignment, density, visual grouping, and
  responsive presentation.
- Do not modify copy, emoji, navigation labels, navigation order, widgets,
  information sequence, routing, or functionality.
- Do not add features, remove controls, reorder navigation, or invent components
  that imply new functionality.
- Do not change `use_container_width`; its deprecation is out of scope.
- Keep changes isolated primarily in `src/styles.py` and narrowly scoped
  className/style changes in `app.py` where necessary.
- Do not modify `main` directly; use a reviewed visual-refresh branch and pull
  request when implementation begins.

## Phase 2 status

**Complete.** This specification is implementation-ready for Phases 3–5.
