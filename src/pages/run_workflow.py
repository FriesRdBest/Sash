"""Streamlit page: Run Workflow (Aurora happy path demo)."""

import streamlit as st

from src.e2e.aurora_happy_path import create_aurora_session, get_audit_timeline, get_session_details
from src.styles import COLOR_BORDER, COLOR_PRIMARY, COLOR_WARNING, get_custom_css
from src.workflow.designer import create_sample_workflow

st.set_page_config(page_title="Run Workflow · Sash", page_icon="▶️", layout="wide")
st.markdown(get_custom_css(), unsafe_allow_html=True)

st.title("▶️ Run Workflow")
st.markdown("End-to-end Aurora Marketplace verification (mock mode)")

st.sidebar.title("Sash")
st.sidebar.markdown("Production readiness accelerator")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Domain Models", "Qualification", "Engagements", "Workflows", "Run Workflow"],
    index=5,
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Version:** v0.8.0")
st.sidebar.markdown("**Phase:** 8 - End-to-end happy path")

# Form
st.markdown("## Start a verification session")

with st.form(key="run_workflow_form"):
    phone = st.text_input("Customer phone number", value="+12065550123")
    email = st.text_input("Customer email (optional)", value="")
    external_id = st.text_input("External ID (optional)", value="")
    mode = st.selectbox("Provider mode", ["mock", "real"], index=0)
    submitted = st.form_submit_button("Run verification workflow")

if submitted:
    if not phone or len(phone) < 10:
        st.error("Phone number must be at least 10 digits.")
    else:
        workflow = create_sample_workflow()
        with st.spinner("Running Aurora verification..."):
            session = create_aurora_session(
                phone_number=phone,
                workflow=workflow,
                email=email or None,
                external_id=external_id or None,
                mode=mode,
            )

        st.success(f"Session completed: **{session.status}** (correlation ID: `{session.correlation_id}`)")

        # Customer & workflow summary
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""
                <div style="background-color: {COLOR_PRIMARY}10; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid {COLOR_PRIMARY};">
                    <strong>Customer</strong><br>
                    ID: <code>{session.customer.id[:8]}...</code><br>
                    Phone: <code>{session.customer.phone_number}</code><br>
                    Email: <code>{session.customer.email or "(none)"}</code>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f"""
                <div style="background-color: {COLOR_PRIMARY}10; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid {COLOR_PRIMARY};">
                    <strong>Workflow</strong><br>
                    Name: <code>{session.workflow.name}</code><br>
                    Steps: <code>{len(session.workflow.steps)}</code><br>
                    Mode: <code>{mode}</code>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Events & latencies
        st.markdown("### Events & latencies")
        events_data = []
        for i, event in enumerate(session.execution_result.events):
            events_data.append(
                {
                    "#": i + 1,
                    "Channel": event.channel,
                    "Status": event.status.value,
                    "Latency (ms)": round(event.metadata.get("latency_ms", 0.0), 2),
                    "Message ID": event.metadata.get("message_id", "(none)"),
                    "Failure reason": event.metadata.get("failure_reason", ""),
                }
            )
        st.table(events_data)

        # Audit timeline
        st.markdown("### Audit timeline")
        timeline = get_audit_timeline(session.correlation_id)
        if timeline:
            for entry in timeline:
                st.markdown(
                    f"""
                    <div style="background-color: {COLOR_BORDER}20; padding: 0.75rem; border-radius: 0.5rem; margin-bottom: 0.5rem;">
                        <strong>{entry["timestamp"]}</strong> — {entry["summary"]}<br>
                        <small>Actor: {entry["actor"]} | Entity: {entry["entity_type"]} ({entry["entity_id"][:8]}...)</small>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("No audit entries found for this correlation ID.")

        # Session details (debug)
        with st.expander("View raw session details (JSON)"):
            details = get_session_details(session.correlation_id)
            st.json(details)

# Footer
st.markdown("---")
st.markdown(
    f"""
    <div style="text-align: center; color: {COLOR_WARNING};">
        <strong>Demo mode:</strong> This uses the mock provider. No real messages are sent.
    </div>
    """,
    unsafe_allow_html=True,
)
