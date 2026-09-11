# MK0 Playbook — LinkedIn Professional Inbound

Status: `WORKING CANON WITHIN MK0`  
Date: `2026-09-11`

This playbook captures the current LinkedIn operating model derived from the 2026-09-11 analytics snapshot. It is usable now but remains falsifiable.

## 1. Objective

Turn LinkedIn into a **professional inbound acquisition channel**.

North Star:

> Each week, more people with the ability to hire, pay, recommend or include the author in projects should know who he is and have evidence that he can build.

Funnel:

```text
Reach
→ Credibility
→ Evidence
→ Profile
→ Conversation
→ Opportunity
→ Employment / Contract / Client / Referral / Collaboration
```

## 2. Audience architecture

| Audience | Potential value | What they need to see |
|---|---|---|
| Recruiters / HR | interviews, employment | stack, clarity, projects, employability |
| Tech Leads / Engineering Managers | hiring, referrals, projects | judgment, depth, system thinking |
| Founders / businesses | clients, contracts | problem-solving and pragmatic delivery |
| Developers / professionals | network, referrals, collaboration | useful knowledge + technical respect |
| Students / juniors | reach and interaction | accessible, useful learning |

Students and juniors are intentionally part of the distribution layer even when they are not immediate buyers/hirers.

## 3. Professional identity

> **Explico software de forma sencilla, pero construyo sistemas de verdad.**

The account should not become a tutorial archive. It should accumulate evidence of judgment, execution and business usefulness.

## 4. Reach Engine

Current strongest family: SQL / databases.

Preferred shape:

```text
known concept
→ obvious assumption
→ counterintuitive behavior
→ concise explanation
→ low-friction question
```

Examples of candidate families:

- `COUNT(*)` vs `COUNT(column)`;
- `WHERE` vs `HAVING`;
- `UNION` vs `UNION ALL`;
- `NOT IN` + `NULL`;
- transaction behavior;
- `DELETE` / `TRUNCATE` / `DROP`;
- indexes that can worsen a query.

SQL is the current acquisition engine, not the entire identity.

## 5. Engineering Authority

Use real production concerns rather than textbook definitions:

- API idempotency;
- retries and duplicate side effects;
- caching;
- concurrency;
- queues;
- observability;
- distributed systems;
- security;
- cloud;
- CI/CD;
- data contracts;
- architecture trade-offs.

Target balance:

> understandable by a junior, credible to a senior.

## 6. Proof of Work

Goal: move perception from:

> “knows how to explain”

into:

> “knows how to build and make engineering decisions”.

Do not publish project content as:

> “Today I added MongoDB / Docker / framework X.”

Prefer:

```text
real problem
→ risk
→ decision
→ rejected alternatives / trade-off
→ verification / gate
→ lesson
```

Useful sources include actual release blocks, architecture decisions, debugging, operational failures and evidence-based project gates.

## 7. AI / Automation / Business

Avoid generic AI content and commodity prompt lists.

Prefer engineering concerns such as:

- explicit state;
- retries;
- idempotency;
- audit log;
- human approval;
- rollback;
- integration failures;
- process quality;
- business-system architecture.

One strong post can simultaneously signal:

```text
developer → useful engineering idea
recruiter → technical capability
business owner → relevant problem-solving capacity
```

## 8. Opportunity Magnets

Do not default to “I am looking for work”.

Prefer demonstrations that imply:

> “I can solve this class of problem.”

Examples:

- how to automate a SME commercial process safely;
- first decisions before building a SaaS;
- handling 100K events/day without unnecessary microservices;
- why automating a broken process only amplifies failure.

## 9. Technical judgment

Publish defendable opinions, not controversy for its own sake.

Candidate shapes:

- microservices are not a natural evolution for every monolith;
- not every application needs Kubernetes;
- more architecture complexity does not imply more scalability;
- more AI does not automatically create a better product;
- automating a bad process makes errors happen faster.

## 10. Daily role system

Current baseline: ~4 posts/day coexisted with strong growth.

Use four differentiated jobs:

```text
SLOT 1 — Reach Engine
SLOT 2 — Engineering Authority
SLOT 3 — Proof of Work
SLOT 4 — Opportunity / Business / AI
```

Portfolio-level mix candidate:

```text
25% Reach
30% Authority
25% Proof
20% Opportunity / Business / AI
```

Cadence is an experiment, not a permanent law.

## 11. CTA system

Alternate two families:

### Knowledge CTA

Short, easy answer.

Example:

> TRUE, FALSE or UNKNOWN?

Purpose: reduce comment friction.

### Experience CTA

Example:

> Which of these bugs cost you the most time the first time?

Purpose: increase conversation quality.

The goal is to retain saves while creating more conversations.

## 12. Profile conversion

The post is landing page #1. The profile is landing page #2.

Desired sequence:

```text
viral / useful technical post
→ “who is this?”
→ profile
→ follow
→ deeper Backend / AI / Systems content
→ proof
→ conversation
→ opportunity
```

Profile should make visible in seconds:

```text
Software Engineer / Full Stack
Backend + AI + Automation + DevOps
Builds real systems
Portfolio
GitHub
Best projects
Contact
```

`Featured` should be a showroom of roughly 3–5 strongest proof artifacts, not an archive.

## 13. Aggressiveness boundary

Aggressive means:

- stronger hooks;
- sharper contradiction;
- faster payoff;
- clearer visual hierarchy;
- deliberate experimentation;
- stronger profile/proof conversion.

It does **not** mean:

- fake controversy;
- misleading clickbait;
- empty outrage;
- unsupported certainty;
- repeating the same winning post structure until fatigue.

## 14. No-repeat gate

Before publishing, compare against recent content on:

```text
topic
angle
lesson
hook
creative structure
visual pattern
```

Wording changes do not make a semantic duplicate new.

Continuation / Part 2 / controlled variation must be deliberate.

## 15. Measurement policy

Do not optimize only for likes.

Primary business metric:

```text
Opportunities Generated
```

Track:

- recruiter DMs;
- interviews;
- referrals;
- client inquiries;
- proposals;
- contracts;
- collaborations;
- invitations;
- relevant portfolio visits;
- high-value connections.

Then learn mappings such as:

```text
SQL → reach
system design → technical followers
proof-of-work → recruiters
AI/automation → potential clients
```

These mappings are hypotheses until attributed.

## 16. Example batch — 2026-09-11

This batch is an experiment example, not evergreen canon.

| Time | Role | Topic |
|---|---|---|
| 09:00 | Reach | `UNION` vs `UNION ALL` |
| 12:00 | Authority | retry can duplicate an API side effect → idempotency |
| 15:00 | Proof / DevOps | deploy after every tiny change can waste pipeline/infrastructure |
| 18:00 | Opportunity | automating a bad process makes failure happen faster |

## 17. Current operating decision

```text
KEEP    high posting discipline while quality survives
KEEP    SQL as reach acquisition
EXPAND  backend / system design / cloud / DevOps authority
EXPAND  proof-of-work from real projects
EXPAND  business-relevant AI/automation
IMPROVE reach → profile conversion
IMPROVE conversation and shares
MEASURE professional opportunities, not only engagement
BLOCK   SQL-only identity
BLOCK   generic AI content
BLOCK   repeated topic/angle/hook
BLOCK   tutorial-only perception
```

## 18. Promotion boundary

The current strategy is strong enough to guide publishing now, but MK0 is not closed from one analytics window.

Future evidence must validate:

- whether ~4 posts/day remains efficient;
- whether profile CTR improves;
- which content families create which opportunity types;
- whether outside-network distribution persists;
- whether higher conversation can coexist with strong save behavior.