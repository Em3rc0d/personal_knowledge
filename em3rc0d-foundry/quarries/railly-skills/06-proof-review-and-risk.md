# Railly Skills — Proof, Review and Risk

Provenance: OBSERVED + INFERRED
Primary upstream: review-gate, test-strength, resilience-audit, security-review, quality-baseline

## Review Gate principle

Review Gate decides whether **one exact diff/state** is ready for human promotion.

It consumes specialized receipts instead of reimplementing Test Strength, Resilience or Security methods.

## Deterministic checks before judgment

The gate catalog is harvested from real cases and confirmed review misses.

Examples include:

- stale-value zero-hit search;
- surface sweep;
- caller sweep;
- producer sweep;
- docs sibling sweep;
- exact-head coverage;
- force-red + green control;
- shell metacharacter coverage;
- installer/runtime dependency parity;
- changed-domain matrices.

Portable principle:

    enumerate what can be enumerated;
    spend judgment only where judgment is required

A deterministic check has stable recall for its class and does not “forget” because context grew.

## Lens admission

A review lens enters the catalog only from:

- a recorded case; or
- a confirmed external-review miss.

It becomes promoted after recurrence across independent cases or a maintainer-confirmed miss under the source’s rules.

This is an important anti-theory mechanism: gates are harvested from escaped defects.

## Property vs proxy

proof-obligations.md explicitly rejects convenient proxies as final proof.

Examples:

- permissions != confidentiality;
- successful write != durability;
- PID != capability;
- final state equality != atomic visibility.

Required method:

1. name the property;
2. name the proxy;
3. construct a counterexample where proxy is true but property false;
4. observe the property at its own layer.

## Commit-point map

For durable/external side effects:

- identify commit point;
- enumerate later fallible stages;
- partition by ownership region;
- force representative failure;
- inspect residual state and cleanup;
- immediately retry the same user operation.

Writer-local cleanup does not prove caller-level rollback.

## Test Strength

A strong test must:

- have an independent oracle;
- use semantically valid fixtures;
- fail against a representative wrong implementation;
- fail at the product’s real execution seam when that differs from helper definition;
- restore to green;
- cover explicit dimensions rather than imply Cartesian coverage from examples.

Global coverage percentage is rejected as a universal target.

## Resilience

A happy path says nothing about:

- timeout after possible commit;
- cancellation;
- ambiguous retry;
- partial write;
- dependency refusal/malformed data;
- overload/backpressure;
- resource leaks;
- concurrency;
- restart/recovery.

Unavailable platform/environment remains a verification gap.

## Security

security-review keeps threat classification separate from generic reliability.

Exploitability chain:

    attacker capability
      → reachability
      → attacker control
      → trust boundary crossed
      → security impact

A secret-shaped flow is not automatically a vulnerability if the receiver already possesses equivalent authority.

A lifecycle failure is not automatically an availability vulnerability without an attacker-controlled path.

Security classification and scope are separate from final merge/promotion policy.

## High-risk independence

High-risk work needs an independent challenge source when possible:

- different model family;
- human reviewer;
- normative reference;
- independent substrate corpus.

If only sequential self-review is available, the independence gap remains explicit.

## Review Gate evolution lesson

Round 002 is unusually important.

Initial blind replication against six maintainer findings:

- 3/6 caught;
- 2/6 generated but wrongly dismissed;
- 1/6 not represented by the lens catalog.

The two wrongly dismissed findings were verification-layer mistakes.

The method was changed to require:

    refute a finding at the same layer as the claim
    verification gap != refutation

A browser-capable rerun improved the result.

Portable lesson:

    review quality is not only finding generation;
    verification can destroy correct findings if its oracle is weaker than the claim

## Quality baseline

quality-baseline is read-only and rejects generic “code smell” scoring.

A retained finding needs connection to:

- violated contract;
- failure mode;
- change-safety cost;
- measured bottleneck;
- repository rule.

Missing repo-local control cannot be generalized to “the organization has no control” without evidence.

## EM3RC0D adaptation

INSPIRED:

Create a shared Proof Model that every Foundry product can use:

- claim;
- property;
- oracle;
- exact state;
- command/observation;
- limitations;
- independent challenge when risk warrants;
- durable receipt.

Product-specific review lenses should be harvested from escaped defects and external feedback, not invented as an ever-growing checklist.
