# ADR-20 · The state script checks its own conditions before every move; the orchestrator rebuilds its view from the state each run

- **Status:** Accepted
- **Source:** `docs/architecture/06-decisions-and-risks.md` (6.1); audits in `docs/audits/`

## Decision

The state script checks its own conditions before every move; the orchestrator rebuilds its view from the state each run

## Rejected options

Trust the orchestrator to call `advance` correctly

## Consequences

"AI never moves the state" becomes true in practice

## Notes

_Add spike results or later changes here, with dates._
