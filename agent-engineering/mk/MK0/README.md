# MK0 — Mine & Frame

Status: **CLOSED**  
Closure receipt: [`CLOSURE.md`](./CLOSURE.md)

## Mission

Build a defensible foundation for agent engineering before turning individual tutorial patterns into reusable system rules.

The initial mining corpus is `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`, contrasted with specialized memory/production sources, the current MCP specification, official runtime guidance and scientific literature.

MK0 is closed because the domain can now describe new systems without trusting framework names, tutorial categories or marketing labels.

## Problem statement resolved by MK0

“AI agent” is overloaded. Systems with very different control authority, state, tool use, persistence, human oversight and evaluation are routinely grouped together.

MK0 made these questions explicit:

- When is a deterministic workflow sufficient?
- What exactly may the model decide?
- Which rules are prompts and which are enforced invariants?
- What state survives a crash or human pause?
- What can create real-world side effects?
- How does the system know it succeeded?
- What stops a failed loop?
- What evidence justifies another agent or layer of abstraction?

MK1 now normalizes the answers into a reusable classification model.

## Initial ontology retained as historical frame

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

MK0 concluded that a strict hierarchy is insufficient by itself. MK1 therefore uses orthogonal dimensions such as control authority, capability, side-effect class, state/persistence, memory lifecycle, human control, retries, termination and evaluation.

## Core components established

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

## Critical distinctions established

### Workflow vs agent

Control authority is the key discriminator. Framework identity is not taxonomy.

### Prompt vs invariant

```text
PROMPT RULE
asks the model to behave a certain way

RUNTIME INVARIANT
makes forbidden behavior impossible or intercepts it before execution
```

### Context vs state vs memory

```text
STATE       what the runtime currently knows/needs
CONTEXT     what is projected into this model call
MEMORY      information intentionally retained/retrieved across a lifecycle
PERSISTENCE mechanism that keeps state/checkpoints durable
```

### Result vs evidence

```text
MODEL CLAIM        generated assertion/explanation
TRACE              calls/actions that occurred
OUTCOME            external state/result produced
EVIDENCE           observation supporting success/failure
```

## Candidate invariant families transferred to MK1/MK2

These remain **candidate rules**, not certified canon:

1. **Execution boundary** — model proposes; execution layer validates, authorizes and acts.
2. **Bounded autonomy** — iterative paths have explicit budgets and terminal behavior.
3. **Typed tools** — invalid/forbidden/transient failures are machine-distinguishable.
4. **Consequential action safety** — approval precedes effects and edited actions are revalidated.
5. **Durable resume** — resumable execution has durable identity/checkpoint and understood replay semantics.
6. **Outcome-grounded completion** — external evidence outranks self-reported completion.
7. **Eval as system contract** — outcome, trajectory, policy, latency, cost, errors and repeated trials are separable.
8. **Evidence-gated complexity** — extra agents/planners/critics/memory layers must earn their cost.
9. **Contained capabilities** — high-blast-radius authority is independently constrained.
10. **Reproducible runtime** — model/framework/tool/API versions belong in evidence receipts.

## Evidence graph

```text
S-001 GenAI_Agents
  ├─ 55-tutorial normalized inventory
  ├─ minimal model/tool loop
  ├─ HITL + dispatcher tests
  ├─ trace-evaluation + tests
  ├─ generated-code/browser/shell P0 paths
  ├─ communication/publication/data-egress P0 paths
  └─ reflection/memory/research/multi-agent/MCP P1 claims

S-002 Agent_Memory_Techniques
  └─ specialized memory lifecycle/taxonomy pressure test

S-003 agents-towards-production
  └─ production-concern expansion + production-label qualification

MCP 2026-07-28
  └─ current protocol lifecycle/version contradiction

official + scientific sources
  └─ workflow/agent, tools, context, HITL, eval, reflection and multi-agent pressure tests
```

## Anti-pattern catalog established

- Prompt as firewall
- Retry-by-error-string
- Infinite/oscillating agent
- Agent-certified completion
- Memory soup
- Approval after mutation
- Edited-but-not-revalidated
- Multi-agent by enthusiasm
- Framework-defined architecture
- Notebook-green fallacy
- Intended-source grounding
- Uncontained general executor

The capability-centered threat model extends these into concrete trust boundaries and adversarial fixtures.

## What MK0 does not certify

- framework superiority;
- one universal agent architecture;
- production safety of upstream tutorials;
- current executability of every notebook;
- reliability of intrinsic reflection;
- benefit of multi-agent topology without measurement;
- exact runtime behavior under changing model/provider versions;
- operational readiness of candidate rules.

## MK0 exit gate

| Gate | Result |
|---|---|
| high-impact source families sampled | PASS |
| candidate rules have evidence paths + adversarial questions | PASS at MK0 depth |
| terminology framework-independent | PASS |
| legal/provenance boundaries preserved | PASS |
| UNKNOWNs remain explicit | PASS |
| MK1 can classify systems without marketing labels | PASS |

Full evidence and qualifications: [`CLOSURE.md`](./CLOSURE.md).

## Promotion state

```text
MK0 = CLOSED
MK1 = OPEN / IN PROGRESS
MK2 = BLOCKED BY MK1
CANON RULE CERTIFICATION = NOT YET
```

Closing MK0 promotes the framing and evidence discipline, not every candidate rule.