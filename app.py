"""Sash: Production readiness and deployment accelerator for programmable customer communications."""

import streamlit as st
from src.styles import get_custom_css, COLOR_PRIMARY, COLOR_SUCCESS, COLOR_WARNING, COLOR_ERROR, COLOR_TEXT_MUTED, COLOR_SURFACE, COLOR_BORDER

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
    ["Home", "Domain Models", "Engagements", "Workflows"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Version:** v0.5.0")
st.sidebar.markdown("**Phase:** 5 - Domain Core")

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
                Phase 5: Domain and persistence core now available.
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
                    <li>Engagement qualification</li>
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
                <li>Engagement qualification module with scoring</li>
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
                    <li><code>metadata</code> (dict)</li>
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
                    <li><code>started_at</code>, <code>completed_at</code></li>
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
                    <li><code>content</code>, <code>metadata</code></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    st.markdown(
        """
        ### Enums
        
        - **ChannelType**: SMS, WhatsApp, Email, Voice
        - **EventStatus**: pending, sent, delivered, failed, bounced
        - **WorkflowStatus**: draft, active, paused, completed, failed
        
        ### Persistence
        
        All entities are stored in in-memory repositories for the demo.
        Export to JSON is supported via `JsonSerializer`.
        """
    )

elif page == "Engagements":
    st.title("Engagements")
    st.markdown("Customer engagement tracking and qualification.")
    
    st.markdown("---")
    
    st.markdown(
        f"""
        <div class="sash-card">
            <h4 style="color: {COLOR_PRIMARY}; margin-top: 0;">📋 Engagement Entity</h4>
            <p>Track customer engagements through qualification and delivery.</p>
            <ul>
                <li><code>customer_name</code>, <code>company</code></li>
                <li><code>use_case</code></li>
                <li><code>priority</code>: low/medium/high/critical</li>
                <li><code>status</code>: new/qualified/active/completed/archived</li>
                <li><code>notes</code></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.info("💡 Engagement qualification module coming in Phase 6.")

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
    
    st.info("💡 Workflow designer UI coming in Phase 7.")

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
