# Amberglass All Page Audit

This audit records the shared treatment and validation focus for all Sash navigation pages. It preserves application behavior while applying the Amberglass visual system.

| Page | Primary content | Shared treatment | Validation focus |
|---|---|---|---|
| Home | Purpose, scenario, resource links, footer | Glass cards, quick link grid, responsive stacking | Desktop and mobile card layout |
| Domain Models | Entity reference cards | Two column information cards | Code labels and card height |
| Qualification | Intake form, readiness result, JSON export | Form surface, metric cards, decision and risk states | Validation, result states, download |
| Engagements | Seed action, engagement records, empty state | Toolbar, record cards, status badges | Empty and populated states |
| Workflows | Workflow summary, steps, JSON download | Summary card, step sequence, download action | Long templates and compact layouts |
| Run Workflow | Verification form, event and audit tables | Form surface, event panels, data tables | Long IDs, table overflow, success/error |
| Event Timeline | Search, metric strip, audit records, JSON, table | Search controls, metric cards, timeline records | Long correlation IDs and JSON |
| Failure Lab | Scenario selection, simulations, evidence | Scenario cards, control row, result tables, expanders | Success/failure status and evidence |
| Scorecard | Checks, metrics, report export | Metric hierarchy, check results, export actions | Blocking states and report output |
| Observability | Operational metrics and alerts | Metrics, trend or status panels, tables | Dense metrics and alert readability |
| Security Review | Security controls and findings | Review cards, severity states, JSON or evidence | Severity hierarchy and long findings |
| AI Review | Review controls and generated findings | Form controls, response cards, evidence blocks | Loading, empty, and completed review states |
| Handoff Package | Delivery package generation and export | Summary cards, package content, downloads | Long generated content and export |

## Shared component rules

- Primary actions use black fill and white text.
- Secondary and download actions use warm cream surfaces with bronze borders.
- Cards, metrics, forms, tables, expanders, and alerts use one glass surface family.
- Inputs and data-dense surfaces remain more opaque than decorative cards.
- Semantic status remains explicit through labels and supporting color.
- Long IDs, JSON, code, and tables must wrap or scroll within their containers.
- At narrow widths, multi-column content stacks without horizontal page overflow.
