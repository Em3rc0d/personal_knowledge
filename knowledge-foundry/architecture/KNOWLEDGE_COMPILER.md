# Knowledge Compiler — MK0 Architecture Draft

Provenance: **GENERATED**, informed by current `personal_knowledge` governance and S-001 through S-006.

Status: **DRAFT / not validated**

## Objective

Compile trustworthy knowledge into an educational artifact without duplicating source canon, losing provenance, overstating learning evidence or inheriting unknown rights.

## Compiler stages

### 1. Domain eligibility

Apply `DOMAIN_INPUT_CONTRACT.md`.

The unit of admission is a **bounded knowledge slice**, not a folder or entire domain.

Capture:

- authority;
- maturity/promotion state;
- exact revision;
- evidence path;
- contradictions/unknowns;
- freshness;
- rights boundary;
- allowed claim scope.

### 2. Candidate extraction

Extract a bounded teachable capability, not an arbitrary chapter topic.

Good:

> Design an agent skill with explicit triggers, workflow and verification.

Weak:

> Everything about AI agents.

### 3. Learner contract

Define:

- target learner;
- prerequisites;
- starting capability;
- desired observable capability;
- non-goals;
- delivery constraints.

### 4. Concept dependency graph

Represent which concepts/capabilities depend on which others.

A curriculum is an ordering of dependencies, not a list of interesting topics.

### 5. Learning outcomes

Each significant outcome must be observable and have an assessment path.

Prefer:

`Design a skill trigger description that distinguishes positive and negative routing cases.`

over:

`Understand skill routing.`

### 6. Instructional-strategy selection

Select teaching mechanisms based on the outcome, learner expertise and evidence.

Candidate mechanisms from S-002 include:

- retrieval practice;
- worked examples;
- spacing;
- formative assessment/feedback.

Each selection records:

```yaml
strategy:
target_outcome:
learner_expertise:
evidence_basis:
applicability:
when_not_to_use:
verification:
```

Do not create a universal recipe from an effect size.

### 7. Instructional units

A lesson spec may contain:

- outcome;
- prerequisite nodes;
- minimal explanation;
- worked example where justified;
- misconception/anti-pattern;
- retrieval/practice opportunity where justified;
- evidence pointers;
- exit check;
- accessibility/inclusion requirements.

Progressive disclosure is preferred over context dumping.

### 8. Labs

Labs should test application in a realistic artifact.

A lab needs:

- task;
- constraints;
- fixture/context;
- expected evidence;
- failure cases;
- grader/rubric;
- accessibility/tooling boundary.

### 9. Assessment

Use `ASSESSMENT_EVIDENCE_MODEL.md`.

Important outcomes should include direct or transfer-oriented evidence appropriate to the verb/claim.

Keep distinct:

- practice feedback;
- outcome evidence;
- certification-like claims.

Never silently map completion or satisfaction to mastery.

### 10. Accessibility and inclusion

Use `ACCESSIBILITY_AND_INCLUSION.md`.

For web-delivered first-party surfaces, evaluate WCAG 2.2 AA as the initial internal dogfood target.

Use UDL 3.0 as a barrier-reduction/inclusive-design lens, not as a conformance badge.

### 11. Rights + dependency manifest

Use:

- `RIGHTS_AND_LICENSING.md`;
- `KNOWLEDGE_DEPENDENCY_MANIFEST.md`.

Every product must answer:

- Which canonical nodes support this?
- Which exact revisions were compiled?
- Which external sources influenced this?
- What may be reproduced/adapted?
- What is reference-only?
- What attribution is required?
- What change would make this product stale?

### 12. Pilot

Run with target learners or a defensible proxy.

Capture only what is necessary:

- outcome evidence;
- incorrect mental models;
- friction points;
- accessibility barriers;
- assessment performance;
- feedback;
- required revisions.

Follow `PILOT_DATA_BOUNDARY.md`; raw learner-identifiable evidence does not belong in this public repository.

### 13. Promotion

A product may advance only when its declared gates pass.

A valid result may be:

- promote;
- revise;
- hold;
- kill;
- inconclusive.

## Candidate durable artifact set

```text
DOMAIN_INPUT_RECORD
PRODUCT_BRIEF
AUDIENCE_PREREQUISITES
CONCEPT_GRAPH
LEARNING_OUTCOMES
INSTRUCTIONAL_STRATEGY_MAP
CURRICULUM
LESSON_SPECS
LAB_SPECS
ASSESSMENT_SPEC
ACCESSIBILITY_PROFILE
SOURCE_RIGHTS_MANIFEST
KNOWLEDGE_DEPENDENCY_MANIFEST
PILOT_DATA_PLAN
PILOT_RECEIPT
RELEASE_RECEIPT
```

MK0 must validate whether these artifacts earn their maintenance cost. They are candidates, not mandatory canon.

## Design principles

- compile, do not duplicate;
- bounded eligibility before compilation;
- outcome before content volume;
- dependency order before chapter aesthetics;
- evidence-bounded instructional strategy;
- assessment interpretation before score;
- transfer before memorization for performance claims;
- progressive disclosure over context flooding;
- misconceptions are instructional data;
- accessibility is designed, not patched;
- source provenance and rights survive transformation;
- pin knowledge dependencies and define staleness;
- collect the least learner data necessary;
- course maintenance and retirement are first-class lifecycle concerns.
