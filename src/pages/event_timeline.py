"""Streamlit page: Event Timeline & Audit View."""

import streamlit as st

from src.styles import COLOR_BORDER, COLOR_PRIMARY, COLOR_TEXT_MUTED, get_custom_css
from src.timeline.queries import build_timeline, compute_metrics, get_state_transitions, search_events

st.set_page_config(page_title="Event Timeline · Sash", page_icon="📜", layout="wide")
st.markdown(get_custom_css(), unsafe_allow_html=True)

st.title("📜 Event Timeline & Audit View")
st.markdown("Operator view: correlation search, event details, state transitions, and metrics")

st.sidebar.title("Sash")
st.sidebar.markdown("Production readiness accelerator")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Domain Models", "Qualification", "Engagements", "Workflows", "Run Workflow", "Event Timeline"],
    index=6,
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Version:** v0.10.0")
st.sidebar.markdown("**Phase:** 10 - Event timeline and audit view")

# Correlation search
st.markdown("## Correlation search")

col1, col2 = st.columns([3, 1])
with col1:
    correlation_id = st.text_input(
        "Correlation ID",
        placeholder="e.g., from Run Workflow page",
    )
with col2:
    search_btn = st.button("Search", type="primary")

if search_btn and correlation_id:
    st.session_state["selected_correlation"] = correlation_id

if "selected_correlation" not in st.session_state:
    st.info("Enter a correlation ID above to view the event timeline.")
    st.stop()

corr_id = st.session_state["selected_correlation"]
st.markdown(f"**Viewing timeline for:** `{corr_id}`")

# Metrics
st.markdown("## Metrics")
metrics = compute_metrics(corr_id)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total events", metrics["total_events"])
m2.metric("Sent", metrics["sent_events"])
m3.metric("Delivered", metrics["delivered_events"])
m4.metric("Failed", metrics["failed_events"])

with st.expander("View all metrics (including simulated)"):
    st.json(metrics)

# Timeline
st.markdown("## Event timeline")
timeline = build_timeline(corr_id)

if not timeline:
    st.warning("No events or audit records found for this correlation ID.")
else:
    for entry in timeline:
        color = {
            "event": COLOR_PRIMARY,
            "audit": COLOR_BORDER,
            "dead_letter": "#dc3545",
        }.get(entry["type"], COLOR_TEXT_MUTED)

        st.markdown(
            f"""
            <div style="background-color: {color}10; padding: 0.75rem; border-radius: 0.5rem; border-left: 3px solid {color}; margin-bottom: 0.5rem;">
                <strong>{entry["timestamp"]}</strong> — <code>{entry["type"].upper()}</code>: {entry["summary"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

# State transitions
st.markdown("## State transitions")
transitions = get_state_transitions(corr_id)
if transitions:
    for t in transitions:
        st.markdown(
            f"""
            <div style="background-color: {COLOR_BORDER}20; padding: 0.75rem; border-radius: 0.5rem; margin-bottom: 0.5rem;">
                <strong>{t["timestamp"]}</strong> — {t["action"]}<br>
                <small>Actor: {t["actor"]}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.info("No state transitions recorded.")

# Event search
st.markdown("## Event search (global)")

q = st.text_input("Search query (optional)", placeholder="text in content or execution ID")
status_filter = st.selectbox("Status filter", ["all", "sent", "delivered", "failed"])
limit = st.slider("Limit", 10, 100, 50)

if st.button("Search events"):
    status = None if status_filter == "all" else status_filter
    results = search_events(query=q or None, status=status, limit=limit)
    st.write(f"Found {len(results)} events")
    if results:
        st.json(results[:5])  # show first 5

# Footer
st.markdown("---")
st.markdown(
    f"""
    <div style="text-align: center; color: {COLOR_TEXT_MUTED};">
        <strong>Note:</strong> Some metrics are simulated for demo purposes and labelled under "simulated".
    </div>
    """,
    unsafe_allow_html=True,
)
