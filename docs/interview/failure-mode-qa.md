# Failure-Mode Q&A

Present only scenarios currently implemented in `src/resilience/scenarios.py`; confirm the list before recording.

## Provider timeout
Explain the modeled timeout and only the retry/fallback behavior implemented in the current workflow. Discuss timeout budgets, safe retry semantics, duplicate-send risk, and correlation across attempts.

## Rate limit
Explain modeled rate-limit handling. It is not a provider quota or throughput guarantee. Discuss quotas, backoff, concurrency, queue depth, and alert thresholds.

## Duplicate or out-of-order callback
Explain the event engine's idempotency and ordering policy and point to tests. Discuss provider event identifiers, replay windows, durable deduplication, and reconciliation.

## Webhook, persistence, queue, or CRM failure
Use only scenarios present in the simulator. Describe the simulated result, then discuss durable receipt, replay, dead letters, downstream idempotency, recovery ownership, and integrity tests as production follow-up.

## Is this production-ready?
“No. It is a locally tested reference/demo. It demonstrates patterns, but provider behavior, customer-specific controls, capacity, compliance, live operations, and on-call ownership require separate evidence.”