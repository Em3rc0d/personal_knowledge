# MK2 — Contract Catalog

Status: **DESIGN SEED / BLOCKED BY MK1**

The catalog defines the operational contract families MK2 expects to derive from the stabilized MK1 schema.

## 1. AgentSystemContract

Purpose: describe the whole system boundary.

Expected fields:

- objective/scope;
- control-authority profile;
- topology;
- reachable capabilities;
- side-effect classes;
- state/persistence model;
- human-control model;
- budgets/termination;
- evaluation plan;
- security boundaries;
- evidence/reproducibility receipts;
- explicit unknowns.

## 2. ToolContract

Purpose: define the model/runtime-facing semantics of one tool.

Expected fields:

```text
identity / purpose
input schema
validation
authorization
risk/capability class
side-effect semantics
idempotency
error taxonomy
retryability
time/cost budget
output schema
provenance/evidence
observability receipt
```

## 3. CapabilityPolicy

Purpose: state who/what may access filesystem, network, browser, shell, database, communication, publication, memory or other capabilities.

Expected controls:

- principal/actor;
- allowed capability;
- resource/origin scope;
- credential scope;
- read/write distinction;
- environment/sandbox boundary;
- escalation path;
- denial behavior;
- receipt/audit requirements.

## 4. SideEffectPolicy

Purpose: define safe treatment of external mutations and data movement.

Expected fields:

- effect class;
- reversibility;
- preview/dry-run support;
- approval requirement;
- idempotency strategy;
- compensation strategy;
- unknown-outcome strategy;
- external receipt identifier;
- verification after execution.

## 5. HumanApprovalContract

Purpose: guarantee approval semantics where human control is required.

Expected fields:

- trigger/risk rule;
- exact proposed action/arguments;
- approval timing;
- approve/edit/reject semantics;
- revalidation after edit;
- durable approval identity;
- dispatcher enforcement;
- expiration/revocation;
- audit receipt.

## 6. RetryPolicy

Purpose: prevent model-driven retry chaos and duplicated effects.

Expected fields:

- error class;
- retry owner;
- retryable/not-retryable decision;
- max attempts;
- backoff/jitter;
- wall-clock budget;
- idempotency/verification behavior;
- unknown-outcome behavior;
- terminal escalation.

## 7. TerminationPolicy

Purpose: define both semantic completion and hard resource bounds.

Expected fields:

- success predicate;
- terminal failure predicate;
- turn budget;
- tool-call budget;
- retry budgets;
- deadline;
- token/cost budget;
- oscillation detection;
- cancellation path;
- incomplete/aborted receipt.

## 8. MemoryPolicy

Purpose: operationalize semantic memory separately from checkpoint/persistence.

Expected fields:

- semantic role;
- scope/isolation key;
- write eligibility;
- validation/provenance;
- retrieval policy;
- retention/TTL/deletion;
- correction/tombstone behavior;
- privacy/data classification;
- poisoning resistance;
- quality/evaluation metrics.

## 9. ProtocolReceipt

Purpose: make protocol assumptions versioned and reproducible.

Expected fields:

- protocol name/revision;
- host/client/server role;
- transport;
- capability negotiation/discovery;
- authentication/identity;
- extensions;
- timeout/cancellation;
- compatibility evidence.

## 10. EvidenceReceipt

Purpose: separate claims from externally inspectable proof.

Expected fields:

- claim;
- evidence type;
- source/trace/outcome identifier;
- timestamp;
- validated arguments/config;
- external result identifier;
- evaluator/grader version;
- confidence/limitations.

## 11. EvaluationPlan

Purpose: define what must be measured before promotion.

Expected layers:

- static contracts;
- unit/integration;
- trajectory/policy;
- outcome;
- repeated stochastic trials;
- latency/cost;
- adversarial/security;
- regression gates;
- production observability.

## 12. ReproducibilityReceipt

Purpose: make operational evidence replayable enough to interpret later.

Expected fields:

- code/source SHA;
- model/provider/version;
- dependency lock/versions;
- protocol/API revisions;
- environment/runtime assumptions;
- test fixture version;
- execution timestamp;
- result/evidence artifacts.

## Catalog rule

No contract becomes mandatory merely because it appears here. MK1 must first prove the underlying distinction is stable and MK2 must define measurable acceptance behavior.
