# DOGFOOD-002 — F3 Public Claim Audit

Date: 2026-10-07  
Target: `Em3rc0d/em3rc0d-portfolio`  
Mode: **READ-ONLY SOURCE-OF-TRUTH AUDIT + ONE BOUNDED CLAIM CORRECTION**  
Verdict: **PARTIAL PASS — 1 MATERIAL DRIFT FOUND**

## Question

Do the current public flagship claims remain below or equal to the current evidence in their source projects?

## Current runtime flagship routing

At portfolio `main@514e9acea5ae1692c62ccfd86f0eace7ed886357`:

```text
PlacaClara
AutoPulse
ECHO
```

The portfolio's `PROJECT_STATE.md` had stale routing and is already addressed separately in PR #39.

## Audit result

### PlacaClara — KEEP

Portfolio claim:

- live public product;
- provider-backed vehicle report;
- payments/report/delivery boundaries;
- SEO and first-party analytics.

Current external/source evidence:

- PlacaClara `main@9f6797c766945119f0203092b9772b030e72e019`;
- Vercel production deployment `dpl_2coNxjFHy5LKpzvCvmLBrcmoyXvk`;
- deployment state `READY`;
- deployment source is exact `main@9f6797c...`;
- current repo documents payment/provider/report/analytics implementation and explicit limitations.

Result:

`NO MATERIAL CLAIM CORRECTION REQUIRED`

Historical BUILD-STATUS text from 2026-09-28 said SEO/funnel promotion was still pending, but current Vercel evidence supersedes that old operational state. Do not downgrade a current claim from stale documentation when newer executable deployment evidence exists.

### AutoPulse — KEEP

Portfolio claim:

- field-tested foundation / active R&D;
- selected vehicle/adapter evidence;
- durable local sessions;
- no universal compatibility/public-release claim.

Current AutoPulse source states:

- local-first v1;
- physical Logan and Duster evidence;
- RC4 code/CI for Off-Road isolation and clean Stop semantics;
- physical RC4 retest still pending;
- public v1 not certified.

Result:

`NO MATERIAL CLAIM CORRECTION REQUIRED`

The portfolio already stays below the current source claim ceiling.

### ECHO — CORRECT

Portfolio claim before correction:

- `MVP runtime active`;
- replay/MQTT path being exercised.

Canonical ECHO current state:

```text
MK0                               CERTIFIED
MK1 spec/design/architecture      CLOSED_FOR_BUILD
Corpus readiness                  BLOCKED_FAIL_CLOSED
Coverage                          FAIL / 16 empirical gaps
CERT-MK1-DF-CORPUS-001            OPEN
modeling_allowed                  false
Benchmark A/B/C                   LOCKED
replay progression                BLOCKED
real-camera progression           BLOCKED
```

Result:

`PUBLIC CLAIM > CURRENT EVIDENCE`

Safe correction branch:

`foundry/dogfood002-echo-claim-sync`

Exact head:

`071c3d600a38ebbd746dc840f9feff85269524b7`

Changed file:

`src/content/systems/echo.ts`

Draft PR:

`Em3rc0d/em3rc0d-portfolio#40`

The correction keeps the architectural/runtime contracts visible but stops presenting them as executed MVP runtime proof.

## Foundry behavior under pressure

This audit exercised three different dispositions:

```text
newer executable evidence > stale old doc
        → KEEP PlacaClara claim

current source evidence matches bounded public claim
        → KEEP AutoPulse claim

public claim exceeds current canonical source
        → CORRECT ECHO claim
```

A claim audit must therefore support **KEEP**, not merely search for edits.

## What this supports

- source-of-truth precedence matters;
- fresh executable/provider evidence may legitimately supersede stale operational docs;
- public portfolio claims should be bounded by source-project evidence;
- claim correction can be isolated from product-source mutation.

## What this does not support

- complete audit of every portfolio case;
- independent certification of PlacaClara or AutoPulse;
- production promotion of PR #40;
- any change to ECHO itself;
- a universal claim-scoring system.

## Next boundary

PR #40 must pass existing portfolio gates.

If green, human review/promotion is the next boundary.

No merge is authorized by this receipt.
