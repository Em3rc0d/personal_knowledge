# MK2 — Entry, Exit & Promotion Gates

Status: **BLOCKED BY MK1**

## MK2 entry gate

MK2 may become active only when MK1 provides:

- [ ] a frozen classification-schema revision;
- [ ] representative normalized records across every engineering family;
- [ ] resolved/accepted dimension overlap;
- [ ] explicit capability composition for P0 systems;
- [ ] normalized memory lifecycle fields;
- [ ] revision-aware protocol fields;
- [ ] retry/error/termination vocabulary;
- [ ] stable evidence-state semantics;
- [ ] explicit UNKNOWNs routed forward.

Until then, this directory is design scaffolding only.

## MK2 exit gate

MK2 closes only when normalized knowledge has been converted into usable operational artifacts:

- [ ] contract catalog is stable and non-duplicative;
- [ ] machine-readable schemas are versioned and validated;
- [ ] at least one fixture exists for each contract family;
- [ ] tool/side-effect/HITL/retry/termination/memory contracts have measurable acceptance criteria;
- [ ] evidence and reproducibility receipts have schemas;
- [ ] checklists link to evidence rather than acting as evidence themselves;
- [ ] deterministic validators exist for static contract rules;
- [ ] adversarial test obligations are mapped to threat-model paths;
- [ ] repeated-trial requirements are defined for stochastic claims;
- [ ] production-readiness claims require operational evidence outside documentation;
- [ ] all mandatory failures fail closed where appropriate;
- [ ] MK3 can integrate these contracts with Jett Engineering Method and project delivery without redefining them.

## Promotion semantics

MK2 may promote a rule from `candidate` to `operational contract` only when:

1. the rule maps to a stable MK1 distinction;
2. inputs/outputs and enforcement owner are explicit;
3. failure behavior is explicit;
4. acceptance criteria are measurable;
5. at least one positive and one adversarial fixture exist;
6. evidence/receipt expectations are defined;
7. the contract is framework-independent unless intentionally adapter-specific.

## Claims MK2 still cannot make by itself

Even a closed MK2 does not prove:

- cross-framework universality;
- real production reliability;
- security under every threat model;
- stable performance across model/provider changes;
- successful operation at real scale.

Those require later integration/automation/certification MKs.

## State

```text
MK2 ENTRY = BLOCKED BY MK1
MK2 DESIGN = SEEDED
MK2 IMPLEMENTATION = NOT STARTED
MK2 CERTIFICATION = NOT APPLICABLE YET
```
