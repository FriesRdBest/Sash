# Amberglass Final Test Checklist

Run this checklist in the Streamlit application before merging the all page polish branch.

## Global checks

- [ ] Sidebar is black with white labels and amber active navigation
- [ ] Main content uses amber workspace and readable black text
- [ ] Cards, forms, metrics, tables, alerts, and expanders use consistent bronze borders
- [ ] Primary actions are black with white labels
- [ ] Secondary and download actions use cream backgrounds and bronze borders
- [ ] Keyboard focus is clearly visible
- [ ] Narrow layouts stack content without page-level horizontal scrolling
- [ ] Long IDs, JSON, code, and tables stay readable and scroll inside their own containers

## Page checks

- [ ] Home: paired cards, four desktop Quick Links, mobile Quick Links, and footer attribution
- [ ] Domain Models: cards remain aligned and code labels wrap
- [ ] Qualification: complete the form, assess engagement, inspect score/risk states, export JSON
- [ ] Engagements: inspect empty state, load seed data, inspect populated engagement cards
- [ ] Workflows: inspect workflow summary, long workflow steps, download JSON, reset workflow
- [ ] Run Workflow: submit valid and invalid phone values, inspect event and audit tables
- [ ] Event Timeline: use a correlation ID, inspect metrics, timeline cards, JSON details, and global search
- [ ] Failure Lab: run one scenario and all scenarios, inspect result table and evidence expanders
- [ ] Scorecard: run scorecard, inspect blocking state, export JSON and Markdown
- [ ] Observability: inspect metrics, alerts, and tables
- [ ] Security Review: run review and inspect findings/evidence
- [ ] AI Review: run review and inspect generated findings
- [ ] Handoff Package: generate and download the package

## Final commands

- [ ] `ruff check .`
- [ ] `pytest -q`
- [ ] `python -m py_compile app.py src/styles.py`
- [ ] `git diff --check`
