# ADR-19 · Guard hook fails closed: every error returns "deny"; no agent can start agents

- **Status:** Accepted
- **Source:** `docs/architecture/06-decisions-and-risks.md` (6.1); audits in `docs/audits/`

## Decision

Guard hook fails closed: every error returns "deny"; no agent can start agents

## Rejected options

Trust the hook not to crash

## Consequences

A broken guard blocks work instead of allowing everything

## Notes

_Add spike results or later changes here, with dates._
