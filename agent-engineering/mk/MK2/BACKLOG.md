# MK2 — Backlog

Status: **BLOCKED / QUEUED**

This backlog becomes executable only after MK1 closes.

## P0 — Operational contracts

- [ ] freeze `AgentSystemContract` v0.x from MK1 schema;
- [ ] define `ToolContract` with typed validation/errors/permissions;
- [ ] define `CapabilityPolicy` including capability composition;
- [ ] define `SideEffectPolicy` with preview/live, idempotency and verification;
- [ ] define dispatcher-enforced `HumanApprovalContract`;
- [ ] define `RetryPolicy` including timeout-unknown-outcome behavior;
- [ ] define `TerminationPolicy` with semantic + resource limits;
- [ ] define `EvidenceReceipt` and `ReproducibilityReceipt`.

## P1 — Memory / protocols / evaluation

- [ ] define `MemoryPolicy` lifecycle schema;
- [ ] define `ProtocolReceipt` with revision/role/capabilities/auth;
- [ ] define `EvaluationPlan` schema;
- [ ] map memory poisoning/privacy fixtures;
- [ ] map protocol discovery-vs-authorization fixtures;
- [ ] define repeated-trial evidence requirements.

## P1 — Validators

- [ ] schema validator for contract records;
- [ ] static check for missing side-effect classification;
- [ ] static check for mutating tools without idempotency/unknown-outcome strategy;
- [ ] static check for approval-required actions without dispatcher binding;
- [ ] static check for loops without hard budgets;
- [ ] static check for unversioned protocol receipts;
- [ ] static check for unresolved material UNKNOWNs hidden as null/default values.

## P2 — Fixtures/templates

- [ ] safe read-only tool fixture;
- [ ] idempotent mutating tool fixture;
- [ ] approval/edit/reject fixture;
- [ ] generated-code containment fixture;
- [ ] browser origin-restriction fixture;
- [ ] checkpoint/replay fixture;
- [ ] memory lifecycle fixture;
- [ ] outcome-vs-trace eval fixture;
- [ ] multi-agent baseline comparison fixture.

## P2 — Integration handoff preparation

- [ ] map MK2 contracts to Jett Engineering Method gates;
- [ ] map evidence receipts to build/test/prove lifecycle;
- [ ] define adapter boundary for framework-specific implementations;
- [ ] define migration/versioning process for contract schemas.

## Work-in-progress rule

Do not implement the entire backlog simultaneously. Once MK2 opens, select the smallest vertical contract slice that can be specified, tested and reviewed end-to-end.
