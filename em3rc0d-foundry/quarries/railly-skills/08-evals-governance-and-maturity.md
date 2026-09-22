# Railly Skills — Evals, Governance and Maturity

Provenance: OBSERVED + INFERRED
Primary upstream: foundry/governance.md, eval-protocol.md, maturity.json, rounds/

## Two independent axes

### Distribution channel

Answers: how strongly should the catalog recommend installation?

- stable;
- candidate;
- experimental.

### Evidence maturity

Answers: what has actually been demonstrated?

- experimental;
- dogfooded;
- evaluated;
- validated;
- deprecated.

A stable package can still be only dogfooded/evaluated. Channel does not upgrade evidence.

## Candidate lifecycle

Governance also separates a proposed method’s decision state:

    observed
      → candidate
      → evaluated
      → reviewed
      → promoted
      → deprecated

Only promoted procedure enters runtime distribution.

## Evaluation matrix

The standard comparison is:

- no skill;
- released/current skill;
- candidate skill.

Hold constant:

- repository snapshot;
- model;
- tools;
- permissions;
- user prompt.

Use:

- at least one originating case;
- at least one transfer holdout;
- positive trigger;
- near-miss negative trigger.

## Evaluation layers

### Trigger

Does the procedure invoke only when it should?

### Method

Did required gates/order happen?

### Outcome

Did the claimed evidence actually occur?

### Transfer

Does the method work outside the originating repo/stack?

### Regression

Does candidate improve intended behavior without losing current behavior?

## Evidence classes inside evals

The protocol distinguishes:

- agent-demonstrated evidence;
- artifact evidence;
- grader reconstruction.

A later grader can verify artifact state. It cannot retroactively prove that the evaluated agent performed a required method step.

## Promotion threshold

A candidate must:

- preserve safety/provenance/confidentiality;
- avoid regressions against released behavior;
- improve at least one target failure;
- beat no-skill baseline on intended behavior;
- pass trigger and near-miss cases;
- pass transfer holdout;
- receive human review.

If candidate changes prose but observable behavior is equal, do not promote it.

## Judge discipline

Use deterministic checks whenever possible.

Use a judge only for contextual behavior not reducible to deterministic artifacts.

The judge receives rubric + evidence, not the candidate’s “intended answer”.

## Evolution rounds — important lessons

### Round 001

Candidate skill additions tied current method at 20/20.

Decision: reject skill change; keep new evaluation infrastructure.

Lesson:

    no measured behavioral delta = no procedural promotion

### Round 002

Blind review replication exposed catches, misses and wrong-layer verification.

Lesson:

    evals must measure failure modes in the method itself, not merely final answer quality

### Round 004

Broad Unfold umbrella had little observed operational use while smaller phase-specific methods carried real work.

Decision: archive/deprecate umbrella, preserve source/evals, adopt phase-neutral contracts.

Lesson:

    broad orchestration should earn itself from use; decomposition can be a success

### Round 006

Invocation/name matches were checked against cases/runs.

Only actual method application supported maturity changes.

Lesson:

    usage telemetry is a lead, not evidence of benefit

### Round 007

Human override advanced some maturity/channel decisions while preserving explicit evidence debt.

Lesson:

    human authority can decide policy, but must not rewrite evidence history

### Round 011 / software-factory

The source explicitly records overlap risk and says a first real run that cannot demonstrate coordination value may justify deprecation.

Lesson:

    even architecturally attractive abstractions are provisional until they earn their cost

### Round 014 / security-review

Five-case comparison: skill 18/18 assertions vs no-skill 16/18 in one trial per configuration.

The source labels it evaluated, not validated, because transfer/repeated trials are missing.

Lesson:

    one positive benchmark is evidence, not universal validation

## EM3RC0D adaptation

INSPIRED:

Every reusable asset class should have an evidence lifecycle appropriate to its risks.

Do not force skill-style evals onto all artifacts. A code primitive, design component and research method may require different proof.

But preserve one invariant:

    promotion state must be justified by retrievable evidence, not reputation or enthusiasm
