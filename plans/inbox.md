# Inbox

New work waits here until the Lead sorts it. Nothing is built from the inbox directly.

**Add a line:** date · who · what · why.
**The Lead sorts each item into:** a new task in an existing epic, a new epic, or "no / later" with a reason.
If it changes the architecture, it also needs an ADR.

## Waiting

| Date | Who | What | Why |
|---|---|---|---|
| 2026-10-03 | Lead (from T-02.2) | Make `tools/guard_holdout.py` and its hook command fail closed fully: add `\|\| exit 2` to the hook command and a timer inside the guard that exits 2 before Claude Code's timeout | T-02.2 proved a crashing, missing or timed-out hook lets the call through; ADR-19 wording to update in T-02.8 |
| 2026-10-03 | Lead (from T-02.2) | Branch names in task files are long auto-generated ones; the guide and `docs/process/names.md` use short ones. Make task files match the short names | Avoid confusion when creating worktrees and merging |

## Sorted

| Date | Item | Decision | Where it went |
|---|---|---|---|
