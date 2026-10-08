# Collaborator — Agentic Desktop Workspace Patterns

Status: **QUARRY / NON-CANONICAL**  
Source: [S-116](../mining-site/S-116-collaborator.md)  
Observed: 2026-10-08  
Evidence boundary: pinned upstream \`main@476b8efc942ee5f430a9b8bf832b8560a8cf76c2\`, \`dev@516ce5ddb9f58a29b64ffc2f86c1e7ffd52cd8bc\`; code inspection only.

## Research question

What can an agent-controllable desktop canvas teach us about state, tool affordances, execution authority and safe local software development, independently of Collaborator as a product?

## Main distinction

\`\`\`text
visual workspace / canvas     = presentation and interaction surface
terminal / PTY / sidecar       = persistent local execution surface
filesystem                    = mutable user-owned source of truth
canvas/CLI/JSON-RPC           = tool control plane
LLM/agent                     = optional decision actor
policy / review / acceptance  = separate authority, not proven by the UI
\`\`\`

This source illustrates an **agent-controllable development environment**. It does not demonstrate a complete multi-agent scheduler or governance system.

## Candidate patterns — not new canonical rules

### CW-01 — Spatial view is a projection, not the execution owner

**Provenance:** OBSERVED → INFERRED

Canvas tiles represent terminal sessions/files/browser surfaces. Sessions and canvas layout have different lifecycles; a visual tile's disappearance cannot silently be equated with process termination or task completion.

**Candidate test:** create session, move/close/reopen the tile and restart the renderer; assert expected process lifetime, explicit termination behavior and reconnection recovery. Classify lost-process versus lost-layout state separately.

**Failure mode:** UI state treated as durable execution truth, causing abandoned agents or false success.

### CW-02 — Agent-facing visual control needs a capability contract

**Provenance:** OBSERVED → INSPIRED

The \`collab-canvas\` CLI and JSON-RPC expose distinct actions: inspect canvas, create/move/focus tiles, send input/read terminal output, interact with a browser. This is a useful ACI pattern, but tool availability is not consent or authorization.

**Candidate test:** catalog tools with read-only vs mutating vs externally consequential classes; reject unauthorized calls and record input, actor, target, revision/time and result. Terminal input and browser JS evaluation are high-consequence even when invoked from an attractive canvas.

**Failure mode:** a model's ability to arrange information silently expands into permission to mutate user files, execute commands or transmit data.

### CW-03 — Local-first is not a security perimeter

**Provenance:** OBSERVED → INFERRED / AUDIT TARGET

Filesystem IPC handlers and local socket services are authorization boundaries. Merely using a local filesystem or Unix socket does not establish workspace isolation or authenticated intent.

**Candidate tests:** path-traversal and symlink escape; sender identity by IPC channel; cross-workspace read/write attempt; socket access from another local process/user; token/capability check per sensitive sidecar operation; bounded message size and backpressure.

**Failure mode:** unchecked \`path\` / \`sessionId\` / \`webContentsId\` arguments become ambient host authority. Exact exploitability is UNKNOWN pending controlled testing.

### CW-04 — Persistent terminal, saved layout and remembered context are different

**Provenance:** OBSERVED → INFERRED

The architecture has PTY state, JSON configuration/layout and workspace files. None automatically implies semantic memory, verified task completion or replay-safe execution.

**Candidate test:** document independently which state survives tile close, renderer crash, app quit, reboot and workspace move. Model source revision and unsaved editor buffer separately.

**Failure mode:** "session persists" is mistaken for durable, resumable, correct agent workflow.

### CW-05 — UI/editor file integrity must be an explicit gate

**Provenance:** COMMUNITY REPORT → PROPOSED TEST, not validated behavior

Upstream issue #143 reports unexpected writes and truncation when opening files, and #146 reports Windows filename corruption. Do **not** promote issue text into confirmed exploit or generalized fact.

**Candidate tests:** open/read-only interactions produce byte-identical files; unsaved buffers never overwrite externally restored content; rename/move paths preserve filenames across platforms; atomic write/conflict handling and crash/restart paths preserve bytes; verify with Git diff and content hashes.

**Failure mode:** viewing or reorganizing source material changes the source of truth without informed intent.

### CW-06 — Agent permission should be enforced outside model behavior

**Provenance:** OBSERVED → INFERRED

The dev source contains bypass-approval switches and an ACP permission callback that selects an allow option. This is inconsistent with treating visible agent interaction as proof of effective HITL.

**Candidate test:** destructive actions require a policy-authorized and auditable approval at the actual dispatch boundary; denial, cancellation, retry, and hidden-background execution paths must all fail closed; persisted sessions must not inherit silently elevated authority.

**Failure mode:** user-visible UI implies approvals while runtime performs automatic allow.

### CW-07 — Cross-platform and release claims need a test matrix

**Provenance:** OBSERVED + COMMUNITY REPORT → INSPIRED

Electron packaging describes macOS, Windows and Linux targets, while actual report surface includes packaging/platform regressions. \`dev\` improves dependency locking but this alone cannot prove reliability.

**Candidate matrix:** macOS ARM/x64, Windows x64/ARM and WSL, Linux x64; install/update/uninstall, PTY attach/reconnect, paths, editor integrity, window focus, browser auth, background process termination and offline behavior. Distinguish source configuration, CI pass, artifact existence, actual install and user report.

**Failure mode:** "target declared" promoted to "platform verified".

### CW-08 — Privacy boundaries apply to local apps too

**Provenance:** OBSERVED → INSPIRED

Persistent telemetry identifiers, remote feature flags and outreach metadata coexist with local source files and local terminal execution.

**Candidate test:** inspect network egress in normal and offline modes; ensure telemetry does not include user file content, terminal output or secrets; require transparent controls and clear retention/data-flow documentation.

**Failure mode:** "all project data is local" misconstrued as "the application makes no outbound requests".

## Negative findings / anti-overclaim

- No evidence of global task DAGs, conflict resolution, measurable multi-agent advantage, cost budgets, coordinated acceptance gates or full agent governance.
- No runtime benchmark, app build, tests or independent exploit proof in this intake.
- Source-specific UI and terminal choices are **options**, not mandatory architecture for future tools.
- FSL-1.1-ALv2 limits derivative/commercial reuse; knowledge mining must not import implementation code.
- This evidence does **not** satisfy the existing MK1 REC-012 multi-agent baseline: there is no equivalent-task baseline comparison or evaluation result.

## Where it may be reused

- \`agent-engineering\`: ACI/tool topology; UI vs execution vs policy; HITL; state/persistence; host authority and side effects.
- \`jett-engineering-method\`: potential cross-check for source-integrity gates and evidence-based claims, **not a methodology change**.
- \`web-design\`: only a possible INSPIRED reference for spatial interaction, with usability tests required; not a canonical design system.

## Evidence / promotion gate

Maintain this as quarry-only until a future task needs it. For promotion require: independent second source or controlled reproduction, a bounded engineering invariant, failing-then-passing test evidence for the target system, explicit tradeoffs, and review. No new flagship, domain, MK1 field or Collaborator implementation is proposed here.
