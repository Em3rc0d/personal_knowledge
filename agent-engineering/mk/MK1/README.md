# MK1 — Normalize & Classify

Status: **OPEN / IN PROGRESS**

Precondition: MK0 Mine & Frame has enough evidence to classify new systems without trusting framework or marketing labels.

## Mission

Turn the mined agent corpus into a **framework-independent classification model** that is:

- orthogonal where possible;
- explicit about authority and side effects;
- explicit about state/memory/persistence;
- explicit about retries/termination/evaluation;
- version-aware for protocols/integrations;
- capable of preserving `UNKNOWN` instead of forcing a label;
- useful to later MK2 contracts, checklists and automated tests.

MK1 is not yet operational policy. It normalizes vocabulary and architecture descriptions.

## Core rule

> Classify what the system can actually decide and do, not what the repository/framework calls it.

A single system can be:

- deterministic in one stage;
- model-routed in another;
- model-directed for tool selection;
- human-gated for writes;
- stateless at the model boundary while durably checkpointed in runtime.

Therefore a one-dimensional `agent_type` is insufficient.

---

## 1. Classification record

Every representative system should be expressible with this shape:

```yaml
identity:
  name:
  source:
  snapshot:
  evidence_state: observed | source_claim | inferred | unknown

control:
  primary_authority: deterministic | model_routed | model_directed | mixed
  horizon: single_step | bounded_multistep | open_ended
  topology: single_model | router_workers | manager_workers | peers | mixed
  model_count:

capabilities:
  reads: []
  writes: []
  generated_code_execution: false
  shell: false
  browser: none | read_only | transactional | general
  database: none | read_only | write_capable
  communication: none | draft | external_send
  publication: none | draft | live
  file_egress: false
  capability_compositions: []

state:
  runtime_state: none | transient | structured
  checkpointing: none | memory | durable
  persistence_backend:
  replay_semantics: known | partial | unknown

memory:
  semantic_role: []
  scope: none | session | cross_session | user | project | shared
  persistence: none | process | local_durable | remote_durable
  retrieval_policy:
  write_policy:
  isolation_key:
  retention_policy:
  provenance:

human_control:
  mode: none | review_after | approval_before | edit_before | mixed
  dispatcher_enforcement: yes | no | unknown
  approval_binding:

errors_and_retries:
  error_model: prose | structured | mixed | unknown
  retry_owner: model | tool | runtime | mixed | none
  retry_budget:
  idempotency:
  unknown_outcome_handling:

termination:
  success_predicate:
  terminal_failure_predicate:
  turn_budget:
  tool_budget:
  time_budget:
  cost_or_token_budget:
  oscillation_detection:
  cancellation:

evaluation:
  static_contracts: []
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols:
  - name:
    revision:
    role:
    transport:
    capabilities:
    auth_model:
    extensions:

security:
  trust_boundaries: []
  least_privilege: yes | no | partial | unknown
  sandbox: none | process | container | vm | managed | unknown
  data_classification:
  receipts:

reproducibility:
  model_receipt:
  dependency_receipt:
  external_api_receipt:
  execution_evidence:

unknowns: []
```

No implementation is required to populate every field. Missing material facts remain `unknown`.

---

## 2. Control-authority normalization

### C0 — Deterministic

Code selects the next operation. LLM may transform/classify content but does not control the execution path.

### C1 — Model-routed

Code defines a bounded set of routes; the model selects among them.

### C2 — Model-directed bounded agent

The model repeatedly selects tools/actions based on observations, but runtime budgets bound the loop.

### C3 — Model-directed open-horizon agent

The model can continue acting until a semantic objective or external cancellation terminates execution. This class demands the strongest termination/evaluation evidence.

### C4 — Mixed / nested

Different subgraphs use different control-authority levels.

These classes describe **control**, not maturity.

---

## 3. Capability normalization

Risk derives from reachable capabilities and their composition.

### Capability families

```text
GENERATION
RETRIEVAL
FILESYSTEM_READ
FILESYSTEM_WRITE
DATA_EGRESS
DATABASE_READ
DATABASE_WRITE
EXTERNAL_COMMUNICATION
PUBLICATION
BROWSER_READ
BROWSER_TRANSACTION
SHELL
GENERATED_CODE
FINANCIAL_OR_IRREVERSIBLE_MUTATION
MEMORY_READ
MEMORY_WRITE
DELEGATION
```

### Important rule

A read-like label can hide a consequential capability:

```text
document conversion
 = local read + external upload + remote processing
```

A browser used for scraping may be read-only today but still sits on an R4-capable substrate if future code exposes arbitrary authenticated actions.

---

## 4. Side-effect normalization

```text
S0 none
S1 local/reversible artifact
S2 external but reversible/draft
S3 external consequential mutation
S4 irreversible/high-impact mutation
```

