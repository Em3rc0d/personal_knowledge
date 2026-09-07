# MK0 — Candidate Invariants & Anti-Patterns

Status: **CANDIDATE RULES TRANSFERRED FOR NORMALIZATION/OPERATIONALIZATION**

These are not yet certified production rules. MK0 established evidence paths and adversarial questions; MK1 normalizes them and MK2 converts surviving rules into executable contracts/checklists/tests.

## Candidate invariant families

### I-01 — Execution boundary

The model may propose an action. The execution layer owns validation, authorization and the actual side effect.

### I-02 — Bounded autonomy

Every recursive or iterative path has explicit budgets and terminal behavior.

### I-03 — Typed tools

Tool contracts make invalid, forbidden, transient and unknown-outcome failures machine-distinguishable instead of relying only on prose errors.

### I-04 — Consequential action safety

When approval is required, it occurs before the side effect. Edited actions are revalidated. Authorization cannot be bypassed by invoking a lower-level dispatcher directly.

### I-05 — Durable resume

If execution can pause/resume after process or session loss, state has durable identity/checkpointing and replay semantics are understood.

### I-06 — Outcome-grounded completion

Externally inspectable outcome/evidence outranks model narration when certifying task completion.

### I-07 — Evaluation as a system contract

Correctness and operational behavior are separate dimensions: outcome, trajectory, policy, latency, cost, errors and stability across repeated trials.

### I-08 — Evidence-gated complexity

Additional agents, planners, critics, memories or abstraction layers require measurable benefit against a simpler baseline.

### I-09 — Contained capabilities

High-blast-radius capabilities are constrained by policy, sandboxing and permissions independently of the prompt.

### I-10 — Reproducible runtime

Model, framework, tool/API versions and relevant environment assumptions belong in evidence receipts.

## Anti-pattern catalog

### AP-01 — Prompt as firewall

A high-impact prohibition exists only in natural-language instructions.

### AP-02 — Retry-by-error-string

The model sees text such as `try again` and effectively owns retry policy without structured failure semantics or budget.

### AP-03 — Infinite / oscillating agent

No turn/tool/time/cost cap or repeated-action/state detection.

### AP-04 — Agent-certified completion

Generated text asserting success is treated as the only completion proof.

### AP-05 — Memory soup

Transcript, checkpoints, vector memory, RAG and durable runtime state are all called `memory` without lifecycle contracts.

### AP-06 — Approval after mutation

Human review happens after the effect or does not gate the actual dispatcher.

### AP-07 — Edited-but-not-revalidated

Arguments change but prior validation/authorization is reused.

### AP-08 — Multi-agent by enthusiasm

More agents are introduced without baseline comparison or measurable specialization/parallelization benefit.

### AP-09 — Framework-defined architecture

A system is described as a `LangGraph agent`, `CrewAI system`, etc. without documenting authority, state, tools and boundaries.

### AP-10 — Notebook-green fallacy

A clean/renderable notebook is interpreted as proof that dependencies, integrations and behavior still work.

### AP-11 — Intended-source grounding

A URL/source label is recorded but there is no evidence that the expected content was actually passed to the model.

### AP-12 — Uncontained general executor

A model receives broad shell/code/network/filesystem authority where narrow capabilities would suffice.

## Threat-model linkage

Concrete trust boundaries, abuse paths and adversarial fixtures live in [`../../architecture/THREAT_MODEL.md`](../../architecture/THREAT_MODEL.md).

## Promotion rule

```text
MK0 candidate invariant
        ↓
MK1 normalized dimension/rule
        ↓
MK2 operational contract + acceptance test
        ↓
later cross-system certification
```

No invariant skips these stages merely because it appears intuitively correct.
