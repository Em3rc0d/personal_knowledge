# Architecture — Content-to-Opportunity Funnel

## System model

```text
                     ┌─────────────────────┐
                     │   Reach Engine      │
                     │ SQL / basics / traps│
                     └─────────┬───────────┘
                               │
                               v
                     ┌─────────────────────┐
                     │ Feed discovery      │
                     │ outside network     │
                     └─────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  v                         v
        ┌──────────────────┐      ┌────────────────────┐
        │ save / react     │      │ profile visit      │
        │ algorithmic loop │      │ conversion hinge   │
        └────────┬─────────┘      └─────────┬──────────┘
                 │                          │
                 │                          v
                 │                ┌────────────────────┐
                 │                │ follow / Featured  │
                 │                └─────────┬──────────┘
                 │                          │
                 └──────────────┐           v
                                │ ┌────────────────────┐
                                └>│ deeper content     │
                                  │ authority / proof  │
                                  └─────────┬──────────┘
                                            │
                                            v
                                  ┌────────────────────┐
                                  │ conversation / DM  │
                                  └─────────┬──────────┘
                                            │
                                            v
                                  ┌────────────────────┐
                                  │ opportunity        │
                                  │ job/client/referral│
                                  └────────────────────┘
```

## Current bottleneck

Observed baseline:

- unique reach: 30,302;
- profile views: 125;
- reach → profile ≈ 0.41%.

Therefore the current bottleneck is not basic discovery. It is the transition:

```text
DISCOVERY → PROFILE → FOLLOW / CONVERSATION
```

## Control surfaces

### Content surface

Controls:

- topic;
- hook;
- visual format;
- post role;
- CTA;
- timing;
- technical depth.

### Profile surface

Controls:

- headline;
- About;
- Featured;
- project proof;
- portfolio/GitHub/contact;
- consistency with content identity.

### Conversation surface

Controls:

- CTA quality;
- comment replies;
- DM follow-up;
- clarity of contact path;
- opportunity qualification.

### Measurement surface

Controls:

- post-role tags;
- topic tags;
- profile CTR;
- save/comment/share ratios;
- follower growth;
- opportunity ledger;
- outcome attribution.

## Failure modes

1. **Reach without identity** — viral post, no profile interest.
2. **SQL identity collapse** — audience recognizes only SQL.
3. **Tutorial-only perception** — useful teacher, weak builder evidence.
4. **Generic AI dilution** — broad audience, low technical/commercial credibility.
5. **Proof without accessibility** — deep content that fails acquisition.
6. **Commercial overreach** — posts feel like ads rather than useful engineering.
7. **Vanity optimization** — likes rise while opportunities remain flat.
8. **Cadence fatigue** — volume starts reducing marginal reach/quality.
9. **Repetition** — same hook/angle weakens novelty.
10. **Attribution blindness** — opportunities occur but system cannot learn why.

## Design principle

Each post should be assignable to one primary job. If a post has no clear role in the funnel, it is a weak candidate for publication.
