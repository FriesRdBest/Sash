"""Sash: Production readiness and deployment accelerator for programmable customer communications."""


from datetime import datetime

import streamlit as st

from src.e2e.aurora_happy_path import create_aurora_session, get_audit_timeline
from src.persistence.seed_data import load_seed_data
from src.persistence.sqlite_repo import engagement_repo
from src.qualification.assess import assess_engagement
from src.resilience.scenarios import FailureScenario, get_scenario_definition
from src.resilience.simulator import FailureSimulator
from src.scorecard.engine import ScorecardEngine
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
from src.timeline.queries import (
    build_timeline,
    compute_metrics,
    get_state_transitions,
    search_events,
)
from src.workflow.designer import create_sample_workflow

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
        "Failure Lab",
        "Scorecard",
    ],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Version:** v0.12.0")
st.sidebar.markdown("**Phase:** 12 - Production Readiness Scorecard")

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

elif page == "Failure Lab":
    st.title("🧪 Failure & Resilience Laboratory")
    st.markdown(
        "Run deterministic failure simulations against the mock integration "
        "boundaries. Every result documents detection, behavior, impact, "
        "alerting, recovery, and residual risk."
    )

    scenario_labels = {
        FailureScenario.PROVIDER_TIMEOUT: "Provider timeout",
        FailureScenario.RATE_LIMIT: "Provider rate limit",
        FailureScenario.WEBHOOK_OUTAGE: "Webhook receiver outage",
        FailureScenario.DUPLICATE_CALLBACK: "Duplicate callback",
        FailureScenario.OUT_OF_ORDER_EVENT: "Out-of-order event",
        FailureScenario.CRM_FAILURE: "CRM adapter failure",
        FailureScenario.DATABASE_FAILURE: "Database persistence failure",
        FailureScenario.QUEUE_BACKLOG: "Queue backlog",
        FailureScenario.FALLBACK_EXECUTION: "Primary failure + fallback",
    }

    scenario = st.selectbox(
        "Failure scenario",
        list(FailureScenario),
        format_func=lambda item: scenario_labels[item],
    )

    definition = get_scenario_definition(scenario)

    st.markdown("### Scenario contract")
    contract_left, contract_right = st.columns(2)

    with contract_left:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">
                    Detection & behavior
                </h4>
                <p><strong>Detection:</strong> {definition.detection}</p>
                <p><strong>Expected behavior:</strong>
                {definition.expected_behavior}</p>
                <p><strong>Impact:</strong> {definition.impact}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with contract_right:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_WARNING}; margin-top: 0;">
                    Operations & recovery
                </h4>
                <p><strong>Alert:</strong> {definition.alert}</p>
                <p><strong>Recovery:</strong> {definition.recovery}</p>
                <p><strong>Residual risk:</strong> {definition.residual_risk}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    controls_left, controls_right = st.columns(2)

    with controls_left:
        run_scenario = st.button(
            "Run selected simulation",
            type="primary",
            use_container_width=True,
        )

    with controls_right:
        run_all = st.button(
            "Run all scenarios",
            use_container_width=True,
        )

    simulator = FailureSimulator(queue_threshold=3)

    if run_scenario:
        result = simulator.run(scenario)
        st.session_state["resilience_results"] = [result.to_dict()]

    if run_all:
        results = simulator.run_all()
        st.session_state["resilience_results"] = [
            result.to_dict() for result in results
        ]

    results = st.session_state.get("resilience_results", [])

    if results:
        st.markdown("### Simulation results")

        result_rows = [
            {
                "Scenario": result["scenario"],
                "Passed": result["passed"],
                "Detected": result["detected"],
                "State corrupted": result["state_corrupted"],
                "Correlation ID": result["correlation_id"],
                "Behavior": result["behavior"],
            }
            for result in results
        ]
        st.dataframe(result_rows, use_container_width=True)

        for result in results:
            icon = "✅" if result["passed"] else "❌"
            with st.expander(f'{icon} {result["scenario"]}'):
                st.markdown(f"**Correlation ID:** `{result['correlation_id']}`")
                st.markdown(f"**Behavior:** {result['behavior']}")

                details_left, details_right = st.columns(2)

                with details_left:
                    st.markdown(f"**Detection:** {result['detection']}")
                    st.markdown(f"**Impact:** {result['impact']}")
                    st.markdown(f"**Alert:** {result['alert']}")

                with details_right:
                    st.markdown(f"**Recovery:** {result['recovery']}")
                    st.markdown(
                        f"**Residual risk:** {result['residual_risk']}"
                    )
                    st.markdown(
                        f"**State corrupted:** `{result['state_corrupted']}`"
                    )

                st.markdown("**Evidence**")
                st.json(result["evidence"])

        st.caption(
            "All scenarios use deterministic mock fault injection. "
            "No real provider, CRM, or queue operations occur."
        )