Side-effect class is independent of control authority.

A deterministic system can have S4 side effects; a highly autonomous research agent can remain S0/S1.

---

## 5. State / checkpoint / memory normalization

### Runtime state

Facts needed for current execution.

### Checkpoint

Serialized runtime state at an execution boundary.

### Persistence

Durability mechanism for state/checkpoints.

### Memory

Information intentionally retained and recalled under a lifecycle/retrieval policy.

### Knowledge/RAG

External source material retrieved because it may answer the task.

### Rule

Never infer semantic memory merely because a framework object is named `MemorySaver`.

---

## 6. Human-control normalization

```text
H0 none
H1 review after effect
H2 approval before effect
H3 approval/edit before effect + revalidation
H4 dispatcher-enforced authorization receipt
```

`H4` is the strongest pattern because orchestration bypass does not bypass the policy boundary.

Human review in one node does not imply every consequential tool in the graph is protected.

---

## 7. Retry normalization

### Retry owner

- model-selected;
- tool-local;
- runtime/orchestrator;
- provider SDK;
- mixed.

### Error class

```text
INVALID_INPUT
POLICY_DENIED
AUTHENTICATION
AUTHORIZATION
NOT_FOUND
CONFLICT
RATE_LIMIT
TRANSIENT_UPSTREAM
TIMEOUT_KNOWN_FAILURE
TIMEOUT_UNKNOWN_OUTCOME
INTERNAL
UNKNOWN
```

### Rule

A prose string such as `temporarily unavailable, try again` is not a retry contract.

Mutation retries require idempotency or a compensating/verification strategy.

---

## 8. Termination normalization

Do not reduce termination to `max_turns` or framework recursion limit.

Record separately:

- semantic success;
- terminal failure;
- model-turn cap;
- tool-call cap;
- per-tool retry budget;
- wall-clock deadline;
- token/cost budget;
- repeated-state/action detection;
- external cancellation.

A hard cap is a kill switch, not a success definition.

---

## 9. Evaluation normalization

```text
E0 none / demo output
E1 static schema/contract tests
E2 unit/integration tests
E3 trajectory/trace evaluation
E4 external outcome evaluation
E5 repeated stochastic trials
E6 regression gate
E7 production observability/feedback
```

These are cumulative evidence layers, not a maturity score that automatically increases with every layer.

Exact expected trajectories are suitable for policy-contract tests but may be too brittle for open-ended capability evaluation.

---

## 10. Protocol normalization

A protocol flag without a revision is incomplete.

For MCP record at least:

- revision;
- host/client/server role;
- transport;
- capability set;
- extensions;
- auth/identity model;
- policy boundary;
- timeout/cancellation semantics.

`MCP = interoperability`, not automatic authorization.

---

## 11. Multi-agent normalization

Do not classify `multi-agent` as `advanced`.

Record topology and admission hypothesis:

```yaml
topology:
reason:
  parallelism: true|false
  context_partition: true|false
  permission_isolation: true|false
  independent_verifier: true|false
  specialization: true|false
baseline:
measured_benefit:
coordination_cost:
```

No measured benefit → topology remains an experiment, not a promoted architecture rule.

---

## 12. Evidence-state normalization

Every non-trivial classification carries one of:

```text
OBSERVED
SOURCE_CLAIM
INFERRED
SUPPORTED
QUALIFIED
CONTRADICTED
UNKNOWN
```

Example:

```yaml
publication: live               # OBSERVED
human_approval_for_publish: ?   # UNKNOWN
```

Do not fill `?` using the existence of an unrelated HITL node.

---

## 13. MK1 first classification set

Normalize these first because MK0 already has strong evidence:

1. minimal while-loop agent;
2. HITL approval agent;
3. trace-evaluation harness;
4. E2E testing agent;
5. self-healing code agent;
6. HR messaging agent;
7. social publishing agent;
8. document-intake agent;
9. DataScribe;
10. self-improving/reflection example;
11. representative memory agent;
12. representative multi-agent system;
13. MCP tutorial as a legacy protocol example.

Then expand to the remaining inventory families.

---

## 14. MK1 closure gate

MK1 closes only when:

- [ ] every engineering family has at least one normalized record;
- [ ] control, side effect, state/memory and human-control axes do not depend on framework labels;
- [ ] P0 examples have capability-composition records;
- [ ] retries/errors/termination are normalized for representative loop families;
- [ ] memory examples use lifecycle dimensions rather than `memory=true`;
- [ ] protocol examples are revision-aware;
- [ ] multi-agent examples carry admission hypotheses/baselines;
- [ ] every material unknown remains explicit;
- [ ] duplicate/overlapping dimensions are resolved;
- [ ] schema can classify a new external system without inventing a new top-level category.

MK2 remains blocked until this normalization survives classification pressure tests.