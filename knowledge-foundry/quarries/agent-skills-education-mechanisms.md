# Quarry — Agent Skills → Educational Mechanisms

Source: `../mining-site/S-001-agent-skills.md`  
Status: **NON-CANONICAL / MK0 input**

## Purpose

Extract mechanisms that may improve a knowledge-to-course compiler without promoting upstream implementation choices directly.

| Observed mechanism | Educational translation candidate | Status |
|---|---|---|
| precise skill triggers | explicit audience/prerequisite and "when this lesson applies" contracts | ADAPT |
| progressive disclosure | layered lessons + optional deep references | ADAPT |
| process over knowledge | capability/workflow-centered teaching rather than encyclopedia chapters | ADAPT |
| verification checklist | observable lesson exit criteria | ADAPT |
| anti-rationalization tables | misconception + shortcut handling | ADAPT |
| routing evals | test whether learners choose the right technique for a scenario | EXPLORE |
| behavioral evals | artifact/lab grading against expectations | ADAPT |
| pressure evals | transfer tests under time/authority/ambiguity pressure | EXPLORE |
| context budgeting | limit prerequisite/background material per lesson | ADAPT |
| greenfield/brownfield adoption | differentiated learner paths based on starting state | EXPLORE |
| shallow orchestration | avoid curricula that require repeated lossy summaries between modules | INSPIRED |

## Candidate rules

### KF-C01 — Teach capabilities, not source structure

Do not mirror a repository table of contents as a curriculum. Extract the learner capability first.

### KF-C02 — Every significant outcome needs observable evidence

A learner saying "I understand" is not evidence. Prefer an artifact, decision, diagnosis, implementation or defensible explanation.

### KF-C03 — Misconceptions belong in the lesson contract

Known shortcuts and rationalizations should be surfaced where the learner is likely to make them.

### KF-C04 — Progressive disclosure is a compiler concern

The compiler should separate core path from deep reference so lessons do not become context dumps.

### KF-C05 — Assessment routing is distinct from assessment execution

Two different competencies may exist:

1. recognizing which method applies;
2. executing that method correctly.

Both may need separate evaluation.

## Explicit rejections

- Do not copy the 25 skills into a course.
- Do not use repository popularity as proof of educational quality.
- Do not assume agent behavioral evals map 1:1 to human learning assessment.
- Do not treat upstream wording as our canonical terminology.
- Do not infer that MIT covers third-party linked assets.

## Open questions created by this quarry

- How much of pressure testing transfers usefully from agent evaluation to learner evaluation?
- Should a lesson have trigger-negative cases analogous to skill routing negatives?
- What is the minimum assessment evidence before a product may claim a learning outcome?
- How do we version a course when the underlying domain canon changes?
