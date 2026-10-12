# MK0 — 28-chapter screening inventory

Source: [liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes/tree/9d8388721e7231442763ad37398b8d82224aa68f), `main@9d8388721e7231442763ad37398b8d82224aa68f`; observed 2026-10-12. Inventory is verified against the root table of contents and repository tree. **Titles alone do not verify technical details.** Detailed inspection: chapters 02, 03, 04, 10, 16, 19, 20, 21 and 26; other rows are title-only triage, not full-content audit.

| # | Chapter | Disposition | Basis / boundary |
|---|---|---|---|
| 01 | Scaling | `REFERENCE_ONLY` | Capacity context; not a scale requirement |
| 02 | Back-of-the-Envelope Estimation | `P0_EXTRACTED` | Quantified assumptions, units, QPS and storage |
| 03 | System Design Framework | `P0_EXTRACTED` | Decision framing and critical deep dive |
| 04 | Rate Limiter | `P1_REFERENCE` | Algorithm choice contingent on actual abuse and workload |
| 05 | Consistent Hashing | `DEFER` | Distributed partitioning not justified |
| 06 | Key-Value Store | `DEFER` | Distributed storage not justified |
| 07 | Unique-ID Generator | `REFERENCE_ONLY` | Collision/domain decision when required |
| 08 | URL Shortener | `DEFER` | Domain-specific example; no immediate reuse |
| 09 | Web Crawler | `DEFER` | Domain-specific and compliance-intensive |
| 10 | Notification System | `P0_SUPPORT` | Failure paths and delivery evidence |
| 11 | News Feed System | `DEFER` | Scale-specific fanout |
| 12 | Chat System | `DEFER` | Realtime-state complexity |
| 13 | Search Autocomplete | `DEFER` | Specialized indexes |
| 14 | YouTube | `DEFER` | Video platforms at scale |
| 15 | Google Drive | `DEFER` | Sync and object storage at scale |
| 16 | Proximity Service | `P2_REFERENCE` | Maps URLs first for Logan Garage |
| 17 | Nearby Friends | `DEFER` | Continuous location not needed |
| 18 | Google Maps | `DEFER` | Map infrastructure not needed |
| 19 | Distributed Message Queue | `P0_SUPPORT` | At-least-once, ordering, duplicate semantics |
| 20 | Metrics Monitoring and Alerting System | `P0_EXTRACTED` | Telemetry pipeline and alert reliability |
| 21 | Ad Click Event Aggregation | `P0_SUPPORT` | Deduplication, delayed events and reconciliation |
| 22 | Hotel Reservation System | `REFERENCE_ONLY` | Concurrency and inventory reservation concept |
| 23 | Distributed Email Service | `P1_REFERENCE` | Delivery semantics, bounce/feedback |
| 24 | S3-like Object Storage | `DEFER` | Storage internals not justified |
| 25 | Real-time Gaming Leaderboard | `DEFER` | High-volume ranked stream not needed |
| 26 | Payment System | `P0_EXTRACTED` | Payment lifecycle, idempotency, reconciliation |
| 27 | Digital Wallet | `REFERENCE_ONLY` | Ledger concepts; not general payment requirement |
| 28 | Stock Exchange | `DEFER` | Matching/ordering domain-specific |

## Decision semantics

- `P0_EXTRACTED`: core bounded insight used in an MK1 candidate; not production certified.
- `P0_SUPPORT`: inspected supporting material only, not a standalone production rule.
- `P1_REFERENCE` / `P2_REFERENCE` / `REFERENCE_ONLY`: keep pointer, consult only on relevant problem.
- `DEFER`: no extraction now, not a judgment of chapter quality.

## Deferred work

No Kafka, sharding, distributed cache, microservices, multi-region database, queue or vendor SDK is authorized by this inventory. Benchmark figures in the notes are illustrative/historical; obtain contemporary environment-specific measurements before estimating production requirements.
