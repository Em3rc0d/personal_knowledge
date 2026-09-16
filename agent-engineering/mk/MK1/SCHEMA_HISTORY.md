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

- initial tutorial-derived evidence;
- Strands Agents first pressure test.

Resolution:

Strands surfaced candidate qualifiers, but no schema change was promoted from one framework alone.

### `mk1-draft-2026-09-16.1`

State: **ACTIVE DRAFT / FREEZE CANDIDATE**  
Change type from prior draft: **ADDITIVE + CLARIFYING**

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

Cross-runtime result:

```text
concurrency semantics        PROMOTED under state
budget enforcement semantics PROMOTED under termination
intervention owner/boundary  PROMOTED under human_control
```

Why additive:

Prior records remain meaningful; newly promoted fields may remain `unknown` where evidence does not establish them.

## Pressure already survived by this draft

The current revision now classifies materially distinct families without adding framework-specific top-level axes:

```text
model-tool loop / general shell
HITL / dispatcher enforcement
trajectory vs outcome evaluation
generated-code execution + browser authority
external publication / safe mode / idempotency
data egress / confidentiality pressure
database effective authority
reflection/adaptation vs persistent improvement
state/checkpoint/persistence/memory lifecycle
MCP legacy/current revision drift
Strands modern mixed runtime
A2A 0.3 implementation vs current A2A 1.0 version drift
```

Record state:

```text
11 MATERIALIZED / QUALIFIED
2  COVERED_BY
1  OPEN → REC-012 multi-agent baseline
```

Protocol pressure:

- Strands MCP `2026-07-28` fits the protocol model with modern execution evidence;
- A2A classification-shape gate fits the same model in qualified form while preserving `0.3 → 1.0` drift and incomplete execution receipt;
- no MCP- or A2A-specific top-level category has been required.

## Still required before freeze

```text
1. materialize REC-012 from actual multi-agent baseline/admission evidence
2. run final representative-set / COVERED_BY review
3. reconcile every material OPEN_MK1 unknown
4. decide cross-dimension questions surfaced by REC-008/REC-011 and other records
5. verify no duplicated or framework-accidental fields remain
6. verify MK2 contract families map to stable MK1 semantics
7. record final schema delta and closure receipt
```

Potential freeze target:

```text
mk1-v1
```

Do not create that name until `GATES.md` + `CLOSURE_PLAN.md` pass.

## Explicit freeze questions

The final audit must decide, with evidence rather than aesthetic preference:

- whether `horizon` remains nested under control or becomes independently modeled;
- whether `data_egress` plus S0–S4 is sufficient or confidentiality/data-classification needs stronger MK1 structure;
- whether memory update-conflict/forgetting/evaluation belongs in MK1 classification or MK2 operational contracts;
- whether `sandbox` needs capability-specific qualifiers at classification depth;
- whether H0–H4 adds useful shorthand beyond enforcement-owner/boundary/dispatcher fields;
- whether evaluation fields remain sufficiently orthogonal without an ordinal maturity score;
- whether nested child-agent authority is representable without framework-specific fields.

A question may be resolved by **keeping the existing schema and routing operational detail to MK2**. More fields are not automatically better.

## Freeze procedure

1. materialize REC-012;
2. complete representative-set review;
3. close/qualify/route material UNKNOWNs;
4. run cross-dimension audit;
5. classify any proposed schema change as additive/clarifying/breaking;
6. rerun only affected records if the schema changes;
7. verify MK2 contract families map to stable fields;
8. record final diff from this active draft;
9. create MK1 `CLOSURE.md`;
10. declare the frozen revision in `STATUS.md` and MK2 handoff.

## Migration rule

If a new draft becomes necessary before closure:

- retain this revision in the ledger;
- state exactly why existing semantics failed;
- identify impacted records;
- migrate only records whose interpretation changes;
- never silently reinterpret historical pressure tests.

## Reopen rule after freeze

A frozen schema may be superseded later only when new evidence demonstrates a material classification failure, not merely because a framework introduces a new feature name.

A reopen must identify:

```text
new evidence
→ failed existing representation
→ material engineering consequence
→ proposed change type
→ impacted records/contracts
```

## LLM rule

Interpret a record against the schema revision it names. For current comparison, normalize forward only through documented additive/clarifying changes. Never infer a favorable value for an omitted historical field.
