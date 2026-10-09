# Architecture and Trade-offs

## Streamlit interface
The Streamlit interface provides a fast demonstration surface. It is not by itself a production API, authenticated operations portal, or multi-tenant customer application.

## Mock-first provider boundary
Mock mode supports repeatable, credential-free evaluation. It does not prove live Sinch connectivity, account setup, sender registration, channel availability, production delivery, billing, or provider quotas.

## SQLite demo persistence
SQLite supports local demonstration. Production multi-instance use requires an explicit durable database choice, migrations, concurrency testing, backups, retention, and recovery procedures.

## In-process event processing
The event engine illustrates normalization, idempotency, ordering, and modeled failures. Production-scale operation requires measured capacity, durable queueing, replay/dead-letter operations, backpressure, and recovery testing.

## Optional API boundary
An API module may establish a service boundary. Its presence is not evidence it is deployed, secured, or used by the Streamlit interface.

## AI review
AI findings are advisory. Human engineering review, deterministic checks, tests, and customer fit remain necessary; AI output does not authorize production deployment.