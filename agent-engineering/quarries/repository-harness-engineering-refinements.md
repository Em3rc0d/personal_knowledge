# Repository Harness Engineering Refinements

Source basis: [S-115](../mining-site/S-115-learn-harness-engineering.md)

Status: **QUARRY / NON-CANONICAL**

## Thesis

The current `agent-engineering` domain already models harness/runtime, policy, context, state, tools, termination, evaluation and observability more rigorously than the source course.

The useful delta from S-115 is therefore not a replacement taxonomy. It is a set of **repository-level mechanisms** that make those abstractions executable and resumable.

```text
domain invariant
      ↓
repository artifact
      ↓
machine-checkable transition
      ↓
evidence receipt
      ↓
clean handoff
```

The source is most valuable when used to refine how agent-engineering principles are materialized in real repositories.

## Existing canon reinforced, not replaced

S-115 strongly supports several principles already present in `agent-engineering/README.md`:

| Existing principle | S-115 pressure/result |
|---|---|
| simplest sufficient architecture | loop → graph only when routing/specialization/shared state justify it |
| policy belongs in enforceable code | architecture/review rules should become executable checks |
| context is curated state | progressive disclosure + explicit context operations |
| persistence is not memory | progress/handoff files are execution state, not semantic memory |
| runtime DONE != task DONE | layered verification + externalized completion |
| outcome and trajectory are separate surfaces | generator/evaluator separation + runtime evidence |
| multi-agent must earn complexity | graph admission is treated as an escalation decision |
| production readiness is an evidence vector | source grades are useful summaries but insufficient as truth |

No schema change follows automatically from this reinforcement.

## Candidate refinements

### HE-01 — Evidence owns completion state

**State:** CANDIDATE / SUPPORTED BY SOURCE + PRIMARY CONTRAST

Problem:

```text
agent writes code
→ agent evaluates own work
→ agent marks done
```

Preferred direction:

```text
agent proposes completion
→ verifier executes required checks
→ evidence is recorded
→ state transition is accepted/rejected
```

Important refinement over the source:

```text
VERIFIED is revision-bound
```

A later mutation may invalidate old evidence and move the unit to `STALE` or `REGRESSED`.

Potential MK2 contract fields:

```yaml
work_unit_id:
target_revision:
state:
verification_contract:
evidence_refs:
verified_at:
invalidated_by:
```

### HE-02 — Verification authority and implementation authority should be separable

**State:** CANDIDATE / SUPPORTED

Generator/evaluator separation should not be reduced to "use two agents."

The deeper distinction is authority:

```text
implementation authority
!=
acceptance authority
```

The checker may be:

- deterministic tests;
- a policy engine;
- a separate agent;
- a human reviewer;
- a composite gate.

This fits the current domain's emphasis on enforcement owner/boundary.

### HE-03 — Session completion has two gates

**State:** CANDIDATE / SUPPORTED

A session may finish a task yet still leave unusable continuation state.

Candidate invariant:

```text
SESSION_COMPLETE =
    TASK_ACCEPTANCE_PASS
    AND
    HANDOFF_READINESS_PASS
```

Possible handoff-readiness evidence:

- standard startup path still works;
- baseline verification still passes;
- active work state is recorded;
- unresolved blockers are explicit;
- no undocumented half-finished state;
- next action is discoverable from repository artifacts.

This should be modeled separately from task correctness.

### HE-04 — Review feedback should be promoted into executable invariants

**State:** CANDIDATE / STRONG

Repeated human correction is evidence of a missing harness mechanism.

```text
review finding
→ classify recurring defect
→ encode check
→ design actionable failure output
→ add to normal verification path
```

Promotion candidates:

- lint rule;
- architecture dependency test;
- schema validator;
- static scanner;
- regression test;
- policy hook;
- CI gate.

This complements, rather than replaces, human review.

### HE-05 — Diagnostics are part of the agent-computer interface

**State:** CANDIDATE / STRONG

A binary failure signal wastes correction capacity.

