# Accessibility and Inclusive Learning

Status: **MK0 candidate / GENERATED**, informed by S-004.

## Two distinct layers

### Web/content accessibility

For first-party web-delivered educational surfaces, the default quality target is **WCAG 2.2 Level AA**, unless the product declares a different medium-specific requirement and documents why.

WCAG is a conformance-oriented accessibility standard.

### Inclusive learning design

CAST UDL Guidelines 3.0 are used as a design lens for reducing barriers through options around:

- engagement;
- representation;
- action and expression.

UDL is not treated as a substitute for WCAG conformance.

## Product requirements

A digital product should declare:

```yaml
delivery_medium:
accessibility_target:
supported_input_modes:
caption_transcript_policy:
keyboard_policy:
visual_contrast_policy:
motion_policy:
document_accessibility:
assessment_accommodations:
known_limitations:
```

## Compiler implications

The compiler should ask:

- Can essential information be perceived without one exclusive sensory channel?
- Can essential actions be completed without a mouse where the medium is web?
- Are video/audio alternatives available where needed?
- Are diagrams explained sufficiently for the learning objective?
- Does reduced motion preserve instructional meaning?
- Can learners demonstrate an outcome through an alternative expression mode without changing the construct being assessed?

## Assessment boundary

Accessibility support must preserve the intended construct.

If an accommodation changes what is actually being measured, the assessment interpretation must be re-evaluated rather than pretending equivalence.

## Anti-patterns

- `accessible PDF` assumed because it visually looks clean;
- captions added only after release;
- inaccessible code/lab tooling treated as learner failure;
- UDL used as a compliance badge;
- WCAG conformance used as proof of pedagogical quality.