elif page == "Scorecard":
    st.title("📊 Production Readiness Scorecard")
    st.markdown(
        "Convert engineering quality into an evidence-backed delivery decision. "
        "API, webhook, reliability, security, scalability, observability, testing, "
        "operations, and customer-readiness checks are combined into a weighted score "
        "with blocking-risk logic and an exportable report."
    )

    engine = ScorecardEngine()

    st.markdown("### Run checks")
    st.caption(
        "This demo uses default pass/fail states. In a real deployment, "
        "these would be driven by CI results, config scans, and test reports."
    )

    col_run, col_export = st.columns([1, 1])

    with col_run:
        run_checks = st.button("Run scorecard", type="primary", use_container_width=True)

    with col_export:
        export_format = st.selectbox("Export format", ["json", "markdown"])
        export_report = st.button("Export report", use_container_width=True)

    if run_checks:
        # Demo: simulate one blocking failure to illustrate behavior.
        test_results = {
            "api_contract_tests": False,
        }
        config_checks = {}
        result = engine.run(
            test_results=test_results,
            config_checks=config_checks,
            metadata={"environment": "demo"},
        )
        st.session_state["last_scorecard"] = result.to_dict()
        st.session_state["last_scorecard_md"] = result.to_markdown()

    last_result_data = st.session_state.get("last_scorecard")
    if not last_result_data:
        st.info("Run the scorecard to see results.")
    else:
        from src.scorecard.engine import (
            CheckDefinition,
            CheckResult,
            CheckStatus,
            Dimension,
            DimensionScore,
            ScorecardResult,
        )

        # Reconstruct result object for display.
        result = ScorecardResult(
            run_id=last_result_data["run_id"],
            overall_score=last_result_data["overall_score"],
            dimensions=[],
            blocking_items=[],
            started_at=datetime.fromisoformat(last_result_data["started_at"]),
            completed_at=datetime.fromisoformat(last_result_data["completed_at"]),
            metadata=last_result_data.get("metadata", {}),
        )

        for dim_data in last_result_data["dimensions"]:
            dim = Dimension(dim_data["dimension"])
            checks = []
            for c_data in dim_data["checks"]:
                definition = CheckDefinition(
                    id=c_data["id"],
                    dimension=Dimension(c_data["dimension"]),
                    name=c_data["name"],
                    description=c_data["description"],
                    weight=c_data["weight"],
                    blocking=c_data["blocking"],
                    evidence_path=c_data.get("evidence_url", ""),
                    config_path=c_data.get("config_path", ""),
                )
                checks.append(
                    CheckResult(
                        definition=definition,
                        status=CheckStatus(c_data["status"]),
                        message=c_data["message"],
                        evidence_url=c_data.get("evidence_url", ""),
                        started_at=datetime.fromisoformat(c_data["started_at"]),
                        completed_at=(
                            datetime.fromisoformat(c_data["completed_at"])
                            if c_data["completed_at"]
                            else None
                        ),
                    )
                )
            result.dimensions.append(
                DimensionScore(
                    dimension=dim,
                    score=dim_data["score"],
                    checks=checks,
                    blocking_count=dim_data["blocking_count"],
                )
            )

        for b_data in last_result_data["blocking_items"]:
            definition = CheckDefinition(
                id=b_data["id"],
                dimension=Dimension(b_data["dimension"]),
                name=b_data["name"],
                description=b_data["description"],
                weight=b_data["weight"],
                blocking=b_data["blocking"],
                evidence_path=b_data.get("evidence_url", ""),
                config_path=b_data.get("config_path", ""),
            )
            result.blocking_items.append(
                CheckResult(
                    definition=definition,
                    status=CheckStatus(b_data["status"]),
                    message=b_data["message"],
                    evidence_url=b_data.get("evidence_url", ""),
                    started_at=datetime.fromisoformat(b_data["started_at"]),
                    completed_at=(
                        datetime.fromisoformat(b_data["completed_at"])
                        if b_data["completed_at"]
                        else None
                    ),
                )
            )

        st.metric("Overall score", f"{result.overall_score:.1f}/100")

        if result.blocking_items:
            st.error(
                f"{len(result.blocking_items)} blocking item(s) must be resolved before release."
            )
            for item in result.blocking_items:
                st.markdown(
                    f"- **{item.definition.name}** ({item.definition.dimension.value}): {item.message}"
                )

        st.markdown("### Dimension scores")
        dim_cols = st.columns(len(result.dimensions))
        for i, dim in enumerate(result.dimensions):
            with dim_cols[i]:
                st.metric(
                    dim.dimension.value.replace("_", " ").title(),
                    f"{dim.score:.1f}",
                )

        st.markdown("### Details")
        for dim in result.dimensions:
            with st.expander(
                f"{dim.dimension.value.replace('_', ' ').title()} ({dim.score:.1f})"
            ):
                for check in dim.checks:
                    icon = {
                        "pass": "✅",
                        "fail": "❌",
                        "blocking": "🚫",
                        "skip": "⏭️",
                    }.get(check.status.value, "❓")
                    st.markdown(
                        f"{icon} **{check.definition.name}** (weight={check.definition.weight:.2f}): "
                        f"{check.message}"
                    )
                    if check.evidence_url or check.definition.evidence_path:
                        st.caption(
                            f"Evidence: `{check.evidence_url or check.definition.evidence_path}`"
                        )

        if export_report and "last_scorecard_md" in st.session_state:
            md = st.session_state["last_scorecard_md"]
            st.download_button(
                label="Download Markdown report",
                data=md.encode(),
                file_name=f"scorecard_{last_result_data['run_id']}.md",
                mime="text/markdown",
            )

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
