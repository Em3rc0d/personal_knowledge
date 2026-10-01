# S-115 — walkinglabs / learn-harness-engineering

Status: **SOURCE RECEIPT — NON-CANONICAL**  
Observed: **2026-10-01**

## Identity

| Field | Value |
|---|---|
| ID | `S-115` |
| Type | public GitHub repository / project-based harness-engineering course + templates |
| Repository | https://github.com/walkinglabs/learn-harness-engineering |
| Pinned snapshot | `38ddcd2bf8d65271f668b94e7c875ca1d629d622` |
| Snapshot date observed | 2026-10-01 |
| Upstream commit date | 2026-10-01 |
| License | MIT |
| Primary implementation/content | Markdown courseware, TypeScript/JavaScript tooling, shell templates, VitePress docs |
| Authority | primary for artifacts and claims about this repository; secondary/synthetic for general harness claims that it attributes to OpenAI, Anthropic, Pi, DeepSeek or community sources |
| Use here | repository-harness pressure test, context/state/verification/lifecycle refinement, loop/graph vocabulary comparison, practical harness-artifact patterns |

## Why collected

This repository is useful because it translates broad agent-runtime ideas into concrete repository mechanics that can be inspected and operationalized:

- short root instruction files used as routers rather than encyclopedias;
- persistent feature/progress/handoff artifacts;
- explicit startup/verification paths;
- one-active-feature discipline;
- evidence-gated completion;
- session cleanup and resumability;
- generator/evaluator separation;
- context operations such as selection, persistence, compression and isolation;
- loop and graph escalation only when coordination requirements justify it.

The source aligns strongly with the existing `agent-engineering` domain, but it should refine rather than replace the current taxonomy.

## High-value upstream evidence inspected

Pinned at the snapshot above:

- `README.md`;
- `CLAUDE.md`;
- `docs/en/lectures/lecture-01-why-capable-agents-still-fail/index.md`;
- `docs/en/lectures/lecture-02-what-a-harness-actually-is/index.md`;
- `docs/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/index.md`;
- `docs/en/lectures/lecture-04-why-one-giant-instruction-file-fails/index.md`;
- `docs/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/index.md`;
- `docs/en/lectures/lecture-06-why-initialization-needs-its-own-phase/index.md`;
- `docs/en/lectures/lecture-07-why-agents-overreach-and-under-finish/index.md`;
- `docs/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/index.md`;
- `docs/en/lectures/lecture-09-why-agents-declare-victory-too-early/index.md`;
- `docs/en/lectures/lecture-10-why-end-to-end-testing-changes-results/index.md`;
- `docs/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/index.md`;
- `docs/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/index.md`;
- `docs/en/lectures/lecture-13-loop-engineering/index.md`;
- `docs/en/lectures/lecture-14-graph-engineering/index.md`;
- `docs/en/harness-designs/{claude-code,codex,pi,deepseek}/index.md`;
- `docs/en/resources/`;
- `skills/harness-creator/SKILL.md`;
- `skills/harness-creator/templates/`;
- `skills/harness-creator/references/`;
- `tools/audit-harness.sh`;
- recent repository commits around evidence auditing and source qualification.

## Primary-source contrast checked

The following upstream primary sources were also checked independently during this pass:

### OpenAI — Harness engineering: leveraging Codex in an agent-first world

Published 2026-02-11.

Primary support found for:

- repository knowledge as the system of record;
- short `AGENTS.md` as a map/table of contents rather than a giant manual;
- progressive disclosure into structured repository docs;
- versioned execution plans, progress and decision logs;
- mechanical enforcement of architecture/invariants;
- explicit feedback loops and agent-legibility as engineering goals;
- recurring cleanup / garbage-collection behavior for agent-generated entropy.

Source: https://openai.com/index/harness-engineering/

### Anthropic — Effective harnesses for long-running agents

Published 2025-11-26.

Primary support found for:

- dedicated initializer phase;
- `init.sh`, progress log and git history as resumability artifacts;
- feature lists with end-to-end behavior descriptions;
- selecting one unfinished feature per session;
- startup verification before adding new work;
- clean-state handoff between context windows;
- the observed failure mode of premature project completion.

Source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

### Anthropic — Harness design for long-running application development

Published 2026-03-24.

Primary support found for:

- planner / generator / evaluator separation;
- structured artifacts for cross-session handoff;
- evaluator quality as a first-class engineering problem;
- simplification pressure: every harness component encodes an assumption about what the model cannot do and should be periodically stress-tested as models improve.

Source: https://www.anthropic.com/engineering/harness-design-long-running-apps

## Core observations

### 1. Repository harnessing is an execution-control problem, not a prompt-file problem

The repository repeatedly treats the model as only one component inside a larger execution system. Reliability is sought through persisted instructions, state, environment setup, verification and lifecycle rules.

This is compatible with the current `agent-engineering` principle that model capability and runtime/policy authority are distinct.

### 2. Root instructions work best as a router

The strongest source-backed pattern is:

```text
small stable entrypoint
  → topic-specific docs
  → task-local evidence/resources
```

The course's `harness-creator` skill also encodes the same design rule: keep the root instruction file short and put project facts in project docs.

This is a concrete repository-level implementation of progressive disclosure.

### 3. Persistent state should be executable enough to constrain work

The source treats feature/state files as more than human notes. The strongest version is a tuple:

```text
behavior
+ verification method
+ current state
+ evidence
```

