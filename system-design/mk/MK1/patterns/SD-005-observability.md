# SD-005 — Outcome-first Observability Contract

Status: `CANDIDATE / MK1 CLASSIFIED` · Class: `INSPIRED` + primary contrast.
Upstream: [chapter 20](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/20.%20Metrics%20Monitoring%20and%20Alerting%20System/README.md), [chapter 21](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/21.%20Ad%20Click%20Event%20Aggregation/README.md).
Primary: [Google SRE Four Golden Signals](https://sre.google/sre-book/monitoring-distributed-systems/); [OpenTelemetry concept](https://opentelemetry.io/docs/what-is-opentelemetry/).

## Decision rule
- State **user-visible correctness/outcome** before picking logging stack or dashboard widgets.
- Choose appropriate SLIs: latency, traffic, errors and saturation for online endpoints; correctness, processing delay, duplicates/reconciliation for async payments/events where applicable.
- For each SLI record exact event definition, numerator/denominator, sampling and time window, **data source**, target owner and action on breach.
- Preserve correlation IDs with bounded metadata; avoid cardholder data, sensitive audio, secrets, user identifiers in unrestricted logs. Keep retention and label cardinality under control.
- Alert only on a meaningful, actionable symptom and attach a runbook/owner; deduplicate repeated alerts.
- Metrics/logs/traces are possible signal types, **not mandatory deployment of OpenTelemetry, Prometheus or extra SaaS**.

## Test/falsification
Induce known negative outcomes (failed API, latency spike, duplicate event, delayed processing); show that the defined signal detects it, operators can interpret it, and signal noise/privacy remain acceptable.

## Adversarial boundary
SLIs must distinguish *eligible/confirmed events* from attempted, test, retried or duplicated events; otherwise success-rate and purchase conversion may miscount. Define denominator, excluded cohorts (sandbox/test), delay/late-data window and privacy redaction. Instrumenting a metric without a corresponding owner and actionable response is not proof of operational readiness.

## Boundary
Targets/SLOs, providers and alert thresholds are `UNKNOWN` until measured and ratified in each project. A chart without verified instrumentation proves nothing.
