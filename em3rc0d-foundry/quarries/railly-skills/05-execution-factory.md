# Railly Skills — Execution Factory

Provenance: OBSERVED + INFERRED
Primary upstream: skills/.experimental/software-factory/, simplify, resilience-audit, test-strength, performance-proof

## Factory boundary

software-factory sits between accepted solution and final Review Gate.

It does not select work, choose the shape or decide final promotion.

Observed pipeline:

    accepted shape / Formula
      → implement
      → reduce
      → harden when triggered
      → strengthen tests
      → prove real behavior
      → Review Gate

This is a protocol, not a specific runtime.

## Stage contract first

Before implementation, the source discovers what the repository can actually verify:

- test command;
- build/type/lint;
- complexity or line-budget gates when relevant;
- mutation/falsification capability;
- failure injection;
- user-visible behavior observation.

Thresholds are fixed **before** seeing the result.

Portable rule:

    define success/rejection before optimization or implementation evidence appears

If a tool does not exist, the stage becomes unavailable with owed evidence. It is not silently satisfied.

## Independent passes

Each stage receives:

- accepted contract;
- previous stage evidence;

but not the previous stage’s full reasoning.

The rationale is explicit: an actor asked to defend its own choices tends to preserve them.

This supports a general pattern:

    writer context
      != reducer/challenger context
      != final reviewer context

## Implement

The first stage owns the behavior change and repository checks.

It does not own final judgment.

## Reduce

simplify reduces maintenance surface while preserving:

- public contract;
- security/operational behavior;
- distinct regression invariants;
- supported implementations/runtimes.

Important safeguards:

- measure full scope, including untracked files;
- no metric gaming through minification or type-safety downgrade;
- tests are compared by invariant, not file count;
- apply reversible slices;
- prove equivalence after each reduction class.

## Harden

resilience-audit is conditional.

It maps material process/network/storage/queue/cache/filesystem/browser/third-party boundaries and forces relevant failure partitions.

Hardening happens **before final Test Strength** because resilience fixes can change production behavior and tests.

This ordering was corrected in Round 013 after the source identified stale-evidence risk.

## Strengthen

test-strength asks whether tests can reject realistic wrong implementations.

Core pattern:

    fixed implementation + green test
      → inject/revert representative defect
      → test must fail for intended reason
      → restore
      → test must pass

For matrices/state machines/protocols, each declared cell or equivalence class needs evidence, not just a sampled happy path.

Definition-site testing may not protect a broken call site.

## Prove

The final execution stage observes behavior at the layer of the claim.

Examples of the broader source principle:

- code reading does not prove runtime behavior;
- unit helper pass does not prove caller ordering;
- final state equality does not prove timing/atomicity;
- configured value does not prove effective substrate behavior.

## Performance is separate

performance-proof is not a default stage. It fires only for an evidenced performance claim.

Its sequence:

    define measurable claim
      → stable baseline
      → profile cost center
      → compare candidates including current implementation
      → bounded change
      → same benchmark
      → reject honestly if within noise or required metric regresses
      → durable guard

## Thrashing

software-factory treats repeated reversals as a signal that the **shape**, not merely the implementation, is wrong.

After two reversals on the same behavior pair, it returns to Solution Gate instead of continuing repair loops.

The exact threshold is explicitly unproven in the source’s own promotion questions.

## EM3RC0D adaptation

INSPIRED:

Keep the staged idea, but allow product-specific stages:

    build
      → simplify where useful
      → harden when risk-triggered
      → strengthen verification
      → prove user-visible behavior

Do not create standing agent “staff”. Spawn bounded roles/passes when evidence obligations justify them.
