# EM3RC0D Foundry — Candidate System Model

Provenance: **GENERATED**, informed by S-001 and existing Jett Engineering Method.
MK status: MK0 candidate, not operational canon.

## Product promise

EM3RC0D Foundry should convert real evidence and accumulated engineering/design/product knowledge into **portable reusable capital** that makes valuable future products cheaper to build and easier to verify.

## Architecture

    ┌──────────────────────────────────────────────┐
    │ PRODUCT OUTPUT                              │
    │ apps · SaaS · agents · CLIs · automations  │
    │ research products · developer tools         │
    ├──────────────────────────────────────────────┤
    │ PRODUCT FACTORY                             │
    │ intake · contract · design · architecture   │
    │ build · prove · review · package · release  │
    ├──────────────────────────────────────────────┤
    │ REUSABLE CAPITAL                            │
    │ skills · primitives · components · shells   │
    │ patterns · tests · recipes · design rules   │
    ├──────────────────────────────────────────────┤
    │ KNOWLEDGE FOUNDRY                           │
    │ sources · quarries · cases · evidence       │
    │ evals · provenance · promotion · gaps       │
    └──────────────────────────────────────────────┘

## Control principle

The Foundry is not one agent.

It is a graph of:

- durable artifacts;
- deterministic checks;
- bounded procedures;
- ephemeral specialist execution;
- explicit human authority.

Models/runtimes are replaceable execution substrates.

## Three state domains

### Product state

What is true about the product/work item now?

Examples:

- requirements;
- design;
- architecture;
- implementation;
- evidence;
- release identity;
- production observation.

### Factory state

What procedures/assets are available to build?

Examples:

- product shell version;
- primitive registry;
- design system;
- skill version;
- test harness;
- deployment recipe.

### Knowledge state

Why do those procedures/assets exist and how strong is their evidence?

Examples:

- source;
- case;
- pattern;
- eval;
- transfer evidence;
- contradiction;
- rejection;
- maturity.

These domains may reference one another but should not collapse into one document.

## Core orchestration invariant

A work item enters at the earliest incomplete or invalidated node whose prerequisites are satisfied.

A change invalidates only its downstream dependency cone.

Final external promotion always binds to an exact current state.

## Human authority model

The machine may reason about what should happen next.

It must not infer authority to perform external side effects.

Candidate authority ladder:

- read;
- local analysis;
- local mutation;
- commit;
- push;
- PR/change request;
- merge;
- release;
- deploy;
- external communication;
- destructive/financial/regulated action where applicable.

Exact taxonomy remains an MK1 question.

## Factory output types

A product cycle can output:

1. user-facing product increment;
2. evidence pack;
3. case;
4. reusable asset candidate;
5. coverage gap;
6. explicit no-change;
7. kill/hold decision.

A cycle is not successful only when it creates code.

## Reusable-capital admission

A candidate asset should answer:

- What repeated cost does it remove?
- What contract does it preserve?
- What evidence supports it?
- What contexts should not use it?
- What maintenance cost does it add?
- What test/eval detects its regression?
- What version/provenance identifies it?

## Anti-goals

- giant all-knowing prompt;
- permanent multi-agent staff without bounded purpose;
- every project becoming a framework;
- every lesson becoming a skill;
- optimizing repository count;
- auto-promoting from telemetry;
- requiring every gate for every change;
- hiding evidence debt behind polished artifacts.

## Success metric direction

The Foundry should optimize for something closer to:

    valuable shipped outcomes
    × external/real usage
    × reusable capital produced
    ÷ total engineering + coordination cost

This is conceptual. No synthetic global score is promoted in MK0.
