"""Timeline page — premium, no emojis."""

import streamlit as st

st.set_page_config(page_title="Timeline", layout="wide")

st.markdown(
    """
    <style>
    .page-title { font-size: 1.6rem; font-weight: 700; margin-bottom: 0.5rem; }
    .card { border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; margin: 0.75rem 0; background: #fafafa; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="page-title">Timeline</p>', unsafe_allow_html=True)

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
