"""Sash: Production readiness and deployment accelerator for programmable customer communications."""

import streamlit as st
from src.styles import get_custom_css, COLOR_PRIMARY, COLOR_SUCCESS, COLOR_WARNING, COLOR_ERROR, COLOR_TEXT_MUTED, COLOR_SURFACE, COLOR_BORDER
from src.qualification.assess import assess_engagement
from src.persistence.seed_data import load_seed_data
from src.persistence.sqlite_repo import engagement_repo

# Page configuration
st.set_page_config(
    page_title="Sash",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Sash")
st.sidebar.markdown("Production readiness accelerator")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Domain Models", "Qualification", "Engagements", "Workflows"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Version:** v0.5.0")
st.sidebar.markdown("**Phase:** 5 - Domain Core + Qualification")

# Main content
if page == "Home":
    st.title("Sash")
    st.subheader("Production readiness and deployment accelerator for programmable customer communications")
    
    # Status banner
    status_col1, status_col2 = st.columns([3, 1])
    with status_col1:
        st.markdown(
            f"""
            <div style="background-color: {COLOR_PRIMARY}10; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid {COLOR_PRIMARY};">
                <strong>🚧 Under Active Development</strong><br>
                Phase 5: Domain/persistence core + Engagement qualification now available.
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with status_col2:
        st.markdown(
            f"""
            <div style="text-align: right;">
                <span class="status-badge status-info">v0.5.0</span>
            </div>
            """,
            unsafe_allow_html=True
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
                <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">✅ Phase 0-5 Complete</h4>
                <ul style="margin-bottom: 0; padding-left: 1.25rem;">
                    <li>Operating charter</li>
                    <li>Repository foundation</li>
                    <li>Research and domain model</li>
                    <li>Architecture and ADRs</li>
                    <li>Design system</li>
                    <li><strong>Domain & persistence core</strong></li>
                    <li><strong>Engagement qualification</strong></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with roadmap_col2:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_WARNING}; margin-top: 0;">🚧 In Progress</h4>
                <ul style="margin-bottom: 0; padding-left: 1.25rem;">
                    <li>Workflow designer</li>
                    <li>Integration laboratory</li>
                    <li>Event and webhook engine</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with roadmap_col3:
        st.markdown(
            f"""
            <div class="sash-card">
                <h4 style="color: {COLOR_TEXT_MUTED}; margin-top: 0;">⏳ Planned</h4>
                <ul style="margin-bottom: 0; padding-left: 1.25rem;">
                    <li>End-to-end happy path</li>
                    <li>Failure and resilience lab</li>
                    <li>Production-readiness scorecard</li>
                    <li>Observability console</li>
                    <li>Handoff package generator</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
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
            unsafe_allow_html=True
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
            unsafe_allow_html=True
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
            unsafe_allow_html=True
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
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    # Next steps
    st.markdown("## ▶️ Next Steps")
    
    st.markdown(
        f"""
        <div class="sash-card">
            <p><strong>Coming in the next 24-48 hours:</strong></p>
            <ol>
                <li>Workflow designer with JSON export</li>
                <li>Mock Sinch provider integration</li>
                <li>Event timeline and audit view</li>
            </ol>
            <p style="margin-top: 1rem; color: {COLOR_TEXT_MUTED};">
                This application will grow rapidly. Check back frequently to see new features being added.
            </p>
        </div>
        """,
        unsafe_allow_html=True
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
            unsafe_allow_html=True
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
            unsafe_allow_html=True
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
            unsafe_allow_html=True
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
            unsafe_allow_html=True
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
        use_case = st.text_area("Use Case", "User verification for marketplace platform", height=100)
    
    with col2:
        priority = st.selectbox("Priority", ["low", "medium", "high", "critical"])
        channels = st.multiselect("Channels", ["sms", "whatsapp", "email", "voice"], default=["sms"])
        expected_volume = st.number_input("Expected Monthly Volume", min_value=0, value=5000, step=1000)
        timeline_days = st.number_input("Timeline (days)", min_value=1, value=30, step=7)
    
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
            score_color = COLOR_SUCCESS if assessment.score >= 80 else (COLOR_WARNING if assessment.score >= 60 else COLOR_ERROR)
            st.markdown(
                f"""
                <div class="metric-card" style="background: linear-gradient(135deg, {score_color} 0%, #000 100%);">
                    <div class="metric-value">{assessment.score}</div>
                    <div class="metric-label">Readiness Score</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with score_col2:
            decision_emoji = "✅" if assessment.decision == "proceed" else ("⚠️" if assessment.decision == "proceed_with_conditions" else "❌")
            st.markdown(
                f"""
                <div class="sash-card" style="text-align: center;">
                    <div style="font-size: 2rem;">{decision_emoji}</div>
                    <strong>{assessment.decision.replace('_', ' ').title()}</strong>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with score_col3:
            risk_count = len(assessment.risk_flags)
            risk_color = COLOR_ERROR if risk_count > 2 else (COLOR_WARNING if risk_count > 0 else COLOR_SUCCESS)
            st.markdown(
                f"""
                <div class="sash-card" style="text-align: center; border-left: 4px solid {risk_color};">
                    <div style="font-size: 2rem;">{risk_count}</div>
                    <strong>Risk Flags</strong>
                </div>
                """,
                unsafe_allow_html=True
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
        st.success(f"Loaded {result['engagements']} engagements, {result['customers']} customers, {result['workflows']} workflows")
    
    st.markdown("---")
    
    # List engagements
    st.markdown("### 📋 Existing Engagements")
    
    engagements = engagement_repo.get_all()
    
    if not engagements:
        st.markdown("<div class='empty-state'><div class='empty-state-icon'>📭</div><p>No engagements yet. Load seed data or create a new assessment.</p></div>", unsafe_allow_html=True)
    else:
        for eng in engagements:
            st.markdown(
                f"""
                <div class="sash-card">
                    <h4 style="margin-top: 0;">{eng.get('customer_name', 'Unknown')} @ {eng.get('company', 'Unknown')}</h4>
                    <p><strong>Use Case:</strong> {eng.get('use_case', 'N/A')}</p>
                    <p><strong>Priority:</strong> {eng.get('priority', 'medium')} | <strong>Volume:</strong> {eng.get('expected_volume', 0):,}/mo | <strong>Timeline:</strong> {eng.get('timeline_days', 30)} days</p>
                    <p><strong>Channels:</strong> {', '.join(eng.get('channels', []))}</p>
                    <p><strong>Status:</strong> <span class="status-badge status-info">{eng.get('status', 'new')}</span></p>
                </div>
                """,
                unsafe_allow_html=True
            )

elif page == "Workflows":
    st.title("Workflows")
    st.markdown("Design and execute communication workflows.")
    
    st.markdown("---")
    
    st.markdown(
        f"""
        <div class="sash-card">
            <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">🔀 Workflow Designer</h4>
            <p>Visual workflow designer with step configuration.</p>
            <ul>
                <li>Add/remove steps</li>
                <li>Configure channels and templates</li>
                <li>Set conditions and branching</li>
                <li>Export to JSON</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.info("💡 Workflow designer UI coming in Phase 6.")

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
    unsafe_allow_html=True
)
