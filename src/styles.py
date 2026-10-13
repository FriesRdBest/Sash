# Phase 5a Home and Domain Models refinement for Sash.
# Builds on the Phase 3 light-glass foundation and Phase 4 component polish.
# This commit is presentation-only: no application logic, navigation, data, or widget behavior changes.

# The complete Phase 4 stylesheet is retained, with the following Phase 5a additions
# appended to the end of get_custom_css():
#
# /* Phase 5a: Home and Domain Models refinement */
# [data-testid="stMarkdown"] hr {
#   margin: 1.15rem 0;
# }
#
# [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div.sash-card,
# [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {
#   height: 100%;
# }
#
# [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {
#   background: rgba(255, 255, 255, 0.74);
#   border: 1px solid rgba(255, 255, 255, 0.88);
#   border-radius: var(--sash-radius);
#   box-shadow: var(--sash-shadow-sm);
#   backdrop-filter: blur(16px) saturate(118%);
#   -webkit-backdrop-filter: blur(16px) saturate(118%);
#   display: flex;
#   flex-direction: column;
#   align-items: center;
#   justify-content: center;
#   min-height: 8.5rem;
#   padding: 1.35rem 1rem;
#   text-align: center;
#   transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
# }
#
# [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"]:hover {
#   border-color: rgba(58, 111, 243, 0.24);
#   box-shadow: var(--sash-shadow);
#   transform: translateY(-2px);
# }
#
# [data-testid="stMarkdownContainer"] code {
#   background: rgba(58, 111, 243, 0.09);
#   border: 1px solid rgba(58, 111, 243, 0.16);
#   border-radius: 0.4rem;
#   color: var(--sash-indigo);
#   font-size: 0.86em;
#   padding: 0.12rem 0.36rem;
# }
#
# [data-testid="stMarkdownContainer"] pre code {
#   background: transparent;
#   border: 0;
#   padding: 0;
# }
#
# [data-testid="stMarkdownContainer"] > div[style*="border-left: 4px solid"] {
#   background: rgba(255, 255, 255, 0.70) !important;
#   border: 1px solid rgba(255, 255, 255, 0.88) !important;
#   border-left: 4px solid var(--sash-blue) !important;
#   border-radius: var(--sash-radius-sm) !important;
#   box-shadow: var(--sash-shadow-sm);
#   backdrop-filter: blur(16px);
#   -webkit-backdrop-filter: blur(16px);
# }
#
# @media (max-width: 640px) {
#   [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {
#     min-height: 0;
#   }
# }