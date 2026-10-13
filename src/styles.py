# Palette: periwinkle, indigo, blue, plum, black, and white.
COLOR_PRIMARY = "#3A6FF3"
COLOR_PRIMARY_LIGHT = "#CED5E8"
COLOR_PRIMARY_DARK = "#1D2240"
COLOR_SECONDARY = "#564957"
COLOR_SECONDARY_LIGHT = "#CED5E8"
COLOR_SUCCESS = "#26734D"
COLOR_WARNING = "#805600"
COLOR_ERROR = "#B42318"
COLOR_INFO = "#1D2240"
COLOR_BACKGROUND = "#F6F7FB"
COLOR_SURFACE = "#FFFFFF"
COLOR_BORDER = "#CED5E8"
COLOR_TEXT = "#1D2240"
COLOR_TEXT_MUTED = "#564957"
FONT_FAMILY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
FONT_MONO = "'SFMono-Regular', Consolas, monospace"
SPACING_XS = "0.25rem"
SPACING_SM = "0.5rem"
SPACING_MD = "1rem"
SPACING_LG = "1.5rem"
SPACING_XL = "2rem"
RADIUS_SM = "0.25rem"
RADIUS_MD = "0.5rem"
RADIUS_LG = "0.75rem"
RADIUS_FULL = "9999px"
SHADOW_SM = "0 2px 8px rgba(29, 34, 64, 0.06)"
SHADOW_MD = "0 6px 18px rgba(29, 34, 64, 0.09)"
SHADOW_LG = "0 12px 30px rgba(29, 34, 64, 0.12)"


