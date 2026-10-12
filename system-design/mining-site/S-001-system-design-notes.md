# S-SD-001 — liquidslr/system-design-notes

## Identity / access / capture

| Dimension | Observation |
|---|---|
| Input pointer / resolved source | https://github.com/liquidslr/system-design-notes |
| Publisher | GitHub owner `liquidslr`; independent notes referencing Alex Xu's *System Design Interview* books |
| Source type / provenance | Public Git repository; `OBSERVED` headings/tree, `INSPIRED` transferred rules; **not OFFICIAL vendor specifications** |
| Pinned revision | `9d8388721e7231442763ad37398b8d82224aa68f` (main head checked 2026-10-12) |
| Observed at | 2026-10-12 |
| Access state | `ACCESSIBLE` |
| Capture state | `PARTIAL` (root contents, full targeted chapters, tree; not 28 full texts copied) |
| Verification state | `INCONCLUSIVE` for completeness/correctness of all notes; targeted assertions compared to primary sources where possible |
| Promotion state | `QUARRY_ONLY`; derived cards are MK1 **candidates**, not certified canon |
| License | **UNKNOWN**; no LICENSE / COPYING file visible in inspected upstream tree; do not infer permission from GitHub publicity |
| Historical limitation | Upstream README calls notes **a work in progress**; sample latencies, availability, sizing and architectures are not benchmarks or validated requirements |

## Content actually inspected

Targeted full chapters at pinned paths: `02. Back Of the Envelope Estimation/Readme.md`, `03. System Design Framework/Readme.md`, `04. Rate Limiter/Readme.md`, `10. Notification System/Readme.md`, `16. Proximity Service/Readme.md`, `19. Distributed Message Queue/README.md`, `20. Metrics Monitoring and Alerting System/README.md`, `21. Ad Click Event Aggregation/README.md`, `26. Payment System/README.md`. Root `Readme.md` and recursive tree inspected. Remaining chapters only title-screened.

Chapter links: [02](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/02.%20Back%20Of%20the%20Envelope%20Estimation/Readme.md) · [03](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/03.%20System%20Design%20Framework/Readme.md) · [10](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/10.%20Notification%20System/Readme.md) · [19](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/19.%20Distributed%20Message%20Queue/README.md) · [20](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/20.%20Metrics%20Monitoring%20and%20Alerting%20System/README.md) · [21](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/21.%20Ad%20Click%20Event%20Aggregation/README.md) · [26](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/26.%20Payment%20System/README.md).

## What this evidence supports

- The inspected notes **discuss** rough sizing, scoped design, delivery semantics, metric collection, retry/deduplication and reconciliation.
- They do **not** establish that any specific product needs queues, distributed storage, circuit breakers, exactly-once infrastructure or 99.99% SLA.
- Nothing has been copied wholesale; downstream artifacts are original commentary, checklists and synthetic test ideas, linked to upstream.

## Primary cross-checks — separate sources / separate authority

- AWS Builders' Library: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ — transient retries, bounded backoff, jitter and retry amplification. Consult current page before operationalizing.
- Martin Fowler, Circuit Breaker: https://martinfowler.com/bliki/CircuitBreaker.html — optional circuit breaking, **not necessarily present in upstream chapter**.
- Google SRE, Monitoring Distributed Systems: https://sre.google/sre-book/monitoring-distributed-systems/ — latency, traffic, errors, saturation.
- OpenTelemetry: https://opentelemetry.io/docs/what-is-opentelemetry/ — signal model; not a required dependency.
- Stripe, Idempotent Requests: https://docs.stripe.com/api/idempotent_requests — provider-specific API behavior; **not proof PlacaClara uses Stripe**.

These authoritative documents were inspected as contrasts on 2026-10-12; they do not independently verify every statement in the secondary notes, and their product/version-specific details must be rechecked upon adoption.