Prefer machine/action-oriented diagnostics:

```text
FAILED
what:
observed:
expected:
likely boundary:
evidence:
repair pointer:
```

The diagnostic must not fabricate a root cause. "Repair pointer" should identify the violated contract or relevant location, not assert certainty where none exists.

This can improve self-repair loops without granting the model more authority.

### HE-06 — Context management can be expressed as four operations

**State:** CANDIDATE VOCABULARY / SOURCE-SYNTHESIZED

Useful vocabulary:

```text
SELECT    load only relevant context
WRITE     persist important state outside the window
COMPRESS  reduce historical context while preserving required state
ISOLATE   keep delegated work from polluting unrelated context
```

This vocabulary maps well onto the existing canon but should remain descriptive until independently pressure-tested.

Possible normalized mapping:

| Source term | Current domain concept |
|---|---|
| SELECT | context selection / retrieval |
| WRITE | persistence / checkpoint / external state |
| COMPRESS | context compaction / summarization |
| ISOLATE | context boundary / worker isolation |

### HE-07 — Root agent instructions should be routing infrastructure

**State:** CANDIDATE / PRIMARY-SOURCE SUPPORTED

Avoid:

```text
AGENTS.md = entire project manual
```

Prefer:

```text
AGENTS.md
  ├─ invariants
  ├─ startup path
  ├─ verification path
  ├─ authority boundaries
  └─ pointers to scoped docs
```

The actual project truth stays near the relevant code/domain artifacts.

This reduces instruction bloat and creates mechanical freshness/ownership opportunities.

### HE-08 — WIP=1 is a baseline concurrency policy

**State:** QUALIFIED CANDIDATE

Default:

```text
single agent
+ shared mutable workspace
+ no explicit ownership
→ WIP=1
```

Parallelism may be admitted when the system establishes:

- distinct ownership boundaries;
- isolated workspaces/worktrees;
- state merge/reducer semantics;
- conflict detection;
- bounded shared-state mutation;
- independent verification.

Thus S-115's WIP=1 rule is best interpreted as a safe admission baseline.

### HE-09 — Model-visible consequential observations should become durable evidence

**State:** CANDIDATE / PARTLY INSPIRED BY SOURCE BREAKDOWNS

The DeepSeek breakdown highlights a useful direction:

```text
material observation visible to model
→ trace/event/receipt
```

Do not interpret this as "log every token." The candidate concerns consequential inputs/outputs that can affect execution, decisions or verification.

Potential examples:

- tool result used for a state transition;
- test result used to mark work verified;
- permission decision;
- external side-effect receipt;
- evaluator verdict.

This requires direct DeepSeek/source-specific verification before stronger promotion.

### HE-10 — Harness components have expiry pressure

**State:** CANDIDATE / PRIMARY-SOURCE SUPPORTED

Every special harness mechanism encodes an assumption:

```text
model/runtime cannot reliably do X
→ add mechanism M
```

As models/runtimes improve:

```text
periodically test whether M is still necessary
```

Otherwise the harness accumulates its own complexity, latency, token and maintenance debt.

Candidate lifecycle:

```text
ADD
→ MEASURE
→ KEEP / MODIFY
→ RE-TEST
→ REMOVE when no longer justified
```

This is a useful complement to ordinary code/harness garbage collection.

## Candidate state machine refinement

S-115's source-level feature states are useful but its "passing is irreversible" claim should not be promoted.

A stronger revision-aware model:

```text
NOT_STARTED
     ↓
ACTIVE
 ┌───┴────────┐
 ↓            ↓
BLOCKED     VERIFIED
               ↓
        mutation / dependency drift
               ↓
         STALE / REGRESSED
               ↓
             ACTIVE
```

Key rule:

```text
verification evidence is bound to
work unit + revision + verification contract
```

A status without its evidence revision is incomplete.

## Repository-harness artifact model

A minimal practical repository harness can be described without adopting the source's conflicting five-part taxonomies.

