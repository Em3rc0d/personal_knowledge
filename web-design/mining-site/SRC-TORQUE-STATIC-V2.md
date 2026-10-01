# SRC-TORQUE-STATIC-V2 — Static componentized commercial landing

Status: **INTERNAL OBSERVED / GENERATED PRESSURE TEST**  
Observed: **2026-10-01**

## Identity

| Field | Value |
|---|---|
| ID | `SRC-TORQUE-STATIC-V2` |
| Type | internal prototype / worked website experiment |
| Product shape | premium automotive workshop commercial landing |
| Delivery target | static HTML + CSS + JavaScript + local image assets |
| Cost constraint | no paid runtime API; no server/SSR requirement; no GitHub Actions required for the prototype |
| Role in this domain | pressure test for component-system quality under a static-delivery constraint |
| Provenance | `OBSERVED` for prototype behavior/structure; `GENERATED` for generalized rules |

## Problem tested

The prototype asked whether a website could preserve:

- cinematic narrative;
- responsive behavior;
- accessible interaction primitives;
- reusable component discipline;
- strong commercial hierarchy;
- rich visual states and microinteraction;

while keeping the shipped runtime close to:

    index.html
    styles.css
    app.js
    assets/

and avoiding a framework/server requirement that the product did not need.

## Iteration evidence

### V1 — cinematic story, weak static sections

The first version proved the scroll-led visual story but exposed a discontinuity: sections without imagery became visibly flatter and more static than the immersive story.

Observed lesson:

    strong hero/story motion
    + flat downstream sections
    = broken experiential continuity

A visually premium page needs atmospheric continuity, not only one impressive section.

### V2 — static runtime, stronger component system

The second version kept static delivery but reorganized the UI around:

    tokens
      ↓
    primitives
      ↓
    domain components
      ↓
    compositions
      ↓
    interaction/state

Examples included interactive service selection, native disclosure/FAQ behavior, richer CTA composition, visual state changes, reveals and domain-specific components.

## High-value observations

### 1. Component discipline is independent of framework choice

A component can be a semantic/visual/interaction contract even when the final artifact is plain HTML/CSS/JS.

`shadcn/ui` is therefore useful as a reference for component discipline — variants, states, accessibility and composition — without requiring its React implementation to be shipped.

### 2. Authoring stack and delivery runtime are different decisions

Do not collapse:

    how we author
    =
    what the browser must execute

A project may use a component-oriented authoring model while still shipping a static artifact.

### 3. Native browser primitives can carry meaningful interaction

Where they satisfy the contract, prefer semantic native primitives such as:

- `button`;
- `details` / `summary`;
- `dialog`;
- anchors and landmarks;
- CSS state and media queries;

before adding a client framework solely for interaction plumbing.

### 4. Domain components should sit above generic primitives

Useful layering:

    primitive
      ↓
    visual variant
      ↓
    domain component
      ↓
    product composition

Example:

    Button → TorqueButton → WhatsAppCTA

or:

    tab primitive → ServiceSelector → InteractiveServiceDeck

The product should not look like the component library used to build it.

### 5. Commercial pages must not expose implementation-meta copy

Technical explanations such as `parallax`, `crossfade` or `reduced motion` are implementation knowledge, not customer value propositions.

Internal mechanism should be translated into domain value:

    implementation explanation
      ↓
    customer-relevant promise / evidence

### 6. Static sections still need state and atmosphere

Motion is not limited to hero video. Continuity can come from:

- hover/focus states;
- scroll reveals;
- interactive selection;
- background light/texture;
- imagery tied to component state;
- progressive disclosure;
- animated but restrained separators/progress;
- responsive composition changes.

### 7. Framework tax must be justified by product needs

A heavier runtime should be introduced because the product requires capabilities that materially benefit from it, not because component quality is mistakenly equated with React/Next.

This is a `GENERATED` candidate rule, not a universal prohibition on frameworks.

## What this source does not prove

- that static HTML/CSS/JS is always cheaper at every traffic/deployment configuration;
- that React/Next is inappropriate for complex applications;
- full WCAG conformance;
- performance superiority without controlled measurement;
- cross-browser correctness beyond the prototype checks performed;
- that shadcn visual styling should be copied.

## Reusable pressure-test question

Before adopting a runtime/framework, ask:

> Which user-visible or operational requirement becomes materially easier or safer because this runtime ships to production?

If the answer is only `we want components`, first test whether the component contract can remain framework-independent.
