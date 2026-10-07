# Assessment Evidence Model

Status: **MK0 candidate / GENERATED**, informed by S-003.

## Principle

An assessment score is evidence only for a **specific interpretation and use**.

Do not collapse:

```text
completed quiz
→ understands
→ can apply
→ can transfer
→ is certified
```

Each arrow needs evidence.

## Minimum assessment contract

```yaml
outcome_id:
construct_or_capability:
assessment_task:
evidence_expected:
scoring_rubric:
interpretation:
intended_use:
validity_evidence:
reliability_plan:
fairness_accessibility:
decision_rule:
limitations:
pilot_population:
confidence:
```

## Evidence strength by claim

### Practice feedback

Low-stakes checks may use:

- self-check;
- automated unit checks;
- simple rubric;
- immediate formative feedback.

They must not be described as certification.

### Outcome validation

Important outcomes should include direct evidence such as:

- produced artifact;
- diagnosis of a faulty artifact;
- implementation under constraints;
- explanation/defense of trade-offs;
- transfer task with changed surface details.

### Certification-like claims

If a product later grants a credential or makes strong mastery claims, require stronger evidence around:

- validity of the intended score interpretation;
- reliability/consistency;
- fairness;
- accessibility;
- sufficient sampling of the capability;
- decision thresholds;
- false-positive/false-negative risk;
- scoring transparency and review.

## Alignment rule

A product is internally aligned when:

```text
learning outcome
↕
assessment
↕
instructional activity
↕
materials/examples
↕
technology/delivery constraints
```

An assessment must not measure a capability the learning path did not provide a fair opportunity to develop.

## Routing vs execution

Where the capability includes choosing the appropriate method, assess separately:

1. **selection/routing** — can the learner recognize when a method applies?
2. **execution** — can the learner perform it correctly?

This is a candidate pattern, not mandatory for every outcome.

## Fairness boundary

Assessment difficulty must come from the intended construct, not irrelevant barriers such as inaccessible presentation, ambiguous wording, unnecessary language complexity or tooling that is not part of the capability being measured.

## Promotion rule

A pilot may say:

- `OUTCOME_EVIDENCE_PRESENT`;
- `OUTCOME_EVIDENCE_WEAK`;
- `INCONCLUSIVE`;
- `FAIL`.

It may not silently promote `completion rate` or learner satisfaction into proof of learning.
