# MK1 — Schema History

Status: **ACTIVE VERSION LEDGER**

## Purpose

Track why the MK1 classification schema changes, whether changes are additive/clarifying/breaking, which evidence justified them, and when a revision becomes frozen input for MK2.

A schema revision is an engineering decision, not a documentation date stamp.

## Revision semantics

```text
DRAFT      under pressure test; may change
FROZEN     accepted as MK1 output / MK2 input
SUPERSEDED retained for historical interpretation only
```

Change types:

```text
ADDITIVE    new fields; prior records remain interpretable
CLARIFYING  semantics/allowed values tightened without material migration
BREAKING    prior records require migration or reinterpretation
```

## Ledger

### Pre-versioned MK1 draft

State: **SUPERSEDED / historical**

Characteristics:

- framework-independent control/capability/side-effect/state/memory/HITL/retry/termination/evaluation/protocol/security axes established;
- did not explicitly encode enough detail for concurrency, budget enforcement boundary or intervention enforcement ownership.

Pressure source:

- initial tutorial-derived records;
- Strands Agents first pressure test.

Resolution:

Strands surfaced candidate qualifiers, but no schema change was promoted from one framework alone.

### `mk1-draft-2026-09-16.1`

State: **ACTIVE DRAFT**  
Change type: **ADDITIVE + CLARIFYING**

Added/strengthened:

```text
state.invocation_concurrency
state.writer_model
state.concurrency_conflict_semantics
state.locking

termination.*_budget_enforcement
termination.overshoot_semantics
termination.cancellation_effective_boundary

human_control.enforcement_owner
human_control.enforcement_boundary
```

Evidence basis:

- Strands Agents;
- LangGraph;
- OpenAI Agents SDK.

Cross-runtime decision:

```text
concurrency semantics        PROMOTED under state
budget enforcement semantics PROMOTED under termination
intervention owner/boundary  PROMOTED under human_control
```

Why additive:

Prior records remain meaningful; newly promoted fields can remain `unknown` until reclassified from evidence.

Additional pressure already survived:

- Strands MCP `2026-07-28` revision-aware classification;
- separation of protocol interoperability, authorization and cancellation/rollback.

Still required before freeze:

- representative record family coverage;
- A2A reproducibility receipt;
- multi-agent admission/baseline evidence;
- duplicate/overlap audit;
- UNKNOWN reconciliation;
- MK2 derivability audit.

Potential freeze target:

```text
mk1-v1
```

Do not create that name until `GATES.md` + `CLOSURE_PLAN.md` pass.

## Freeze procedure

1. materialize required representative records;
2. run cross-dimension audit;
3. close/route material UNKNOWNs;
4. classify any proposed field change as additive/clarifying/breaking;
5. re-run affected records if schema changed;
6. verify MK2 contract families map to stable fields;
7. record final diff from active draft;
8. create MK1 `CLOSURE.md`;
9. declare frozen revision in `STATUS.md` and MK2 handoff.

## Migration rule

If a breaking draft becomes necessary before MK1 closes:

- keep old revision in this ledger;
- state why existing semantics failed;
- identify impacted records;
- migrate only records whose interpretation changes;
- do not silently reinterpret old historical pressure tests.

## LLM rule

When a record names a schema revision, interpret it against that revision first.

For current comparison, normalize forward using documented additive/clarifying changes. Never assume an old omitted field had a favorable value.
