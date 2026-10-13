"""Shared premium Amberglass design system for Sash."""

COLOR_PRIMARY = "#000000"
COLOR_PRIMARY_LIGHT = "#FEBD3C"
COLOR_PRIMARY_DARK = "#000000"
COLOR_SECONDARY = "#B98A68"
COLOR_SECONDARY_LIGHT = "#FFF1CC"
COLOR_SUCCESS = "#1E7A46"
COLOR_WARNING = "#8A5A00"
COLOR_ERROR = "#B42318"
COLOR_INFO = "#1F4F8F"
COLOR_BACKGROUND = "#FEBD3C"
COLOR_SURFACE = "#FFF7E5"
COLOR_BORDER = "#B98A68"
COLOR_TEXT = "#000000"
COLOR_TEXT_MUTED = "#4B3529"
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
SHADOW_SM = "0 6px 18px rgba(66, 43, 17, 0.10)"
SHADOW_MD = "0 14px 34px rgba(66, 43, 17, 0.16)"
SHADOW_LG = "0 22px 54px rgba(66, 43, 17, 0.22)"


def get_custom_css() -> str:
    """Return Sash's responsive Amberglass visual system."""
    return f"""
    <style>
    :root {{
      --sash-black: {COLOR_PRIMARY};
      --sash-amber: {COLOR_PRIMARY_LIGHT};
      --sash-bronze: {COLOR_SECONDARY};
      --sash-cream: {COLOR_SURFACE};
      --sash-cream-deep: #F3DFC0;
      --sash-text: {COLOR_TEXT};
      --sash-muted: {COLOR_TEXT_MUTED};
      --sash-success: {COLOR_SUCCESS};
      --sash-warning: {COLOR_WARNING};
      --sash-danger: {COLOR_ERROR};
      --sash-info: {COLOR_INFO};
      --sash-radius-sm: {RADIUS_SM};
      --sash-radius: {RADIUS_MD};
      --sash-radius-lg: {RADIUS_LG};
      --sash-radius-full: {RADIUS_FULL};
      --sash-shadow-sm: {SHADOW_SM};
      --sash-shadow: {SHADOW_MD};
      --sash-shadow-lg: {SHADOW_LG};
    }}

    .stApp, [data-testid="stAppViewContainer"] {{
      background:
        radial-gradient(circle at 7% -10%, rgba(255,255,255,0.48), transparent 34%),
        radial-gradient(circle at 100% 0%, rgba(185,138,104,0.31), transparent 30%),
        linear-gradient(145deg, #FEBD3C 0%, #FFD66F 48%, #F2B331 100%);
      color: var(--sash-text);
      font-family: {FONT_FAMILY};
    }}

    [data-testid="stMainBlockContainer"] {{
      max-width: 1440px;
      padding: clamp(1.25rem, 3vw, 3.25rem) clamp(1rem, 3.5vw, 4rem) 3.5rem;
    }}

    h1, h2, h3, h4, h5, h6 {{
      color: var(--sash-text);
      font-family: {FONT_FAMILY};
      font-weight: 760;
      letter-spacing: -0.04em;
      line-height: 1.16;
    }}

    h1 {{
      font-size: clamp(2.1rem, 4vw, 3.35rem);
      letter-spacing: -0.06em;
      margin-bottom: 0.35rem;
    }}

    h2 {{
      border-bottom: 1px solid rgba(185,138,104,0.70);
      font-size: clamp(1.5rem, 2.8vw, 2.15rem);
      margin-bottom: 0.7rem;
      margin-top: 2rem;
      padding-bottom: 0.55rem;
    }}

    h3 {{ font-size: 1.25rem; margin-bottom: 0.55rem; margin-top: 1.4rem; }}
    h4 {{ font-size: 1.02rem; margin-bottom: 0.55rem; }}
    p, li, label {{ color: var(--sash-text); line-height: 1.62; }}
    a {{ color: var(--sash-text); font-weight: 720; text-decoration-color: var(--sash-bronze); text-decoration-thickness: 0.11em; text-underline-offset: 0.18em; }}
    a:hover {{ color: #5E3E28; }}
    code, pre {{ font-family: {FONT_MONO}; }}
    [data-testid="stCaptionContainer"] {{ color: var(--sash-muted); }}

    [data-testid="stSidebar"] {{
      background: #000000;
      border-right: 1px solid rgba(254,189,60,0.42);
    }}

    [data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {{
      padding-top: 1.25rem;
    }}

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] * {{
      color: #FFFFFF;
    }}

    [data-testid="stSidebar"] h1 {{
      border: 0;
      font-size: 1.55rem;
      letter-spacing: -0.05em;
      margin-bottom: 0.12rem;
      padding: 0;
    }}

    [data-testid="stSidebar"] hr {{
      border-color: rgba(254,189,60,0.25);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] {{
      gap: 0.18rem;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label {{
      align-items: center;
      background: transparent;
      border: 1px solid transparent;
      border-radius: 0.85rem;
      margin: 0.08rem 0;
      min-height: 2.85rem;
      padding: 0.48rem 0.62rem;
      transition: background 160ms ease, border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label p {{
      color: #FFFFFF;
      font-size: 0.93rem;
      font-weight: 580;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {{
      background: rgba(255,255,255,0.10);
      border-color: rgba(254,189,60,0.42);
      transform: translateX(1px);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{
      background: #FEBD3C;
      border-color: #FEBD3C;
      box-shadow: 0 8px 18px rgba(0,0,0,0.28);
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {{
      color: #000000;
      font-weight: 760;
    }}

    .sash-card,
    .metric-card,
    [data-testid="stVerticalBlockBorderWrapper"] {{
      background: rgba(255,247,229,0.72);
      border: 1px solid rgba(185,138,104,0.86);
      border-radius: var(--sash-radius);
      box-shadow: var(--sash-shadow-sm);
      backdrop-filter: blur(18px) saturate(112%);
      -webkit-backdrop-filter: blur(18px) saturate(112%);
      transition: border-color 180ms ease, box-shadow 180ms ease, transform 180ms ease;
    }}

    .sash-card:hover,
    .metric-card:hover {{
      border-color: rgba(0,0,0,0.72);
      box-shadow: var(--sash-shadow);
      transform: translateY(-2px);
    }}

    .sash-card {{
      margin: 0.55rem 0 1.1rem;
      overflow-wrap: anywhere;
      padding: clamp(1.15rem, 2.1vw, 1.75rem);
      position: relative;
    }}

    .sash-card h4 {{
      align-items: center;
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.7rem;
      margin-top: 0;
    }}

    .sash-card h4::before {{
      background: #000000;
      border-radius: 999px;
      content: "";
      display: inline-block;
      flex: 0 0 auto;
      height: 1.05rem;
      width: 0.22rem;
    }}

    .sash-card p {{ margin: 0.42rem 0; }}
    .sash-card ul, .sash-card ol {{ margin: 0.55rem 0 0; padding-left: 1.25rem; }}
    .sash-card li {{ margin-bottom: 0.38rem; }}
    .sash-card strong {{ color: #000000; }}

    .metric-card {{ color: #000000; padding: 1.35rem; }}
    .metric-value {{ color: #000000; font-size: clamp(2rem, 4vw, 2.75rem); font-weight: 780; letter-spacing: -0.06em; line-height: 1; }}
    .metric-label {{ color: var(--sash-muted); font-size: 0.76rem; font-weight: 760; letter-spacing: 0.065em; margin-top: 0.55rem; text-transform: uppercase; }}

    .status-badge {{
      align-items: center;
      border: 1px solid transparent;
      border-radius: var(--sash-radius-full);
      box-shadow: 0 2px 8px rgba(66,43,17,0.10);
      display: inline-flex;
      font-size: 0.76rem;
      font-weight: 740;
      letter-spacing: 0.02em;
      padding: 0.34rem 0.72rem;
    }}

    .status-info {{
      background: rgba(254,189,60,0.78);
      border-color: rgba(0,0,0,0.24);
      color: #000000;
    }}

    .empty-state {{
      background: rgba(255,247,229,0.66);
      border: 1px dashed rgba(0,0,0,0.46);
      border-radius: var(--sash-radius);
      color: var(--sash-muted);
      margin: 0.7rem 0 1.1rem;
      padding: 2.25rem 1.25rem;
      text-align: center;
    }}

    .empty-state p {{ color: var(--sash-muted); margin: 0; }}

    [data-testid="stButton"] button,
    [data-testid="stDownloadButton"] button,
    [data-testid="stFormSubmitButton"] button {{
      border-radius: 0.85rem;
      font-weight: 740;
      letter-spacing: -0.01em;
      min-height: 2.8rem;
      transition: background 160ms ease, border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
    }}

    [data-testid="stButton"] button:hover,
    [data-testid="stDownloadButton"] button:hover,
    [data-testid="stFormSubmitButton"] button:hover {{
      transform: translateY(-1px);
    }}

    [data-testid="stButton"] button[kind="primary"],
    [data-testid="stFormSubmitButton"] button[kind="primary"] {{
      background: #000000;
      border: 1px solid #000000;
      box-shadow: 0 9px 20px rgba(0,0,0,0.22);
      color: #FFFFFF;
    }}

    [data-testid="stButton"] button[kind="primary"]:hover,
    [data-testid="stFormSubmitButton"] button[kind="primary"]:hover {{
      background: #2A211A;
      border-color: #2A211A;
      box-shadow: 0 12px 24px rgba(0,0,0,0.30);
    }}

    [data-testid="stButton"] button[kind="secondary"],
    [data-testid="stDownloadButton"] button {{
      background: rgba(255,247,229,0.82);
      border: 1px solid var(--sash-bronze);
      color: #000000;
    }}

    [data-testid="stButton"] button[kind="secondary"]:hover,
    [data-testid="stDownloadButton"] button:hover {{
      background: #FFF1CC;
      border-color: #000000;
    }}

    [data-testid="stForm"] {{
      background: rgba(255,247,229,0.72);
      border: 1px solid rgba(185,138,104,0.86);
      border-radius: var(--sash-radius);
      box-shadow: var(--sash-shadow-sm);
      margin-bottom: 1.35rem;
      padding: clamp(1rem, 2vw, 1.45rem);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }}

    [data-testid="stTextInput"] label,
    [data-testid="stTextArea"] label,
    [data-testid="stNumberInput"] label,
    [data-testid="stSelectbox"] label,
    [data-testid="stMultiselect"] label,
    [data-testid="stRadio"] label,
    [data-testid="stCheckbox"] label {{
      color: #000000;
      font-size: 0.9rem;
      font-weight: 700;
    }}

    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stNumberInput"] input,
    [data-testid="stSelectbox"] div[data-baseweb="select"],
    [data-testid="stMultiselect"] div[data-baseweb="select"] {{
      background: rgba(255,252,244,0.94);
      border-radius: 0.72rem;
      color: #000000;
    }}

    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus,
    [data-testid="stNumberInput"] input:focus {{
      border-color: #000000;
      box-shadow: 0 0 0 3px rgba(254,189,60,0.65);
    }}

    [data-testid="stAlert"] {{
      background: rgba(255,247,229,0.80);
      border: 1px solid rgba(185,138,104,0.86);
      border-radius: var(--sash-radius-sm);
      box-shadow: var(--sash-shadow-sm);
      margin: 0.7rem 0 1.1rem;
      overflow-wrap: anywhere;
    }}

    [data-testid="stExpander"] {{
      background: rgba(255,247,229,0.76);
      border: 1px solid rgba(185,138,104,0.82);
      border-radius: var(--sash-radius-sm);
      box-shadow: 0 4px 14px rgba(66,43,17,0.08);
      margin: 0.7rem 0 1.1rem;
      overflow: hidden;
      overflow-wrap: anywhere;
      transition: border-color 160ms ease, box-shadow 160ms ease;
    }}

    [data-testid="stExpander"]:hover {{
      border-color: rgba(0,0,0,0.64);
      box-shadow: var(--sash-shadow-sm);
    }}

    [data-testid="stExpander"] summary {{ border-radius: var(--sash-radius-sm); font-weight: 700; }}
    [data-testid="stExpander"] summary:hover {{ background: rgba(254,189,60,0.24); }}

    [data-testid="stMetric"] {{
      background: rgba(255,247,229,0.74);
      border: 1px solid rgba(185,138,104,0.86);
      border-radius: var(--sash-radius-sm);
      box-shadow: var(--sash-shadow-sm);
      min-height: 100%;
      min-width: 0;
      padding: 1.1rem;
      transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
    }}

    [data-testid="stMetric"]:hover {{
      border-color: rgba(0,0,0,0.68);
      box-shadow: var(--sash-shadow);
      transform: translateY(-2px);
    }}

    [data-testid="stMetricLabel"] {{ color: var(--sash-muted); font-weight: 700; }}
    [data-testid="stMetricValue"] {{ color: #000000; font-size: 1.85rem; font-weight: 780; letter-spacing: -0.04em; }}

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {{
      background: rgba(255,252,244,0.88);
      border: 1px solid rgba(185,138,104,0.88);
      border-radius: var(--sash-radius-sm);
      box-shadow: var(--sash-shadow-sm);
      margin: 0.7rem 0 1.2rem;
      max-width: 100%;
      overflow: hidden;
    }}

    [data-testid="stTabs"] [data-baseweb="tab-list"] {{
      border-bottom: 1px solid rgba(185,138,104,0.76);
      gap: 0.35rem;
      overflow-x: auto;
      padding-bottom: 0.45rem;
    }}

    [data-testid="stTabs"] [data-baseweb="tab"] {{
      background: rgba(255,247,229,0.55);
      border: 1px solid transparent;
      border-radius: var(--sash-radius-full);
      color: var(--sash-muted);
      font-weight: 680;
      height: 2.5rem;
      padding: 0.35rem 0.85rem;
    }}

    [data-testid="stTabs"] [data-baseweb="tab"]:hover {{
      background: rgba(255,247,229,0.82);
      border-color: rgba(185,138,104,0.72);
      color: #000000;
    }}

    [data-testid="stTabs"] [aria-selected="true"] {{
      background: #000000;
      border-color: #000000;
      color: #FFFFFF;
    }}

    [data-testid="stMarkdown"] hr {{
      border-color: rgba(185,138,104,0.74);
      margin: 1.25rem 0;
    }}

    [data-testid="stMarkdownContainer"] code {{
      background: rgba(255,247,229,0.76);
      border: 1px solid rgba(185,138,104,0.70);
      border-radius: 0.4rem;
      color: #000000;
      font-size: 0.86em;
      overflow-wrap: anywhere;
      padding: 0.12rem 0.36rem;
      white-space: normal;
    }}

    [data-testid="stMarkdownContainer"] pre {{
      background: rgba(255,252,244,0.90);
      border: 1px solid rgba(185,138,104,0.84);
      border-radius: 0.7rem;
      box-shadow: var(--sash-shadow-sm);
      overflow-x: auto;
      padding: 0.9rem;
    }}

    [data-testid="stMarkdownContainer"] pre code {{
      background: transparent;
      border: 0;
      color: #000000;
      padding: 0;
      white-space: pre;
    }}

    [data-testid="stAppViewContainer"] :focus-visible,
    [data-testid="stSidebar"] :focus-visible,
    button:focus-visible,
    a:focus-visible,
    input:focus-visible,
    textarea:focus-visible,
    [role="button"]:focus-visible,
    [role="tab"]:focus-visible {{
      outline: 3px solid #000000 !important;
      outline-offset: 3px !important;
    }}

    [data-testid="stHorizontalBlock"] {{ align-items: stretch; }}
    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] {{ height: 100%; }}

    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div.sash-card,
    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {{
      height: 100%;
    }}

    [data-testid="stHorizontalBlock"] > [data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdown"] > div[data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {{
      align-items: center;
      background: rgba(255,247,229,0.72);
      border: 1px solid rgba(185,138,104,0.86);
      border-radius: var(--sash-radius);
      box-shadow: var(--sash-shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: center;
      min-height: 8.5rem;
      padding: 1.35rem 1rem;
      text-align: center;
      backdrop-filter: blur(16px) saturate(112%);
      -webkit-backdrop-filter: blur(16px) saturate(112%);
    }}

    [data-testid="stMarkdownContainer"] > div[style*="border-left: 4px solid"],
    [data-testid="stMarkdownContainer"] > div[style*="border-left: 3px solid"] {{
      background: rgba(255,247,229,0.76) !important;
      border: 1px solid rgba(185,138,104,0.86) !important;
      border-left: 4px solid #000000 !important;
      border-radius: var(--sash-radius-sm) !important;
      box-shadow: var(--sash-shadow-sm);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }}

    .metric-card[style] {{
      border: 1px solid rgba(255,247,229,0.60) !important;
      border-radius: var(--sash-radius) !important;
      box-shadow: var(--sash-shadow) !important;
    }}

    .metric-card[style] .metric-value,
    .metric-card[style] .metric-label {{
      color: #FFFFFF !important;
    }}

    @supports not (backdrop-filter: blur(1px)) {{
      .sash-card,
      .metric-card,
      [data-testid="stForm"],
      [data-testid="stMetric"],
      [data-testid="stAlert"],
      [data-testid="stExpander"] {{
        background: #FFF7E5;
      }}
    }}

    @media (hover: none) {{
      .sash-card:hover,
      .metric-card:hover,
      [data-testid="stMetric"]:hover,
      [data-testid="stButton"] button:hover,
      [data-testid="stDownloadButton"] button:hover,
      [data-testid="stFormSubmitButton"] button:hover {{
        transform: none;
      }}
    }}

    @media (max-width: 1024px) {{
      [data-testid="stMainBlockContainer"] {{ padding: 1.35rem 1.15rem 2.75rem; }}
      [data-testid="stHorizontalBlock"] {{ gap: 0.9rem; }}
    }}

    @media (max-width: 640px) {{
      [data-testid="stMainBlockContainer"] {{ padding: 1rem 0.85rem 2rem; }}
      h1 {{ font-size: 2.05rem; }}
      h2 {{ margin-top: 1.5rem; }}
      [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap; gap: 0.8rem; }}
      [data-testid="stHorizontalBlock"] > [data-testid="column"] {{ flex: 1 1 100%; min-width: min(100%, 18rem); }}
      .sash-card {{ padding: 1rem; }}
      .sash-card:hover {{ transform: none; }}
      [data-testid="stSidebar"] [role="radiogroup"] label {{ min-height: 2.95rem; }}
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

    /* Amberglass surface and responsive polish */
    :root {{
      --sash-shadow-sm:
        inset 0 1px 0 rgba(255,255,255,.85),
        inset 0 -1px 0 rgba(108,68,34,.08),
        0 8px 20px rgba(82,49,16,.10);
      --sash-shadow:
        inset 0 1px 0 rgba(255,255,255,.90),
        0 14px 32px rgba(82,49,16,.15);
    }}

    [data-testid="stMainBlockContainer"] {{
      padding: clamp(1.25rem,3vw,3rem) clamp(1rem,3vw,3rem) 3rem;
    }}

    .sash-card,
    [data-testid="stMetric"],
    [data-testid="stForm"],
    [data-testid="stExpander"] {{
      border-color: #B98A68;
      border-radius: 1.25rem;
      box-shadow: var(--sash-shadow-sm);
    }}

    .sash-card {{
      background: linear-gradient(
        145deg, rgba(255,252,243,.86), rgba(255,241,210,.74)
      );
      padding: clamp(1.25rem,2.4vw,2rem);
      margin: 0 0 1.25rem;
    }}

    .sash-card:hover,
    [data-testid="stMetric"]:hover {{
      border-color: #B98A68;
      transform: none;
      box-shadow: var(--sash-shadow);
    }}

    .sash-home-card {{
      box-sizing: border-box;
      height: 100%;
    }}

    .sash-home-card h2 {{
      font-size: clamp(1.5rem,2.2vw,2rem);
      margin: .55rem 0 1rem;
      padding: 0;
      border: 0;
      line-height: 1.2;
    }}

    .sash-eyebrow {{
      color: #4B3529;
      font-size: .72rem;
      font-weight: 750;
      letter-spacing: .12em;
      line-height: 1.5;
    }}

    .sash-home-card p {{ margin: 0 0 .8rem; }}
    .sash-home-card ul,
    .sash-home-card ol {{ padding-left: 1.3rem; margin: 0; }}
    .sash-home-card li {{ padding-left: .15rem; margin-bottom: .55rem; }}

    .sash-home-card .sash-card-footer {{
      border-top: 1px solid rgba(185,138,104,.55);
      margin: 1.25rem 0 0;
      padding-top: 1rem;
    }}

    [data-testid="stMarkdownContainer"] > div[style*="text-align: center"] {{
      background: linear-gradient(
        145deg, rgba(255,252,243,.86), rgba(255,241,210,.74)
      ) !important;
      border: 1px solid #B98A68 !important;
      border-radius: 1.25rem !important;
      padding: 1.5rem !important;
      box-shadow: var(--sash-shadow-sm);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
    }}

    [data-testid="stHorizontalBlock"] {{
      gap: clamp(1rem,2vw,1.75rem);
      align-items: stretch;
    }}

    [data-testid="stColumn"],
    [data-testid="column"] {{
      min-width: 0;
    }}

    [data-testid="stSidebar"] :focus-visible {{
      outline-color: #FEBD3C !important;
    }}

    [data-testid="stButton"] button[kind="primary"] p,
    [data-testid="stFormSubmitButton"] button[kind="primary"] p,
    [data-testid="stTabs"] [aria-selected="true"] p {{
      color: #FFFFFF;
    }}

    @media (max-width: 760px) {{
      [data-testid="stMainBlockContainer"] {{
        padding: 1.25rem 1rem 2rem;
      }}

      [data-testid="stHorizontalBlock"] {{
        flex-direction: column;
        gap: 1rem;
      }}

      [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
      [data-testid="stHorizontalBlock"] > [data-testid="column"] {{
        width: 100% !important;
        flex: 1 1 auto !important;
        min-width: 0 !important;
      }}

      .sash-home-card {{ height: auto; }}
      .sash-card {{ padding: 1.25rem; margin-bottom: .5rem; }}
      h1 {{ font-size: 2.1rem; }}
    }}

    @supports not (backdrop-filter: blur(1px)) {{
      .sash-card {{ background: #FFF7E5; }}
    }}




    .sash-app-footer {{
      align-items: center;
      background: rgba(0,0,0,0.94);
      border: 1px solid rgba(254,189,60,0.42);
      border-radius: 1rem;
      box-shadow: 0 10px 26px rgba(0,0,0,0.18);
      color: rgba(255,255,255,0.92);
      display: flex;
      flex-wrap: wrap;
      font-size: 0.82rem;
      font-weight: 560;
      gap: 0.45rem;
      justify-content: center;
      letter-spacing: 0.005em;
      line-height: 1.55;
      margin: 2rem 0 1.25rem;
      padding: 0.95rem 1.2rem;
      text-align: center;
    }}

    .sash-footer-product,
    .sash-footer-byline {{
      color: #FEBD3C;
      font-weight: 760;
    }}

    .sash-footer-separator {{
      color: rgba(254,189,60,0.70);
    }}

    @media (max-width: 640px) {{
      .sash-app-footer {{
        align-items: center;
        flex-direction: column;
        gap: 0.18rem;
        margin: 1.5rem 0 .75rem;
        padding: 1rem;
      }}

      .sash-footer-separator {{
        display: none;
      }}
    }}


    /* Dedicated Quick Links grid: four desktop cards, stacked mobile cards. */
    .sash-quick-links {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: clamp(.75rem, 1.5vw, 1.25rem);
      margin-bottom: 1.5rem;
      width: 100%;
    }}

    .sash-quick-links .sash-link-card {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: .45rem;
      box-sizing: border-box;
      min-width: 0;
      min-height: 7rem;
      margin: 0;
      padding: 1.25rem .75rem;
      text-align: center;
    }}

    @media (max-width: 600px) {{
      .sash-quick-links {{
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }}
    }}

    @media (max-width: 380px) {{
      .sash-quick-links {{
        grid-template-columns: minmax(0, 1fr);
      }}
    }}


    /* All page operational polish */
    [data-testid="stForm"] [data-testid="stHorizontalBlock"] {{
      gap: clamp(.8rem, 1.6vw, 1.25rem);
    }}

    [data-testid="stTextInput"],
    [data-testid="stTextArea"],
    [data-testid="stNumberInput"],
    [data-testid="stSelectbox"],
    [data-testid="stMultiselect"],
    [data-testid="stDateInput"] {{
      min-width: 0;
    }}

    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stNumberInput"] input {{
      border: 1px solid rgba(185,138,104,.86);
      box-sizing: border-box;
      color: #000000;
    }}

    [data-testid="stTextInput"] input:hover,
    [data-testid="stTextArea"] textarea:hover,
    [data-testid="stNumberInput"] input:hover {{
      border-color: #000000;
    }}

    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMultiselect"] [data-baseweb="select"] > div {{
      border-color: rgba(185,138,104,.86) !important;
      color: #000000 !important;
    }}

    [data-testid="stDataFrame"] {{
      border-color: #B98A68;
      border-radius: 1rem;
      box-shadow: var(--sash-shadow-sm);
    }}

    [data-testid="stDataFrame"] > div {{
      border-radius: inherit;
      max-width: 100%;
    }}

    [data-testid="stJson"] {{
      background: rgba(255,252,244,.90);
      border: 1px solid rgba(185,138,104,.78);
      border-radius: .8rem;
      color: #000000;
      max-width: 100%;
      overflow-x: auto;
      padding: .8rem;
    }}

    [data-testid="stCodeBlock"] {{
      border: 1px solid rgba(185,138,104,.82);
      border-radius: .8rem;
      box-shadow: var(--sash-shadow-sm);
      max-width: 100%;
      overflow-x: auto;
    }}

    [data-testid="stAlert"] {{
      border-left-width: 4px;
    }}

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] div {{
      color: #000000;
    }}

    [data-testid="stSuccess"] {{
      border-left-color: var(--sash-success);
    }}

    [data-testid="stWarning"] {{
      border-left-color: var(--sash-warning);
    }}

    [data-testid="stError"] {{
      border-left-color: var(--sash-danger);
    }}

    [data-testid="stInfo"] {{
      border-left-color: var(--sash-info);
    }}

    [data-testid="stDownloadButton"],
    [data-testid="stFormSubmitButton"],
    [data-testid="stButton"] {{
      min-width: 0;
    }}

    [data-testid="stDownloadButton"] button,
    [data-testid="stFormSubmitButton"] button,
    [data-testid="stButton"] button {{
      max-width: 100%;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    [data-testid="stSpinner"] > div {{
      border-top-color: #000000 !important;
    }}

    [data-testid="stExpander"] details > summary {{
      color: #000000;
      padding: .15rem .1rem;
    }}

    [data-testid="stExpander"] [data-testid="stMarkdownContainer"],
    [data-testid="stExpander"] [data-testid="stJson"] {{
      max-width: 100%;
    }}

    .sash-card [style*="word-break"],
    .sash-card code,
    .sash-card pre {{
      overflow-wrap: anywhere;
      word-break: break-word;
    }}

    @media (max-width: 760px) {{
      [data-testid="stForm"] {{
        padding: 1rem;
      }}

      [data-testid="stDataFrame"] {{
        border-radius: .8rem;
      }}

      [data-testid="stMetric"] {{
        min-height: auto;
      }}

      [data-testid="stExpander"] {{
        margin-bottom: .8rem;
      }}
    }}


    /* Final operational page polish */
    .sash-card,
    .metric-card,
    [data-testid="stForm"],
    [data-testid="stMetric"],
    [data-testid="stAlert"],
    [data-testid="stExpander"],
    [data-testid="stDataFrame"],
    [data-testid="stTable"] {{
      border-color: #B98A68;
    }}

    [data-testid="stForm"] {{
      overflow: visible;
    }}

    [data-testid="stForm"] [data-testid="stHorizontalBlock"] {{
      align-items: flex-start;
      gap: clamp(.85rem, 1.75vw, 1.35rem);
    }}

    [data-testid="stTextInput"],
    [data-testid="stTextArea"],
    [data-testid="stNumberInput"],
    [data-testid="stSelectbox"],
    [data-testid="stMultiselect"],
    [data-testid="stDateInput"],
    [data-testid="stTimeInput"] {{
      min-width: 0;
    }}

    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stNumberInput"] input {{
      background: rgba(255,252,244,.96);
      border: 1px solid rgba(185,138,104,.86);
      box-sizing: border-box;
      color: #000000;
    }}

    [data-testid="stTextInput"] input:hover,
    [data-testid="stTextArea"] textarea:hover,
    [data-testid="stNumberInput"] input:hover {{
      border-color: #000000;
    }}

    [data-testid="stTextInput"] input:disabled,
    [data-testid="stTextArea"] textarea:disabled,
    [data-testid="stNumberInput"] input:disabled {{
      background: rgba(243,223,192,.84);
      color: rgba(0,0,0,.58);
      cursor: not-allowed;
    }}

    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMultiselect"] [data-baseweb="select"] > div {{
      background: rgba(255,252,244,.96) !important;
      border-color: rgba(185,138,104,.86) !important;
      color: #000000 !important;
    }}

    [data-testid="stSelectbox"] [data-baseweb="select"]:focus-within > div,
    [data-testid="stMultiselect"] [data-baseweb="select"]:focus-within > div {{
      border-color: #000000 !important;
      box-shadow: 0 0 0 3px rgba(254,189,60,.65) !important;
    }}

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {{
      background: rgba(255,252,244,.92);
      border-radius: 1rem;
      max-width: 100%;
      overflow: auto;
    }}

    [data-testid="stDataFrame"] > div,
    [data-testid="stTable"] > div {{
      max-width: 100%;
      overflow: auto;
    }}

    [data-testid="stJson"] {{
      background: rgba(255,252,244,.94);
      border: 1px solid rgba(185,138,104,.78);
      border-radius: .8rem;
      color: #000000;
      max-width: 100%;
      overflow-x: auto;
      padding: .8rem;
    }}

    [data-testid="stCodeBlock"],
    [data-testid="stMarkdownContainer"] pre {{
      border: 1px solid rgba(185,138,104,.82);
      border-radius: .8rem;
      max-width: 100%;
      overflow-x: auto;
    }}

    [data-testid="stAlert"] {{
      border-left-width: 4px;
      overflow-wrap: anywhere;
    }}

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] div {{
      color: #000000;
    }}

    [data-testid="stSuccess"] {{ border-left-color: #1E7A46; }}
    [data-testid="stWarning"] {{ border-left-color: #8A5A00; }}
    [data-testid="stError"] {{ border-left-color: #B42318; }}
    [data-testid="stInfo"] {{ border-left-color: #1F4F8F; }}

    [data-testid="stDownloadButton"],
    [data-testid="stFormSubmitButton"],
    [data-testid="stButton"] {{
      min-width: 0;
    }}

    [data-testid="stDownloadButton"] button,
    [data-testid="stFormSubmitButton"] button,
    [data-testid="stButton"] button {{
      max-width: 100%;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    [data-testid="stButton"] button:disabled,
    [data-testid="stDownloadButton"] button:disabled,
    [data-testid="stFormSubmitButton"] button:disabled {{
      background: rgba(75,53,41,.28) !important;
      border-color: rgba(75,53,41,.34) !important;
      box-shadow: none !important;
      color: rgba(0,0,0,.62) !important;
      cursor: not-allowed;
      opacity: 1;
    }}

    [data-testid="stExpander"] details > summary {{
      color: #000000;
      font-weight: 720;
      padding: .18rem .12rem;
    }}

    [data-testid="stExpander"] [data-testid="stMarkdownContainer"],
    [data-testid="stExpander"] [data-testid="stJson"] {{
      max-width: 100%;
      overflow-wrap: anywhere;
    }}

    [data-testid="stMarkdownContainer"] code,
    [data-testid="stMarkdownContainer"] pre,
    .sash-card code,
    .sash-card pre {{
      overflow-wrap: anywhere;
      word-break: break-word;
    }}

    [data-testid="stMarkdownContainer"] > div[style*="border-left: 3px solid"],
    [data-testid="stMarkdownContainer"] > div[style*="border-left: 4px solid"] {{
      margin-bottom: .75rem !important;
      margin-top: .4rem !important;
      padding: 1rem 1.1rem !important;
    }}

    [data-testid="stHorizontalBlock"] [data-testid="stMetric"],
    [data-testid="stHorizontalBlock"] .sash-card {{
      min-width: 0;
    }}

    @media (max-width: 760px) {{
      [data-testid="stForm"] {{
        padding: 1rem;
      }}

      [data-testid="stDataFrame"],
      [data-testid="stTable"] {{
        border-radius: .8rem;
      }}

      [data-testid="stMetric"] {{
        min-height: auto;
      }}

      [data-testid="stExpander"] {{
        margin-bottom: .8rem;
      }}

      [data-testid="stMarkdownContainer"] pre,
      [data-testid="stJson"] {{
        font-size: .82rem;
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
