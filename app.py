"""Sash — premium single-page app (no emojis) with top tabs."""

import streamlit as st
from src.styles import page_config, local_css
from src.persistence.seed_data import load_seed_data
from src.persistence.sqlite_repo import reset_database
from src.workflow.designer import create_sample_workflow

page_config(title="Sash", layout="wide")
local_css()

st.markdown('<h1>Sash — Event-driven Messaging Workflow Engine</h1>', unsafe_allow_html=True)
st.markdown(
    """<p style="font-size:1.1rem; color:#555; margin-bottom:1.5rem;">
    A polished demo of reliable, observable messaging workflows (Sinch/Twilio-style)
    with idempotency, dead-lettering, scorecards, and resilience testing.
    </p>""",
    unsafe_allow_html=True,
)

# Top navigation tabs
home_tab, run_tab, timeline_tab, scorecard_tab, admin_tab = st.tabs(
    ["Home", "Run Workflow", "Timeline", "Scorecard", "Admin"]
)

with home_tab:
    st.markdown(
        """
        <div class="card">
        <h3>What this is</h3>
        <p>A reference implementation showing how to build a robust messaging workflow engine:
        ingest provider events, normalize them, enforce idempotency and ordering, apply qualification/scorecard rules,
        and expose an observable timeline for each correlation ID. Designed for demos, interviews, and architecture discussions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
        <h3>How to use it</h3>
        <ol>
        <li><b>Seed data</b> — Load reproducible demo customers, workflows, and engagements (Admin tab).</li>
        <li><b>Run a workflow</b> — Execute a sample workflow for a phone number and correlation ID.</li>
        <li><b>Inspect timeline</b> — View normalized events, statuses, and sequencing for that correlation ID.</li>
        <li><b>Review scorecard</b> — See qualification outcomes, risk flags, and observability summaries.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
        <h3>What it's not for</h3>
        <ul>
        <li>Not a production messaging gateway or provider integration.</li>
        <li>Not a multi-tenant SaaS; no auth, rate limits, or billing.</li>
        <li>Not a full monitoring stack; observability is demo-grade, not enterprise.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
        <h3>Links</h3>
        <p>
        <a href="https://FriesRdBest.github.io/Sash/" target="_blank">Documentation site</a>
        &nbsp;
        <a href="https://github.com/FriesRdBest/Sash" target="_blank">GitHub repository</a>
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with run_tab:
    st.markdown("<h2>Run Workflow</h2>", unsafe_allow_html=True)

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

with timeline_tab:
    st.markdown("<h2>Timeline</h2>", unsafe_allow_html=True)

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

with scorecard_tab:
    st.markdown("<h2>Scorecard</h2>", unsafe_allow_html=True)

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

with admin_tab:
    st.markdown("<h2>Admin</h2>", unsafe_allow_html=True)

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
        reset_database()
        st.success("Database reset complete")
