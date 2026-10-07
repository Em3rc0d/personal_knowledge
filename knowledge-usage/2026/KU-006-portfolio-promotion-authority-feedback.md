# KU-006 — Portfolio promotion authority feedback

Date: 2026-10-07  
Consumer: `EM3RC0D Foundry / DOGFOOD-002 promotion`  
Outcome: `HELPED`  
Confidence: `high`

## Problem

After promoting the portfolio state-sync and claim-correction PRs, determine whether the new current-state documentation remained truthful under the actual deployment lifecycle.

## What happened

PR #39 wrote an exact SHA/deployment as **current production authority**.

That was accurate at the observation boundary.

But merging the documentation changed `main`, and Vercel automatically deployed the new `main`.

After PR #40, current production had already advanced to:

```text
main@5a0da2dd633d47530e8d88150428e717584480d6
Vercel dpl_GLF9anbhs8uKatu92iBMdoyYFdbs
READY
```

while the static document still called an older exact identity “current”.

The problem was not bad evidence. It was an **authority model that could self-invalidate when observed state changed because of the observation's own merge**.

## Knowledge reused

- exact-state evidence;
- historical/current separation;
- claim <= evidence;
- minimal mutation;
- external operational truth outranks stale prose.

## Correction

PR #41: `foundry/dogfood002-production-authority-model`

Exact head:

`210d0937a5b3190bd7092f9dec5b812fc247ad09`

Verification:

- Portfolio CI `37700520889` — PASS;
- V2 Experience Quality `37700520851` — PASS.

Merged as:

`c898d743817d0fc6b8d9548444b166810c76ce83`

Final observed production:

- GitHub `main@c898d743817d0fc6b8d9548444b166810c76ce83`;
- Vercel `dpl_4r3uvZA3nMbJFfiTXbFzha5pHX3G`;
- state `READY`;
- deployment source exactly `c898d743...`.

## Knowledge returned

Candidate rule:

> Static repository documents may pin exact identities as observations, but a mutable concept such as **current deployment authority** should be resolved from the live authority surface rather than encoded as a perpetual exact SHA.

This is narrower than “never record SHAs”. Exact identities remain essential for receipts, audits and historical proof.

```text
receipt / observation
→ pin exact SHA

current mutable authority
→ resolve live
→ optionally record last observed snapshot
```

## Work avoided

```yaml
infinite_sha_chasing_avoided: true
runtime_code_change_avoided: true
manual_production_mutation_avoided: true
existing_branch_mutation_avoided: true
time_saved: UNKNOWN
```

## Interpretation

This receipt is evidence that real promotion fed a failure mode back into the knowledge system and changed the abstraction.

That is stronger compounding evidence than merely producing another document, but it still does not quantify time savings.

## Disposition

- `KEEP` — exact identities for receipts/history.
- `KEEP` — resolve mutable current authority from live surfaces.
- `SIMPLIFY` — do not maintain a manually chased permanent current SHA.
- `NO_CHANGE` — no automation required yet.
