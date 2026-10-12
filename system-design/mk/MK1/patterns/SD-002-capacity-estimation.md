# SD-002 — Capacity Estimation with Assumption Ledger

Status: `CANDIDATE / IN REVIEW` · Class: `INSPIRED` + `GENERATED`.
Source: [chapter 02](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/02.%20Back%20Of%20the%20Envelope%20Estimation/Readme.md).

## Use when
Choosing hosting, storage, API quotas, job batching, retention or estimating cost. Not required as an artificial step for every small feature.

## Input ledger (each `MEASURED` / `ASSUMED` / `UNKNOWN`)
- Active users per day `U`; operations per active user/day `O`; peak-to-average multiplier `P`.
- Payload bytes/event `B`; retention days `D`; replication/backup overhead `R`.
- Unit price, free tier conditions, provider quotas and region **version-checked**.
- Availability/latency targets only if derived from actual product need.

## Derivations (unit-bearing, no guessed production traffic)
- Average requests/s = `U × O / 86400`.
- Peak requests/s (scenario, not measurement) = `average × P`.
- Raw logical storage (bytes) = `U × O × B × D`; physical = raw × `R` + index/metadata overhead.
- Monthly cost = sum of applicable volume × price tier + fixed charges, with a range and unit verification.

## Decision/test
Perform dimensional check, independent second calculation and low/base/high sensitivity. Record whether cost or capacity alters the architectural choice. If `P`, `R` or price are unknown, **display unknown/scenario**—do not silently set a typical multiplier or claim a vendor SLA.

## Anti-pattern
Using the chapter's illustrative Twitter/SaaS latency figures as benchmark or budget for a current product. Measure deployment-specific latency instead.
