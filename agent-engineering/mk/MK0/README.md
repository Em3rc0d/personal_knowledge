# MK0 — Mine & Frame

Status: **IN PROGRESS**

## Mission

Build a defensible foundation for agent engineering before turning individual tutorial patterns into reusable system rules.

The initial mining corpus is `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`, contrasted with official agent/runtime/protocol documentation and scientific literature.

## Problem statement

“AI agent” is currently an overloaded label. Systems with very different control authority, state, tool use, persistence, human oversight and evaluation are routinely grouped together.

If we import that ambiguity into engineering, we cannot answer basic questions reliably:

- When is a deterministic workflow sufficient?
- What exactly may the model decide?
- Which rules are prompts and which are enforced invariants?
- What state survives a crash or human pause?
- What can create real-world side effects?
- How does the system know it succeeded?
- What stops a failed loop?
- What evidence justifies another agent or another layer of abstraction?

MK0 exists to make these questions explicit before implementation templates are designed.

## Initial ontology

### System classes

```text
LLM CALL
single inference; no autonomous iteration

LLM WORKFLOW
multi-step system whose main path/control flow is predetermined by code

MODEL-ROUTED WORKFLOW
code defines available branches; model selects among constrained routes

TOOL-USING AGENT
model can repeatedly select actions/tools and adapt using observations within runtime limits

MULTI-AGENT SYSTEM
multiple model-directed execution loops coordinate, delegate, critique or partition work
```

These are provisional classes. MK1 must test whether a strict hierarchy is less useful than orthogonal dimensions.

### Core components

```text
OBJECTIVE
POLICY
HARNESS / RUNTIME
MODEL
CONTEXT BUILDER
STATE
CHECKPOINTER / PERSISTENCE
MEMORY
TOOLS / ENVIRONMENT
HUMAN CONTROL
TRACE / RECEIPTS
EVALUATOR
BUDGET / TERMINATION
```

## Critical distinctions

### Workflow vs agent

Control authority is the key discriminator.

A system can use LangGraph and still be mostly deterministic. A custom Python loop can be genuinely model-directed. Framework identity is therefore not the primary taxonomy.

### Prompt vs invariant

```text
PROMPT RULE
asks the model to behave a certain way

RUNTIME INVARIANT
makes forbidden behavior impossible or intercepts it before execution
```

Prompts remain useful for behavior shaping. They are not the sole enforcement mechanism for security, authorization, budgets or critical side effects.

### Context vs state vs memory

```text
STATE       what the runtime currently knows/needs
CONTEXT     what is projected into this model call
MEMORY      information intentionally retained/retrieved across an interaction horizon
PERSISTENCE mechanism that keeps state/checkpoints durable
```

A transcript is one possible context source; it is not a universal definition of state or memory.

### Result vs evidence

```text
MODEL CLAIM        “done” / explanation / generated answer
TRACE              what calls/actions occurred
OUTCOME            external state/result produced
EVIDENCE           observation that supports a success/failure claim
```

A model's completion message cannot certify its own effect.

## Candidate invariant families

### I-01 — Execution boundary

The model may **propose** an action. The execution layer owns validation, authorization and actual side effect.

### I-02 — Bounded autonomy

Every recursive/iterative execution path has explicit budgets and terminal behavior.

### I-03 — Typed tools

Tool contracts must make invalid/forbidden/temporary failures machine-distinguishable rather than relying on prose error interpretation.

### I-04 — Consequential action safety

Approval, when required, occurs before side effects; edited actions are revalidated; authorization cannot be bypassed by calling a lower-level dispatcher directly.

### I-05 — Durable resume

If an execution can pause and resume asynchronously or after process loss, checkpoint state must be durably identifiable and replay semantics understood.

### I-06 — Outcome-grounded completion

Success gates prefer externally inspectable outcome/evidence over self-reported completion.

### I-07 — Eval as system contract

Evaluation covers both correctness and operational behavior: outcomes, trajectory, policy, latency, cost, errors and stability across repeated trials.

### I-08 — Evidence-gated complexity

Additional agents, planners, critics, memories or framework layers require measurable benefit over a simpler baseline.

### I-09 — Contained capabilities

High-blast-radius capabilities are restricted by policy/sandbox/permissions independent of the model prompt.

### I-10 — Reproducible runtime

Model, framework, tool/API versions and relevant environment assumptions belong in evidence receipts.

## Evidence graph from S-001

