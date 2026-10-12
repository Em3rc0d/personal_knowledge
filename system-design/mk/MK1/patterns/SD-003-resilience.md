# SD-003 — Controlled Remote-Failure Resilience

Status: `CANDIDATE / MK1 CLASSIFIED` · Class: `INSPIRED` upstream, independently contrasted.
Upstream: [chapters 10](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/10.%20Notification%20System/Readme.md), [19](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/19.%20Distributed%20Message%20Queue/README.md), [26](https://github.com/liquidslr/system-design-notes/blob/9d8388721e7231442763ad37398b8d82224aa68f/26.%20Payment%20System/README.md).
Independent: [AWS Builders' Library](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), [Fowler Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html). Circuit breaking is supplementary, **not attributed to the individual upstream chapters**.

## Decision rule
- Model failure types separately: timeout, unavailable, explicit terminal failure, rate limit, duplicate acknowledgement, uncertain commit.
- Define end-to-end deadline; split per-attempt timeout and retry allowance within budget.
- Retry **only** known transient and **provably safe/idempotent** operations; bounded attempts, exponential backoff + jitter, respect `Retry-After` where contractually applicable. If commit outcome is unknown and no idempotency guarantee exists, **do not automatically retry the side effect**. No retry storm.
- If overloaded, fail fast, shed load or postpone safely; circuit breaker/bulkhead only if measured repeated dependent failure warrants them.
- After unknown outcome of a side-effecting request, **look up authoritative state or reconcile** before retrying blindly.
- Define degradation behavior and operator recovery signal before deployment.

## Test matrix
Inject timeout-before-commit, timeout-after-commit, 429/retry hint, 5xx burst, terminal 4xx, dependency restored, concurrent replays. Assert max attempts/deadline, **no unintended duplicate side effect**, recovery signal and bounded resource use.

## Adversarial boundary
A retryable HTTP status is not by itself proof an operation is safe to repeat; the service contract, provider idempotency scope, expiration and response semantics must be verified. A timeout can happen **after** the remote side effect. Client deadlines do not cancel committed remote operations. Read [SD-004](./SD-004-idempotency-consistency.md) for separate local and provider guarantees.

## Anti-pattern / boundary
At-least-once delivery does **not** mean exactly-once effect. Neither retries nor circuit breakers are mandatory dependencies; no production fault-injection evidence yet.
