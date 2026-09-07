# MK2 — Operational Checklists

Status: **DESIGN SEED / BLOCKED BY MK1**

These checklists are intentionally provisional. They illustrate how normalized knowledge should become executable engineering behavior.

## Pre-build checklist

Before implementation begins:

- [ ] objective/scope is explicit;
- [ ] control authority is classified;
- [ ] capabilities and capability compositions are classified;
- [ ] side effects are classified separately from autonomy;
- [ ] trust boundaries are named;
- [ ] consequential tools have an authorization model;
- [ ] generated code/shell/browser authority has a containment strategy;
- [ ] state/checkpoint/persistence/memory are separated;
- [ ] retry owner and error taxonomy are defined;
- [ ] semantic success and hard termination budgets are defined;
- [ ] evaluation plan exists;
- [ ] protocol/API/model/dependency assumptions are versioned;
- [ ] material UNKNOWNs are accepted explicitly or block build.

## Tool readiness checklist

For every tool:

- [ ] purpose is narrow and unambiguous;
- [ ] input/output schemas are machine-validatable;
- [ ] capability/permission scope is explicit;
- [ ] side-effect class is explicit;
- [ ] validation is separate from model instruction;
- [ ] authorization is enforceable outside the prompt;
- [ ] error classes are structured;
- [ ] retryability is defined;
- [ ] timeout/unknown-outcome behavior is defined;
- [ ] idempotency or compensation exists for retryable writes;
- [ ] time/cost budgets exist;
- [ ] provenance/receipts are recorded where material.

## Consequential action checklist

- [ ] preview/draft mode exists when feasible;
- [ ] approval occurs before effect when required;
- [ ] reviewer sees the actual action/arguments being approved;
- [ ] edited arguments are revalidated;
- [ ] approval is bound to the action/version/args;
- [ ] low-level dispatcher independently enforces authorization when required;
- [ ] retry cannot silently duplicate the effect;
- [ ] post-execution evidence/receipt verifies the effect;
- [ ] cancellation/expiration semantics are defined.

## Agent-loop checklist

- [ ] semantic success predicate exists;
- [ ] terminal failures exist;
- [ ] max model turns exist;
- [ ] max tool calls exist;
- [ ] per-tool retry budgets exist;
- [ ] wall-clock deadline exists;
- [ ] token/cost budget exists when material;
- [ ] oscillation/repeated-action detection exists or is explicitly waived;
- [ ] external cancellation path exists;
- [ ] incomplete/aborted execution has a receipt/state.

## Memory checklist

- [ ] semantic role is explicit;
- [ ] scope/isolation key is explicit;
- [ ] write policy is explicit;
- [ ] provenance/validation is explicit;
- [ ] retrieval policy is explicit;
- [ ] retention/TTL/deletion is explicit;
- [ ] correction/tombstone behavior is explicit;
- [ ] private/sensitive-data handling is explicit;
- [ ] poisoning/injection controls are considered;
- [ ] memory quality can be evaluated independently of answer quality.

## Pre-release evidence checklist

- [ ] static contract validation passes;
- [ ] unit/integration tests pass;
- [ ] side-effect policy tests pass;
- [ ] trajectory/policy evals pass where material;
- [ ] outcome evals pass;
- [ ] repeated trials cover stochastic behavior;
- [ ] latency/cost budgets are measured;
- [ ] adversarial fixtures pass;
- [ ] dependency/model/protocol receipts are frozen;
- [ ] production observability plan exists;
- [ ] unresolved UNKNOWNs are listed in the release evidence.

## Checklist rule

A checked box is not evidence by itself. Every material item should reference a machine-verifiable artifact, test, receipt or explicit human review decision when MK2 becomes active.