```text
minimal while-loop tutorial
    ├── shows model/tool/observation iteration
    ├── shows hard turn cap
    └── shows runtime guard outperforming prompt-only prohibition

HITL tutorial + tests
    ├── pre-side-effect approval
    ├── approve/edit/reject
    ├── revalidation
    ├── dispatcher authorization
    └── checkpointed resume

trace-eval tutorial + tests
    ├── tool sequence/args
    ├── grounding/evidence
    ├── error handling
    ├── latency
    └── regression gate

repo-level evidence
    ├── broad architecture corpus
    ├── old/new dependency mismatch risk
    ├── structural notebook validator
    ├── partial dedicated tests
    └── community failure/taxonomy signals
```

## External contradiction graph

```text
SOURCE CLAIM / PATTERN                  INDEPENDENT PRESSURE
────────────────────────────────────────────────────────────────────
"agent" used broadly                  official workflow-vs-agent distinction
reflection/self-improvement            Reflexion + limits of intrinsic self-correction
multi-agent sophistication             empirical MAS failure taxonomy
trace scoring                          current agent-eval guidance: trials/outcomes/graders
in-memory checkpoints                  production persistence guidance
many available tools                   tool-interface evaluation + context-cost discipline
transcript as entire mind              context engineering: broader curated context/state
MCP as integration bridge              MCP is protocol/capability boundary, not full runtime
```

## Initial anti-pattern catalog

### AP-01 — Prompt as firewall

A high-impact prohibition exists only in natural-language instructions.

### AP-02 — Retry-by-error-string

The model sees “try again” and decides retry behavior without structured failure semantics or budget.

### AP-03 — Infinite/oscillating agent

No turn/tool/time/cost cap or repeated-action detection.

### AP-04 — Agent-certified completion

The only evidence of success is generated text asserting success.

### AP-05 — Memory soup

Transcript, checkpoints, vector memory, RAG and durable state are all called “memory” without lifecycle contracts.

### AP-06 — Approval after mutation

Human review occurs after the consequential effect or does not gate the actual dispatcher.

### AP-07 — Edited-but-not-revalidated

Reviewer/model edits an action and execution reuses validation/authorization from the original action.

### AP-08 — Multi-agent by enthusiasm

More agents are introduced without baseline comparison or measurable partition/parallelization benefit.

### AP-09 — Framework-defined architecture

The system is described as “LangGraph agent” rather than documenting actual control, state, tools and boundaries.

### AP-10 — Notebook-green fallacy

A structurally clean/renderable notebook is treated as proof that dependencies, integrations and behavior still work.

### AP-11 — Intended-source grounding

The system records a URL/source name but does not prove what content was actually supplied to the model.

### AP-12 — Uncontained general executor

A model receives broad shell/code/network/filesystem authority when narrow capabilities would suffice.

## What MK0 intentionally does not claim

- that LangGraph is better/worse than other agent frameworks;
- that one universal agent architecture exists;
- that chain-of-thought text is a reliable source of causal explanation;
- that reflection is useless;
- that multi-agent systems are ineffective;
- that every `GenAI_Agents` notebook is broken or unsafe;
- that current source sampling is exhaustive;
- that candidate rules are ready for `main` promotion.

## MK0 next work

### Inventory normalization

For every representative tutorial family, record:

```yaml
control_authority:
horizon:
model_count:
tools:
external_reads:
external_writes:
generated_code_execution:
state:
persistence:
memory:
human_gate:
retry_policy:
termination_policy:
error_model:
evaluation:
security_boundary:
dependency_receipt:
```

### High-risk source sampling

Prioritize examples with:

- shell/code execution;
- browser automation;
- database access;
- email/social publication;
- files and document ingestion;
- financial/contract/compliance actions;
- external mutations.

### Cross-source expansion

Before MK0 closes, mine or compare:

- `NirDiamant/agents-towards-production` for production-specific claims;
- dedicated agent-memory sources for memory taxonomy;
- current MCP specification at capability/message level;
- additional independent agent-evaluation/security research.

## MK0 gate

MK0 can close only when:

1. high-impact source families are sampled;
2. all candidate rules have at least one evidence path and one counterexample/adversarial question;
3. terminology is framework-independent;
4. legal/provenance boundaries are preserved;
5. UNKNOWNs remain explicit;
6. MK1 can classify new agent systems without relying on their marketing labels.

Until then:

```text
MK0 = IN PROGRESS
MK1 = BLOCKED
MAIN PROMOTION = BLOCKED
```
