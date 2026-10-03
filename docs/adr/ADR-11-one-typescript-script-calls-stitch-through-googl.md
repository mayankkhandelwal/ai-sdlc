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

- 2026-10-03 · T-02.1 (`docs/spikes/T-02.1-stitch.md`): confirmed SDK + keychain + one script (3 screens, 1 edit,
  HTML and image). Plugin secrets do not reach Bash, so the script reads the keychain itself. Not proven:
  "resumable" (no job ID, no read-back of screens). The SDK says it is "not an officially supported Google
  product". Wording change goes to T-02.8.
