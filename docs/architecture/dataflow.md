# Data flow diagram

This document describes the data flow for the Aurora Marketplace verification workflow.

## Level 0: Context flow

```
[Aurora] --verification request--> [Sash] --send message--> [Sinch] --deliver--> [User]
   ^                                  |                          |
   |                                  |                          |
   |------view dashboard-------------|                          |
   |                                  |                          |
   |------query status--------------|                          |
   |                                                             |
   '-------------delivery reports<------------------------------'
```

## Level 1: Sash internal flow

```
1. Aurora calls Sash API
         ↓
2. Workflow Engine creates workflow (state: pending)
         ↓
3. Event Processor logs verification.requested event
         ↓
4. Provider Adapter sends message via Sinch
         ↓
5. Persistence Layer stores workflow and event
         ↓
6. Sinch returns message ID
         ↓
7. Workflow Engine transitions to code_sent
         ↓
8. Event Processor logs verification.sent event
         ↓
9. Sinch sends delivery webhook
         ↓
10. Event Processor normalizes webhook
         ↓
11. Idempotency Manager checks for duplicates
         ↓
12. Workflow Engine processes delivery status
         ↓
13. Persistence Layer stores delivery event
         ↓
14. Observability logs all events
```

## Data stores

### Workflows

- **Schema:** workflow_id, customer_id, correlation_id, current_state, channel_history, attempt_count, created_at, updated_at, metadata
- **Operations:** create, read, update, query by customer_id, query by state

### Events

- **Schema:** event_id, event_type, workflow_id, customer_id, correlation_id, channel, recipient, timestamp, metadata
- **Operations:** append, read by workflow_id, read by correlation_id, read by event_type

### Audit

- **Schema:** audit_id, workflow_id, event_id, previous_state, new_state, actor, timestamp, details
- **Operations:** append, read by workflow_id, read by timestamp range

## Data flow properties

- **Append-only:** Events are never modified, only appended
- **Idempotent:** Duplicate events do not change state twice
- **Correlated:** All events share correlation_id for tracing
- **Auditable:** All state changes logged with actor and timestamp

## References

- Event model: ../research/event_model.md
- Workflow states: ../research/workflow_states.md
