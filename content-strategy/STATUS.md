# Content Strategy — Status

Updated: 2026-09-24

## Current gate

```text
DOMAIN                    content-strategy
CURRENT MK                MK0
STATE                     IN PROGRESS
ACTIVE PROFILES           Content Seller / @emerc0d; Logan / mi.logan.pe; LinkedIn professional account
PLATFORMS                 TikTok + LinkedIn
CONTENT SELLER SNAPSHOT   2026-09-11 CAPTURED
LOGAN SNAPSHOT            2026-09-24 CAPTURED
LINKEDIN SNAPSHOT         2026-09-11 CAPTURED
POSITIONING               FRAMED PER PROFILE / PLATFORM
NOVELTY RULES             HARDENED; LOGAN TOPIC REPOST BLOCKED BY DEFAULT
LOGAN SEARCH MODEL        ACTIVE EXPERIMENT
LOGAN 4-ROLE MODEL        SEARCH / HERO / SHARE ENGINE / LAB
LOGAN PRODUCT SEEDING     BLOCKED IN CURRENT PHASE
MEASUREMENT WINDOWS       BASE T+2h / T+24h / T+7d; LOGAN ADDS T+72h
AUTOMATION                NOT YET STARTED
```

## MK progression

| MK | Objective | State |
|---|---|---|
| MK0 | Capture evidence, audience, positioning, metrics, editorial rules and hypotheses | IN PROGRESS |
| MK1 | Normalize taxonomies for profile/platform/role/topic/angle/hook/format/visual/metric | BLOCKED BY MK0 |
| MK2 | Operationalize scorecards, planners, cooldowns and decision rules | BLOCKED |
| MK3 | Integrate Profile, Editorial Memory and Analytics contracts | BLOCKED |
| MK4 | Automate planning/measurement/recommendations with safe gates | BLOCKED |
| MK5+ | Controlled experiments and certification/refinement | BLOCKED |

## Logan / `mi.logan.pe` — latest state

```text
latest snapshot             2026-09-24
views_7d                    OBSERVED 8.5K
For You                     OBSERVED 90.0%
Search                      OBSERVED 7.7%
profile views               OBSERVED 26
likes                       OBSERVED 111
comments                    OBSERVED 0
shares                      OBSERVED 7 / +600% shown
followers shown             OBSERVED 21
recent common view cluster  OBSERVED ~475–600
distribution exists         INFERRED / HIGH CONFIDENCE
interaction bottleneck      INFERRED / WORKING
search acquisition          WORKING EXPERIMENT
4-role daily model          ACTIVE / NOT CERTIFIED
hard no-repeat              ACTIVE
topic ledger                PARTIAL / HISTORICAL NORMALIZATION OPEN
aggressive-hook boundary    HARDENED
product public seeding      BLOCKED
```

## Logan — strategic decision

Current public mission:

> build relevant automotive audience, retention and interaction.

Current funnel:

```text
DISCOVERY
→ STOP
→ RETENTION
→ SHARE / RESPONSE
→ PROFILE
→ FOLLOW
```

Current daily roles:

```text
SEARCH
HERO
SHARE ENGINE
LAB
```

Current non-negotiable:

> **winning mechanisms may repeat; published topics do not.**

## MK0 closure gate

Already framed:

- [x] domain contract;
- [x] provenance vocabulary;
- [x] current active profile positioning;
- [x] Logan 2026-09-11 snapshot;
- [x] Logan 2026-09-24 snapshot;
- [x] Logan Search acquisition thesis;
- [x] Logan four-role growth model;
- [x] Logan hard no-repeat gate;
- [x] Logan aggressive-but-honest hook boundary;
- [x] Logan retention architecture;
- [x] Logan T+2h/T+24h/T+72h/T+7d loop;
- [x] Logan current product-seeding block;
- [x] LinkedIn professional-inbound frame;
- [x] Content Seller audience / positioning frame.

Still open:

- [ ] historical posts normalized into a canonical editorial-memory dataset per profile/platform;
- [ ] all Logan historical topics classified `PUBLISHED / COOLDOWN / NEW`;
- [ ] top/bottom performers classified by role, topic, hook, format and visual pattern;
- [ ] enough dated observations to compare Logan `SEARCH / HERO / SHARE ENGINE / LAB`;
- [ ] metric definitions normalized across profiles;
- [ ] LinkedIn opportunity ledger active;
- [ ] no unlabeled `OBSERVED → causal claim` jumps.

## Current unknowns — Logan

- Can intentionally query-aligned Search posts raise Search contribution repeatedly?
- Which hook family improves retention without reducing trust?
- Which format creates shares without needing explicit share CTA?
- Which interaction mechanism can move comments above the current zero baseline?
- Can a reusable mechanism repeatedly break the ~475–600 cluster on different topics?
- Which role contributes most to profile visits and follows?
- Is 4/day optimal, merely tolerable or excessive after strict novelty gating?
- How quickly does the published-topic ledger need to expand before ideation becomes the bottleneck?

## Next gate

Normalize Logan’s complete historical corpus.

Minimum schema:

```text
date
post_id
role
topic_key
symptom_key
decision_key
status: PUBLISHED | COOLDOWN | NEW
hook_family
format
visual_pattern
target_query
views_2h
views_24h
views_72h
views_7d
retention / completion
likes
comments
shares
saves
profile_views
followers_gained
search_share
search_queries
classification
notes
```

Only after this ledger exists can no-repeat become fully machine-enforceable rather than partly memory-based.
