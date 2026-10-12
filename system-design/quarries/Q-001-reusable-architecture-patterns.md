# Q-001 — System Design Notes: transferable engineering decisions

Provenance: `OBSERVED` pinned upstream text/tree + `INSPIRED` domain transfer + `GENERATED` cards. **Quarry, not canon.** Source receipt: [S-SD-001](../mining-site/S-001-system-design-notes.md).

| Candidate | Upstream chapter evidence | Independent contrast | What survives | What does not follow |
|---|---|---|---|---|
| SD-001 architectural decision | 03 framing / high-level design / targeted deep dive | [JEM architecture](../../jett-engineering-method/architecture/README.md) | options tied to measurable constraints | second independent methodology, default microservices |
| SD-002 capacity estimate | 02 assumptions, QPS and storage; 16 load example | Requirements + real telemetry required | explicitly labeled input assumptions, peak/bounds, units | copying example QPS as actual demand |
| SD-003 resilience | 10 failure/retries; 19 delivery tradeoffs; 26 payment retries | AWS Builders' Library; Martin Fowler Circuit Breaker | timeout budget, retry limits, idempotency, overload protection | unbounded retry, universal circuit breaker |
| SD-004 idempotency/consistency | 19 at-least-once; 21 dedup/reconciliation; 26 order states & settlement | Stripe API idempotent-requests **API-specific** | deduplicate side effects by business key, track state, reconcile unknown | end-to-end exactly-once assertion, provider assumptions |
| SD-005 observability | 20 metrics/alerts; 21 event integrity | Google SRE golden signals; OpenTelemetry signal model | user-impact SLIs plus operational signals and action response | deploying OTel stack/Prometheus by default |

## Preliminary project fit — hypotheses, not audits

- **PlacaClara:** SD-004/SD-005 likely useful for payment-access correctness; PSP, existing implementation and failure cases **UNKNOWN**. Pilot must remain synthetic and separate.
- **ECHO:** SD-003/SD-005 useful to frame false-positive/negative evidence and event delivery; no automatic claim that queues fix classifier robustness.
- **Prompt Machine:** SD-002/SD-003 useful for bounded job volume, retries and quota cost. Workload unknown.
- **Content Seller / NINFA:** SD-003/SD-005 potentially useful for media workflow integrity, but not a justification for messaging infrastructure.
- **Logan Garage:** SD-002 can inform SQLite capacity; no network/LLM/backend dependency is required; geospatial infrastructure **DEFERRED**, Maps URLs remains proposal.
- **Foundry / JEM:** SD-001 can improve evidence quality of architecture decisions; JEM remains canonical process owner.

## Reuse rule

Open **one** pattern on demand, replace hypothetical workload/threshold with measurements or explicitly `UNKNOWN`. Document alternative and evidence, then select `ADOPT`, `REFERENCE_ONLY`, `REJECT`, or `NEEDS_EVIDENCE`. No product edits based on quarry alone.
