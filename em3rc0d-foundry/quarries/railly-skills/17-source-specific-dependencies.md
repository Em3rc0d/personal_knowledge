# Railly Skills — Source-Specific Dependencies

Provenance: OBSERVED
Purpose: prevent accidental cargo-culting into EM3RC0D Foundry.

## Runtime/tool dependencies observed

Some procedures reference:

- RAILLY_SKILLS_REPO;
- fixed local checkout conventions;
- .agents/skills and .claude/skills;
- Bun;
- git/gh;
- xref;
- agent-browser;
- SkillKit;
- Herdr;
- FX review worker;
- Vercel AI Gateway;
- macOS Keychain;
- Tailscale SSH;
- repository-specific test/build tools.

These are implementation choices or adapters.

## Context-specific work model

Much of the workflow grew from:

- GitHub issues;
- external/contributor pull requests;
- Vercel Labs maintenance;
- CLI/browser tooling;
- maintainer review feedback.

EM3RC0D product creation includes additional concerns:

- market validation;
- product design;
- business constraints;
- user feedback;
- launch/distribution;
- reusable full-stack primitives;
- commercial evidence.

Therefore issue/PR semantics must be generalized rather than renamed superficially.

## Source-specific visual guidance

before-after includes a Vercel visual-system reference.

Portable:

- common comparison basis;
- evidence-first composition;
- accessible semantic structure;
- restrained visual noise;
- direct labels;
- fast read + audit path.

Not portable as Foundry canon:

- Vercel brand identity;
- required Geist fonts;
- specific Vercel palette steps.

## Source-specific maturity evidence

A skill’s maturity in Railly/skills reflects that repository’s evidence corpus.

It does not transfer automatically to:

- different models;
- different agent harnesses;
- EM3RC0D repos;
- product-development rather than maintenance;
- non-code product work.

## Abstraction rule

When importing a mechanism, ask:

    which property do we need?
    which source-specific tool currently realizes it?

Example:

    property: independent reviewer execution
    source implementation: FX/Herdr/native Agent fallback
    EM3RC0D architecture: reviewer-runtime adapter with explicit independence evidence

This prevents tool names from becoming architecture.
