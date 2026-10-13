# Phase 5b Qualification and Engagements refinement for Sash.
# Restores the complete Phase 3/4/5a light-glass stylesheet and adds Phase 5b refinements.
# Presentation-only: no application logic, navigation, data, or widget behavior changes.
COLOR_PRIMARY = "#3A6FF3"
COLOR_PRIMARY_LIGHT = "#CED5E8"
COLOR_PRIMARY_DARK = "#1D2240"
COLOR_SECONDARY = "#564957"
COLOR_SECONDARY_LIGHT = "#E8ECF7"
COLOR_SUCCESS = "#26734D"
COLOR_WARNING = "#805600"
COLOR_ERROR = "#B42318"
COLOR_INFO = "#1D2240"
COLOR_BACKGROUND = "#F5F7FC"
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
RADIUS_SM = "0.75rem"
RADIUS_MD = "1rem"
RADIUS_LG = "1.25rem"
RADIUS_FULL = "9999px"
SHADOW_SM = "0 6px 18px rgba(29, 34, 64, 0.07)"
SHADOW_MD = "0 14px 34px rgba(29, 34, 64, 0.10)"
SHADOW_LG = "0 22px 54px rgba(29, 34, 64, 0.14)"


def get_custom_css() -> str:
    """Return Sash's responsive, accessible light-glass design system."""
    return f"""
    <style>
    :root {{
      --sash-blue: {COLOR_PRIMARY};
      --sash-blue-deep: #275CD8;
      --sash-periwinkle: {COLOR_PRIMARY_LIGHT};
      --sash-indigo: {COLOR_PRIMARY_DARK};
      --sash-text: {COLOR_TEXT};
      --sash-muted: {COLOR_TEXT_MUTED};
      --sash-page: {COLOR_BACKGROUND};
      --sash-surface: {COLOR_SURFACE};
      --sash-border: {COLOR_BORDER};
      --sash-success: {COLOR_SUCCESS};
      --sash-warning: {COLOR_WARNING};
      --sash-danger: {COLOR_ERROR};
      --sash-radius-sm: {RADIUS_SM};
      --sash-radius: {RADIUS_MD};
      --sash-radius-lg: {RADIUS_LG};
      --sash-shadow-sm: {SHADOW_SM};
      --sash-shadow: {SHADOW_MD};
      --sash-shadow-lg: {SHADOW_LG};
    }}

    .stApp, [data-testid="stAppViewContainer"] {{
      background:
        radial-gradient(circle at 8% -12%, rgba(58, 111, 243, 0.19), transparent 34%),
        radial-gradient(circle at 94% 8%, rgba(206, 213, 232, 0.90), transparent 35%),
        linear-gradient(180deg, #F8FAFF 0%, var(--sash-page) 48%, #F2F5FC 100%);
      color: var(--sash-text);
      font-family: {FONT_FAMILY};
    }}

    [data-testid="stMainBlockContainer"] {{
      max-width: 1440px;
      padding: clamp(1.25rem, 3vw, 3.25rem) clamp(1rem, 3.5vw, 4rem) 3.5rem;
    }}

    h1, h2, h3, h4, h5, h6 {{
      color: var(--sash-indigo);
      font-family: {FONT_FAMILY};
      font-weight: 720;
      letter-spacing: -0.035em;
      line-height: 1.16;
    }}

    h1 {{ font-size: clamp(2.1rem, 4vw, 3.35rem); letter-spacing: -0.055em; margin-bottom: 0.35rem; }}
    h2 {{ font-size: clamp(1.5rem, 2.8vw, 2.15rem); margin-top: 2rem; margin-bottom: 0.7rem; padding-bottom: 0.55rem; border-bottom: 1px solid rgba(206, 213, 232, 0.80); }}
    h3 {{ font-size: 1.25rem; margin-top: 1.4rem; margin-bottom: 0.55rem; }}
    h4 {{ font-size: 1.02rem; margin-bottom: 0.55rem; }}

    p, li, label {{ color: var(--sash-text); line-height: 1.62; }}
    a {{ color: var(--sash-blue-deep); font-weight: 650; text-decoration-thickness: 0.08em; text-underline-offset: 0.18em; }}
    a:hover {{ color: var(--sash-blue); }}
    code, pre {{ font-family: {FONT_MONO}; }}
    [data-testid="stCaptionContainer"] {{ color: var(--sash-muted); }}

    [data-testid="stSidebar"] {{
      background: rgba(255, 255, 255, 0.76);
      border-right: 1px solid rgba(206, 213, 232, 0.95);
      backdrop-filter: blur(22px) saturate(120%);
      -webkit-backdrop-filter: blur(22px) saturate(120%);
    }}

    [data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {{ padding-top: 1.25rem; }}
    [data-testid="stSidebar"] h1 {{ font-size: 1.55rem; letter-spacing: -0.05em; margin-bottom: 0.12rem; border: 0; padding: 0; }}
    [data-testid="stSidebar"] [role="radiogroup"] {{ gap: 0.18rem; }}

    [data-testid="stSidebar"] [role="radiogroup"] label {{
      align-items: center; border: 1px solid transparent; border-radius: 0.85rem; margin: 0.08rem 0;
      min-height: 2.85rem; padding: 0.48rem 0.62rem;
      transition: background 160ms ease, border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {{ background: rgba(58, 111, 243, 0.08); border-color: rgba(58, 111, 243, 0.16); transform: translateX(1px); }}

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{
      background: linear-gradient(135deg, rgba(58, 111, 243, 0.18), rgba(255, 255, 255, 0.72));
      border-color: rgba(58, 111, 243, 0.34);
      box-shadow: inset 3px 0 0 var(--sash-blue), 0 7px 18px rgba(58, 111, 243, 0.10);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label p {{ color: var(--sash-text); font-size: 0.93rem; font-weight: 560; }}
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {{ color: var(--sash-indigo); font-weight: 720; }}

    .sash-card, .metric-card, [data-testid="stVerticalBlockBorderWrapper"] {{
      background: rgba(255, 255, 255, 0.78);
      border: 1px solid rgba(255, 255, 255, 0.88);
      border-radius: var(--sash-radius);
      box-shadow: var(--sash-shadow-sm);
      backdrop-filter: blur(18px) saturate(118%);
      -webkit-backdrop-filter: blur(18px) saturate(118%);
      transition: box-shadow 180ms ease, transform 180ms ease, border-color 180ms ease;
    }}

    .sash-card:hover {{ border-color: rgba(58, 111, 243, 0.22); box-shadow: var(--sash-shadow); transform: translateY(-2px); }}

    .sash-card {{ margin: 0.55rem 0 1.1rem; overflow-wrap: anywhere; padding: clamp(1.15rem, 2.1vw, 1.75rem); }}
    .sash-card h4 {{ align-items: center; display: flex; gap: 0.5rem; margin-top: 0; }}

    .sash-card h4::before {{
      background: linear-gradient(180deg, var(--sash-blue), var(--sash-indigo));
      border-radius: 999px; content: ""; display: inline-block; flex: 0 0 auto; height: 1.05rem; width: 0.22rem;
    }}

    .sash-card p {{ margin: 0.35rem 0; }}
    .sash-card ul, .sash-card ol {{ margin: 0.5rem 0 0; padding-left: 1.25rem; }}
    .sash-card li {{ margin-bottom: 0.32rem; }}

    .metric-card {{ color: var(--sash-indigo); padding: 1.35rem; }}
    .metric-card:hover {{ border-color: rgba(58, 111, 243, 0.24); box-shadow: var(--sash-shadow); transform: translateY(-2px); }}

    .metric-value {{ color: var(--sash-indigo); font-size: clamp(2rem, 4vw, 2.75rem); font-weight: 760; letter-spacing: -0.06em; line-height: 1; }}
    .metric-label {{ color: var(--sash-muted); font-size: 0.76rem; font-weight: 720; letter-spacing: 0.065em; margin-top: 0.55rem; text-transform: uppercase; }}

    .status-badge {{ align-items: center; border: 1px solid transparent; border-radius: var(--sash-radius-full); display: inline-flex; font-size: 0.76rem; font-weight: 720; letter-spacing: 0.02em; padding: 0.34rem 0.72rem; }}
    .status-info {{ background: rgba(58, 111, 243, 0.13); border-color: rgba(58, 111, 243, 0.22); color: var(--sash-blue-deep); }}

    .empty-state {{
      background: rgba(255, 255, 255, 0.62); border: 1px dashed rgba(58, 111, 243, 0.35); border-radius: var(--sash-radius);
      color: var(--sash-muted); margin: 0.7rem 0 1.1rem; padding: 2.25rem 1.25rem; text-align: center;
    }}

    .empty-state-icon {{ font-size: 2.1rem; margin-bottom: 0.55rem; }}

    [data-testid="stButton"] button,
    [data-testid="stDownloadButton"] button,
    [data-testid="stFormSubmitButton"] button {{
      border-radius: 0.85rem; font-weight: 700; letter-spacing: -0.01em; min-height: 2.8rem;
      transition: background 160ms ease, border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
    }}

    [data-testid="stButton"] button:hover,
    [data-testid="stDownloadButton"] button:hover,
    [data-testid="stFormSubmitButton"] button:hover {{ transform: translateY(-1px); }}

    [data-testid="stButton"] button[kind="primary"],
    [data-testid="stFormSubmitButton"] button[kind="primary"] {{
      background: linear-gradient(135deg, var(--sash-indigo), var(--sash-blue));
      border: 1px solid var(--sash-indigo); box-shadow: 0 9px 20px rgba(58, 111, 243, 0.23); color: #FFFFFF;
    }}

    [data-testid="stButton"] button[kind="primary"]:hover,
    [data-testid="stFormSubmitButton"] button[kind="primary"]:hover {{
      background: linear-gradient(135deg, var(--sash-blue-deep), var(--sash-blue));
      box-shadow: 0 12px 24px rgba(58, 111, 243, 0.29);
    }}

    [data-testid="stButton"] button[kind="secondary"],
    [data-testid="stDownloadButton"] button {{
      background: rgba(255, 255, 255, 0.76); border: 1px solid rgba(58, 111, 243, 0.22); color: var(--sash-indigo);
    }}

    [data-testid="stButton"] button[kind="secondary"]:hover,
    [data-testid="stDownloadButton"] button:hover {{ background: rgba(58, 111, 243, 0.08); border-color: rgba(58, 111, 243, 0.40); }}

    [data-testid="stForm"] {{
      background: rgba(255, 255, 255, 0.68); border: 1px solid rgba(255, 255, 255, 0.90); border-radius: var(--sash-radius);
      box-shadow: var(--sash-shadow-sm); margin-bottom: 1.35rem; padding: clamp(1rem, 2vw, 1.45rem);
      backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    }}

    [data-testid="stTextInput"] label,
    [data-testid="stTextArea"] label,
    [data-testid="stNumberInput"] label,
    [data-testid="stSelectbox"] label,
    [data-testid="stMultiselect"] label,
    [data-testid="stRadio"] label,
    [data-testid="stCheckbox"] label {{ color: var(--sash-indigo); font-size: 0.9rem; font-weight: 680; }}

    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stNumberInput"] input,
    [data-testid="stSelectbox"] div[data-baseweb="select"],
    [data-testid="stMultiselect"] div[data-baseweb="select"] {{ background: rgba(255, 255, 255, 0.84); border-radius: 0.72rem; }}

    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus,
    [data-testid="stNumberInput"] input:focus {{ border-color: var(--sash-blue); box-shadow: 0 0 0 3px rgba(58, 111, 243, 0.15); }}

    [data-testid="stAlert"] {{
      background: rgba(255, 255, 255, 0.72); border: 1px solid rgba(206, 213, 232, 0.95); border-radius: var(--sash-radius-sm);
      box-shadow: var(--sash-shadow-sm); margin: 0.65rem 0 1rem;
    }}

    [data-testid="stExpander"] {{
      background: rgba(255, 255, 255, 0.72); border: 1px solid rgba(206, 213, 232, 0.92); border-radius: var(--sash-radius-sm);
      box-shadow: 0 4px 14px rgba(29, 34, 64, 0.045); margin: 0.65rem 0 1rem; overflow: hidden;
      transition: border-color 160ms ease, box-shadow 160ms ease;
    }}

    [data-testid="stExpander"]:hover {{ border-color: rgba(58, 111, 243, 0.24); box-shadow: var(--sash-shadow-sm); }}
    [data-testid="stExpander"] summary {{ border-radius: var(--sash-radius-sm); font-weight: 680; }}
    [data-testid="stExpander"] summary:hover {{ background: rgba(58, 111, 243, 0.06); }}

    [data-testid="stMetric"] {{
      background: rgba(255, 255, 255, 0.70); border: 1px solid rgba(255, 255, 255, 0.88); border-radius: var(--sash-radius-sm);
      box-shadow: var(--sash-shadow-sm); min-height: 100%; padding: 1.05rem;
      transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
    }}

    [data-testid="stMetric"]:hover {{ border-color: rgba(58, 111, 243, 0.24); box-shadow: var(--sash-shadow); transform: translateY(-2px); }}
    [data-testid="stMetricLabel"] {{ color: var(--sash-muted); font-weight: 680; }}
    [data-testid="stMetricValue"] {{ color: var(--sash-indigo); font-weight: 760; letter-spacing: -0.04em; }}

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {{
      background: rgba(255, 255, 255, 0.70); border: 1px solid rgba(206, 213, 232, 0.94); border-radius: var(--sash-radius-sm);
      box-shadow: var(--sash-shadow-sm); margin: 0.6rem 0 1.1rem; max-width: 100%; overflow: hidden;
    }}

    [data-testid="stTabs"] [data-baseweb="tab-list"] {{ border-bottom: 1px solid rgba(206, 213, 232, 0.80); gap: 0.35rem; overflow-x: auto; padding-bottom: 0.45rem; }}

    [data-testid="stTabs"] [data-baseweb="tab"] {{
      background: rgba(255, 255, 255, 0.56); border: 1px solid transparent; border-radius: var(--sash-radius-full);
      color: var(--sash-muted); font-weight: 650; height: 2.5rem; padding: 0.35rem 0.85rem;
      transition: background 160ms ease, border-color 160ms ease, color 160ms ease;
    }}

    [data-testid="stTabs"] [data-baseweb="tab"]:hover {{ background: rgba(58, 111, 243, 0.08); color: var(--sash-indigo); }}
    [data-testid="stTabs"] [aria-selected="true"] {{ background: rgba(58, 111, 243, 0.13); border-color: rgba(58, 111, 243, 0.27); color: var(--sash-indigo); }}

    [data-testid="stMarkdown"] hr {{ border-color: rgba(206, 213, 232, 0.92); margin: 1.15rem 0; }}

    [data-testid="stAppViewContainer"] :focus-visible,
    [data-testid="stSidebar"] :focus-visible {{ outline: 3px solid rgba(58, 111, 243, 0.68); outline-offset: 3px; }}

    /* Phase 5a: Home and Domain Models refinement */
    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div.sash-card,
    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {{ height: 100%; }}

    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {{
      align-items: center; background: rgba(255, 255, 255, 0.74); border: 1px solid rgba(255, 255, 255, 0.88);
      border-radius: var(--sash-radius); box-shadow: var(--sash-shadow-sm); backdrop-filter: blur(16px) saturate(118%);
      -webkit-backdrop-filter: blur(16px) saturate(118%); display: flex; flex-direction: column; justify-content: center;
      min-height: 8.5rem; padding: 1.35rem 1rem; text-align: center;
      transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
    }}

    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"]:hover {{
      border-color: rgba(58, 111, 243, 0.24); box-shadow: var(--sash-shadow); transform: translateY(-2px);
    }}

    [data-testid="stMarkdownContainer"] code {{
      background: rgba(58, 111, 243, 0.09); border: 1px solid rgba(58, 111, 243, 0.16); border-radius: 0.4rem;
      color: var(--sash-indigo); font-size: 0.86em; padding: 0.12rem 0.36rem;
    }}

    [data-testid="stMarkdownContainer"] pre code {{ background: transparent; border: 0; padding: 0; }}

    [data-testid="stMarkdownContainer"] > div[style*="border-left: 4px solid"] {{
      background: rgba(255, 255, 255, 0.70) !important; border: 1px solid rgba(255, 255, 255, 0.88) !important;
      border-left: 4px solid var(--sash-blue) !important; border-radius: var(--sash-radius-sm) !important;
      box-shadow: var(--sash-shadow-sm); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    }}

    /* Phase 5b: Qualification and Engagements refinement */
    [data-testid="stForm"] [data-testid="stHorizontalBlock"] {{ gap: 1.1rem; }}

    [data-testid="stForm"] [data-testid="stTextInput"],
    [data-testid="stForm"] [data-testid="stTextArea"],
    [data-testid="stForm"] [data-testid="stNumberInput"],
    [data-testid="stForm"] [data-testid="stSelectbox"],
    [data-testid="stForm"] [data-testid="stMultiselect"] {{ min-width: 0; }}

    .metric-card[style] {{
      border: 1px solid rgba(255, 255, 255, 0.28) !important;
      border-radius: var(--sash-radius) !important;
      box-shadow: var(--sash-shadow) !important;
      color: #FFFFFF !important;
    }}

    .metric-card[style] .metric-value,
    .metric-card[style] .metric-label {{ color: #FFFFFF !important; }}

    .metric-card[style] .metric-label {{ opacity: 0.92; }}

    .sash-card[style*="text-align: center"] {{
      align-items: center; display: flex; flex-direction: column; justify-content: center; min-height: 9rem; text-align: center;
    }}

    .sash-card[style*="border-left"] {{
      border-left-width: 4px !important;
      box-shadow: var(--sash-shadow-sm);
    }}

    .sash-card .status-badge {{ margin-top: 0.4rem; }}

    .sash-card p strong {{ color: var(--sash-indigo); }}

    .empty-state p {{ color: var(--sash-muted); margin: 0; }}

    @media (max-width: 900px) {{
      [data-testid="stMainBlockContainer"] {{ padding: 1.25rem 1.1rem 2.5rem; }}
    }}

    @media (max-width: 640px) {{
      [data-testid="stMainBlockContainer"] {{ padding: 1rem 0.85rem 2rem; }}
      h1 {{ font-size: 2.05rem; }}
      h2 {{ margin-top: 1.5rem; }}
      [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap; gap: 0.8rem; }}
      [data-testid="stHorizontalBlock"] > [data-testid="column"] {{ flex: 1 1 100%; min-width: min(100%, 18rem); }}
      .sash-card {{ padding: 1rem; }}
      .sash-card:hover {{ transform: none; }}
      [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {{ min-height: 0; }}
      [data-testid="stButton"] button,
      [data-testid="stDownloadButton"] button,
      [data-testid="stFormSubmitButton"] button {{ width: 100%; }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        animation-duration: 0.01ms !important;
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
      }}
    }}
    </style>
    """


def page_config(title: str = "Sash", layout: str = "wide") -> None:
    """Set shared Streamlit page configuration."""
    import streamlit as st

    st.set_page_config(page_title=title, page_icon="", layout=layout)


def local_css() -> None:
    """Inject Sash's shared design system into the Streamlit page."""
    import streamlit as st

    st.markdown(get_custom_css(), unsafe_allow_html=True)
