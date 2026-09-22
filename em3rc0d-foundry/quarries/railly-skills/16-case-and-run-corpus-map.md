# Railly Skills — Case and Run Corpus Map

Provenance: OBSERVED
Source: complete pinned Git tree inventory + cases/README.md

## Why map the corpus

The Foundry’s methods are not supported equally.

Artifact volume is not quality, but corpus shape tells us where the system has most real feedback.

## Cases tree

The pinned cases/ tree has 113 files total.

Important distinction:

- 28 are repository conventions files;
- cases/README.md is inventory;
- agent-browser/session-observations.md is cross-case observation;
- remaining case-like files include validated, contributor-validated and unvalidated/backfill records with different status.

Do not report 113 “validated cases”.

## Case concentration by repository/surface

Largest case directories by file count:

- agent-browser: 35 files;
- portless: 26;
- wterm: 16;
- json-render: 5;
- vercel-labs-emulate: 3;
- skills: 3;
- native: 2;
- ovation: 2;
- many other repos: one convention/case file each.

INFERRED: much of the Foundry’s failure vocabulary was harvested from a few deeply worked systems. Transfer evidence therefore matters.

## Run corpus concentration

Pinned foundry/runs artifact counts:

| Run family | Files |
|---|---:|
| review-gate | 616 |
| solution-gate | 149 |
| security-review-eval | 38 |
| resilience-audit | 21 |
| xref | 18 |
| proposal-impact | 15 |
| test-strength | 15 |
| spec | 8 |
| before-after | 4 |
| software-factory | 3 |
| quality-baseline | 2 |

Again: a file count is not an independent run count or success rate.

## What the corpus supports strongly

Relative to other skills, the source itself identifies stronger evidence around:

- Review Gate repeated application and blind answer-key comparison;
- Solution Gate repeated runs;
- Test Strength applied mutations;
- xref repeated graph runs;
- selected quality/resilience/security cases.

## What remains weak

The compiled knowledge coverage explicitly exposes gaps for:

- before-after public application provenance;
- handoff repository case;
- herdr-workstreams full dogfood;
- performance-proof application;
- software-factory full staged real-work run;
- trail-decisions published procedure run;
- work-intake real application set;
- several transfer/baseline comparisons.

## How EM3RC0D should use the corpus

Use these artifacts for:

- failure-shape mining;
- schema examples;
- evidence-boundary examples;
- negative examples;
- eval fixture inspiration.

Do not inherit their maturity into our own environment.

The raw run/case files remain retrievable under:

research-corpora/railly-skills-2026-09-22/upstream/

A future EM3RC0D claim should cite the specific upstream file when the exact historical detail matters.
