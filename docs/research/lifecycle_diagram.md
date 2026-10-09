# Event lifecycle diagram

This document describes the lifecycle of a verification event from send request to final delivery status.

## Lifecycle stages

```
┌─────────────────────────────────────────────────────────────────┐
│                     Verification Event Lifecycle                │
└─────────────────────────────────────────────────────────────────┘

1. REQUEST
   User initiates verification
   ↓
   Event: verification.requested
   State: pending

2. SEND
   Sash calls provider (Sinch)
   ↓
   Event: verification.sent
   State: code_sent

3. DELIVERY (provider processing)
   Provider routes message
   ↓
   [Success path]
   Event: verification.delivered
   ↓
   [Failure path]
   Event: verification.failed
   State: failed or fallback_initiated

4. SUBMISSION
   User submits code
   ↓
   Event: verification.code_submitted

5. VALIDATION
   Sash validates code
   ↓
   [Valid]
   Event: verification.completed
   State: verified (terminal)
   ↓
   [Invalid]
   Event: verification.code_submitted (valid=false)
   State: code_sent (retry allowed)

6. EXPIRATION (timeout path)
   Code expires without submission
   ↓
   Event: verification.expired
   State: expired (terminal)

7. FALLBACK (if primary fails)
   Primary channel fails
   ↓
   Event: verification.failed (retryable=true)
   State: fallback_initiated
   ↓
   Retry via secondary channel
   ↓
   Return to stage 2 (SEND)

8. AUDIT
   All events persisted
   ↓
   Event timeline available for query
   Correlation ID connects all events
```

## Event flow with webhooks

```
Aurora App → Sash API → Sinch API → Mobile Network → User Device
     ↓            ↓           ↓            ↓              ↓
  request    workflow    message      delivery       received
  created    created     sent         report         by user
     ↓            ↓           ↓            ↓              ↓
     └────────────┴───────────┴────────────┴──────────────┘
                          correlation_id

User Device → Mobile Network → Sinch Webhook → Sash Webhook Handler
     ↓              ↓               ↓                  ↓
  code entered  delivery      delivery event    event normalized
  by user       status        received          and persisted
     ↓              ↓               ↓                  ↓
     └──────────────┴───────────────┴──────────────────┘
                      correlation_id (same throughout)
```

## State transitions

```
pending
  ↓ (send)
code_sent
  ├─→ verified (success)
  ├─→ failed (send error)
  ├─→ expired (timeout)
  └─→ fallback_initiated (primary failed)
        ├─→ verified (fallback success)
        ├─→ failed (fallback failed)
        └─→ expired (fallback timeout)
```

## Idempotency guarantees

- Duplicate webhooks: Same `event_id` → ignored
- Retries: Same `correlation_id` → no duplicate workflows
- Replays: Events reprocessed → state converges to same result

## Correlation

Every event in the lifecycle shares:

- `correlation_id`: Set at workflow creation, never changes
- `workflow_id`: Groups events within one verification attempt
- `event_id`: Unique per event

## References

- Workflow states: `workflow_states.md`
- Event model: `event_model.md`
- Sinch webhook documentation: https://developers.sinch.com/docs/messaging/webhooks
