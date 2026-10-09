import streamlit as st

st.set_page_config(
    page_title="Sash", page_icon="🔗", layout="wide", initial_sidebar_state="expanded"
)

st.title("Sash")
st.subheader(
    "Production readiness and deployment accelerator for programmable customer communications"
)

st.markdown("""
This application demonstrates how an engineer can qualify an engagement, design an API driven architecture, build resilient communication workflows, test failure modes, instrument operations, and produce a customer handoff package.

**Status:** Under active development. This is the initial application shell.

**Flagship scenario:** Aurora Marketplace user verification workflow with SMS primary channel and WhatsApp or email fallback.
""")

st.divider()

st.markdown("### Navigation")

st.info("🚧 Pages under construction. Check back soon for:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Engagement qualification**
    
    Intake form, feasibility rules, readiness scoring, product fit assessment, risk flags, recommended decision.
    """)

with col2:
    st.markdown("""
    **Workflow designer**
    
    Workflow configuration, channel selection, fallback rules, retry policy, timeout policy, consent requirement.
    """)

with col3:
    st.markdown("""
    **Observability console**
    
    KPI cards, event table, workflow timeline, correlation search, channel breakdown, failure breakdown.
    """)

st.divider()

st.markdown("""
### Repository

- [View source code on GitHub](https://github.com/FriesRdBest/Sash)
- [Read the project charter](https://github.com/FriesRdBest/Sash/blob/main/README.md)
- [Review the changelog](https://github.com/FriesRdBest/Sash/blob/main/CHANGELOG.md)

### Next steps

This application will grow rapidly over the coming days. Planned features include:

1. Engagement qualification module
2. Workflow designer with JSON export
3. Mock Sinch provider integration
4. Event and webhook engine
5. Failure and resilience laboratory
6. Production readiness scorecard
7. Observability console
8. Handoff package generator

**Built for the Senior Forward Deployed Engineer role at Sinch.**
""")
