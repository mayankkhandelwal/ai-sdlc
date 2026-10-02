# ADR-11 · One TypeScript script calls Stitch through Google's official SDK; it reads the key from the OS keychain itself

- **Status:** Accepted
- **Source:** `docs/architecture/06-decisions-and-risks.md` (6.1); audits in `docs/audits/`

## Decision

One TypeScript script calls Stitch through Google's official SDK; it reads the key from the OS keychain itself

## Rejected options

Agent calls Stitch MCP; unofficial Python client

## Consequences

Exact, countable, resumable calls; Node.js needed on testers' machines

## Notes

_Add spike results or later changes here, with dates._
