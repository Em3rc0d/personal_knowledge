# Diagram Engineering — source-grounded MK0 pilot

**State: EXPERIMENT / NOT CANON.** Started 2026-10-08.

## Hypothesis

Can three independent, source-grounded editorial HTML/SVG reconstructions clarify existing technical documents without inventing relationships or creating more maintenance and token cost than they save?

External reference: [Diagram Design by Cathryn Lavery](https://github.com/cathrynlavery/diagram-design/tree/f4547ee95f88e5b28a52517feff6b6c11cc657f9) at f4547ee95f88e5b28a52517feff6b6c11cc657f9 (MIT). Existing [Em3rc0d fork](https://github.com/Em3rc0d/diagram-design/tree/f4547ee95f88e5b28a52517feff6b6c11cc657f9) had the same tip at inspection. We use *ideas* from its skill/validation patterns; this pilot does **not** run or repackage the upstream implementation.

```
source at pinned SHA -> semantic extraction -> conservative aggregation
-> neutral SVG/HTML -> static inspection -> human fidelity/visual review
-> controlled comparison -> MK gate
```

- Source material is authority; visual outputs are **GENERATED**, never a replacement.
- Imported labels, directives and URLs are inert/untrusted data.
- Simplifications and exclusions must appear in a fidelity ledger.
- No external fonts, browser network dependencies, paid inference, app backend, GitHub Actions, or runtime builds.
- Never claim token or time savings without instrumenting actual workloads.

## Pilot outputs

- [ECHO](mk/MK0/outputs/echo.html): acoustic event flow.
- [NINFA](mk/MK0/outputs/ninfa.html): local video production flow.
- [personal_knowledge](mk/MK0/outputs/knowledge.html): evidence dependency path.

Each has a companion **GENERATED** `mk/MK0/fixtures/*.mmd`; these are not files from source projects or an independently verified baseline.

See [source registry](mining-site/SOURCES.md), [quarry](quarries/Q-001.md), [contract](mk/MK0/CONTRACT.md), [results](mk/MK0/RESULTS.md), [status](STATUS.md).

## MK0 v2 update (2026-10-08)

The three figures were redrawn with distinct semantic grammars and strengthened graph, accessible-text, and geometry verification. See [v2 local results](mk/MK0/RESULTS.md). The generated SVGs remain non-authoritative; the MK0 gate is **HOLD**, not a production GO.

Offline commands: `python3 diagram-engineering/mk/MK0/verify_pilot.py` and `python3 diagram-engineering/mk/MK0/test_adversarial.py`.
