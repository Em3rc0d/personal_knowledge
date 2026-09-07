# MK1 — Closure Gates

Status: **OPEN / IN PROGRESS**

MK1 closes only when the classification model survives pressure across materially different system families.

## Closure checklist

- [ ] every engineering family has at least one normalized classification record;
- [ ] control, capability, side-effect, state/memory and human-control axes remain framework-independent;
- [ ] P0 examples have capability-composition records;
- [ ] retries/errors/termination are normalized for representative loop families;
- [ ] memory examples use lifecycle dimensions rather than `memory=true`;
- [ ] protocol examples are revision-aware;
- [ ] multi-agent examples carry admission hypotheses and baseline/benefit fields;
- [ ] every material unknown remains explicit;
- [ ] duplicate or overlapping dimensions are resolved;
- [ ] the schema can classify a new external system without inventing a new top-level category;
- [ ] classification records distinguish architecture description from production certification;
- [ ] MK2 contract families can be derived from MK1 without reopening basic terminology disputes.

## Pressure-test questions

Before closure, ask:

1. Can a deterministic S4 workflow and an autonomous S0 research agent both be described without implying one is more mature?
2. Can generated code be represented separately from permission to execute it?
3. Can an in-memory checkpoint and a cross-session semantic memory be represented without both becoming `memory=true`?
4. Can human review exist while dispatcher enforcement remains `UNKNOWN`?
5. Can a timeout after a mutating request be represented as `unknown outcome` rather than ordinary retryable failure?
6. Can legacy MCP and current MCP implementations be differentiated by revision rather than protocol name alone?
7. Can multi-agent topology be represented without implying measured benefit?
8. Can an implementation be fully classified while still being explicitly unverified for production?

If the answer to any is no, MK1 remains open.

## Exit decision semantics

Closing MK1 will promote:

- stable vocabulary;
- orthogonal dimensions;
- classification schemas;
- normalized records and evidence-state discipline.

It will **not** yet certify operational policies. Those belong to MK2.

## State transition

```text
MK1 PASS
   ↓
freeze schema version for MK2 input
   ↓
open MK2 operationalization work
   ↓
derive contracts / schemas / checklists / test obligations
```

Until every gate closes:

```text
MK1 = IN PROGRESS
MK2 = BLOCKED
```
