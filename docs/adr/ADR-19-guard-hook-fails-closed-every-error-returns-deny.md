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

- **2026-10-03 · T-02.2 spike (`docs/spikes/T-02.2-guard.md`): confirmed, with a build change.** The hook sees the
  caller (`agent_type`, `agent_id`; none for the main session) and the agent about to start (`Agent` tool,
  `subagent_type`). Deny works by JSON `permissionDecision: "deny"` or exit 2. But Claude Code runs the tool when a
  hook exits 1, exits 127 or times out, so wrapping the logic is not enough. Fail closed needs all three:
  `try/except` → exit 2 in the script; `|| exit 2` on the hook command; a timer in the script that exits 2 before
  the hook's timeout. All three proven on Windows. T-02.8 to update 4.8 to match.
