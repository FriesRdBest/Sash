"""Run Workflow page — premium, no emojis."""

import streamlit as st
from src.styles import page_config, local_css
from src.workflow.designer import create_sample_workflow

page_config(title="Run Workflow", layout="wide")
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
        if label == "Run Workflow":
            pass  # current page content below
        else:
            st.page_link(path, label=f"Open {label}")

st.markdown("<h1>Run Workflow</h1>", unsafe_allow_html=True)

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
