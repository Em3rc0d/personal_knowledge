# MK1 — Normalized Dimensions

Status: **OPEN / IN PROGRESS**

MK1 replaces one-dimensional labels such as `agent`, `multi-agent`, `LangGraph agent` or `self-improving` with orthogonal engineering dimensions.

## 1. Control authority

### C0 — Deterministic

Code selects the next operation. The model may transform or classify content but does not control the execution path.

### C1 — Model-routed

Code defines a bounded set of routes; the model selects among them.

### C2 — Model-directed bounded agent

The model repeatedly selects actions/tools from observations, while runtime budgets bound the loop.

### C3 — Model-directed open-horizon agent

The model may continue until semantic success, terminal failure or external cancellation. This class requires the strongest termination/evaluation evidence.

### C4 — Mixed / nested

Different subgraphs or stages use different levels of control authority.

These classes describe control, not maturity or quality.

## 2. Capability families

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

### Capability composition

Risk derives from reachable compositions, not labels.

Example:

```text
document conversion
  = local file read
  + external upload
  + remote processing
  + returned artifact
```

A workflow described as `conversion` is therefore also a data-egress path.

## 3. Side-effect class

```text
S0  no external mutation
S1  local/reversible artifact
S2  external but reversible/draft
S3  external consequential mutation
S4  irreversible/high-impact mutation
```

Side-effect class is independent of autonomy. A deterministic workflow may be S4; an autonomous research agent may remain S0/S1.

## 4. State / checkpoint / persistence / memory

### Runtime state

Facts needed by the current execution.

### Checkpoint

Serialized runtime state at an execution boundary.

### Persistence

Durability mechanism for state/checkpoints.

### Memory

Information intentionally retained and recalled under a lifecycle/retrieval policy.

### Knowledge / RAG

External source material retrieved to answer or ground the task.

### Normalization rule

Never infer semantic memory solely because a framework object is named `MemorySaver`, `Store` or similar.

## 5. Human control

```text
H0  none
H1  review after effect
H2  approval before effect
H3  approval/edit before effect + revalidation
H4  dispatcher-enforced authorization receipt
```

`H4` is strongest because orchestration bypass does not bypass the policy boundary.

Human review in one part of a graph does not imply that every consequential tool is protected.

## 6. Error and retry semantics

### Retry owner

- model-selected;
- tool-local;
- runtime/orchestrator;
- provider SDK;
- mixed;
- none.

### Error classes

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

A prose error such as `temporarily unavailable, try again` is not a retry contract.

Mutating retries require idempotency, verification or a compensating strategy.

## 7. Termination

Record separately:

- semantic success predicate;
- terminal failure predicate;
- model-turn cap;
- tool-call cap;
- per-tool retry budget;
- wall-clock deadline;
- token/cost budget;
- repeated-state/action detection;
- external cancellation.

A recursion limit or `max_turns` is a kill switch, not a success definition.

## 8. Evaluation layers

```text
E0  demo output / no explicit evaluation
E1  static schema/contract tests
E2  unit/integration tests
E3  trajectory/trace evaluation
E4  external outcome evaluation
E5  repeated stochastic trials
E6  regression gate
E7  production observability/feedback
```

These are evidence layers, not an automatic maturity score.

Exact expected trajectories may be appropriate for policy/contract tests and too brittle for open-ended capability evaluation.

## 9. Protocol dimension

A protocol name without a revision is incomplete.

For MCP or analogous protocols record:

- revision;
- host/client/server role;
- transport;
- capability set;
- extensions;
- auth/identity model;
- policy boundary;
- timeout/cancellation semantics.

Interoperability is not authorization.

## 10. Multi-agent topology

Do not classify `multi-agent` as `advanced`.

Record:

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

Without measured benefit, multi-agent remains an experimental topology rather than a promoted architecture rule.

## 11. Evidence state

Every non-trivial classification uses one of:

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

The existence of an unrelated HITL node does not fill the `?`.

## 12. Reproducibility

Record evidence for:

- model/provider/version;
- dependency versions;
- external API/protocol revision;
- runtime assumptions;
- execution receipt when available.

A tutorial's conceptual value can survive version drift while its operational reference status degrades.
