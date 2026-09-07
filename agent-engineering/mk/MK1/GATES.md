# MK1 — Closure Gates

Status: **OPEN / IN PROGRESS**

MK1 closes only when the classification model survives pressure across materially different system families and at least one genuinely independent external system family.

## Closure checklist

- [x] every engineering family has at least one normalized classification record;
- [ ] control, capability, side-effect, state/memory and human-control axes remain framework-independent under broader independent-source pressure;
- [x] all nine MK0 P0 call-path examples have normalized capability-composition records;
- [x] retries/errors/termination are normalized for representative loop and mutation families;
- [x] memory examples use lifecycle dimensions rather than `memory=true`;
- [x] protocol examples are revision-aware;
- [ ] multi-agent examples cover both deterministic multi-role and dynamic delegation while carrying admission hypotheses/baselines;
- [x] material unknowns are explicit in the current record set;
- [ ] duplicate or overlapping dimensions remain resolved after the next pressure-test set;
- [x] the schema classified an external source (`Agent_Memory_Techniques`) without inventing a new top-level category;
- [x] classification records distinguish architecture description from production certification;
- [ ] MK2 contract families can be derived from a schema frozen after remaining pressure tests without reopening basic terminology disputes.

## Evidence for closed gates

### Engineering-family coverage

R-001..R-016 cover:

- deterministic single-step generation/conversation;
- graph/workflow orchestration;
- model-tool loop;
- retrieval/document processing;
- memory/state;
- evaluation/critic infrastructure;
- generated code/browser;
- external mutation/communication/publication/data egress;
- database authority;
- multi-role/multi-agent presentation;
- protocol integration.

### P0 coverage

The nine MK0 P0 call paths are represented by:

- R-004 E2E;
- R-005 self-healing;
- R-001 shell loop;
- R-006 HR messaging;
- R-007 social publishing;
- R-014 ShopGenie email;
- R-008 document intake;
- R-009 DataScribe;
- R-015 Car Buyer browser.

### External-source test

R-016 classifies `Agent_Memory_Techniques` Conversation Buffer Memory using existing axes. No schema extension was necessary.

## Material schema changes produced by pressure testing

1. `side_effects.class` became separate `observed_class` and `reachable_class`;
2. capability booleans gained explicit `unknown` values;
3. topology gained `deterministic_multi_role` so model count does not imply dynamic control;
4. a `multi_agent` admission block was added for hypothesis/baseline/benefit/coordination evidence.

See [`PRESSURE_TESTS.md`](./PRESSURE_TESTS.md).

## Pressure-test questions

Before closure, ask:

1. Can a deterministic S4 workflow and an autonomous S0 research agent both be described without implying one is more mature? **YES in current set.**
2. Can generated code be represented separately from permission to execute it? **YES.**
3. Can an in-memory checkpoint and a cross-session semantic memory be represented without both becoming `memory=true`? **YES for in-process cases; durable cross-session case still required.**
4. Can human review exist while dispatcher enforcement remains `UNKNOWN`? **YES: R-006.**
5. Can a timeout after a mutating request be represented as `unknown outcome` rather than ordinary retryable failure? **SCHEMA YES; dedicated real case still required.**
6. Can legacy MCP and current MCP implementations be differentiated by revision rather than protocol name alone? **YES: R-013.**
7. Can multi-agent topology be represented without implying measured benefit? **YES: R-012; dynamic delegation still pending.**
8. Can an implementation be fully classified while still being explicitly unverified for production? **YES throughout current records.**

## Remaining closure blockers

- C1 model-routed example;
- C3/open-horizon example;
- dynamic multi-agent delegation example;
- durable cross-session memory example;
- authenticated transactional browser example;
- explicit unknown-outcome mutation/reconciliation example;
- production-oriented external source pressure;
- at least one independent source/framework outside the NirDiamant corpus;
- final dimension-overlap review and schema freeze.

## Exit decision semantics

Closing MK1 will promote:

- stable vocabulary;
- orthogonal dimensions;
- classification schema revision;
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
