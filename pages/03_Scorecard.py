"""Scorecard page — premium, no emojis."""

import streamlit as st
from src.styles import page_config, local_css

page_config(title="Scorecard", layout="wide")
local_css()

# Top navigation tabs
pages = {
    "Home": "app.py",
    "Run Workflow": "pages/01_Run_Workflow.py",
    "Timeline": "pages/02_Timeline.py",
    "Scorecard": "pages/03_Scorecard.py",
    "Admin": "pages/04_Admin.py",
}

tabs = st.tabs(list(pages.keys()))
for i, (label, path) in enumerate(pages.items()):
    with tabs[i]:
        if label == "Scorecard":
            pass  # current page content below
        else:
            st.page_link(path, label=f"Open {label}")

st.markdown("<h1>Scorecard</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
    <p>Qualification outcomes and risk summary for the selected engagement.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div class="metric-card">
        <div class="metric-label">Qualified engagements</div>
        <div class="metric-value">1</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="metric-card">
        <div class="metric-label">Risk flags</div>
        <div class="metric-value">0</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="metric-card">
        <div class="metric-label">Events processed</div>
        <div class="metric-value">3</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
