# MK1 — Normalized Dimensions

Status: **OPEN / IN PROGRESS**  
Aligned schema: **`mk1-draft-2026-09-16.1`**

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

## 4. State / checkpoint / persistence / concurrency / memory

### Runtime state

Facts needed by the current execution.

### Checkpoint

Serialized runtime state at an execution boundary.

### Persistence

Durability mechanism for state/checkpoints.

### Concurrency semantics

Persistence does not answer whether simultaneous execution is safe.

Record separately when material:

```text
invocation concurrency
writer model
conflict/merge semantics
locking/serialization mechanism
```

Representative normalized values:

- `serial_only` — overlapping invocation is rejected or unsupported;
- `concurrent` — overlapping work is supported without a framework-level bound;
- `bounded_concurrent` — runtime/config limits concurrency;
- `single_writer` — one writer owns a state/session scope;
- `multi_writer` — multiple writers can update state;
- `reducer_merge` — concurrent updates are reconciled by an explicit reducer/merge function;
- `optimistic` / `locked` — conflicts are controlled by version checks or locking;
- `framework_defined` — semantics exist but do not map safely to a stronger normalized claim;
- `unknown` — evidence is insufficient.

Cross-runtime evidence:

- Strands documents overlapping-invocation/session-writer constraints;
- LangGraph requires explicit reducer semantics for conflicting parallel state updates;
- OpenAI Agents SDK separately controls local function-tool concurrency from provider-side parallel tool calls.

Therefore concurrency belongs under **state/runtime semantics**, not as an infrastructure footnote.

### Memory

Information intentionally retained and recalled under a lifecycle/retrieval policy.

### Knowledge / RAG

External source material retrieved to answer or ground the task.

### Normalization rule

Never infer semantic memory solely because a framework object is named `MemorySaver`, `Store` or similar. Never infer concurrency safety solely because state is durable.

## 5. Human control and intervention enforcement

```text
H0  none
H1  review after effect
H2  approval before effect
H3  approval/edit before effect + revalidation
H4  dispatcher-enforced authorization receipt
```

`H4` is strongest because orchestration bypass does not bypass the policy boundary.

Human review in one part of a graph does not imply that every consequential tool is protected.

### Enforcement owner

Two systems can both claim `guardrails` while providing materially different guarantees. Record who/what owns enforcement:

```text
runtime_code
human
model_judge
provider_guardrail
infrastructure
mixed
unknown
```

Also record `enforcement_boundary`: where the check sits relative to the model call, tool call, handoff or external side effect.

Examples:

- a blocking pre-dispatch runtime check can prevent a side effect from starting;
- a parallel model/guardrail check may discover a violation after model/tool work has begun;
- a human interrupt inside the consequential tool can gate the dispatcher;
- an LLM steering/judge layer is probabilistic guidance unless backed by a deterministic authorization boundary.

`enforcement_owner` complements, but does not replace, `dispatcher_enforcement` and `approval_binding`.

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

## 7. Termination and budget enforcement

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

### Budget enforcement boundary

A numeric limit is incomplete when the runtime can perform additional work before the limit becomes effective.

For each material budget, record:

```text
value/type
where enforcement occurs
whether in-flight work may complete
over/undershoot semantics
what exception/stop reason is emitted
```

Useful boundary descriptions include:

- `pre_dispatch` — checked before new model/tool work begins;
- `loop_boundary` — checked between iterations/steps;
- `post_turn` — evaluated after a turn has produced work;
- `tool_local` — tool owns timeout/limit enforcement;
- `external_supervisor` — process/runtime outside the harness owns the deadline;
- `cooperative` — running code must observe cancellation;
- `best_effort_remote` — remote cancellation can be requested but completion is not guaranteed;
- `unknown`.

Cross-runtime evidence shows that Strands turn/token caps, LangGraph recursion limits and OpenAI Agents SDK `max_turns`/tool timeout controls do not have identical semantics.

### Cancellation

`cancellation: yes` is insufficient. Record the effective boundary and whether already-running consequential work can continue.

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

- schema revision;
- model/provider/version;
- dependency versions;
- external API/protocol revision;
- runtime assumptions;
- execution receipt when available.

A tutorial's conceptual value can survive version drift while its operational reference status degrades.
