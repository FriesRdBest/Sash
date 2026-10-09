# Production limitations

This document explicitly documents the limitations of the Sash demo compared to a production system.

## Current limitations (demo)

### Persistence

- **Limitation:** SQLite file-based storage
- **Impact:** No concurrency, no durability guarantees, no backup
- **Production requirement:** PostgreSQL with replication and backup

### Concurrency

- **Limitation:** Single-threaded Streamlit app
- **Impact:** Cannot handle concurrent requests
- **Production requirement:** FastAPI service with multiple workers

### Scalability

- **Limitation:** No horizontal scaling
- **Impact:** Cannot handle high volume
- **Production requirement:** Container orchestration, auto-scaling

### Reliability

- **Limitation:** No redundancy, no failover
- **Impact:** Single point of failure
- **Production requirement:** Multi-AZ deployment, health checks, circuit breakers

### Security

- **Limitation:** No API authentication, no webhook signature validation
- **Impact:** Unauthorized access possible
- **Production requirement:** API authentication, HMAC webhook validation

### Observability

- **Limitation:** In-memory metrics, no distributed tracing
- **Impact:** Limited debugging capability
- **Production requirement:** Prometheus, Grafana, OpenTelemetry

### Data retention

- **Limitation:** No retention policies, no archival
- **Impact:** Unbounded storage growth
- **Production requirement:** Retention policies, archival strategy

### Multi-tenancy

- **Limitation:** No customer isolation
- **Impact:** Cannot support multiple customers securely
- **Production requirement:** Tenant isolation, access controls

### Compliance

- **Limitation:** No explicit GDPR, CCPA, or HIPAA controls
- **Impact:** Cannot be used for regulated data
- **Production requirement:** Compliance controls, data residency, consent management

### Disaster recovery

- **Limitation:** No backup, no recovery procedures
- **Impact:** Data loss on failure
- **Production requirement:** Backup strategy, DR runbook, RTO/RPO targets

## What this demo proves

Despite limitations, this demo demonstrates:

1. **Domain understanding:** Workflow states, event model, retry logic
2. **Reliability patterns:** Idempotency, correlation, audit trail
3. **Observability mindset:** Structured logging, metrics, dashboards
4. **Security awareness:** Threat model, PII handling principles
5. **Operational thinking:** Handoff package, runbooks, failure modes

## Path to production

To move from demo to production:

1. Replace SQLite with PostgreSQL
2. Extract Domain Core into FastAPI service
3. Add API authentication
4. Add webhook signature validation
5. Implement proper observability stack
6. Add multi-tenancy support
7. Implement compliance controls
8. Add backup and disaster recovery
9. Performance testing and optimization
10. Security audit and penetration testing

## References

- Threat model: `threat_model.md`
- Assumptions register: ../research/assumptions_register.md
- Deployment diagram: `deployment.md`
