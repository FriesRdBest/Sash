"""Timeline page — premium, no emojis."""

import streamlit as st
from src.styles import page_config, local_css

page_config(title="Timeline", layout="wide")
local_css()

st.sidebar.title("Navigation")
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/01_Run_Workflow.py", label="Run Workflow")
st.sidebar.page_link("pages/02_Timeline.py", label="Timeline")
st.sidebar.page_link("pages/03_Scorecard.py", label="Scorecard")
st.sidebar.page_link("pages/04_Admin.py", label="Admin")

st.markdown("<h1>Timeline</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
    <p>View normalized events for a correlation ID. This demo shows a static sample.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

sample_events = [
    {"ts": "2026-10-09T07:00:00Z", "type": "message.sent", "status": "processed"},
    {"ts": "2026-10-09T07:00:05Z", "type": "message.delivered", "status": "processed"},
    {"ts": "2026-10-09T07:00:10Z", "type": "message.failed", "status": "dead_letter"},
]

st.dataframe(
    sample_events,
    column_config={
        "ts": "Timestamp",
        "type": "Event type",
        "status": "Status",
    },
    use_container_width=True,
)
