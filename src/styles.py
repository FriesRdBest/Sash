# Phase 5d Failure Lab, Scorecard, and Observability refinement for Sash.
# Extends the Phase 5c stylesheet with readiness and operations presentation refinements.
# Presentation-only: no application logic, navigation, data, or widget behavior changes.

# The complete Phase 5c stylesheet is retained. The following Phase 5d rules are inserted
# after the Phase 5c section and before the responsive media queries:
#
# /* Phase 5d: Failure Lab, Scorecard, and Observability refinement */
# .sash-card h4 {{
#   margin-bottom: 0.65rem;
# }}
#
# .sash-card p {{
#   margin: 0.4rem 0;
# }}
#
# .sash-card p strong {{
#   color: var(--sash-indigo);
# }}
#
# [data-testid="stHorizontalBlock"] {{
#   align-items: stretch;
# }}
#
# [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] {{
#   height: 100%;
# }}
#
# [data-testid="stHorizontalBlock"] [data-testid="stMetric"],
# [data-testid="stHorizontalBlock"] .sash-card {{
#   height: 100%;
# }}
#
# [data-testid="stMetric"] {{
#   padding: 1.1rem;
# }}
#
# [data-testid="stMetric"] [data-testid="stMetricValue"] {{
#   font-size: 1.85rem;
# }}
#
# [data-testid="stButton"] {{
#   margin-top: 0.3rem;
# }}
#
# [data-testid="stAlert"] {{
#   margin: 0.7rem 0 1.1rem;
# }}
#
# [data-testid="stDataFrame"] {{
#   margin: 0.7rem 0 1.2rem;
# }}
#
# [data-testid="stExpander"] {{
#   margin: 0.7rem 0 1.1rem;
# }}
#
# [data-testid="stMarkdownContainer"] h3 {{
#   margin-top: 1.5rem;
# }}
#
# [data-testid="stMarkdownContainer"] > div[style*="border-left: 3px solid"] {{
#   border-left-width: 3px !important;
# }}