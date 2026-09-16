# REC-001 — Minimal While-Loop Agent

Status: **MATERIALIZED / QUALIFIED**  
Schema: **`mk1-draft-2026-09-16.1`**  
Classified: **2026-09-16**

## Record identity

```yaml
record_id: REC-001
name: GenAI_Agents minimal while-loop agent
schema_revision: mk1-draft-2026-09-16.1
classification_scope: pedagogical single-agent model→tool loop
source_receipts:
  - S-001
primary_quarries:
  - quarries/genai-agents.md
  - quarries/genai-agents-risk-scan.md
evidence_state: QUALIFIED
production_certification: false
```

Pinned upstream snapshot: `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`.

## Classification

```yaml
identity:
  name: minimal while-loop agent
  source: NirDiamant/GenAI_Agents/all_agents_tutorials/agent_while_loop_from_scratch.ipynb
  snapshot: 4c95ae14cc2462c442b5c064cccd74430d02bc46
  evidence_state: QUALIFIED

control:
  primary_authority: model_directed
  horizon: bounded_multistep
  topology: single_model
  model_count: 1

capabilities:
  reads:
    - tool results / environment observations
  writes: unknown
  generated_code_execution: false
  shell: true
  browser: none
  database: none
  communication: none
  publication: none
  file_egress: unknown
  capability_compositions:
    - model-directed tool selection + general shell execution

side_effects:
  class: unknown
  reversible: unknown
  external_mutation: unknown
  data_egress: unknown
  verification: no general external outcome verifier established by current evidence

state:
  runtime_state: structured
  checkpointing: none
  persistence_backend: none established
  replay_semantics: unknown
  invocation_concurrency: unknown
  writer_model: unknown
  concurrency_conflict_semantics: not material to the inspected single invocation example
  locking: unknown

memory:
  semantic_role: []
  scope: none
  persistence: none
  retrieval_policy: none established
  write_policy: none established
  isolation_key: none established
  retention_policy: none established
  provenance: transcript/tool-result context only in the inspected minimal example

human_control:
  level: H0
  mode: none
  dispatcher_enforcement: no
  enforcement_owner: unknown
  enforcement_boundary: no human approval boundary established
  approval_binding: not applicable

errors_and_retries:
  error_model: mixed
  retry_owner: model
  retry_budget: bounded indirectly by model-turn limit; exact per-tool retry budget not established
  idempotency: tool-dependent / not established
  unknown_outcome_handling: not established

termination:
  success_predicate: model produces a terminal answer / loop exits; not external-outcome proof
  terminal_failure_predicate: turn exhaustion or runtime/tool failure path
  turn_budget: MAX_TURNS present
  turn_budget_enforcement: runtime loop boundary
  tool_budget: no independent tool-call cap established
  tool_budget_enforcement: unknown
  time_budget: none established
  time_budget_enforcement: none established
  cost_or_token_budget: none established
  cost_or_token_budget_enforcement: none established
  overshoot_semantics: not established beyond turn boundary
  oscillation_detection: exact repeated failed call is blocked
  cancellation: not established
  cancellation_effective_boundary: unknown

evaluation:
  static_contracts:
    - exact repeated failed call guard
  unit_integration: []
  trajectory: []
  outcome: []
  repeated_trials: false
  regression_gate: false
  production_observability: false

protocols: []

security:
  trust_boundaries:
    - model
    - tool dispatcher
    - host process / shell environment
  least_privilege: no
  sandbox: unknown
  data_classification: not established
  receipts:
    - general shell capability is directly visible in the inspected tutorial

reproducibility:
  model_receipt: provider/model configuration belongs to upstream artifact; not promoted as stable domain fact
  dependency_receipt: repository snapshot pinned; per-slice environment still requires executable receipt
  external_api_receipt: not applicable/unknown
  execution_evidence: source inspection / pedagogical artifact; no repository-wide execution certification

unknowns:
  - shell filesystem/network/credential reachability in a concrete execution environment
  - exact side-effect class of commands the model can reach
  - timeout/cancellation behavior
  - per-tool retry/idempotency semantics
  - external semantic success verification
```

## Material observations

| Observation | State | Evidence |
|---|---|---|
| Model repeatedly selects tool/action from observations | OBSERVED | `quarries/genai-agents.md` |
| Runtime provides an explicit `MAX_TURNS` stop | OBSERVED | `quarries/genai-agents.md` |
| Runtime remembers failed exact calls and blocks an identical failed repeat | OBSERVED | `quarries/genai-agents.md` |
| Tool results/errors are fed back into subsequent model context | OBSERVED | `quarries/genai-agents.md` |
| Model-callable `run_command` exposes general shell execution | OBSERVED | `quarries/genai-agents.md` |
| Prompt-only “do not repeat” is weaker than executable runtime enforcement | SUPPORTED | source observation + domain normalization |

## Capability composition

The important risk is not merely `shell=true`.

```text
model-directed action selection
        +
general shell capability
        +
host-process permissions
        =
high and environment-dependent blast radius
```

The exact side-effect class remains `unknown` because the pinned knowledge does not establish the concrete runtime's filesystem/network/secrets containment.

## Termination result

This record demonstrates why:

```text
bounded=true
```

is too weak.

The example has a model-turn cap and repeated-failure guard, but no independent tool-call/time/token-cost budgets or external success verifier established by current evidence.

## Production-certification boundary

This record classifies a pedagogical control loop. It does **not** certify the example as production-ready, sandboxed, safe for arbitrary shell execution, concurrency-safe or externally outcome-verified.

## Schema pressure result

```yaml
fits_current_schema: true
new_dimension_required: false
normalization_issue: none; record reinforces separation of control, capability, termination and external outcome verification
```

## Evidence

- [`../../../quarries/genai-agents.md`](../../../quarries/genai-agents.md)
- [`../../../quarries/genai-agents-risk-scan.md`](../../../quarries/genai-agents-risk-scan.md)
- [`../../../mining-site/SOURCES.md`](../../../mining-site/SOURCES.md)
