# Daily Operating Model

## Baseline cadence

Current evidence window:

```text
29 posts / 7 days ≈ 4.14 posts/day
```

Because growth coexisted with this cadence, the current plan does not reduce volume by default. Cadence remains an experiment, not a permanent rule.

## Four-slot system

### Slot 1 — Reach Engine

Goal: acquire attention.

Typical topic family:

- SQL / databases;
- programming behavior;
- Git;
- HTTP;
- Docker;
- Linux;
- networking.

### Slot 2 — Engineering Authority

Goal: show depth.

Typical topic family:

- backend;
- APIs;
- concurrency;
- caching;
- queues;
- architecture;
- distributed systems;
- security;
- testing/observability.

### Slot 3 — Proof of Work

Goal: prove real-world execution and engineering judgment.

Use actual project decisions, failures, release gates, architecture trade-offs and debugging stories.

### Slot 4 — Opportunity / Business / AI

Goal: connect engineering capability to business value.

Typical topic family:

- automation;
- AI engineering;
- workflow reliability;
- business-process architecture;
- SaaS/system decisions.

## Example batch — 2026-09-11

This is an `EXPERIMENT EXAMPLE`, not evergreen canon.

| Time | Role | Topic / Hook |
|---|---|---|
| 09:00 | Reach | `UNION` vs `UNION ALL`: similar result, different semantics/cost |
| 12:00 | Authority | Retry can execute the same API operation twice → idempotency |
| 15:00 | Proof / DevOps | Deploying every tiny change can waste pipeline/infrastructure |
| 18:00 | Opportunity | Automating a bad process makes errors happen faster |

### Experiment 1 — `UNION` vs `UNION ALL`

Core lesson:

```text
UNION      → combine + remove duplicates
UNION ALL  → combine + preserve all rows
```

Hook:

> They look equivalent until duplicate removal becomes part of the cost.

CTA:

> If you know there are no duplicates, which would you choose?

### Experiment 2 — retry is not operation safety

Flow:

```text
request
→ operation executes
→ response is lost
→ client retries
→ duplicate side effect
```

Bridge to:

- idempotency;
- idempotency keys;
- production reliability.

### Experiment 3 — deploy ≠ progress

Core distinction:

```text
development
→ preview/test
→ stable
→ production
```

CI/CD does not mean “deploy every mutation everywhere”.

### Experiment 4 — automation amplifies process quality

Example flow:

```text
lead
→ spreadsheet
→ email
→ approval
→ record
```

Failure concerns:

- incomplete input;
- integration failure;
- duplicate operation;
- human exception.

Bridge to:

```text
validation
→ explicit states
→ retries
→ human approval
→ audit trail
```

## Topic freshness gate

Before selecting a topic, check recent published/planned content.

Reject a candidate when it materially repeats:

- topic;
- mental trap;
- hook;
- explanation;
- diagnosis;
- creative structure.

Continuation / part 2 / controlled variation is allowed only when deliberate.

## Daily review

At minimum log:

- post role;
- topic;
- format;
- hook class;
- CTA class;
- impressions;
- unique reach when available;
- saves;
- comments;
- shares;
- profile-view movement;
- follower movement;
- opportunity signals.

The goal is to learn which jobs each content family performs, not merely rank posts by likes.
