# Railly Skills — Design and Product Output

Provenance: OBSERVED + INFERRED
Primary upstream: before-after skill and references, www/

## Scope

Railly/skills is primarily an engineering-method Foundry, not a complete product-design system. The detailed design infrastructure seen in other Railly ecosystem repositories is outside S-001.

Within this corpus, the most relevant product-output mechanism is **Before After**.

## Visual proof is evidence work

before-after does not treat screenshots as decoration.

It freezes:

- exact baseline state;
- exact changed state;
- URL;
- data/auth/session;
- interaction;
- readiness signal;
- selector;
- viewport;
- DPR;
- theme;
- zoom.

The same element/state should be compared on the same basis.

## Smallest meaningful visual boundary

Default capture is the smallest element that still provides enough context.

A full-page screenshot is discouraged when it hides the actual delta and introduces unrelated changes.

This maps directly to evidence quality: reduce visual confounders.

## Semantic readiness

The capture protocol prefers semantic readiness such as:

- expected text;
- URL;
- element state;

over arbitrary sleep.

This converts visual proof into a more reproducible protocol.

## Pixel diff is supporting evidence

Pixel difference detects that pixels changed.

It does not decide whether the product is correct.

Likewise:

- two settled screenshots cannot prove flicker;
- screenshots cannot prove timing;
- visual parity cannot prove hidden state/resource properties.

Temporal claims need video/ordered states/runtime evidence.

## Honest baseline hierarchy

Preferred:

1. baseline captured before implementation;
2. separate exact baseline and changed builds;
3. safely reconstructed baseline with preserved diff;
4. existing screenshot with provenance;
5. deterministic simulation clearly labelled.

A simulated/reconstructed baseline must not be presented as live.

## Evidence package

The skill packages:

- before.png;
- after.png;
- diff.png;
- HTML review surface;
- JSON manifest;
- assets.

The HTML is designed for both quick appreciation and exact audit.

## Visual composition rules inside source

The Vercel visual reference emphasizes:

- comparison dominates first viewport;
- same visual basis for peers;
- fast first read + exact audit path;
- strong whitespace/alignment;
- monochrome by default;
- color only for semantic distinction;
- mono typography only for technical tokens;
- restrained surfaces/radii;
- semantic tables;
- accessible focus/labels;
- responsive reflow before shrinking text;
- stillness/reduced motion.

It explicitly rejects decorative gradient/glow/blob/glass/card-wall treatments.

## EM3RC0D adaptation

INSPIRED:

The Foundry should make **presentation-quality evidence** a product of the build process, not a marketing afterthought.

But EM3RC0D should not inherit Vercel’s visual identity as canon.

Instead, connect future Foundry proof artifacts to the existing EM3RC0D web-design system:

    visual evidence
      → DESIGN.md
      → provenance-tagged tokens/rules
      → components
      → visual verification
      → reusable presentation artifacts

A product release should be able to generate reviewable screenshots/demos/evidence without redesigning the communication layer from scratch.
