# Phase 2 shared visual system for Sash.
# Keep semantic roles here so UI colors, spacing, and type stay consistent.

COLOR_PRIMARY = "#FFE97A"
COLOR_ACCENT = "#B98A68"
COLOR_INK = "#000000"
COLOR_TEXT = "#171717"
COLOR_TEXT_MUTED = "#5F5A52"
COLOR_SURFACE = "#FFFFFF"
COLOR_PAGE = "#FAF9F6"
COLOR_BORDER = "#E7E2D9"
COLOR_SUCCESS = "#26734D"
COLOR_WARNING = "#8A5A00"
COLOR_ERROR = "#B42318"

FONT_DISPLAY = "Raleway"
FONT_BODY = "Arial, Helvetica, sans-serif"

SPACING_XS = "0.5rem"
SPACING_SM = "0.75rem"
SPACING_MD = "1rem"
SPACING_LG = "1.5rem"
SPACING_XL = "2rem"
CONTENT_MAX_WIDTH = "1440px"


def get_custom_css() -> str:
    """Return the shared, responsive Sash presentation layer."""
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700;800&display=swap');

    :root {{
      --sash-yellow: {COLOR_PRIMARY};
      --sash-tan: {COLOR_ACCENT};
      --sash-ink: {COLOR_INK};
      --sash-text: {COLOR_TEXT};
      --sash-muted: {COLOR_TEXT_MUTED};
      --sash-page: {COLOR_PAGE};
      --sash-surface: {COLOR_SURFACE};
      --sash-border: {COLOR_BORDER};
      --sash-success: {COLOR_SUCCESS};
      --sash-warning: {COLOR_WARNING};
      --sash-error: {COLOR_ERROR};
      --sash-space-xs: {SPACING_XS};
      --sash-space-sm: {SPACING_SM};
      --sash-space-md: {SPACING_MD};
      --sash-space-lg: {SPACING_LG};
      --sash-space-xl: {SPACING_XL};
      --sash-content-max: {CONTENT_MAX_WIDTH};
    }}

    html, body, [data-testid="stAppViewContainer"] {{
      background: var(--sash-page);
      color: var(--sash-text);
      font-family: {FONT_BODY};
    }}

    [data-testid="stAppViewContainer"] {{
      font-size: 1rem;
      line-height: 1.55;
    }}

    [data-testid="stHeader"] {{
      background: rgba(250, 249, 246, 0.94);
    }}

    [data-testid="stMainBlockContainer"] {{
      width: 100%;
      max-width: var(--sash-content-max);
      padding: clamp(1rem, 2.5vw, 2.5rem) clamp(1rem, 3.5vw, 3rem) 3rem;
    }}

    h1, h2, h3, h4, h5, h6,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
      color: var(--sash-ink);
      font-family: {FONT_DISPLAY}, {FONT_BODY};
      font-weight: 700;
      letter-spacing: -0.025em;
      line-height: 1.2;
    }}

    h1 {{ font-size: clamp(1.8rem, 3vw, 2.5rem); }}
    h2 {{ font-size: clamp(1.45rem, 2.2vw, 1.85rem); }}
    h3 {{ font-size: clamp(1.2rem, 1.7vw, 1.45rem); }}

    p, li, label, [data-testid="stCaptionContainer"] {{
      color: var(--sash-text);
      line-height: 1.6;
    }}
    [data-testid="stCaptionContainer"] {{ color: var(--sash-muted); }}

    a {{ color: #5B3B20; text-underline-offset: 0.16em; }}
    a:hover {{ color: var(--sash-ink); }}
    :focus-visible {{ outline: 3px solid #6B4B00; outline-offset: 2px; }}

    [data-testid="stSidebar"] {{
      background: var(--sash-surface);
      border-right: 1px solid var(--sash-border);
    }}
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
      font-family: {FONT_DISPLAY}, {FONT_BODY};
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label {{
      border-radius: 0.6rem;
      padding: 0.35rem 0.5rem;
      min-height: 2.75rem;
      align-items: center;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label:hover {{
      background: #FFF8D7;
    }}

    [data-testid="stVerticalBlockBorderWrapper"], .sash-card, .metric-card {{
      border: 1px solid var(--sash-border);
      border-radius: 0.85rem;
      background: var(--sash-surface);
      box-shadow: 0 2px 10px rgba(25, 20, 10, 0.045);
    }}
    .sash-card {{
      padding: clamp(1rem, 2vw, 1.5rem);
      margin: 0.5rem 0 1rem;
      overflow-wrap: anywhere;
    }}
    .metric-card {{
      padding: 1.25rem;
      text-align: center;
      color: var(--sash-ink);
    }}
    .metric-value {{ font-size: clamp(1.75rem, 4vw, 2.5rem); font-weight: 700; }}
    .metric-label {{ font-size: 0.9rem; color: var(--sash-muted); }}
    .status-badge {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 0.25rem 0.7rem;
      font-size: 0.8rem;
      font-weight: 600;
    }}
    .status-info {{ background: #FFF4C2; color: #352900; }}
    .empty-state {{
      border: 1px dashed var(--sash-border);
      border-radius: 0.85rem;
      padding: 2rem 1rem;
      text-align: center;
      background: var(--sash-surface);
    }}

    [data-testid="stDataFrame"], [data-testid="stTable"] {{
      max-width: 100%;
    }}
    [data-testid="stDataFrame"] {{ overflow-x: auto; }}
    [data-testid="stButton"] button,
    [data-testid="stDownloadButton"] button {{
      min-height: 2.75rem;
      border-radius: 0.6rem;
      font-weight: 600;
    }}
    [data-testid="stButton"] button[kind="primary"],
    [data-testid="stFormSubmitButton"] button[kind="primary"] {{
      background: var(--sash-yellow);
      color: var(--sash-ink);
      border: 1px solid #8A6A00;
    }}
    [data-testid="stButton"] button[kind="primary"]:hover,
    [data-testid="stFormSubmitButton"] button[kind="primary"]:hover {{
      background: #F5D94F;
      color: var(--sash-ink);
      border-color: var(--sash-ink);
    }}

    @media (max-width: 900px) {{
      [data-testid="stMainBlockContainer"] {{
        padding: 1.25rem clamp(1rem, 3vw, 1.75rem) 2rem;
      }}
      .sash-card {{ padding: 1rem; }}
    }}

    @media (max-width: 640px) {{
      [data-testid="stMainBlockContainer"] {{
        padding: 1rem 0.9rem 1.5rem;
      }}
      [data-testid="stHorizontalBlock"] {{
        flex-wrap: wrap;
        gap: 0.75rem;
      }}
      [data-testid="stHorizontalBlock"] > [data-testid="column"] {{
        min-width: min(100%, 18rem);
        flex: 1 1 100%;
      }}
      [data-testid="stMetric"] {{ min-width: 0; overflow-wrap: anywhere; }}
      [data-testid="stDataFrame"] {{ font-size: 0.85rem; }}
      .sash-card {{ margin: 0.35rem 0 0.75rem; }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{ scroll-behavior: auto !important; animation-duration: 0.01ms !important; }}
    }}
    </style>
    """
