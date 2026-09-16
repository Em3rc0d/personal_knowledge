# MK1 — Multi-Agent Baseline Specification

Status: **OPEN GATE SPECIFICATION**

## Purpose

Define the evidence required before this domain treats a multi-agent topology as justified for a task rather than assuming that more agents imply more capability.

This gate exists to keep **topology** separate from **measured benefit**.

The expected result may be:

```text
multi-agent better
multi-agent equivalent
multi-agent worse
inconclusive
```

All are valid evidence when the experiment is controlled enough to support the conclusion.

## Domain rule under test

> Multi-agent complexity must earn itself against a simpler sufficient baseline.

This rule does not mean multi-agent is bad. It means additional coordination, context, latency and failure surfaces require evidence proportional to the added complexity.

## Admission hypothesis

Before running the multi-agent variant, state why it might help.

Allowed hypothesis families include:

```text
parallel decomposition
specialized expertise/tools
context partitioning
independent verification/critique
role separation / authority separation
heterogeneous model/tool access
fault isolation
```

Do not use:

```text
“because multi-agent is more advanced”
“because the framework supports Swarm/Graph/crew”
```

as an admission hypothesis.

## Required baseline

Choose the **simplest plausible architecture that can attempt the same task**.

Examples:

```text
single model call
single model + tools
single bounded agent loop
deterministic workflow with model steps
single orchestrator without autonomous peers
```

The baseline must share, as far as practical:

- task set;
- model family/configuration or clearly recorded differences;
- tool access;
- data/context availability;
- evaluation rubric;
- run budget;
- environment.

If parity is impossible, record the asymmetry explicitly.

## Multi-agent variant classification

Record:

```yaml
topology:
  type: router_workers | manager_workers | peers | graph | swarm | mixed
  actor_count:
  authority_distribution:
  handoff_owner:
  shared_state:
  private_state:
  termination_owner:
  coordination_channel:
```

If topology changes during execution, record that behavior rather than forcing a static label.

## Evaluation dimensions

### 1. Outcome quality

Use task-specific objective graders where possible.

Record:

- success/failure;
- correctness/completeness;
- external outcome verification;
- error classes.

Do not rely only on agent self-reports.

### 2. Trajectory quality

Inspect:

- unnecessary tool calls;
- redundant reasoning/work;
- loops/oscillation;
- contradictory agent actions;
- failed handoffs;
- duplicate side effects;
- verifier effectiveness.

### 3. Latency

Record at least:

```text
wall-clock completion time
critical-path latency
parallel work if any
coordination waiting time if observable
```

Parallelism that increases coordination time may or may not improve the final result.

### 4. Token / model cost

Record when measurable:

- total input tokens;
- total output tokens;
- number of model calls;
- model/provider cost;
- duplicate context cost;
- inter-agent message/context cost.

If cost cannot be measured, state `NOT_MEASURED` rather than assuming efficiency.

### 5. Tool/system cost

Record:

- tool calls;
- external API calls;
- browser/shell/database operations;
- rate-limit pressure;
- duplicated work;
- resource contention.

### 6. Failure containment

Test/inspect how the system handles:

- one worker/agent failure;
- malformed handoff;
- conflicting outputs;
- stalled agent;
- partial result;
- coordinator failure;
- duplicated consequential action;
- timeout/unknown outcome.

### 7. Termination

Record:

- who decides completion;
- global vs per-agent budgets;
- handoff/loop limits;
- oscillation detection;
- success predicate;
- what happens when one actor keeps working after the global objective is satisfied/cancelled.

### 8. State/concurrency

Record:

- shared-writer model;
- merge/reducer semantics;
- locking/conflict behavior;
- ordering assumptions;
- checkpoint/session model;
- duplicate/replay behavior.

This is especially important when multi-agent execution introduces concurrency not present in the baseline.

## Experimental design

Minimum useful design:

```text
same task set
baseline architecture
multi-agent architecture
same evaluation contract
multiple trials for stochastic paths where feasible
record quality + latency + cost + failures
```

A single successful showcase is insufficient for a general benefit claim.

For MK1, the goal is classification/evidence pressure, not publication-grade benchmarking. Keep the fixture small but honest.

## Result matrix

Use a neutral comparison table:

| Metric | Baseline | Multi-agent | Evidence |
|---|---:|---:|---|
| outcome success |  |  |  |
| quality score |  |  |  |
| wall time |  |  |  |
| model calls |  |  |  |
| tokens/cost |  |  |  |
| tool calls |  |  |  |
| coordination failures |  |  |  |
| duplicate work/effects |  |  |  |
| termination failures |  |  |  |

Do not collapse the matrix into a single “winner” score.

## Interpretation contract

A positive multi-agent result may support a scoped statement such as:

> For this pinned task set and configuration, the tested topology improved X while costing Y.

It does not support:

> Multi-agent is better.

A negative result is equally useful:

> The extra topology did not justify its coordination/cost overhead for this task.

## Strands-specific candidate fixture

Strands is a useful first baseline target because the same SDK exposes multiple topology surfaces:

```text
single Agent
agents-as-tools
Graph
Swarm
Workflow
```

This can reduce framework/provider confounding.

However, do not choose a Strands topology merely to showcase it. Select a task with a credible admission hypothesis.

Potential comparison shape:

```text
single bounded Agent
vs
manager + specialist agents-as-tools
```

or:

```text
single Agent
vs
parallel/dependency Graph
```

The exact fixture remains open until task/eval design is pinned.

## MK1 pass condition

This gate passes when the repository contains at least one representative multi-agent classification/evidence receipt that includes:

- admission hypothesis;
- simpler baseline;
- topology/authority description;
- outcome evidence;
- cost/latency evidence where measurable;
- failure/termination observations;
- explicit qualification of the result.

The gate validates that MK1 can represent **benefit evidence independently from topology**.

It does not certify the tested topology for production.

## Later-MK routing

MK1 owns:

- topology classification;
- admission hypothesis;
- baseline evidence shape;
- scoped measured comparison.

MK2 should convert surviving principles into operational admission/test contracts.

MK5+ should handle stronger repeated/independent certification where the project risk requires it.
