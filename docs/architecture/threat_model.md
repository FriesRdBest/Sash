# Threat model

This document describes the security threat model for Sash using STRIDE analysis.

## Assets

1. **Workflow data:** Verification workflow state and history
2. **Event data:** Communication events and delivery reports
3. **Audit trail:** Complete history of state changes
4. **Correlation IDs:** Cross-system tracing identifiers
5. **Customer data:** Phone numbers, email addresses (PII)
6. **Provider credentials:** Sinch API keys (future)

## Threats (STRIDE)

### Spoofing

**T1: Spoofed webhook from Sinch**

- **Threat:** Attacker sends fake delivery webhooks
- **Impact:** Workflow state corruption, false delivery confirmations
- **Mitigation:** Webhook signature validation (HMAC)
- **Status:** Documented, implementation pending

**T2: Spoofed Aurora API client**

- **Threat:** Unauthorized system calls Sash API
- **Impact:** Resource exhaustion, data exposure
- **Mitigation:** API authentication (API key or OAuth)
- **Status:** Future requirement

### Tampering

**T3: Workflow state tampering**

- **Threat:** Direct database modification
- **Impact:** Audit trail invalidation, state corruption
- **Mitigation:** Database access controls, application-layer validation
- **Status:** Partially mitigated (SQLite file permissions)

**T4: Event log tampering**

- **Threat:** Delete or modify events
- **Impact:** Audit trail gaps, compliance violations
- **Mitigation:** Append-only event store, cryptographic hashing (future)
- **Status:** Design principle, implementation pending

### Repudiation

**T5: Deny sending verification**

- **Threat:** Aurora claims they never requested verification
- **Impact:** Dispute resolution difficulty
- **Mitigation:** Complete audit trail with timestamps and actors
- **Status:** Implemented via event logging

**T6: Deny receiving delivery**

- **Threat:** User claims they never received message
- **Impact:** Customer support disputes
- **Mitigation:** Provider delivery reports, audit trail
- **Status:** Relies on Sinch delivery reports

### Information Disclosure

**T7: PII exposure in logs**

- **Threat:** Phone numbers, emails logged in plaintext
- **Impact:** Privacy violations, regulatory non-compliance
- **Mitigation:** Log redaction, PII classification
- **Status:** Documented requirement, implementation pending

**T8: Credential exposure**

- **Threat:** Sinch API keys committed to repository
- **Impact:** Unauthorized API usage, cost exposure
- **Mitigation:** Environment variables, secret scanning, .gitignore
- **Status:** Mitigated (no credentials in demo mode)

### Denial of Service

**T9: API rate limiting bypass**

- **Threat:** Excessive API calls exhaust Sinch quota
- **Impact:** Service unavailability, cost overruns
- **Mitigation:** Rate limiting, request queuing
- **Status:** Future requirement

**T10: Database exhaustion**

- **Threat:** Excessive workflow creation fills storage
- **Impact:** Application failure
- **Mitigation:** Pagination, retention policies, quotas
- **Status:** Future requirement

### Elevation of Privilege

**T11: Unauthorized workflow access**

- **Threat:** Access workflows from other customers
- **Impact:** Data breach, privacy violation
- **Mitigation:** Customer isolation, access controls
- **Status:** Future requirement (multi-tenancy not implemented)

**T12: Privilege escalation via retry**

- **Threat:** Exploit retry logic to bypass limits
- **Impact:** Resource exhaustion, fraud
- **Mitigation:** Retry budgets, idempotency, audit
- **Status:** Partially mitigated (retry policy designed)

## Trust boundaries

1. **Network boundary:** Internet ↔ Sash application
2. **Application boundary:** UI ↔ Domain core
3. **Data boundary:** Application ↔ Persistence
4. **Provider boundary:** Sash ↔ Sinch

## Security requirements

- **REQ-SEC-001:** All PII must be redacted from logs
- **REQ-SEC-002:** Webhook signatures must be validated
- **REQ-SEC-003:** API authentication required for all external calls
- **REQ-SEC-004:** No credentials committed to repository
- **REQ-SEC-005:** Audit trail must be complete and tamper-evident

## References

- SECURITY.md: ../../SECURITY.md
- Assumptions register: ../research/assumptions_register.md
