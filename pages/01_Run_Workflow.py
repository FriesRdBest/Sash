"""Run Workflow page — premium, no emojis."""

import streamlit as st
from src.workflow.designer import create_sample_workflow

st.set_page_config(page_title="Run Workflow", layout="wide")

st.markdown(
    """
    <style>
    .page-title { font-size: 1.6rem; font-weight: 700; margin-bottom: 0.5rem; }
    .card { border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; margin: 0.75rem 0; background: #fafafa; }
    .status-ok { color: #1e7e34; font-weight: 600; }
    .status-warn { color: #b45f06; font-weight: 600; }
    .status-error { color: #c62828; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="page-title">Run Workflow</p>', unsafe_allow_html=True)

with st.form("run_workflow_form", clear_on_submit=False):
    to_number = st.text_input("Phone number", value="+12065550123")
    correlation_id = st.text_input("Correlation ID (optional)", value="")
    submitted = st.form_submit_button("Run workflow")

if submitted:
    workflow = create_sample_workflow()
    # Stub execution result for demo
    result = {
        "correlation_id": correlation_id or "corr_demo_001",
        "final_status": "delivered",
        "event_count": 3,
    }
    st.success("Workflow executed")
    st.markdown(
        f"""
        <div class="card">
        <p><b>Correlation ID:</b> {result["correlation_id"]}</p>
        <p><b>Final status:</b> <span class="status-ok">{result["final_status"]}</span></p>
        <p><b>Event count:</b> {result["event_count"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
