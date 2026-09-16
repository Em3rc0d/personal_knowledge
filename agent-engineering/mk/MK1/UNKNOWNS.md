# MK1 — UNKNOWN Register

Status: **ACTIVE**

MK1 does not try to eliminate every unknown. It makes uncertainty classifiable and routes it to the MK where evidence can actually resolve it.

## Inherited from MK0

### Runtime / reproducibility

- per-notebook execution proof under current dependencies;
- exact behavior under current model/provider versions;
- current SDK migration details for legacy examples;
- complete external API compatibility receipts.

### Security / containment

- project-specific sandbox effectiveness;
- tenant/secrets isolation;
- authenticated browser mutation reachability for every browser example;
- complete consequential dispatcher enforcement;
- external-service retention behavior.

### Side effects / retries

- exact retry/idempotency semantics for every tutorial;
- unknown-outcome handling after timeout;
- compensating actions where idempotency is unavailable;
- DataScribe's exact lower-level mutation path and permission enforcement;
- universal approval coverage for HR outbound communication.

### Memory / epistemics

- quality metrics by memory family;
- memory-write validation and poisoning resistance;
- retention/deletion policies;
- persistent improvement evidence for `self-improving` claims.

### Multi-agent / operations

- benchmarked multi-agent gains;
- coordination cost;
- failure containment;
- deployment/rollback/SLO evidence;
- production observability completeness.

## MK1-specific unknowns

The normalization process must determine:

- whether `horizon` should remain inside control or become a completely independent axis;
- whether side-effect class S0-S4 needs a separate confidentiality/data-egress severity dimension;
- whether `sandbox` can be represented by one enum or requires capability-specific isolation fields;
- whether evaluation layers E0-E7 are better represented as independent booleans than an ordinal shorthand;
- whether human-control H0-H4 remains useful after explicit `enforcement_owner`, `enforcement_boundary` and dispatcher binding fields are populated;
- how to represent nested systems where child agents have materially different authorities;
- how to freeze/version the classification schema once MK1 closes.

## Runtime-semantics pressure-test resolution — 2026-09-16

The Strands Agents pass originally surfaced three candidate qualifiers. Independent evidence from LangGraph and OpenAI Agents SDK now satisfies the MK1 admission rule.

### RESOLVED / PROMOTED — concurrency semantics

Promoted into `state` in schema revision `mk1-draft-2026-09-16.1`:

- `invocation_concurrency`;
- `writer_model`;
- `concurrency_conflict_semantics`;
- `locking`.

Cross-source basis:

- Strands: overlapping-invocation/session single-writer constraints;
- LangGraph: concurrent state updates require explicit merge/reducer semantics;
- OpenAI Agents SDK: SDK-side local tool concurrency is separately bounded from provider-side parallel tool calling.

Residual unknowns:

- backend-specific distributed locking / optimistic concurrency behavior;
- conflict recovery semantics for individual persistence implementations;
- application-defined external shared-state concurrency.

### RESOLVED / PROMOTED — budget enforcement boundary

Promoted into `termination` in schema revision `mk1-draft-2026-09-16.1`:

- enforcement qualifiers for turn/tool/time/token-cost budgets;
- `overshoot_semantics`;
- `cancellation_effective_boundary`.

Cross-source basis:

- Strands: soft loop-boundary limits and cooperative cancellation;
- LangGraph: recursion limit as step kill switch rather than success predicate;
- OpenAI Agents SDK: runner turn limit plus distinct tool timeout/cancellation controls.

Residual unknowns:

- exact enforcement boundary for every runtime/provider/tool combination;
- hard-vs-cooperative cancellation for arbitrary user tools;
- remote cancellation behavior after a side effect may have begun.

### RESOLVED / PROMOTED — intervention enforcement owner

Promoted into `human_control` in schema revision `mk1-draft-2026-09-16.1`:

- `enforcement_owner`;
- `enforcement_boundary`;
- stronger `dispatcher_enforcement` semantics retained.

Cross-source basis:

- Strands: deterministic hooks, human confirmation and LLM steering have different guarantees;
- LangGraph: interrupts can gate the consequential tool path before effect;
- OpenAI Agents SDK: blocking vs parallel guardrails and distinct handoff/tool coverage boundaries.

Residual unknowns:

- exact application-level approval binding when arguments are edited;
- whether every consequential dispatcher is covered in a given system;
- adversarial reliability of model-mediated intervention;
- provider/built-in tool paths that bypass application guardrail pipelines.

## Protocol execution evidence — still open

- executable Strands/MCP compatibility against the domain-pinned MCP `2026-07-28` contract;
- exact MCP transport/auth/version receipts for a reproducible fixture;
- A2A protocol revision, authentication and transport receipts for distributed-agent classification;
- behavior when remote MCP/A2A work is cancelled after execution may already have begun.

## Framework/runtime qualification — still open

- provider feature parity across Python and TypeScript releases;
- project-specific idempotency and unknown-outcome handling for consequential tools;
- containment effectiveness for arbitrary tools inheriting host-process permissions;
- benchmarked benefit of Graph/Swarm/agents-as-tools against simpler single-agent or deterministic baselines;
- adversarial/repeated evaluation of LLM-mediated steering before treating it as a reliability mechanism.

## Routing rule

```text
unknown about vocabulary/dimensions
  → MK1

unknown about required operational behavior/contract
  → MK2

unknown requiring integration across domains
  → MK3

unknown requiring automated verification
  → MK4

unknown requiring repeated execution / real-system evidence
  → MK5+
```

## Non-negotiable rule

`UNKNOWN` is not technical debt when the evidence genuinely does not exist. Hidden assumptions are technical debt.
