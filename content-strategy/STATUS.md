# Content Strategy — Status

Updated: 2026-09-11

## Current gate

```text
DOMAIN                    content-strategy
CURRENT MK                MK0
STATE                     IN PROGRESS
ACTIVE CASES              TikTok Content Seller + LinkedIn professional inbound
TIKTOK SNAPSHOT           2026-09-11 CAPTURED
LINKEDIN SNAPSHOT         2026-09-11 CAPTURED
TIKTOK POSITIONING        FRAMED / NOT CERTIFIED
LINKEDIN POSITIONING      FRAMED / NOT CERTIFIED
BATCH MODELS              FRAMED / NOT CERTIFIED
NOVELTY RULES             FRAMED / NOT CERTIFIED
PROMPT MACHINE BRIDGE     FRAMED / NOT CERTIFIED
PROFESSIONAL INBOUND      FRAMED / NOT ATTRIBUTED
AUTOMATION                NOT YET STARTED
```

## MK progression

| MK | Objective | State |
|---|---|---|
| MK0 | Capture evidence, audience, positioning, metrics, editorial rules and hypotheses | IN PROGRESS |
| MK1 | Normalize taxonomies for role/topic/angle/hook/format/visual/metric/platform | BLOCKED BY MK0 |
| MK2 | Operationalize scorecards, planners, cooldowns and decision rules | BLOCKED |
| MK3 | Integrate with Profile, Editorial Memory, project/product surfaces and Analytics contracts | BLOCKED |
| MK4 | Automate planning/measurement/recommendations with safe gates | BLOCKED |
| MK5+ | Run controlled experiments and certify/refine heuristics | BLOCKED |

## MK0 closure gate

MK0 can close only when:

- [x] domain contract exists;
- [x] provenance vocabulary exists;
- [x] `@emerc0d` 2026-09-11 TikTok snapshot is captured;
- [x] LinkedIn 2026-09-11 professional-growth snapshot is captured;
- [x] TikTok audience nucleus and positioning are documented;
- [x] LinkedIn professional-inbound audience architecture is documented;
- [x] TikTok four-slot batch hypothesis is documented;
- [x] LinkedIn four-role batch hypothesis is documented;
- [x] no-repeat / novelty baseline is documented;
- [x] aggressive-hook boundary is documented;
- [x] TikTok Prompt Machine seeding strategy is documented;
- [x] LinkedIn opportunity-generation strategy is documented;
- [x] platform-specific measurement models exist;
- [ ] historical posts are normalized into a canonical editorial-memory dataset;
- [ ] top/bottom performers are classified by platform, role, topic, hook, format and visual pattern;
- [ ] current 4-post cadences have enough dated observations to evaluate by role rather than anecdotes;
- [ ] metric definitions and observation windows are normalized across platforms;
- [ ] LinkedIn opportunity ledger is active and content-family attribution is possible;
- [ ] MK0 review finds no unlabeled `OBSERVED → causal claim` jumps.

Until these boxes close, the strategies remain **working operating hypotheses**, not certified growth formulas.

## Current LinkedIn evidence state

```text
impressions_7d            62,822
unique_reach              30,302
outside_network           98%
interactions              852
saves                     246
comments                  7
shares                    3
profile_views             125
reach_to_profile          ~0.41%
followers                 2,056
follower_growth           +6%
search_appearances        51 / flat
posting_cadence           ~4.14/day
```

Current LinkedIn diagnosis:

- reach / discovery: strong;
- save/reference behavior: strong;
- SQL reach fit: strong;
- profile conversion: improvement area;
- conversation / shares: weak relative to saves;
- professional-opportunity attribution: unknown.

## Current unknowns

Cross-platform:

- Which roles have the highest follower/profile conversion by platform?
- Which hook families improve consumption without harming trust?
- Which formats produce the best save/share behavior for each audience?
- Whether four posts/day is optimal, merely tolerable, or excessive once quality and attribution are controlled.
- Which topic families create broad reach versus high-intent audiences.

LinkedIn-specific:

- Which content families generate recruiter DMs vs clients vs referrals?
- Whether the ~0.41% reach → profile baseline improves after profile/Featured optimization.
- Whether 98% outside-network reach persists.
- Whether SQL remains an acquisition engine without damaging broader software-engineering positioning.

## Next gate

Create a normalized observation ledger containing at minimum:

```text
date
platform
post_id
role
topic
angle
hook_pattern
format
visual_pattern
views / impressions
unique_reach when available
watch_time / slide-through when available
likes / reactions
comments
shares
saves
profile_views
followers_gained
CTA
opportunity_signal
opportunity_type
notes
```

Then classify the historical corpus before changing strategic mixes again.