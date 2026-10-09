# Workflow states

This document defines the state machine for the Aurora Marketplace user verification workflow.

## States

### `pending`

Initial state. User has initiated registration but verification has not started.

Transitions:
- → `code_sent` (verification request submitted)
- → `failed` (validation error before send)

### `code_sent`

Verification code has been sent via primary channel (SMS).

Transitions:
- → `verified` (user submitted correct code)
- → `expired` (timeout without successful verification)
- → `failed` (send failure)
- → `fallback_initiated` (primary channel failed, fallback starting)

### `verified`

User successfully verified. Terminal state.

Transitions:
- None (terminal)

### `expired`

Verification code expired without successful submission. Terminal state.

Transitions:
- None (terminal)

### `failed`

Verification failed due to send error, validation error, or system error. Terminal state.

Transitions:
- None (terminal)

### `fallback_initiated`

Primary channel failed. Fallback channel (WhatsApp or email) is being attempted.

Transitions:
- → `verified` (user verified via fallback)
- → `failed` (fallback send failure)
- → `expired` (timeout on fallback)

## State persistence

Each workflow instance is persisted with:

- `workflow_id`: Unique identifier
- `customer_id`: Aurora user identifier
- `correlation_id`: Tracks all related events
- `current_state`: Current state from the state machine
- `channel_history`: List of channels attempted
- `attempt_count`: Number of send attempts
- `created_at`: Workflow creation timestamp
- `updated_at`: Last state change timestamp
- `metadata`: Additional context (phone number, email, etc.)

## State transitions are triggered by

- User actions (submit code, request new code)
- System events (send success, send failure, timeout)
- Webhook events (delivery reports, inbound messages)

## Idempotency

State transitions must be idempotent:

- Duplicate webhook events must not change state twice
- Retries must not create duplicate workflows
- State changes are logged with event IDs for audit

## Validation rules

- Cannot transition from terminal states (`verified`, `failed`, `expired`)
- Cannot skip `code_sent` state
- Fallback requires primary channel failure or timeout
- Maximum 3 total attempts before hard failure

## Audit requirements

Every state transition is logged with:

- Previous state
- New state
- Trigger event
- Timestamp
- Actor (user, system, webhook)
- Correlation ID
