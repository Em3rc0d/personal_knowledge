# EM3RC0D Foundry — Candidate Product Graph

Provenance: GENERATED + INSPIRED
Status: MK0 candidate.

## Purpose

Generalize the issue-maintenance lifecycle into a product lifecycle without forcing heavyweight phases onto every work item.

## Candidate graph

    SOURCE
      ↓
    QUALIFY
      ↓
    ADMIT
      ↓
    RESEARCH / FRAME
      ↓
    BRAINSTORM
      ↓
    DESIGN
      ↓
    ARCHITECTURE
      ↓
    PLAN / SLICE
      ↓
    BUILD
      ↓
    TEST / PROVE
      ↓
    INDEPENDENT REVIEW
      ↓
    PACKAGE / EVIDENCE
      ↓
    HUMAN PROMOTION
      ↓
    DELIVER
      ↓
    OBSERVE
      ↓
    RECORD / LEARN
      ↺

The graph is not a mandatory linear waterfall.

The router may skip nodes when:

- the work profile does not require them;
- a prior valid artifact already satisfies them;
- the mechanism is mechanically determined;
- the evidence obligation is not triggered.

Every skip needs a reason.

## Candidate source classes

MK0 working taxonomy:

- market opportunity;
- user/customer problem;
- internal product request;
- research question;
- experiment;
- bug;
- feature/change;
- maintenance;
- external contribution/change;
- productization request;
- recovery/resume.

These are GENERATED and must be normalized in MK1.

## Node contracts

### QUALIFY

Question:

    is this worth attention now?

Outputs:

- bounded candidate/source;
- decisive evidence;
- unknowns;
- deferrals;
- no mutation.

### ADMIT

Question:

    what is this work actually asking for, and what authority/path does it deserve?

Output:

- intent/work type;
- minimum workflow;
- allowed/forbidden actions;
- human confirmation where mutation follows.

### RESEARCH / FRAME

Question:

    what is true, what is unknown, and what outcome matters?

Outputs:

- provenance;
- observed state;
- problem frame;
- constraints;
- acceptance;
- non-goals;
- risk.

### BRAINSTORM

Question:

    what solution space is worth considering before narrowing?

Output remains non-canonical until later shape/design gates.

### DESIGN

Question:

    what user interaction, information hierarchy, visual language and behavior should exist?

Should bind to design evidence/provenance and explicit UX constraints.

### ARCHITECTURE

Question:

    who owns state/behavior, what boundaries exist, and what failure/authority model follows?

### PLAN / SLICE

Question:

    what is the smallest independently demonstrable slice?

### BUILD

Question:

    implement the accepted slice without widening scope.

### TEST / PROVE

Question:

    can the evidence reject realistic wrong behavior at the claimed boundary?

Includes conditional performance/resilience/security/visual proof.

### INDEPENDENT REVIEW

Question:

    does the exact current state satisfy contract and standards?

Separate at least:

- Spec: did we build what we said?
- Standards: is the implementation/release quality acceptable?

### PACKAGE / EVIDENCE

Question:

    can a human/user/reviewer inspect the result quickly and exactly?

Possible artifacts:

- demo;
- before/after;
- reproducible command;
- benchmark;
- release candidate;
- docs;
- evidence manifest.

### HUMAN PROMOTION

Question:

    which exact external action is authorized on which exact state?

### DELIVER

Could be:

- merge;
- release;
- deploy;
- publish;
- distribute;
- hand to user;
- launch experiment.

### OBSERVE

Question:

    what happened outside the lab?

Signals:

- users;
- failures;
- support;
- metrics;
- external review;
- commercial evidence;
- operational evidence.

### RECORD / LEARN

Question:

    what should the product and Foundry remember?

Outputs:

- case;
- reusable candidate;
- gap;
- no-change;
- hold/kill/iterate decision.

## Re-entry rule

On resume:

1. read machine/current state;
2. verify drift-prone facts;
3. identify first incomplete/invalid node;
4. reuse only receipts whose dependency cone remains valid;
5. do not reconstruct completed stages from chat memory.

## Candidate profiles

For later MK1 normalization:

- micro/mechanical;
- standard;
- high-risk;
- research;
- productization;
- recovery.

Exact names and budgets are not canon yet.
