# Diagram Engineering — MK0 v2 results

**2026-10-08 · controlled local iteration · no external certification**

## Fixed from previous visual/semantic review

- ECHO: SourceRegistry + Supervisor, WindowProducer, InferenceScheduler, ModelRunner and explicit `RAW_INFERENCE` return; separate MQTT and result-store branches.
- NINFA: fact-check separated from drafting, narration and visual evidence shown in parallel, human approval required, analytics feedback loop.
- personal_knowledge: three governance zones, failed source check → HOLD/BLOCKED; verified sources through mining/quarries and staged development → MK gate → main; material-use condition for receipts.
- Each HTML includes pinned source SHA, visual connection annotations, a keyboard-focusable scroll region, a mobile scroll hint, an explicit textual description of every directed edge, notes on omissions and local-only CSS/fonts.

## Local executed evidence (not a GitHub CI run)

| Case | Nodes | Edges | Static verifier | Desktop/mobile |
|---|---:|---:|---|---|
| ECHO | 11 | 11 | PASS | PASS / PASS |
| NINFA | 9 | 10 | PASS | PASS / PASS |
| personal_knowledge | 11 | 10 | PASS | PASS / PASS |

12 deliberate negative mutations were rejected: inline executable handler, remote CSS import, empty path, changed SHA, blank SVG title, removed inference return, invalid endpoint, diagonal path, remote hyperlink, removed textual alternative, weak contrast and missing textual edge.

Local Chromium inspection used 1440px desktop and 390px mobile. No page errors, no overflowing node labels or whole-page horizontal overflow; scrolling was observable and cue visible on mobile.

Files shipped: `outputs/*.html`, `layout_spec_v2.json`, `graph_contract.json`, `verify_pilot.py`, `test_adversarial.py`.

## What tests DO NOT prove

- These checks are syntactic/structural; they do not prove that the SVG interpretation is semantically equivalent to its canonical source.
- We have not run the upstream Diagram Design `self_check` or `lint-render` on these generated HTMLs.
- Browser checks are local, not third-party accessibility certification, nor a complete WCAG/print audit.
- No blind reader A/B, actual total token usage, or author/review-time reduction has been measured.

**Gate: HOLD.** Do not merge this branch into `main` or use generated overviews as canonical architecture diagrams until human review and independent evidence are available.
