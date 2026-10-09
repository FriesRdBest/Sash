"""Admin / Settings page — premium, no emojis."""

import streamlit as st
from src.styles import page_config, local_css

page_config(title="Admin", layout="wide")
local_css()

st.sidebar.title("Navigation")
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/01_Run_Workflow.py", label="Run Workflow")
st.sidebar.page_link("pages/02_Timeline.py", label="Timeline")
st.sidebar.page_link("pages/03_Scorecard.py", label="Scorecard")
st.sidebar.page_link("pages/04_Admin.py", label="Admin")

st.markdown("<h1>Admin</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
    <p>System controls and data management. Use caution with destructive actions.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h3>Seed data</h3>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
    <p>Load reproducible demo data into the database. This resets existing data.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("Load seed data"):
    from src.persistence.seed_data import load_seed_data

    result = load_seed_data()
    st.success("Seed data loaded")
    st.json(result)

st.markdown("<h3>Danger zone</h3>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="card" style="border-color:#c62828;">
    <p><b>Reset database</b> — Clears all tables and reinitializes schema. This action is irreversible.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("Reset database", type="primary"):
    from src.persistence.sqlite_repo import reset_database

    reset_database()
    st.success("Database reset complete")
