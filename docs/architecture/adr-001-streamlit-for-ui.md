# ADR 001: Use Streamlit for demonstration UI

## Status

Accepted

## Context

Sash needs a user interface to demonstrate:
- Engagement qualification
- Workflow design
- Observability console
- Failure simulation
- Handoff package generation

The UI must be:
- Quick to build
- Easy to deploy
- Professional looking
- Accessible to non-technical stakeholders

## Decision

Use Streamlit for the demonstration UI.

## Rationale

**Pros:**
- Rapid development (hours, not days)
- Python-native (no JavaScript required)
- Built-in deployment (Streamlit Community Cloud)
- Professional appearance out of the box
- Easy to iterate and refine
- Good for demos and prototypes

**Cons:**
- Not suitable for high-scale production
- Limited customization compared to React/Vue
- Tied to Python backend
- Less control over performance optimization

**Why this matters:**

The goal is to demonstrate engineering capability and domain understanding, not to build a production UI framework. Streamlit allows focus on the domain logic while still providing a credible interface.

## Consequences

- UI development is fast
- Deployment is simple (GitHub → Streamlit Cloud)
- Future production UI may need replacement
- Current approach is sufficient for demo and early customer engagements

## References

- Streamlit documentation: https://docs.streamlit.io
- Container diagram: container.md
