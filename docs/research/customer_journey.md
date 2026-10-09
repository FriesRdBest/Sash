# Customer journey: Aurora Marketplace verification

This document maps the user journey for Aurora Marketplace user verification.

## Personas

### New user (Alice)

- Signing up for Aurora Marketplace
- Has a mobile phone with SMS
- May have WhatsApp installed
- Has an email address
- Wants quick, frictionless verification

### Aurora engineering team

- Needs reliable verification
- Wants to minimize fraud
- Needs audit trail for compliance
- Prefers simple integration

### Aurora operations team

- Monitors verification success rates
- Responds to delivery issues
- Needs visibility into failures
- Requires runbooks for common issues

## Journey stages

### Stage 1: Registration initiation

**Alice:**
- Visits Aurora signup page
- Enters name, email, phone number
- Clicks "Send verification code"

**Aurora system:**
- Validates input format
- Creates pending verification workflow
- Calls Sash orchestration service

**Sash:**
- Creates workflow with `pending` state
- Generates correlation ID
- Logs `verification.requested` event

---

### Stage 2: Primary channel send (SMS)

**Sash:**
- Selects SMS as primary channel
- Calls mock Sinch provider
- Logs `verification.sent` event
- Transitions workflow to `code_sent`

**Sinch (mock):**
- Accepts send request
- Returns message ID
- Simulates delivery after delay

**Alice:**
- Receives SMS with 6-digit code
- Enters code in Aurora app

---

### Stage 3: Verification (happy path)

**Aurora system:**
- Receives code from Alice
- Calls Sash to validate

**Sash:**
- Validates code
- Logs `verification.code_submitted` event
- Logs `verification.completed` event
- Transitions workflow to `verified`

**Alice:**
- Sees "Verification successful"
- Completes signup
- Can now use Aurora Marketplace

---

### Stage 4: Failure and fallback (alternate path)

**Scenario:** SMS delivery fails

**Sinch (mock):**
- Returns delivery failure webhook
- Error code: `UNREACHABLE`

**Sash:**
- Logs `verification.failed` event
- Evaluates retry policy
- Initiates fallback to WhatsApp
- Logs `verification.sent` (WhatsApp)
- Transitions to `fallback_initiated`

**Alice:**
- Receives WhatsApp message with code
- Enters code
- Verification completes

---

### Stage 5: Operations visibility

**Aurora operations team:**
- Opens Sash observability console
- Sees verification success rate dashboard
- Drills into failed verifications
- Identifies pattern: specific carrier failures
- Takes action: adjust routing for that carrier

---

## Touchpoints

| Touchpoint | System | Owner |
|---|---|---|
| Signup form | Aurora frontend | Aurora |
| Verification API | Sash orchestration | Sash |
| SMS send | Sinch Messaging API | Sinch |
| WhatsApp send | Sinch Conversation API | Sinch |
| Code validation | Sash orchestration | Sash |
| Audit trail | Sash event store | Sash |
| Operations dashboard | Sash observability | Sash |

## Metrics

Key metrics tracked:

- Verification success rate
- Median time to verify
- Fallback rate
- Failure rate by channel
- Failure rate by carrier/country

## Pain points addressed

- **SMS failure:** Automatic fallback to WhatsApp or email
- **No visibility:** Operations dashboard shows real-time status
- **No audit trail:** Event store provides complete history
- **Manual debugging:** Correlation IDs connect all events
- **Knowledge loss:** Handoff package documents everything

## References

- Aurora Marketplace (fictional customer)
- Sinch product documentation
- Sash flagship scenario definition
