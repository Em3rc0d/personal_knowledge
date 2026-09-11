# LinkedIn Measurement Model — MK0

Date: `2026-09-11`

## Objective

Measure whether LinkedIn content generates professional value, not merely engagement.

## Funnel metrics

### Acquisition

- impressions;
- unique reach;
- outside-network reach;
- reach concentration by content family.

### Utility / resonance

- reactions;
- saves;
- saves / interactions;
- saves / impressions.

### Conversation / redistribution

- comments;
- comments / impressions;
- shares;
- shares / impressions;
- qualitative comment quality.

### Profile conversion

- profile views;
- reach → profile CTR;
- impressions → profile CTR;
- follower growth;
- profile → follow conversion when observable.

### Discovery channel

- search appearances;
- feed-led vs search-led visibility;
- audience shifts by role, industry and geography.

### Professional outcome

Primary business metric:

```text
Opportunities Generated
```

Recommended opportunity ledger:

| Field | Purpose |
|---|---|
| date | time series |
| opportunity_type | recruiter / interview / referral / client / contract / collaboration |
| source_post | direct attribution when known |
| source_role | Reach / Authority / Proof / Opportunity |
| source_topic | topic family |
| first_touch | earliest known touch |
| last_touch | latest known touch |
| profile_visit_known | yes / no / unknown |
| outcome | open / won / lost / no-fit |
| estimated_value | optional economic value |
| notes | qualitative context |

## 2026-09-11 baseline

| Metric | Baseline |
|---|---:|
| impressions | 62,822 |
| unique reach | 30,302 |
| interactions | 852 |
| saves | 246 |
| saves / interactions | 28.9% |
| profile views | 125 |
| reach → profile | 0.41% |
| followers | 2,056 |
| follower growth | +6% |
| search appearances | 51 |
| comments | 7 |
| shares | 3 |
| posting cadence | 4.14/day |

## Review windows

```text
daily      execution / anomaly check
7-day      post-family performance
28-day     audience + funnel behavior
monthly    opportunity / economic review
```

## Experiment dimensions

Change one meaningful dimension where practical:

- topic family;
- post role;
- hook class;
- CTA type;
- visual format;
- time slot;
- proof type.

Avoid declaring a rule from one post.

## Candidate decision rules

A pattern becomes stronger only when:

1. it repeats across comparable windows;
2. its metric is explicit;
3. alternative explanations are recorded;
4. audience quality is not degraded;
5. professional opportunity quality is not sacrificed for vanity reach.

A lower-reach post can be more valuable than a viral post if it creates a high-value opportunity.

## Explicit unknowns

1. Is ~4 posts/day sustainable without cannibalization or fatigue?
2. Which role has the highest profile/follower conversion?
3. Which role generates recruiter DMs, clients, referrals or project invitations?
4. How much SQL lift comes from topic vs hook vs visual vs timing?
5. Will 98% outside-network distribution persist?
6. Can profile optimization materially improve the current ~0.41% reach → profile baseline?
7. Which `Featured` artifacts convert best?
8. Can comments/shares increase without reducing saves?
9. What is the lag between a post impression and an opportunity?
10. How should multi-touch attribution across several posts be handled?
11. At what point does SQL overrepresentation weaken broader software-engineering positioning?
12. Which visual format best serves each role: single infographic, carousel, diagram or text-led post?

`UNKNOWN` remains `UNKNOWN` until evidence resolves it.