This is useful because scheduling, verification and handoff can all consume the same state artifact.

### 4. Completion should be externally evidenced

Lecture 08 proposes pass-state gating: the agent should not simply assert that a feature is passing; verification should control the state transition.

Lecture 09 extends this into layered termination checks:

```text
static / syntax
→ runtime behavior
→ system / end-to-end confirmation
```

This aligns with the current domain rule:

```text
runtime DONE != task DONE
```

but adds a practical state-transition mechanism worth pressure-testing later.

### 5. Review feedback can become executable infrastructure

Lecture 10's strongest refinement is not merely "write more tests." It is:

```text
recurring review defect
→ classify invariant
→ encode automated check
→ produce actionable diagnostic
→ rerun continuously
```

This converts human correction into durable harness capability.

### 6. Session cleanliness is an independent completion invariant

The source treats "feature works" and "next session can safely resume" as separate conditions.

Candidate form:

```text
task verification PASS
AND
restart / handoff state PASS
→ session complete
```

This is stronger than treating cleanup as optional housekeeping.

### 7. Context is an actively managed resource

The bundled context-engineering reference uses four operations:

```text
SELECT
WRITE
COMPRESS
ISOLATE
```

The names are source-level synthesis, not a universal standard, but they form a useful compact vocabulary for:

- just-in-time context loading;
- persistence outside the context window;
- compaction of older material;
- context separation across delegated work.

### 8. Loop and graph are escalation layers, not replacements for the harness

The source frames:

```text
prompt → context → loop → graph
```

and treats the harness as the infrastructure that makes those executions reliable.

The graph lecture is useful mainly for the admission question: topology should become explicit when specialization, parallelism, shared state, routing, verification or recovery can no longer be represented cleanly by one loop.

This supports the existing `agent-engineering` rule that multi-agent/topological complexity must earn its cost.

## Material contradictions / caveats

### A. Two different "five subsystem" models coexist

The source is internally inconsistent in how it names the five harness subsystems.

Lecture 02 states:

```text
Instructions
Tools
Environment
State
Feedback
```

while the root README curriculum summary and `skills/harness-creator/SKILL.md` use:

```text
Instructions
State
Verification
Scope
Lifecycle
```

These are both useful views, but they are not the same orthogonal taxonomy.

**Implication:** do not promote "the five subsystems" verbatim into our canonical schema. Treat them as two source-specific decompositions: conceptual/runtime-facing vs repository-operational.

### B. "Passing is irreversible" is too strong as a universal rule

Lecture 08 says a feature's transition to `passing` is irreversible.

That is not safe as a general engineering invariant because later code/config/dependency changes can invalidate earlier evidence.

Better candidate state model for future pressure-testing:

```text
NOT_STARTED
→ ACTIVE
→ VERIFIED
→ STALE / REGRESSED
→ ACTIVE
```

Evidence should be revision-bound, not timeless.

### C. WIP=1 is a safe default, not a universal optimum

The course strongly advocates one active feature at a time.

This is useful for single-agent/single-writer work, but the current domain already recognizes that explicit ownership, isolation, reducers/merge semantics and conflict handling can justify concurrency.

Therefore:

```text
WIP=1
```

should remain a default baseline, not a canonical prohibition on parallelism.

### D. Template scripts are pedagogical defaults, not production contracts

The bundled `init.sh` is intentionally generic. It installs dependencies and attempts common checks across Node/Python/Go/Rust/Java/.NET projects.

Do not promote it as-is to a universal bootstrap standard. Reproducible environments require project-specific lockfile, runtime, cache, network, secret and side-effect contracts.

### E. Quality letter grades compress too much state

The course's `quality-document.md` uses A/B/C/D grades.

Our current `production readiness is an evidence vector` principle is more expressive and should remain dominant. A letter may be a UI summary, not the underlying truth model.

### F. Source-specific product breakdowns are partly version-bound

Claude Code, Codex, Pi and DeepSeek breakdowns contain useful implementation observations, but some details are tied to product versions or community reverse-engineering.

They require source-specific receipts before any runtime-level fact is promoted.

## Legal boundary

The upstream repository is MIT licensed.

Implications:

- code/templates may legally be reused with preservation of the MIT notice where substantial portions are copied;
- this knowledge base should still prefer independent synthesis rather than wholesale copying;
- source provenance and pinned snapshot remain required;
- externally attributed claims must retain their original-source distinction.

## Promotion boundary

Use S-115 to pressure-test or support:

- repository-as-system-of-record patterns;
- root instruction file as router;
- progressive disclosure;
- explicit persistent work state;
- evidence-bound completion;
- session handoff / clean-state gates;
- review-feedback promotion into executable checks;
- agent-oriented diagnostic feedback;
- context selection/persistence/compression/isolation vocabulary;
- generator/evaluator separation;
- loop/graph admission questions;
- periodic removal/simplification of stale harness mechanisms.

Do not use S-115 alone to:

- replace the current MK1 taxonomy;
- establish one universal five-part harness model;
- claim a feature can never regress after passing;
- require WIP=1 under every concurrency model;
- certify the bundled templates as production-ready;
- promote product-specific Claude/Codex/Pi/DeepSeek internals without source-specific verification;
- promote illustrative course numbers as empirical facts.

Processed synthesis: [`../quarries/repository-harness-engineering-refinements.md`](../quarries/repository-harness-engineering-refinements.md)
