# Agent Engineering — System Packages

`systems/` is the **canonical current-view layer** for concrete agent frameworks/runtimes studied by this domain.

It does not replace the evidence pipeline. It makes the current engineering understanding readable without requiring a human or LLM to reconstruct conclusions from source receipts, quarries and MK promotion history.

## Why this layer exists

The repository keeps two complementary views:

```text
EVIDENCE / HISTORY                         CURRENT SYSTEM VIEW

mining-site/                               systems/<system>/
    ↓ source receipts                          ↓ canonical synthesis
quarries/                                  architecture + classification
    ↓ processed observations                  ↓ evidence map
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
3. `systems/<system>/CLASSIFICATION.md` contains the current normalized MK classification.
4. `systems/<system>/EVIDENCE.md` maps every material conclusion back to receipts/quarries/MK decisions.
5. `systems/<system>/PROTOCOLS.md` records revision-aware interoperability separately from framework identity.
6. `systems/<system>/ENGINEERING_RULES.md` records reusable lessons and explicitly says what the system does **not** prove.
7. Quarries remain evidence, not current canon. They may preserve historical candidate states that were later promoted, qualified or closed.

## Conflict resolution

When documents appear to disagree, distinguish **current state** from **historical evidence**.

For current claims, use this precedence:

```text
STATUS.md
  ↓
systems/<system>/ current package
  ↓
active/frozen MK schema + gates
  ↓
quarries/
  ↓
mining-site/ source receipt
```

For provenance, traverse in the opposite direction until the original source/snapshot is reached.

A newer canonical synthesis may supersede the *status* of an older quarry finding, but must not erase the older evidence or reasoning trail.

## Current packages

- [`strands/`](./strands/) — Strands Agents SDK: runtime/control model, state/memory, tools, interventions, budgets, concurrency, evaluation, MCP `2026-07-28`, security boundary and remaining unknowns.

## Package admission rule

Create a system package only when the system has enough evidence to support a stable cross-document synthesis. A package is **not** an endorsement, production certification or framework ranking.
