# Inbox

New work waits here until the Lead sorts it. Nothing is built from the inbox directly.

**Add a line:** date · who · what · why.
**The Lead sorts each item into:** a new task in an existing epic, a new epic, or "no / later" with a reason.
If it changes the architecture, it also needs an ADR.

## Waiting

| Date | Who | What | Why |
|---|---|---|---|
| 2026-10-03 | Lead (from T-02.2) | Make `tools/guard_holdout.py` and its hook command fail closed fully: add `\|\| exit 2` to the hook command and a timer inside the guard that exits 2 before Claude Code's timeout | T-02.2 proved a crashing, missing or timed-out hook lets the call through; ADR-19 wording to update in T-02.8 |
| 2026-10-03 | Builder (from T-02.1) | Try the Stitch MCP server live through the project `.mcp.json` in a new Claude Code session, with the key put into `STITCH_API_KEY` from the keychain for that session only (no `.env` file); compare with the script path | T-02.1 compared it on paper only; T-02.8 decides whether the agent-calls-MCP path needs a test |

## Sorted

| Date | Item | Decision | Where it went |
|---|---|---|---|
| 2026-10-03 | Branch names in task files cut mid-word | Done by the Lead: all task files now use short whole-word names | `plans/tasks/` |
| 2026-10-03 | Many chats at once was too hard to run | Changed: one task at a time, every chat in the main folder, no worktree folders. Spike work T-02.2/4/7 dropped; tasks back to todo | `CLAUDE.md`, `docs/process/` |
| 2026-10-03 | Three chats per task is too much copy-paste | Changed: `/next` does a whole task in one chat; the Auditor is a sub-agent; the chat does the Lead's merge | `.claude/commands/next.md`, `CLAUDE.md`, `docs/process/` |
| 2026-10-03 | Whole MVP in 2–3 weeks, nothing cut | Accepted with risks named in `docs/plan.md`. Next epics now wait for the previous agent's batch-2 task, not its hold-out and acceptance; live tests likewise | `docs/plan.md`, T-07.1, T-12.1, T-14.1, T-16.1, T-18.3–5 |
