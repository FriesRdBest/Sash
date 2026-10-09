"""Sash: Production readiness and deployment accelerator for programmable customer communications."""

import streamlit as st

from src.persistence.seed_data import load_seed_data
from src.persistence.sqlite_repo import engagement_repo
from src.workflow.designer import create_sample_workflow
from src.e2e.aurora_happy_path import create_aurora_session, get_audit_timeline
from src.timeline.queries import (
    build_timeline,
    compute_metrics,
    get_state_transitions,
    search_events,
)
from src.qualification.assess import assess_engagement
from src.styles import (
    COLOR_BORDER,
    COLOR_ERROR,
    COLOR_PRIMARY,
    COLOR_SUCCESS,
    COLOR_SURFACE,
    COLOR_TEXT_MUTED,
    COLOR_WARNING,
    get_custom_css,
)

# Page configuration
st.set_page_config(
    page_title="Sash", page_icon="🔗", layout="wide", initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Sash")
st.sidebar.markdown("Production readiness accelerator")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Domain Models",
        "Qualification",
        "Engagements",
        "Workflows",
        "Run Workflow",
        "Event Timeline",
    ],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Version:** v0.10.0")
st.sidebar.markdown("**Phase:** 10 - Timeline & Audit")

# Main content
if page == "Home":
    st.title("Sash")
    st.subheader(
        "Production readiness and deployment accelerator for programmable customer communications"
    )

    # Status banner
    status_col1, status_col2 = st.columns([3, 1])
    with status_col1:
        st.markdown(
            f"""
            <div style="background-color: {COLOR_PRIMARY}10; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid {COLOR_PRIMARY};">
                <strong>🚧 Under Active Development</strong><br>
                Phase 10: workflow design, mock execution, webhooks, and event/audit timelines available.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with status_col2:
        st.markdown(
            """
            <div style="text-align: right;">
                <span class="status-badge status-info">v0.10.0</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Main content sections
    st.markdown("## 🎯 Purpose")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            Sash demonstrates how an engineer can:
            
            - **Qualify** customer engagements
            - **Design** API-driven architectures
            - **Build** resilient communication workflows
            - **Test** failure modes
            - **Instrument** operations
            - **Produce** customer handoff packages
            
            Built for the **Senior Forward Deployed Engineer** role at Sinch.
            """
        )

    with col2:
        st.markdown(
            """
            ### Flagship Scenario
            
            **Aurora Marketplace** user verification:
            
            1. SMS primary channel
            2. WhatsApp or email fallback
            3. Delivery-status webhooks
            4. Internal customer database
            5. Operations dashboard
            6. Fraud and abuse controls
            7. Supportable production deployment
            """
        )

    st.markdown("---")

    # Feature roadmap
    st.markdown("## 📋 Feature Roadmap")

    roadmap_col1, roadmap_col2, roadmap_col3 = st.columns(3)

    with roadmap_col1:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">✅ Phase 0-10 Complete</h4>
                <ul style="margin-bottom: 0; padding-left: 1.25rem;">
                    <li>Operating charter</li>
                    <li>Repository foundation</li>
                    <li>Research and domain model</li>
                    <li>Architecture and ADRs</li>
                    <li>Design system</li>
                    <li><strong>Domain & persistence core</strong></li>
                    <li><strong>Engagement qualification</strong></li>
                    <li><strong>Workflow designer</strong></li>
                    <li><strong>Mock provider integration</strong></li>
                    <li><strong>Aurora end-to-end happy path</strong></li>
                    <li><strong>Webhook event engine</strong></li>
                    <li><strong>Event timeline & audit view</strong></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with roadmap_col2:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_WARNING}; margin-top: 0;">🚧 Current Capabilities</h4>
                <ul style="margin-bottom: 0; padding-left: 1.25rem;">
                    <li>Retry and fallback policies</li>
                    <li>Duplicate webhook detection</li>
                    <li>Dead-letter inspection and replay primitives</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with roadmap_col3:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_TEXT_MUTED}; margin-top: 0;">⏳ Planned</h4>
                <ul style="margin-bottom: 0; padding-left: 1.25rem;">
                    <li>Failure and resilience lab</li>
                    <li>Production-readiness scorecard</li>
                    <li>Observability console</li>
                    <li>Handoff package generator</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Quick links
    st.markdown("## 🔗 Quick Links")

    link_col1, link_col2, link_col3, link_col4 = st.columns(4)

    with link_col1:
        st.markdown(
            f"""
            <div style="text-align: center; padding: 1.5rem; background-color: {COLOR_SURFACE}; border-radius: 0.5rem; border: 1px solid {COLOR_BORDER};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📖</div>
                <strong>README</strong><br>
                <a href="https://github.com/FriesRdBest/Sash/blob/main/README.md" target="_blank" style="color: {COLOR_PRIMARY};">View on GitHub</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with link_col2:
        st.markdown(
            f"""
            <div style="text-align: center; padding: 1.5rem; background-color: {COLOR_SURFACE}; border-radius: 0.5rem; border: 1px solid {COLOR_BORDER};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📋</div>
                <strong>Changelog</strong><br>
                <a href="https://github.com/FriesRdBest/Sash/blob/main/CHANGELOG.md" target="_blank" style="color: {COLOR_PRIMARY};">View on GitHub</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with link_col3:
        st.markdown(
            f"""
            <div style="text-align: center; padding: 1.5rem; background-color: {COLOR_SURFACE}; border-radius: 0.5rem; border: 1px solid {COLOR_BORDER};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏗️</div>
                <strong>Architecture</strong><br>
                <a href="https://github.com/FriesRdBest/Sash/tree/main/docs/architecture" target="_blank" style="color: {COLOR_PRIMARY};">View docs</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with link_col4:
        st.markdown(
            f"""
            <div style="text-align: center; padding: 1.5rem; background-color: {COLOR_SURFACE}; border-radius: 0.5rem; border: 1px solid {COLOR_BORDER};">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔬</div>
                <strong>Research</strong><br>
                <a href="https://github.com/FriesRdBest/Sash/tree/main/docs/research" target="_blank" style="color: {COLOR_PRIMARY};">View docs</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Next steps
    st.markdown("## ▶️ Next Steps")

    st.markdown(
        f"""
        <div class="sash-card">
            <p><strong>Available now:</strong></p>
            <ol>
                <li>Workflow designer with JSON export</li>
                <li>Mock Sinch provider execution</li>
                <li>Event timeline and correlation audit view</li>
            </ol>
            <p style="margin-top: 1rem; color: {COLOR_TEXT_MUTED};">
                This application will grow rapidly. Check back frequently to see new features being added.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Domain Models":
    st.title("Domain Models")
    st.markdown("Core entities and value objects in the Sash domain.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">👤 Customer</h4>
                <p>End-user entity in a workflow with contact information.</p>
                <ul>
                    <li><code>phone_number</code> (required)</li>
                    <li><code>email</code> (optional)</li>
                    <li><code>external_id</code> (optional)</li>
                    <li><code>metadata</code> (dict)</li>
                    <li><code>correlation_id</code> (tracking)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">🔀 Workflow</h4>
                <p>Definition of communication steps and logic.</p>
                <ul>
                    <li><code>name</code>, <code>description</code></li>
                    <li><code>steps</code> (list)</li>
                    <li><code>status</code>: draft/active/paused/completed/failed</li>
                    <li><code>correlation_id</code> (tracking)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">▶️ WorkflowExecution</h4>
                <p>Runtime execution of a workflow for a customer.</p>
                <ul>
                    <li><code>workflow_id</code>, <code>customer_id</code></li>
                    <li><code>status</code></li>
                    <li><code>current_step</code></li>
                    <li><code>correlation_id</code> (tracking)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">📬 Event</h4>
                <p>Single communication event (message sent/delivered).</p>
                <ul>
                    <li><code>execution_id</code>, <code>step_index</code></li>
                    <li><code>channel</code>: SMS/WhatsApp/Email/Voice</li>
                    <li><code>status</code>: pending/sent/delivered/failed/bounced</li>
                    <li><code>correlation_id</code> (tracking)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.markdown(
        """
        ### Persistence
        
        All entities are stored in SQLite with full audit trail.
        Data survives application restarts. Correlation IDs enable end-to-end tracing.
        """
    )

elif page == "Qualification":
    st.title("Engagement Qualification")
    st.markdown("Assess customer engagements for technical and operational viability.")

    st.markdown("---")

    # Intake form
    st.markdown("### 📝 Intake Form")

    col1, col2 = st.columns(2)

    with col1:
        customer_name = st.text_input("Customer Name", "Acme Corp")
        company = st.text_input("Company", "Acme Corporation")
        use_case = st.text_area(
            "Use Case", "User verification for marketplace platform", height=100
        )

    with col2:
        priority = st.selectbox("Priority", ["low", "medium", "high", "critical"])
        channels = st.multiselect(
            "Channels", ["sms", "whatsapp", "email", "voice"], default=["sms"]
        )
        expected_volume = st.number_input(
            "Expected Monthly Volume", min_value=0, value=5000, step=1000
        )
        timeline_days = st.number_input(
            "Timeline (days)", min_value=1, value=30, step=7
        )

    notes = st.text_area("Additional Notes", "")

    if st.button("Assess Engagement", type="primary"):
        engagement_data = {
            "customer_name": customer_name,
            "company": company,
            "use_case": use_case,
            "priority": priority,
            "channels": channels,
            "expected_volume": expected_volume,
            "timeline_days": timeline_days,
            "notes": notes,
        }

        assessment = assess_engagement(engagement_data)

        st.markdown("---")

        # Score display
        score_col1, score_col2, score_col3 = st.columns(3)

        with score_col1:
            score_color = (
                COLOR_SUCCESS
                if assessment.score >= 80
                else (COLOR_WARNING if assessment.score >= 60 else COLOR_ERROR)
            )
            st.markdown(
                f"""
                <div class="metric-card" style="background: linear-gradient(135deg, {score_color} 0%, #000 100%);">
                    <div class="metric-value">{assessment.score}</div>
                    <div class="metric-label">Readiness Score</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with score_col2:
            decision_emoji = (
                "✅"
                if assessment.decision == "proceed"
                else ("⚠️" if assessment.decision == "proceed_with_conditions" else "❌")
            )
            st.markdown(
                f"""
                <div class="sash-card" style="text-align: center;">
                    <div style="font-size: 2rem;">{decision_emoji}</div>
                    <strong>{assessment.decision.replace("_", " ").title()}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with score_col3:
            risk_count = len(assessment.risk_flags)
            risk_color = (
                COLOR_ERROR
                if risk_count > 2
                else (COLOR_WARNING if risk_count > 0 else COLOR_SUCCESS)
            )
            st.markdown(
                f"""
                <div class="sash-card" style="text-align: center; border-left: 4px solid {risk_color};">
                    <div style="font-size: 2rem;">{risk_count}</div>
                    <strong>Risk Flags</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        # Recommendation
        st.markdown("### 📊 Assessment Details")
        st.info(assessment.get_recommendation())

        # Conditions
        if assessment.conditions:
            st.markdown("**Conditions:**")
            for condition in assessment.conditions:
                st.markdown(f"- {condition}")

        # Rule results
        st.markdown("**Rule Results:**")
        for result in assessment.rule_results:
            icon = "✅" if result.passed else "❌"
            st.markdown(f"{icon} **{result.rule_name}**: {result.message}")

        # Export
        st.markdown("---")
        st.download_button(
            label="📥 Export Report (JSON)",
            data=assessment.to_json(),
            file_name=f"qualification_{customer_name.replace(' ', '_')}.json",
            mime="application/json",
        )

elif page == "Engagements":
    st.title("Engagements")
    st.markdown("Customer engagement tracking and qualification.")

    st.markdown("---")

    # Load seed data button
    if st.button("🔄 Load Seed Data"):
        result = load_seed_data()
        st.success(
            f"Loaded {result['engagements']} engagements, {result['customers']} customers, {result['workflows']} workflows"
        )

    st.markdown("---")

    # List engagements
    st.markdown("### 📋 Existing Engagements")

    engagements = engagement_repo.get_all()

    if not engagements:
        st.markdown(
            "<div class='empty-state'><div class='empty-state-icon'>📭</div><p>No engagements yet. Load seed data or create a new assessment.</p></div>",
            unsafe_allow_html=True,
        )
    else:
        for eng in engagements:
            st.markdown(
                f"""
                <div class="sash-card">
                    <h4 style="margin-top: 0;">{eng.get("customer_name", "Unknown")} @ {eng.get("company", "Unknown")}</h4>
                    <p><strong>Use Case:</strong> {eng.get("use_case", "N/A")}</p>
                    <p><strong>Priority:</strong> {eng.get("priority", "medium")} | <strong>Volume:</strong> {eng.get("expected_volume", 0):,}/mo | <strong>Timeline:</strong> {eng.get("timeline_days", 30)} days</p>
                    <p><strong>Channels:</strong> {", ".join(eng.get("channels", []))}</p>
                    <p><strong>Status:</strong> <span class="status-badge status-info">{eng.get("status", "new")}</span></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif page == "Workflows":
    st.title("Workflows")
    st.markdown("Design, validate, and export a versioned communication workflow.")

    if "workflow_draft" not in st.session_state:
        st.session_state.workflow_draft = create_sample_workflow()

    workflow = st.session_state.workflow_draft

    st.markdown(
        f"""
        <div class="sash-card">
            <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">🔀 Workflow Designer</h4>
            <p><strong>{workflow.name}</strong> — version {workflow.version}</p>
            <p>{workflow.description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Steps")
    for index, step in enumerate(workflow.steps, start=1):
        fallback = step.fallback_to[:8] + "…" if step.fallback_to else "None"
        st.markdown(
            f"""
            <div class="sash-card">
                <strong>Step {index}: {step.name}</strong><br>
                Channel: <code>{step.channel}</code> |
                Timeout: <code>{step.timeout_seconds}s</code> |
                Retries: <code>{step.retry_policy.max_attempts}</code><br>
                Template: <code>{step.template}</code><br>
                Fallback target: <code>{fallback}</code>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.download_button(
        "⬇️ Download workflow JSON",
        data=workflow.to_json(),
        file_name="sash-workflow.json",
        mime="application/json",
    )

    if st.button("↻ Reset to Aurora sample workflow"):
        st.session_state.workflow_draft = create_sample_workflow()
        st.rerun()

elif page == "Run Workflow":
    st.title("▶️ Run Workflow")
    st.markdown("Run the Aurora Marketplace verification journey in deterministic mock mode.")

    with st.form("run_workflow_form"):
        phone = st.text_input("Customer phone number", value="+12065550123")
        email = st.text_input("Customer email (optional)", value="")
        external_id = st.text_input("External ID (optional)", value="")
        run = st.form_submit_button("Run mock verification")

    if run:
        if not phone or len(phone) < 10:
            st.error("Phone number must be at least 10 digits.")
        else:
            workflow = st.session_state.get("workflow_draft", create_sample_workflow())

            with st.spinner("Running Aurora verification..."):
                session = create_aurora_session(
                    phone_number=phone,
                    workflow=workflow,
                    email=email or None,
                    external_id=external_id or None,
                    mode="mock",
                )

            st.session_state["selected_correlation"] = session.correlation_id
            st.success(
                f"Verification {session.status}. "
                f"Correlation ID: {session.correlation_id}"
            )

            event_rows = [
                {
                    "Step": index + 1,
                    "Channel": event.channel,
                    "Status": event.status.value,
                    "Latency (ms)": round(
                        event.metadata.get("latency_ms", 0.0), 2
                    ),
                    "Message ID": event.metadata.get("message_id", "—"),
                    "Failure reason": event.metadata.get(
                        "failure_reason", "—"
                    ),
                }
                for index, event in enumerate(session.execution_result.events)
            ]

            st.markdown("### Events and latency")
            st.dataframe(event_rows, use_container_width=True)

            st.markdown("### Audit trail")
            st.dataframe(
                get_audit_timeline(session.correlation_id),
                use_container_width=True,
            )

            st.info(
                "Open Event Timeline and use this correlation ID for the "
                "full operator view."
            )

elif page == "Event Timeline":
    st.title("📜 Event Timeline & Audit View")
    st.markdown(
        "Search a correlation ID to inspect events, audit records, "
        "state transitions, and derived metrics."
    )

    default_id = st.session_state.get("selected_correlation", "")
    correlation_id = st.text_input(
        "Correlation ID",
        value=default_id,
        placeholder="Run a workflow first, then paste its correlation ID here.",
    )

    if correlation_id:
        metrics = compute_metrics(correlation_id)
        metric_1, metric_2, metric_3, metric_4, metric_5 = st.columns(5)
        metric_1.metric("Total events", metrics["total_events"])
        metric_2.metric("Sent", metrics["sent_events"])
        metric_3.metric("Delivered", metrics["delivered_events"])
        metric_4.metric("Failed", metrics["failed_events"])
        metric_5.metric("Dead letters", metrics["dead_letter_count"])

        st.caption(
            "Values grouped under `simulated` are labelled demo values, "
            "not production telemetry."
        )

        with st.expander("Metrics detail, including simulated values"):
            st.json(metrics)

        st.markdown("### Combined event and audit timeline")
        timeline = build_timeline(correlation_id)

        if timeline:
            for entry in timeline:
                color = {
                    "event": COLOR_PRIMARY,
                    "audit": COLOR_BORDER,
                    "dead_letter": COLOR_ERROR,
                }.get(entry["type"], COLOR_TEXT_MUTED)

                st.markdown(
                    f"""
                    <div style="background-color: {color}10; padding: 0.75rem;
                    border-radius: 0.5rem; border-left: 3px solid {color};
                    margin-bottom: 0.5rem;">
                        <strong>{entry["timestamp"]}</strong> —
                        <code>{entry["type"].upper()}</code>:
                        {entry["summary"]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                with st.expander(f'Details: {entry["summary"]}'):
                    st.json(entry["details"])
        else:
            st.warning(
                "No events, audit records, or dead letters were found for "
                "this correlation ID."
            )

        st.markdown("### State-transition history")
        transitions = get_state_transitions(correlation_id)
        if transitions:
            st.dataframe(transitions, use_container_width=True)
        else:
            st.info("No state transitions were found.")

    st.markdown("### Global event search")
    query = st.text_input(
        "Search stored events",
        placeholder="Execution ID or event content",
    )
    status = st.selectbox(
        "Status filter",
        ["all", "pending", "sent", "delivered", "failed"],
    )

    if st.button("Search events"):
        results = search_events(
            query=query or None,
            status=None if status == "all" else status,
        )
        st.write(f"Found {len(results)} event(s).")
        st.dataframe(results, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    f"""
    <div style="text-align: center; color: {COLOR_TEXT_MUTED}; font-size: 0.875rem; padding: 1rem;">
        <strong>Sash</strong> — Production readiness and deployment accelerator<br>
        Built for the Senior Forward Deployed Engineer role at Sinch<br>
        <a href="https://github.com/FriesRdBest/Sash" style="color: {COLOR_PRIMARY};">View source on GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)
