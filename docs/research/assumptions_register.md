# Assumptions register

This document tracks assumptions made during Sash design and their validation status.

## Assumptions

### A001: Mock mode is sufficient for initial demonstration

**Statement:** A fully functional mock provider without real Sinch credentials is sufficient to demonstrate engineering capability.

**Rationale:** The goal is to show reliability engineering, not API integration. Real credentials add complexity without proportional value for initial review.

**Validation status:** ✅ Validated

**Evidence:** Providence repository demonstrates complex Streamlit applications built rapidly without external dependencies.

**Risk if wrong:** Low. Real Sinch integration can be added later as an optional mode.

---

### A002: Aurora Marketplace is a realistic customer profile

**Statement:** A fictional marketplace requiring user verification via SMS with fallback is representative of real Sinch customer use cases.

**Rationale:** Verification workflows are common across e-commerce, fintech, and marketplace platforms.

**Validation status:** ✅ Validated

**Evidence:** Sinch documentation highlights verification as a primary use case. Conversation API supports multi-channel fallback patterns.

**Risk if wrong:** Low. The workflow pattern generalizes to other scenarios.

---

### A003: SQLite is adequate for demo persistence

**Statement:** SQLite provides sufficient persistence for the demonstration without requiring PostgreSQL or cloud databases.

**Rationale:** Simplifies deployment, no external dependencies, adequate for demo scale.

**Validation status:** ✅ Validated

**Evidence:** SQLite is widely used for local development and demos. Repository layer can swap to PostgreSQL later.

**Risk if wrong:** Low. Architecture separates persistence interface from implementation.

---

### A004: Streamlit Community Cloud is acceptable for hosting

**Statement:** Streamlit Community Cloud provides a professional enough hosting environment for the demo.

**Rationale:** Free tier, GitHub integration, automatic deployments, acceptable performance for demo traffic.

**Validation status:** ⏳ Pending deployment

**Evidence:** Widely used for Streamlit demos. Professional appearance.

**Risk if wrong:** Low. Can deploy to alternative platforms (Render, Fly.io, AWS) if needed.

---

### A005: Brett will review GitHub repository more deeply than the live app

**Statement:** Technical reviewers will inspect the repository structure, commit history, and code quality more carefully than the live application.

**Rationale:** Engineering roles require code review skills. Repository quality signals engineering discipline.

**Validation status:** ⏳ Assumption to be validated

**Evidence:** Standard practice for engineering hiring. Brett's background in telecommunications and infrastructure suggests appreciation for system design.

**Risk if wrong:** Medium. Mitigated by ensuring both repository and app are high quality.

---

### A006: Five-day build timeline is realistic

**Statement:** The full Sash application can be built to a credible state within 5-9 days of focused work.

**Rationale:** Providence was built in 1-2 days with similar complexity scope.

**Validation status:** ⏳ In progress

**Evidence:** Providence repository commit history shows rapid development capability.

**Risk if wrong:** Medium. Mitigated by phased delivery and clear communication of what is implemented vs. planned.

---

### A007: Email outreach will be well-received

**Statement:** A direct email to Brett with the Sash repository and app will be viewed positively as initiative and genuine interest.

**Rationale:** Demonstrates proactive problem-solving and alignment with "Make it Happen" value.

**Validation status:** ⏳ Pending response

**Evidence:** Non-traditional approaches often stand out. The role requires customer-facing initiative.

**Risk if wrong:** High. Mitigated by professional tone, clear value proposition, and respect for time.

---

## Decision log

Decisions based on assumptions are documented in `.github/ISSUE_TEMPLATE/risk_or_decision.md` issues.

## Review cadence

Assumptions are reviewed:

- At the start of each phase
- When new evidence emerges
- Before major architectural decisions

## References

- Sinch product documentation
- Providence repository development velocity
- Industry hiring practices for Forward Deployed Engineers
