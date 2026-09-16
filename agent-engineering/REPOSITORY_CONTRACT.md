# Agent Engineering — Repository Contract

Status: **CANONICAL STRUCTURE CONTRACT**  
Applies to: `agent-engineering/`

## Purpose

This document defines **where knowledge belongs, which artifact is authoritative for which question, how knowledge changes state, and how humans/LLMs must resolve apparent conflicts**.

The repository is intentionally not a flat notes collection. It separates:

- current state;
- current system-specific synthesis;
- normalized domain semantics;
- processed evidence;
- source provenance;
- historical reasoning;
- future operationalization.

The goal is to make the repository understandable without sacrificing traceability.

## Authority model

No single file is authoritative for every question.

| Question | Authority |
|---|---|
| What is active/closed/blocked now? | `STATUS.md` |
| What do we currently know about a concrete system? | `systems/<system>/` |
| What is the current framework-independent taxonomy/schema? | active/frozen `mk/MK*/` package |
| What evidence produced a conclusion? | `quarries/` |
| What exact source/snapshot was inspected? | `mining-site/` |
| What cross-system architectural constraint exists? | `architecture/` |
| What work should happen next? | `ROADMAP.md` + active MK closure plan |
| What will the next MK receive? | next MK handoff contract |

## Current-state precedence

When historical documents and current synthesis differ because knowledge evolved:

```text
STATUS.md
  > systems/<system>/
  > active/frozen MK schema + gates + unknowns
  > quarries/
  > mining-site/
```

This precedence applies only to **current interpretation**.

It does not mean a higher-level synthesis is stronger provenance than the original source.

## Provenance traversal

For evidence questions, traverse downward:

```text
current claim
  ↓
MK decision / gate
  ↓
processed quarry / cross-source synthesis
  ↓
source receipt
  ↓
pinned upstream source/spec/test
```

A current synthesis must never manufacture provenance.

## Folder contracts

### `systems/`

Role: **current system-specific synthesis**.

A package represents what the domain currently knows about one concrete framework/runtime/system after reconciling evidence and MK decisions.

It is not:

- raw research;
- an endorsement;
- a benchmark ranking;
- a production certificate;
- a substitute for source receipts.

Package requirements are defined in [`systems/PACKAGE_SPEC.md`](./systems/PACKAGE_SPEC.md).

### `mk/`

Role: **maturity pipeline and framework-independent domain canon**.

An MK may contain:

- schemas;
- normalized dimensions;
- promotion/closure gates;
- UNKNOWN registers;
- decision receipts;
- handoff artifacts.

A later MK must not silently rewrite the historical meaning of an earlier MK. State transitions are recorded explicitly.

### `quarries/`

Role: **processed evidence and reasoning history**.

Quarries may preserve:

- candidates later promoted;
- UNKNOWNs later closed;
- contradictions;
- failed hypotheses;
- source-specific observations.

Therefore a quarry can be historically correct while stale as a current-state summary.

### `mining-site/`

Role: **source identity and provenance**.

Every important external source should record, when applicable:

- source ID;
- repository/spec URL;
- exact snapshot/revision;
- observation date;
- source authority;
- license/reuse boundary;
- relation to quarries/current synthesis.

### `architecture/`

Role: **cross-system architectural artifacts**.

Use for material that is not specific to one framework and is broader than one MK record, such as threat models or system boundary models.

## Knowledge states

The repository distinguishes two independent vocabularies.

### Reasoning state

```text
SOURCE_CLAIM
OBSERVED
INFERRED
SUPPORTED
QUALIFIED
CONTRADICTED
UNKNOWN
```

### Provenance state

```text
OFFICIAL
OBSERVED
INFERRED
INSPIRED
GENERATED
```

Do not replace either vocabulary with vague confidence wording.

## Change transaction

A material knowledge update should normally follow:

```text
1. pin new source/revision
2. update/add source receipt
3. process evidence in quarry
4. compare with current MK semantics
5. pressure-test schema changes when required
6. update system package if current understanding changed
7. update GATES / UNKNOWNS / record registry
8. update STATUS and ROADMAP only if state changed
9. preserve superseded reasoning as history
```

Not every update needs every step. The chain must be proportional to claim risk.

## No silent state promotion

Forbidden transitions without explicit evidence/gate:

```text
source claim       → fact
implemented        → verified
verified once      → reliable
framework feature  → application property
protocol support   → authorization
cancellation       → rollback
persistence        → concurrency safety
structured output  → semantic correctness
multi-agent        → superior performance
SDK production docs→ production-ready application
```

## Duplication rule

Duplication is acceptable only when the copies have **different epistemic roles** and link to each other.

Good duplication:

```text
quarry observation
→ normalized MK field
→ current system synthesis
```

Bad duplication:

```text
three independent files each pretending to be the current source of truth
```

When adding a new document, state what question it owns.

## Historical preservation rule

Do not delete or rewrite a historical receipt merely because its conclusion evolved.

Instead:

1. preserve the original observation;
2. mark its historical state;
3. add a resolution pointer;
4. update the current synthesis;
5. update navigation so retrieval does not mistake the old state for current truth.

## Human-readable requirement

Every major package must expose:

- purpose;
- current status;
- what is known;
- what is not known;
- where evidence lives;
- what happens next.

Readers should not need to understand repository history before understanding the current model.

## LLM-readable requirement

Every machine-oriented entrypoint must expose:

- canonical file precedence;
- safe facts;
- prohibited inferences;
- freshness triggers;
- UNKNOWNs;
- exact paths for deeper evidence.

An LLM should retrieve the smallest sufficient canonical context first, then descend into evidence only when needed.

## Versioning rule

Schemas and frozen contracts use explicit revisions.

A revision change must declare whether it is:

```text
additive      — old records remain interpretable
clarifying    — semantics tightened without changing shape materially
breaking      — old records require migration
frozen        — accepted as input to next MK
```

Schema history for MK1 lives in [`mk/MK1/SCHEMA_HISTORY.md`](./mk/MK1/SCHEMA_HISTORY.md).

## Closure rule

An MK closes because its acceptance criteria are satisfied, not because documentation looks complete.

A closure decision requires:

- gate status;
- unresolved UNKNOWN routing;
- frozen input/output revision where relevant;
- explicit next-MK handoff;
- no hidden blocker disguised as future cleanup.

## Current domain contract

```text
MK0 = CLOSED
MK1 = ACTIVE
MK2 = BLOCKED / DESIGN SEEDED

current MK1 schema = mk1-draft-2026-09-16.1
current complete system package = systems/strands/
```

For live status, defer to [`STATUS.md`](./STATUS.md).
