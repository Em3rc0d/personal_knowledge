# MK0 — Scope & Framing

Status: **CLOSED**  
MK: **Mine & Frame**

## Mission

Build a defensible foundation for agent engineering before individual tutorial patterns are promoted into reusable system rules.

MK0 exists because `AI agent` is an overloaded label. Systems with radically different control authority, state, persistence, tool access, human oversight, side effects and evaluation are routinely described with the same words.

## Questions MK0 had to make explicit

- When is a deterministic workflow sufficient?
- What exactly may the model decide?
- Which rules are prompt guidance and which are runtime invariants?
- What state survives a crash, pause or resume?
- What can create real-world side effects?
- How does the system know it succeeded?
- What stops a failed or oscillating loop?
- What evidence justifies another agent, planner, critic, memory layer or abstraction?

## Source frame

The initial mining corpus is:

- `NirDiamant/GenAI_Agents@4c95ae14cc2462c442b5c064cccd74430d02bc46`;
- `NirDiamant/Agent_Memory_Techniques@b7f7240eb4d4510f3b45300a89126858a474b31d` for specialized memory pressure-testing;
- `NirDiamant/agents-towards-production@141b0679f11b48209f2b872419f78a3a13850e0d` for production-oriented claims/patterns;
- MCP official specification revision `2026-07-28` for the closure comparison;
- official agent/runtime/tool/context/HITL/evaluation guidance;
- scientific literature on acting, reflection/self-correction, benchmarking and multi-agent failure modes.

The complete registry and provenance live in [`../../mining-site/SOURCES.md`](../../mining-site/SOURCES.md).

## What closing MK0 means

MK0 is closed because the domain can now describe and challenge a new system without trusting:

- framework names;
- README categories;
- marketing labels such as `agent`, `production-ready` or `self-improving`;
- a successful demo run as proof of reliability.

The framing, vocabulary, evidence discipline and risk boundaries are sufficiently stable to open MK1.

## What MK0 does **not** certify

Closing MK0 does not establish:

- framework superiority;
- one universal agent architecture;
- production safety of upstream tutorials;
- current executability of every notebook;
- reliability of intrinsic reflection;
- benefit of multi-agent topology without measurement;
- exact behavior under changing model/provider versions;
- operational readiness of candidate rules;
- project-specific deployment, rollback, SLO, tenant-isolation or sandbox guarantees.

## Boundary between MK0 and later MKs

```text
MK0  discover + frame + preserve evidence + expose contradictions
MK1  normalize + classify + deduplicate dimensions
MK2  operationalize into contracts + schemas + checklists + tests
MK3+ integrate / automate / certify
```

MK0 promotes the **problem framing and evidence discipline**, not every candidate engineering rule.
