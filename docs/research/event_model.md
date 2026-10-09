# Event model

This document defines the normalized communication event schema used throughout Sash.

## Event types

### `verification.requested`

User initiated verification.

Fields:
- `event_id`: Unique event identifier
- `event_type`: `verification.requested`
- `workflow_id`: Associated workflow
- `customer_id`: Aurora user identifier
- `correlation_id`: Cross-system correlation ID
- `channel`: Requested channel (sms, whatsapp, email)
- `recipient`: Phone number or email address
- `timestamp`: Event timestamp
- `metadata`: Additional context

### `verification.sent`

Verification message was sent successfully.

Fields:
- `event_id`
- `event_type`: `verification.sent`
- `workflow_id`
- `customer_id`
- `correlation_id`
- `channel`
- `recipient`
- `provider_message_id`: Sinch message ID
- `timestamp`
- `metadata`

### `verification.delivered`

Message was delivered to recipient.

Fields:
- `event_id`
- `event_type`: `verification.delivered`
- `workflow_id`
- `customer_id`
- `correlation_id`
- `channel`
- `recipient`
- `provider_message_id`
- `delivered_at`: Delivery timestamp from provider
- `timestamp`: Event processing timestamp
- `metadata`

### `verification.failed`

Message send or delivery failed.

Fields:
- `event_id`
- `event_type`: `verification.failed`
- `workflow_id`
- `customer_id`
- `correlation_id`
- `channel`
- `recipient`
- `error_code`: Provider error code
- `error_message`: Human-readable error
- `retryable`: Boolean indicating if retry is appropriate
- `timestamp`
- `metadata`

### `verification.code_submitted`

User submitted verification code.

Fields:
- `event_id`
- `event_type`: `verification.code_submitted`
- `workflow_id`
- `customer_id`
- `correlation_id`
- `code`: Submitted code (redacted in logs)
- `attempt_number`: Which attempt this is
- `valid`: Boolean indicating if code matches
- `timestamp`
- `metadata`

### `verification.completed`

Verification workflow completed successfully.

Fields:
- `event_id`
- `event_type`: `verification.completed`
- `workflow_id`
- `customer_id`
- `correlation_id`
- `channel`: Final successful channel
- `total_attempts`: Number of attempts
- `duration_seconds`: Time from request to completion
- `timestamp`
- `metadata`

### `verification.expired`

Verification code expired without successful submission.

Fields:
- `event_id`
- `event_type`: `verification.expired`
- `workflow_id`
- `customer_id`
- `correlation_id`
- `channel`
- `expired_at`: Expiration timestamp
- `timestamp`
- `metadata`

## Event normalization

Provider-specific events (Sinch webhooks) are normalized to this schema:

- Provider event → Event normalizer → Normalized event
- Provider fields mapped to standard field names
- Provider-specific metadata preserved in `metadata` field
- Timestamps converted to UTC ISO 8601 format

## Correlation

Every event includes:

- `workflow_id`: Groups events within a workflow
- `correlation_id`: Groups events across systems (Sash, Aurora, Sinch)
- `event_id`: Unique per event

## Ordering

Events are ordered by:

1. `timestamp` (primary)
2. `event_id` (secondary, for tie-breaking)

Out-of-order events are handled via:

- Event buffering for small delays
- Idempotent state transitions
- Event replay capability

## Persistence

Events are persisted in:

- Event store (append-only)
- Workflow timeline (for quick lookup)
- Audit log (for compliance)

## References

- Sinch webhook documentation: https://developers.sinch.com/docs/messaging/webhooks
- Event sourcing patterns: https://martinfowler.com/eaaDev/EventSourcing.html