def get_custom_css() -> str:
    """Return Sash's readable, responsive theme with subtle glass cards."""
    return f"""
    <style>
    :root {{
      --sash-blue: {COLOR_PRIMARY};
      --sash-periwinkle: {COLOR_PRIMARY_LIGHT};
      --sash-indigo: {COLOR_PRIMARY_DARK};
      --sash-plum: {COLOR_SECONDARY};
      --sash-text: {COLOR_TEXT};
      --sash-muted: {COLOR_TEXT_MUTED};
      --sash-page: {COLOR_BACKGROUND};
      --sash-surface: {COLOR_SURFACE};
      --sash-border: {COLOR_BORDER};
    }}

    .stApp, [data-testid="stAppViewContainer"] {{
      background: var(--sash-page);
      color: var(--sash-text);
      font-family: {FONT_FAMILY};
    }}

    [data-testid="stMainBlockContainer"] {{
      width: 100%;
      max-width: 1440px;
      padding: clamp(1rem, 3vw, 2.5rem);
    }}

    h1, h2, h3, h4, h5, h6 {{
      color: var(--sash-indigo);
      font-family: {FONT_FAMILY};
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.25;
    }}

    p, li, label {{ color: var(--sash-text); line-height: 1.6; }}
    [data-testid="stCaptionContainer"] {{ color: var(--sash-muted); }}

    [data-testid="stSidebar"] {{
      background: var(--sash-surface);
      border-right: 1px solid var(--sash-border);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label {{
      min-height: 2.75rem;
      border-radius: 0.6rem;
      padding: 0.35rem 0.55rem;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {{
      background: #EEF1F8;
    }}

    .sash-card, .metric-card, [data-testid="stVerticalBlockBorderWrapper"] {{
      background: rgba(255, 255, 255, 0.90);
      border: 1px solid rgba(206, 213, 232, 0.95);
      border-radius: 0.85rem;
      box-shadow: 0 2px 10px rgba(29, 34, 64, 0.055);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
    }}

    .sash-card {{
      padding: clamp(1rem, 2vw, 1.5rem);
      margin: 0.5rem 0 1rem;
      overflow-wrap: anywhere;
    }}

    .metric-card {{ padding: 1.25rem; color: var(--sash-indigo); }}
    .metric-value {{ color: var(--sash-indigo); font-size: clamp(1.75rem, 4vw, 2.5rem); font-weight: 700; }}
    .metric-label {{ color: var(--sash-muted); font-size: 0.9rem; }}

    .status-badge {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 0.25rem 0.7rem;
      font-size: 0.8rem;
      font-weight: 600;
    }}
    .status-info {{ background: #E9EDFA; color: var(--sash-indigo); }}

    .empty-state {{
      border: 1px dashed var(--sash-border);
      border-radius: 0.85rem;
      padding: 2rem 1rem;
      text-align: center;
      background: var(--sash-surface);
    }}

    a {{ color: var(--sash-indigo); text-underline-offset: 0.16em; }}
    a:hover {{ color: var(--sash-blue); }}

    [data-testid="stButton"] button,
    [data-testid="stDownloadButton"] button {{
      min-height: 2.75rem;
      border-radius: 0.6rem;
      font-weight: 600;
    }}

    [data-testid="stButton"] button[kind="primary"],
    [data-testid="stFormSubmitButton"] button[kind="primary"] {{
      background: var(--sash-indigo);
      color: #FFFFFF;
      border: 1px solid var(--sash-indigo);
    }}

    [data-testid="stButton"] button[kind="primary"]:hover,
    [data-testid="stFormSubmitButton"] button[kind="primary"]:hover {{
      background: var(--sash-blue);
      color: #FFFFFF;
      border-color: var(--sash-blue);
    }}

    [data-testid="stDataFrame"], [data-testid="stTable"] {{
      max-width: 100%;
      overflow-x: auto;
    }}

    /* Phase 3: application shell and navigation refinement */
    [data-testid="stSidebar"] [role="radiogroup"] label {{
      transition: background-color 120ms ease, color 120ms ease;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{
      background: var(--sash-periwinkle);
      color: var(--sash-indigo);
      box-shadow: inset 0 0 0 1px rgba(29, 34, 64, 0.18);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {{
      color: var(--sash-indigo);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:focus-within {{
      outline: 2px solid var(--sash-blue);
      outline-offset: 2px;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {{
      background: #EEF1F8;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked):hover {{
      background: var(--sash-periwinkle);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label p {{
      font-weight: 500;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {{
      font-weight: 650;
    }}

    [data-testid="stAppViewContainer"] :focus-visible,
    [data-testid="stSidebar"] :focus-visible {{
      outline: 2px solid var(--sash-blue);
      outline-offset: 2px;
    }}

    /* Phase 4: shared visual component refinement */
    .stAlert {{
      border: 1px solid var(--sash-border);
      border-radius: 0.6rem;
      box-shadow: 0 2px 8px rgba(29, 34, 64, 0.05);
    }}

    [data-testid="stExpander"] {{
      border: 1px solid var(--sash-border);
      border-radius: 0.6rem;
      background: var(--sash-surface);
      box-shadow: 0 2px 8px rgba(29, 34, 64, 0.04);
    }}

    [data-testid="stExpander"] summary {{
      border-radius: 0.6rem;
    }}

    [data-testid="stExpander"] summary:hover {{
      background: #EEF1F8;
    }}

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {{
      border: 1px solid var(--sash-border);
      border-radius: 0.6rem;
      overflow: hidden;
    }}

    [data-testid="stForm"] {{
      border: 1px solid var(--sash-border);
      border-radius: 0.85rem;
      background: var(--sash-surface);
      padding: 1rem;
    }}

    [data-testid="stForm"] label,
    [data-testid="stTextInput"] label,
    [data-testid="stTextArea"] label,
    [data-testid="stSelectbox"] label,
    [data-testid="stMultiselect"] label,
    [data-testid="stNumberInput"] label {{
      color: var(--sash-text);
      font-weight: 550;
    }}

    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stNumberInput"] input,
    [data-testid="stSelectbox"] div[data-baseweb="select"],
    [data-testid="stMultiselect"] div[data-baseweb="select"] {{
      border-radius: 0.5rem;
    }}

    [data-testid="stTextInput"] input:focus-visible,
    [data-testid="stTextArea"] textarea:focus-visible,
    [data-testid="stNumberInput"] input:focus-visible {{
      outline: 2px solid var(--sash-blue);
      outline-offset: 2px;
    }}

    [data-testid="stButton"] button[kind="secondary"],
    [data-testid="stDownloadButton"] button {{
      background: var(--sash-surface);
      color: var(--sash-indigo);
      border: 1px solid var(--sash-border);
    }}

    [data-testid="stButton"] button[kind="secondary"]:hover,
    [data-testid="stDownloadButton"] button:hover {{
      background: #EEF1F8;
      border-color: var(--sash-periwinkle);
    }}

    .empty-state {{
      box-shadow: 0 2px 8px rgba(29, 34, 64, 0.04);
    }}

    .empty-state-icon {{
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }}

    /* Phase 5: Home and Domain Models page refinement */
    [data-testid="stMainBlockContainer"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {{
      gap: 0.75rem;
    }}

    .sash-card h4 {{
      margin-bottom: 0.65rem;
    }}

    .sash-card ul,
    .sash-card ol {{
      margin-top: 0.35rem;
      margin-bottom: 0;
      padding-left: 1.25rem;
    }}

    .sash-card li {{
      margin-bottom: 0.3rem;
    }}

    [data-testid="stMarkdown"] hr {{
      border-color: var(--sash-border);
      margin: 1.25rem 0;
    }}

    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div.sash-card {{
      height: 100%;
    }}

    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {{
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    /* Phase 5: Qualification and Engagements page refinement */
    [data-testid="stForm"] {{
      margin-bottom: 1.25rem;
    }}

    [data-testid="stForm"] [data-testid="stHorizontalBlock"] {{
      gap: 1rem;
    }}

    .metric-card {{
      border: 1px solid rgba(29, 34, 64, 0.12);
      border-radius: 0.85rem;
      box-shadow: 0 6px 18px rgba(29, 34, 64, 0.09);
    }}

    .metric-card .metric-value,
    .metric-card .metric-label {{
      color: #FFFFFF;
    }}

    .metric-card .metric-label {{
      opacity: 0.92;
    }}

    .sash-card h4 {{
      margin-top: 0;
      margin-bottom: 0.5rem;
    }}

    .sash-card p {{
      margin-top: 0.35rem;
      margin-bottom: 0.35rem;
    }}

    .sash-card .status-badge {{
      margin-top: 0.35rem;
    }}

    .empty-state {{
      margin: 0.5rem 0 1rem;
    }}

    /* Phase 5: Workflows and Run Workflow page refinement */
    [data-testid="stMarkdownContainer"] div.sash-card + div.sash-card {{
      margin-top: 0.75rem;
    }}

    [data-testid="stForm"] {{
      margin-bottom: 1.5rem;
    }}

    [data-testid="stForm"] [data-testid="stHorizontalBlock"] {{
      gap: 1rem;
    }}

    [data-testid="stMarkdownContainer"] h3 {{
      margin-top: 1.5rem;
      margin-bottom: 0.65rem;
    }}

    [data-testid="stDataFrame"] {{
      margin-top: 0.5rem;
      margin-bottom: 1rem;
    }}

    [data-testid="stInfo"] {{
      margin-top: 1rem;
    }}

    @media (max-width: 900px) {{
      [data-testid="stMainBlockContainer"] {{ padding: 1.25rem; }}
    }}

    @media (max-width: 640px) {{
      [data-testid="stMainBlockContainer"] {{ padding: 1rem 0.9rem 1.5rem; }}
      [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap; gap: 0.75rem; }}
      [data-testid="stHorizontalBlock"] > [data-testid="column"] {{
        min-width: min(100%, 18rem);
        flex: 1 1 100%;
      }}
      [data-testid="stMetric"] {{ min-width: 0; overflow-wrap: anywhere; }}
      .sash-card {{ padding: 1rem; }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        scroll-behavior: auto !important;
        animation-duration: 0.01ms !important;
      }}
    }}
    </style>
    """


def page_config(title: str = "Sash", layout: str = "wide") -> None:
    import streamlit as st
    st.set_page_config(page_title=title, page_icon="", layout=layout)


def local_css() -> None:
    import streamlit as st
    st.markdown(get_custom_css(), unsafe_allow_html=True)
