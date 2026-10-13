# Phase 5c Workflows, Run Workflow, and Event Timeline refinement for Sash.
# Extends the Phase 5b stylesheet with workflow-operation presentation refinements.
# Presentation-only: no application logic, navigation, data, or widget behavior changes.

# The complete Phase 5b stylesheet is retained. The following Phase 5c rules are inserted
# after the Phase 5b section and before the responsive media queries:
#
# /* Phase 5c: Workflows, Run Workflow, and Event Timeline refinement */
# .sash-card strong {{ color: var(--sash-indigo); }}
#
# .sash-card code {{
#   background: rgba(58, 111, 243, 0.09);
#   border: 1px solid rgba(58, 111, 243, 0.16);
#   border-radius: 0.4rem;
#   color: var(--sash-indigo);
#   font-size: 0.86em;
#   padding: 0.12rem 0.36rem;
#   white-space: nowrap;
# }}
#
# [data-testid="stForm"] [data-testid="stTextInput"] {{ min-width: 0; }}
#
# [data-testid="stForm"] [data-testid="stFormSubmitButton"] {{ margin-top: 0.35rem; }}
#
# [data-testid="stMarkdownContainer"] h3 {{
#   margin-top: 1.45rem;
#   margin-bottom: 0.6rem;
# }}
#
# [data-testid="stDataFrame"] {{ margin: 0.65rem 0 1.15rem; }}
#
# [data-testid="stMetric"] {{ min-width: 0; }}
#
# [data-testid="stHorizontalBlock"] [data-testid="stMetric"] {{ height: 100%; }}
#
# [data-testid="stMarkdownContainer"] > div[style*="border-left: 3px solid"] {{
#   background: rgba(255, 255, 255, 0.72) !important;
#   border: 1px solid rgba(255, 255, 255, 0.88) !important;
#   border-left: 3px solid var(--sash-blue) !important;
#   border-radius: var(--sash-radius-sm) !important;
#   box-shadow: var(--sash-shadow-sm);
#   margin: 0.55rem 0 !important;
#   padding: 0.9rem 1rem !important;
#   backdrop-filter: blur(16px);
#   -webkit-backdrop-filter: blur(16px);
#   transition: border-color 160ms ease, box-shadow 160ms ease;
# }}
#
# [data-testid="stMarkdownContainer"] > div[style*="border-left: 3px solid"]:hover {{
#   border-color: rgba(58, 111, 243, 0.24) !important;
#   box-shadow: var(--sash-shadow);
# }}
#
# [data-testid="stMarkdownContainer"] > div[style*="border-left: 3px solid"] code {{
#   background: rgba(58, 111, 243, 0.10);
#   border-color: rgba(58, 111, 243, 0.18);
# }}
#
# [data-testid="stExpander"] [data-testid="stJson"] {{
#   background: rgba(248, 250, 255, 0.72);
#   border: 1px solid rgba(206, 213, 232, 0.85);
#   border-radius: 0.65rem;
#   padding: 0.75rem;
# }}
#
# [data-testid="stTextInput"] {{ min-width: 0; }}
#
# [data-testid="stSelectbox"] {{ min-width: 0; }}
#
# [data-testid="stButton"] {{ margin-top: 0.25rem; }}