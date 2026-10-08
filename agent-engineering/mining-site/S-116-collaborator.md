# S-116 — Collaborator (collabs-inc/collab-public)

Status: **SOURCE RECEIPT — NON-CANONICAL**  
Observed: **2026-10-08**  
Purpose: **external reference for agent-engineering; no product implementation or upstream modification authorized**

## Source intake / identity

| Field | Value |
|---|---|
| Source ID | S-116 |
| Received at | 2026-10-08 |
| Input pointer | https://github.com/Em3rc0d/collab-public |
| Resolved identity | https://github.com/collabs-inc/collab-public (upstream; user-provided URL is a fork) |
| Publisher / copyright notice | Softspace Inc. (per LICENSE.md) |
| Source type | public Electron desktop-app repository; agentic development workspace |
| Upstream main pinned | \`476b8efc942ee5f430a9b8bf832b8560a8cf76c2\` |
| Upstream dev pinned | \`516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc\` |
| Fork state at observation | both \`main\` and \`dev\` matched upstream SHA; no fork-specific changes to those branches observed |
| Version at pinned main | \`0.8.4\` (package.json) |
| Version at pinned dev | \`0.9.0\` (package.json; branch version, not a verified release) |
| License | Functional Source License FSL-1.1-ALv2; non-permissive competitive-use limits before future Apache 2.0 conversion |
| Access state | ACCESSIBLE |
| Capture state | PARTIAL — pinned file paths, inspected code excerpts, repository tree, selected issue reports; no full local execution snapshot |
| Verification state | VERIFIED for source-visible repository claims; INCONCLUSIVE for runtime/operational claims |
| Promotion state | QUARRY_ONLY |
| Provenance | OBSERVED for code/metadata; SOURCE CLAIM for README positioning; INFERRED/INSPIRED only where explicitly labeled |
| Confidence | HIGH: inspected repository facts; MEDIUM: source-backed architecture interpretation; LOW/UNKNOWN: cross-platform operational reliability and exploitability |

## Bounded inspection

Primary upstream paths examined at the pinned main/dev revisions:

- \`README.md\`, \`LICENSE.md\`, \`CONTRIBUTING.md\`, \`install.sh\`;
- \`collab-electron/package.json\`;
- \`collab-electron/src/main/index.ts\`, \`ipc-filesystem.ts\`, \`ipc-browser.ts\`, \`ipc-workspace.ts\`, \`files.ts\`;
- \`collab-electron/src/main/json-rpc-server.ts\`, \`ipc-endpoint.ts\`, \`canvas-rpc.ts\`, \`acp-agent.ts\`;
- \`collab-electron/src/main/pty.ts\`, \`sidecar/server.ts\`, \`sidecar/client.ts\`, \`terminal-target.ts\`;
- \`collab-electron/src/windows/shell/src/renderer.js\`, \`tile-manager.js\`, \`terminal-embed.js\`;
- \`collab-electron/packages/collab-canvas-skill/skills/collab-canvas/SKILL.md\`;
- \`collab-electron/src/main/analytics.ts\`, \`outreach.ts\` (dev);
- selected tests (sidecar, terminal, UI) and \`.github/workflows/cla.yml\`;
- compared \`main..dev\` (34 commits ahead) and observed old \`feat/zoom-tile-labels\` branch divergence.

Stable evidence links:

- [Main package](https://github.com/collabs-inc/collab-public/blob/476b8efc942ee5f430a9b8bf832b8560a8cf76c2/collab-electron/package.json)
- [Dev package](https://github.com/collabs-inc/collab-public/blob/516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc/collab-electron/package.json)
- [Canvas RPC](https://github.com/collabs-inc/collab-public/blob/516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc/collab-electron/src/main/canvas-rpc.ts)
- [CLI skill](https://github.com/collabs-inc/collab-public/blob/516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc/collab-electron/packages/collab-canvas-skill/skills/collab-canvas/SKILL.md)
- [ACP permissions](https://github.com/collabs-inc/collab-public/blob/516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc/collab-electron/src/main/acp-agent.ts)
- [Agent target flags](https://github.com/collabs-inc/collab-public/blob/516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc/collab-electron/src/main/terminal-target.ts)
- [Sidecar control plane](https://github.com/collabs-inc/collab-public/blob/516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc/collab-electron/src/main/sidecar/server.ts)
- [Filesystem IPC](https://github.com/collabs-inc/collab-public/blob/516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc/collab-electron/src/main/ipc-filesystem.ts)
- [License](https://github.com/collabs-inc/collab-public/blob/476b8efc942ee5f430a9b8bf832b8560a8cf76c2/LICENSE.md)

## What is supported by source inspection

1. **OBSERVED:** Collaborator is a local desktop workspace based on Electron, React, xterm.js/node-pty, Monaco, BlockNote/TipTap and a pan/zoom canvas. Workspaces refer to local folders, not a hosted account as a prerequisite.
2. **OBSERVED:** A persistent PTY sidecar and socket-mediated control allow session lifecycle and reconnection independent of a particular canvas tile. Persistence of PTY process, canvas layout and source files are **different state surfaces**.
3. **OBSERVED:** The app exposes canvas, terminal and embedded-browser operations through local JSON-RPC/IPC. A CLI and agent-facing skill can list/create/move/focus tiles, write/read terminal content and operate browser tiles.
4. **OBSERVED:** \`dev\` integrates terminals more directly into the shell renderer and removes tmux as a terminal backend. This is an architectural revision, not proof of better performance without benchmarks.
5. **OBSERVED / RISK SIGNAL:** The ACP permission callback selects an allow option programmatically and direct agent target configuration retains bypass-approval flags (even though new-tile menu entry points for agents were removed in a later dev commit). The exact runtime exposure must be assessed before using sensitive workspaces.
6. **OBSERVED / RISK SIGNAL:** Several filesystem IPC handlers accept renderer-supplied paths without a consistently visible workspace-root authorization check in the inspected handler path. Local sidecar control methods do not show per-request token verification. These are audit targets, **not independently demonstrated remote vulnerabilities**.
7. **OBSERVED:** PostHog telemetry generates a persisted device ID; dev adds a feature-flag-driven outreach workflow. Local-first storage does not imply zero outbound telemetry.
8. **OBSERVED:** The root workflow tree shows a CLA workflow, but no test/build CI workflow in the inspected snapshot; \`dev\` adds \`bun.lock\` whereas \`main\` lacks it.

## External problem reports, not reproduced

Community issues are claims by reporters, not validated runtime outcomes of this research:

- [#143 — unintended editor writes / reported truncation](https://github.com/collabs-inc/collab-public/issues/143).
- [#146 — reported Windows markdown filename corruption](https://github.com/collabs-inc/collab-public/issues/146).
- [#141 — reported Linux installer artifact mismatch](https://github.com/collabs-inc/collab-public/issues/141).
- [#110 — user request for multiple canvases](https://github.com/collabs-inc/collab-public/issues/110).

## Unsupported claims / open boundaries

- No local installation, build, test suite, end-to-end replay or security exploitation was performed.
- No demonstration that Collaborator is production-ready, secure-by-default, faster than an IDE, or better at multi-agent orchestration.
- Multiple terminal tiles **do not by themselves establish** agent orchestration (task admission, isolation, dependency scheduling, budget control, conflict handling and acceptance authority).
- No independent data-loss reproduction; the impact of issue reports remains to be tested on pinned builds.
- No legal conclusion beyond recording source license text; do not redistribute or use copied implementation for a competitive product without separate clearance.

## Usage rule

Mine **patterns and anti-patterns**, not code, branding or a roadmap. The quarry is [Collaborator — agentic desktop workspace patterns](../quarries/collaborator-agentic-desktop-workspace.md). Do not change the active MK1 schema, close REC-012 or open a new domain on this evidence alone. Candidate engineering rules require independent corroboration and runnable tests before promotion.
