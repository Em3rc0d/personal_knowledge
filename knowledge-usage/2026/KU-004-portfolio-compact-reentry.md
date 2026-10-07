# KU-004 — Portfolio compact re-entry

Date: 2026-10-07  
Consumer: `EM3RC0D Foundry / DOGFOOD-002 F2`  
Outcome: `HELPED`  
Confidence: `medium-high`

## Problem

Determine whether DOGFOOD-002 could recover the current portfolio state and next safe action from compact state plus drift-prone external confirmation, without replaying project history.

## Knowledge used

- `DOGFOOD-002-STATE.json`;
- PR #39 current state;
- exact PR hosted-check state.

## What was reused

The compact state preserved:

- source identity;
- user branch constraint;
- safe mutation branch;
- exact changed file;
- PR identity;
- merge authority boundary.

Fresh external verification only needed to update the drift-prone PR/check fields.

## Result

Recovered:

```text
PR #39
OPEN
READY FOR REVIEW
MERGEABLE

Portfolio CI
PASS

V2 Experience Quality
PASS

runtime changes
NONE

next safe action
HUMAN REVIEW / PROMOTION
```

No new implementation task was justified.

## Work avoided

```yaml
product_history_replay_avoided: true
design_history_replay_avoided: true
runtime_source_reopen_avoided: true
new_feature_work_avoided: true
time_saved: UNKNOWN
```

This was not an independently timed fresh-session benchmark.

## Interpretation

This supports a bounded claim:

> compact exact-state artifacts can reduce the amount of deep project context required for safe re-entry when only a small set of external fields are drift-prone.

It does not yet prove quantitative compounding.

## Disposition

- `KEEP` — compact exact-state re-entry.
- `KEEP` — revalidate drift-prone external surfaces rather than all history.
- `KEEP` — human promotion as valid terminal boundary.
- `NO_CHANGE` — no new schema required from this case.


## Promotion addendum

The human-promotion boundary was later crossed. This confirms that the compact routing path can terminate in an authorized merge, but it does not convert this receipt into a timed recovery benchmark.

A later promotion feedback loop found the static-current-SHA problem and corrected it separately; KU-004 remains scoped to context recovery and routing.
