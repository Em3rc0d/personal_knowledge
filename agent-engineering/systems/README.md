# Agent Engineering — System Packages

`systems/` is the **canonical current-view layer** for concrete agent frameworks/runtimes studied by this domain.

It does not replace the evidence pipeline. It makes the current engineering understanding readable without requiring a human or LLM to reconstruct conclusions from source receipts, quarries and MK promotion history.

Package contract: [`PACKAGE_SPEC.md`](./PACKAGE_SPEC.md).

## Why this layer exists

The repository keeps two complementary views:

```text
EVIDENCE / HISTORY                         CURRENT SYSTEM VIEW

mining-site/                               systems/<system>/
    ↓ source receipts                          ↓ current synthesis
quarries/                                  mental model + classification
    ↓ processed observations                  ↓ evidence/protocol map
mk/MK*/                                    STATUS / active gates
    ↓ normalization / promotion
STATUS.md
```

The left side answers **“how do we know?”**. The right side answers **“what do we currently know?”**.

A system package must never invent facts that do not exist in the evidence chain.

## Canonicality rules

For a concrete system/framework:

1. `systems/<system>/README.md` is the preferred human entrypoint.
2. `systems/<system>/LLM_CONTEXT.md` is the preferred machine/agent entrypoint.
3. `systems/<system>/CLASSIFICATION.md` contains the current normalized MK classification when applicable.
4. `systems/<system>/EVIDENCE.md` maps material conclusions back to receipts/quarries/MK decisions.
5. `systems/<system>/PROTOCOLS.md` records revision-aware interoperability when protocols are material.
6. `systems/<system>/ENGINEERING_RULES.md` records reusable lessons and explicitly states non-claims.
7. Quarries remain evidence/history, not current canon.

Exact requirements: [`PACKAGE_SPEC.md`](./PACKAGE_SPEC.md).

## Conflict resolution

For current claims:

```text
STATUS.md
  ↓
systems/<system>/
  ↓
active/frozen MK schema + gates + records
  ↓
quarries/
  ↓
mining-site/
```

For provenance, traverse downward until the original source/snapshot is reached.

A newer synthesis may supersede the **status** of an older finding, but must not erase the older evidence or reasoning trail.

## Current packages

- [`strands/`](./strands/) — Strands Agents SDK: runtime/control model, state/memory, tools, interventions, budgets, concurrency, evaluation, MCP `2026-07-28`, security boundary and remaining UNKNOWNs.

## Package admission rule

Create a system package only when the system has enough evidence to support a stable cross-document synthesis.

Minimum admission:

```text
source identity pinned
+ processed evidence exists
+ MK relationship exists
+ current limitations/UNKNOWNs expressible
+ evidence map can be constructed
```

A package is **not**:

- an endorsement;
- production certification;
- framework ranking;
- a reason to duplicate raw quarry content.

## Future package workflow

```text
source receipt
→ quarry/cross-source evidence
→ MK classification pressure
→ package admission check
→ systems/<system>/ current synthesis
→ record registry link
```

If a framework has too little evidence for a stable synthesis, keep it in `mining-site/` + `quarries/` until admission criteria are met.
