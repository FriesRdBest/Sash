"""Sash — premium home page (no emojis)."""

import streamlit as st
from src.styles import page_config, local_css

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
    <li><b>Seed data</b> — Load reproducible demo customers, workflows, and engagements (Admin page).</li>
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
