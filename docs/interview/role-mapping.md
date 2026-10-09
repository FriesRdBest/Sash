# Role Mapping and Roadmap

| FDE responsibility | Sash evidence | Status |
|---|---|---|
| Qualify engagements | Qualification view and rules | Demo rules; customer process not independently validated |
| Design integrations | Workflow, architecture docs, provider boundary | Reference design; customer systems not verified |
| Build resilient flows | Retry/fallback and integration modules | Local implementation; provider mode not established |
| Process asynchronous events | Event engine, timeline, audit model | Local tests; production queue/replay deployment not established |
| Observe operations | Timeline, observability, scorecard | Demo values may be simulated; not production telemetry |
| Address security | Security review and redaction logic | Advisory/demo checks; no certification |
| Enable handoff | Handoff package generator | Demo output; customer ownership requires review |
| Use AI responsibly | AI review module | Advisory; human approval required |

## Roadmap

1. Confirm the live deployment matches the restored Phase 18 snapshot.
2. Complete keyboard, focus, contrast, screen-reader, and error-state review.
3. Validate an authorized provider sandbox using synthetic data.
4. Add provider contract tests and callback fixtures.
5. Measure expected traffic and run load/resilience tests.
6. Select production storage, queue, secrets, identity, retention, and alerting for customer requirements.
7. Define ownership, incident escalation, replay, rollback, and training.
8. Publish only after the release gate is complete.