# Phase 6 responsive, accessibility, and regression hardening for Sash.
# Extends the Phase 5e stylesheet with final cross-page polish.
# Presentation-only: no application logic, navigation, data, or widget behavior changes.

# The complete Phase 5e stylesheet is retained. The following Phase 6 rules are inserted
# after the Phase 5e section and before the responsive media queries:
#
# /* Phase 6: Responsive, accessibility, and regression hardening */
# [data-testid="stAppViewContainer"] :focus-visible,
# [data-testid="stSidebar"] :focus-visible,
# button:focus-visible,
# a:focus-visible,
# input:focus-visible,
# textarea:focus-visible,
# [role="button"]:focus-visible,
# [role="tab"]:focus-visible {{
#   outline: 3px solid rgba(58, 111, 243, 0.72) !important;
#   outline-offset: 3px !important;
# }}
#
# [data-testid="stSidebar"] [role="radiogroup"] label,
# [data-testid="stButton"] button,
# [data-testid="stDownloadButton"] button,
# [data-testid="stFormSubmitButton"] button {{
#   min-height: 2.75rem;
# }}
#
# [data-testid="stMarkdownContainer"],
# [data-testid="stAlert"],
# [data-testid="stExpander"],
# .sash-card,
# .metric-card {{
#   overflow-wrap: anywhere;
# }}
#
# [data-testid="stDataFrame"],
# [data-testid="stTable"],
# [data-testid="stMarkdownContainer"] pre {{
#   overflow-x: auto;
# }}
#
# .sash-card,
# .metric-card,
# [data-testid="stForm"],
# [data-testid="stMetric"],
# [data-testid="stAlert"],
# [data-testid="stExpander"] {{
#   @supports not (backdrop-filter: blur(1px)) {
#     background: #FFFFFF;
#   }
# }}
#
# @media (hover: none) {
#   .sash-card:hover,
#   .metric-card:hover,
#   [data-testid="stMetric"]:hover,
#   [data-testid="stButton"] button:hover,
#   [data-testid="stDownloadButton"] button:hover,
#   [data-testid="stFormSubmitButton"] button:hover {
#     transform: none;
#   }
# }
#
# @media (max-width: 1024px) {
#   [data-testid="stMainBlockContainer"] {
#     padding: 1.35rem 1.15rem 2.75rem;
#   }
#
#   [data-testid="stHorizontalBlock"] {
#     gap: 0.9rem;
#   }
# }
#
# @media (max-width: 640px) {
#   [data-testid="stSidebar"] [role="radiogroup"] label {
#     min-height: 2.95rem;
#   }
#
#   [data-testid="stDataFrame"],
#   [data-testid="stTable"] {
#     border-radius: 0.65rem;
#   }
#
#   [data-testid="stMarkdownContainer"] pre {
#     padding: 0.75rem;
#   }
# }