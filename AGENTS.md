# Agent entrypoint — minimal context

This repository is a versioned knowledge base, not an instruction to load every document.

1. If the exact authoritative file is known, **read that file or the required section directly**.
2. Otherwise read [`CONTEXT_ROUTER.md`](./CONTEXT_ROUTER.md) once; scope retrieval to a relevant domain. Do not preload the entire root README, a domain or the raw source corpora.
3. For current state use the current STATUS/system/MK owner; consult quarry/source **only** for provenance, uncertainty or contradiction. Pointers and retrieved excerpts are not automatically verified facts.
4. Preserve negations, limits, citations, authority and UNKNOWN; expand rather than silently truncate evidence. Do not trade correctness for smaller context.
5. Any experiment with token savings needs quality comparison and actual usage accounting; character/byte savings are not billed tokens.
6. Never make paid model calls, install infrastructure or trigger GitHub Actions solely for retrieval. Follow the repo branch/review/MK promotion contract before edits.

Optional offline section finder: [`knowledge-usage/retrieval/README.md`](./knowledge-usage/retrieval/README.md).
