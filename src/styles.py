"""Global design tokens and Streamlit styling helpers."""

import streamlit as st

# Design tokens (used in CSS and UI)
COLOR_PRIMARY = "#0b57d0"
COLOR_SUCCESS = "#1e7e34"
COLOR_WARNING = "#b45f06"
COLOR_ERROR = "#c62828"
COLOR_BG_CARD = "#fafafa"
COLOR_BORDER = "#e0e0e0"
COLOR_TEXT_MUTED = "#555555"

FONT_STACK = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'


def page_config(title: str = "Sash", layout: str = "wide"):
    """Configure Streamlit page with premium defaults."""
    st.set_page_config(page_title=title, page_icon="🔷", layout=layout)


def local_css():
    """Inject premium CSS for consistent styling across the app."""
    st.markdown(
        f"""
        <style>
        /* Base */
        html, body, [class*="css"] {{
            font-family: {FONT_STACK};
            color: #222;
        }}
        h1, h2, h3, h4, h5, h6 {{
            font-weight: 700;
            letter-spacing: -0.01em;
        }}
        h1 {{ font-size: 2rem; }}
        h2 {{ font-size: 1.6rem; }}
        h3 {{ font-size: 1.2rem; }}
        p {{ line-height: 1.6; }}

        /* Cards */
        .card {{
            border: 1px solid {COLOR_BORDER};
            border-radius: 8px;
            padding: 1rem;
            margin: 0.75rem 0;
            background: {COLOR_BG_CARD};
        }}
        .card h3 {{ margin-top: 0; font-size: 1.05rem; }}

        /* Buttons */
        .stButton > button {{
            background: {COLOR_PRIMARY};
            color: #fff;
            border: none;
            border-radius: 6px;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }}
        .stButton > button:hover {{
            opacity: 0.92;
        }}

        /* Status text helpers */
        .status-ok {{ color: {COLOR_SUCCESS}; font-weight: 600; }}
        .status-warn {{ color: {COLOR_WARNING}; font-weight: 600; }}
        .status-error {{ color: {COLOR_ERROR}; font-weight: 600; }}

        /* Tables */
        .dataframe {{
            font-size: 0.9rem;
            border-collapse: collapse;
        }}
        .dataframe th {{
            background: #f3f3f3;
            font-weight: 600;
            text-align: left;
            padding: 0.4rem 0.6rem;
        }}
        .dataframe td {{
            padding: 0.35rem 0.6rem;
            border-top: 1px solid #eee;
        }}

        /* Metrics */
        .metric-card {{
            border: 1px solid {COLOR_BORDER};
            border-radius: 8px;
            padding: 0.75rem;
            background: #fff;
        }}
        .metric-label {{ font-size: 0.8rem; color: {COLOR_TEXT_MUTED}; }}
        .metric-value {{ font-size: 1.4rem; font-weight: 700; color: #111; }}

        /* Links */
        a {{ color: {COLOR_PRIMARY}; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}

        /* Reduce top margin on first element in main */
        .main > div:first-child {{
            margin-top: 0.5rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