```text
ENTRYPOINT
  routing + invariants + authority

WORK STATE
  atomic units + dependencies + current state

BOOTSTRAP
  reproducible startup / health path

VERIFICATION
  executable acceptance contracts

EVIDENCE
  receipts tied to revision

PROGRESS / DECISIONS
  durable cross-session state

HANDOFF
  restart path + blockers + next action

OBSERVABILITY
  runtime/process signals needed to diagnose and verify
```

These are artifacts/mechanisms, not new MK1 taxonomy dimensions.

## Review-feedback promotion pipeline

Candidate operational pipeline for future MK2:

```text
1. detect recurring review finding
2. assign stable defect class
3. identify enforcement boundary
4. choose deterministic check where possible
5. write agent-readable diagnostic
6. add fixture that proves the check catches the defect
7. add regression fixture proving legitimate behavior still passes
8. attach check to normal verification
9. measure false-positive / false-negative behavior
10. keep human override/escalation path where needed
```

This avoids turning every human preference into an untested lint rule.

## Clean handoff contract candidate

```yaml
session:
  objective:
  active_work_unit:
  branch_or_revision:

task_acceptance:
  status:
  evidence_refs: []

repository_health:
  startup_check:
  baseline_verification:
  dirty_state:
  temporary_artifacts:

continuity:
  decisions: []
  blockers: []
  next_action:
  changed_files: []

handoff_status:
  value: READY | QUALIFIED | BLOCKED
  reason:
```

A handoff can be `QUALIFIED` if a known blocker is explicitly documented and the next session can reproduce it without inference.

## Where S-115 should NOT change current knowledge

Do not replace the current domain taxonomy with either source five-subsystem model.

Do not replace:

```text
state / checkpoint / persistence / concurrency
memory lifecycle
human control / enforcement boundary
termination / budget enforcement
evaluation
security boundary
protocol revision
reproducibility evidence
```

with a smaller pedagogical harness tuple.

Do not treat:

- feature list;
- `AGENTS.md`;
- `init.sh`;
- progress file;
- session handoff;

as universal filenames. Their semantics matter; filenames are adapter choices.

Do not infer that:

- two agents are always better than one;
- graph > loop;
- E2E alone proves correctness;
- a clean repo proves product validity;
- a passing test is valid forever;
- a generic bootstrap script establishes reproducibility.

## Pressure tests required before promotion

### PT-HE-01 — Revision-bound verification

Mutate a dependency/configuration after a feature is verified. Confirm whether the harness can automatically mark the old evidence stale.

### PT-HE-02 — WIP baseline vs isolated parallelism

Run the same bounded workload under:

```text
A: WIP=1
B: isolated parallel workers + explicit merge contract
```

Measure outcome, latency, conflicts, rework and verification cost.

### PT-HE-03 — Diagnostic quality

Compare generic errors vs structured agent-oriented diagnostics on the same failures. Measure repair success, extra tool calls and wrong-fix rate.

### PT-HE-04 — Review-feedback promotion

Take one recurring human review issue, encode it as a check, then measure false positives and escaped defects across representative changes.

### PT-HE-05 — Handoff readiness

Interrupt work across multiple sessions. Compare repository-only recovery with and without explicit handoff artifacts.

### PT-HE-06 — Harness pruning

Remove one harness component believed to be obsolete under a newer model/runtime. Measure whether task reliability materially changes.

## Promotion boundary

Potential future destinations after pressure testing:

```text
HE-01/02  → MK2 verification / authority contracts
HE-03     → MK2 lifecycle / resumability contract
HE-04/05  → MK2 feedback + enforcement contracts
HE-06/07  → context / repository-legibility guidance
HE-08     → concurrency admission policy
HE-09     → observability / receipt contract
HE-10     → harness lifecycle / simplification policy
```

Current state remains:

```text
SOURCE
  ↓
QUARRY
  ↓
pressure tests
  ↓
MK normalization/operationalization only if evidence passes
```

No current MK1 gate is closed or reopened merely by adding S-115.
