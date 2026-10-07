# Quarry — Learning Science Primitives

Source: `../mining-site/S-002-learning-science.md`  
Status: **NON-CANONICAL / MK0 input**

## Candidate mechanisms

### LS-01 Retrieval as learning, not just measurement

Candidate: use low-stakes retrieval opportunities where durable recall/availability of knowledge matters.

Boundary:

- feedback and task design matter;
- evidence is broad but culturally/geographically imbalanced;
- retrieval must not replace application/transfer tasks.

### LS-02 Worked examples before unsupported problem solving for novices

Candidate: technical lessons may use worked examples, code tracing, subgoal labeling or incomplete examples before fully independent tasks.

Boundary:

- learner expertise matters;
- worked examples are not a permanent substitute for independent performance;
- transfer still needs assessment.

### LS-03 Spacing as a scheduling strategy

Candidate: revisit important capabilities across time instead of assuming one exposure is enough.

Boundary:

- current recent meta-analytic evidence inspected is concentrated in medical/health education;
- do not hardcode one spacing interval;
- hold as `EVIDENCE_CANDIDATE` until dogfood.

### LS-04 Formative assessment is part of instruction

Candidate: use assessment evidence to adapt next instructional steps and provide useful feedback.

Boundary:

- do not equate feedback frequency with quality;
- available meta-analysis inspected has geographical/context limitations.

## Compiler implication

Add an **instructional-strategy selection** stage after outcomes/prerequisites and before lesson rendering.

Each selected strategy should state:

```yaml
strategy:
target_outcome:
learner_expertise:
evidence_basis:
expected_mechanism:
when_not_to_use:
verification:
```

## Rejection

Do not create a universal "science-backed course recipe" from effect sizes.
