"""Scorecard page — premium, no emojis."""

import streamlit as st

st.set_page_config(page_title="Scorecard", layout="wide")

st.markdown(
    """
    <style>
    .page-title { font-size: 1.6rem; font-weight: 700; margin-bottom: 0.5rem; }
    .metric-card { border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; margin: 0.5rem 0; background: #fafafa; }
    .metric-label { font-size: 0.85rem; color: #555; }
    .metric-value { font-size: 1.4rem; font-weight: 700; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="page-title">Scorecard</p>', unsafe_allow_html=True)

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
