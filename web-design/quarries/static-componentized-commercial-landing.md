# Static Component Systems for Premium Commercial Websites

Source: [`SRC-TORQUE-STATIC-V2`](../mining-site/SRC-TORQUE-STATIC-V2.md)

Status: **QUARRY / NON-CANONICAL**

## Candidate model

Separate four layers that are often collapsed:

    DESIGN CONTRACT
          ↓
    COMPONENT CONTRACTS
          ↓
    AUTHORING IMPLEMENTATION
          ↓
    DELIVERY RUNTIME

A strong design system should survive substitution of the authoring framework when its semantic contracts remain intact.

## Component architecture

Candidate layering:

    tokens
      ↓
    primitives
      ↓
    variants
      ↓
    domain components
      ↓
    section compositions
      ↓
    page experience

### Primitive

Lowest reusable semantic interaction/surface: button, disclosure, tab/select pattern, separator, badge, panel, dialog.

### Variant

Maps the primitive into the design language: emphasis, density, destructive/primary/quiet states, surface depth, motion behavior.

### Domain component

Names user/product meaning rather than implementation:

- `WhatsAppCTA`;
- `ServiceSelector`;
- `WorkshopStoryStop`;
- `TrustSignal`;
- `DiagnosticProcess`.

### Composition

Combines components around a page job: explain process, compare services, establish trust, convert contact.

## Static-first does not mean visually static

`static delivery` means the deployment artifact does not require a server/client application runtime for its core page. It does **not** imply no motion, no state or no interaction.

A static site can still support:

- scroll-linked state;
- parallax transforms;
- crossfades;
- tab/disclosure interaction;
- native dialogs;
- responsive substitutions;
- focus/hover states;
- reduced-motion behavior;
- local media and progressive loading.

## Shadcn lesson without shadcn dependency

The reusable value is not the default visual skin. It is the discipline of:

- explicit variants;
- predictable states;
- accessible primitives;
- composability;
- local ownership/customization;
- separating generic primitives from product-specific compositions.

Candidate rule:

> Borrow component contracts and interaction discipline; do not force the source library's runtime or visual identity into products that do not need them.

## Runtime budget as a design constraint

Treat runtime complexity like any other constrained resource.

Ask for each dependency:

1. Which requirement does it satisfy?
2. Is that requirement runtime or authoring-only?
3. Can a native browser primitive satisfy it?
4. Does it increase hosting/runtime/maintenance surface?
5. What breaks if it is removed?

Framework adoption should be evidence-bearing, not aesthetic.

## Experiential continuity

A page can fail coherence even when every individual section is polished.

Observed failure shape:

    immersive story
    → abrupt flat grid
    → static explanatory copy
    → sparse CTA

Candidate response:

    maintain a shared atmosphere
    + stateful downstream components
    + visual rhythm
    + domain-relevant imagery
    + restrained motion

without turning every section into spectacle.

## Content boundary

Do not expose internal build rationale as commercial copy.

Bad customer-facing content:

- `Scroll narrativo`;
- `Parallax 2.5D`;
- `Crossfade controlado`;
- `Fallback accesible`.

Better abstraction:

- how diagnosis works;
- what the customer can expect;
- what evidence is shown;
- why the process reduces uncertainty;
- how to take the next action.

Implementation knowledge belongs in the design/build documentation.

## Promotion boundary

Supported as an internal worked pattern:

- framework-independent component layering;
- static delivery with interactive behavior;
- generic primitive → domain component separation;
- customer-value copy separated from implementation-meta copy;
- experiential continuity as a page-level requirement.

Still requires cross-source pressure testing before certification:

- framework-selection thresholds;
- performance-cost claims;
- universal component taxonomy;
- exact static-vs-framework decision matrix.
