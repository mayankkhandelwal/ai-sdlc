# Inbox

New work waits here until the Lead sorts it. Nothing is built from the inbox directly.

**Add a line:** date · who · what · why.
**The Lead sorts each item into:** a new task in an existing epic, a new epic, or "no / later" with a reason.
If it changes the architecture, it also needs an ADR.

## Waiting

| Date | Who | What | Why |
|---|---|---|---|
| 2026-10-03 | Builder (from T-02.1) | Try the Stitch MCP server live through the project `.mcp.json` in a new Claude Code session, with the key put into `STITCH_API_KEY` from the keychain for that session only (no `.env` file); compare with the script path | T-02.1 compared it on paper only; T-02.8 decides whether the agent-calls-MCP path needs a test |
| 2026-10-03 | Lead (from T-02.1) | Stitch resume rule for T-02.8: (1) our disk is the record: write a "started" line before each Stitch call, save HTML + image the moment it returns; (2) after a crash, any "started" screen with no saved file is generated again and counted against quota; (3) test whether `edit` still works on a screen made hours earlier, in a new session. If not, feedback rounds regenerate the screen from its message + the feedback instead of editing | Stitch has no job ID and no read-back, so ADR-25's "resume always works" fails for Stitch |
| 2026-10-03 | Builder (from T-02.4) | Repeat T-02.4 answers 3, 4, 13–16 on macOS and Linux: plugin `bin/` on PATH, the bash wrapper + `.py` script, poppler `pdftotext -f/-l`, `pdftoppm`, Read `pages` (spike plugin files are in `docs/spikes/T-02.4-plugin.md`) | Only Windows was available; testers may use macOS or Linux (3.7) |
| 2026-10-03 | Builder (from T-02.4) | Guard hook rule for every agent with Bash: deny any Bash command that is not one of the plugin's bin scripts; match agent names with the plugin prefix (`mvp:<agent>`) | `tools: Bash(x:*)` exposes all of Bash and read-only commands run with no approval (T-02.4 answer 9) |
| 2026-10-03 | Builder (from T-02.4) | Setup guide: poppler install on Windows (`winget install --id oschwartz10612.Poppler -e --scope user`), restart Claude Code after; scripts must reject Git for Windows' Xpdf `pdftotext` | T-02.4 answers 13–15 |

## Sorted

| Date | Item | Decision | Where it went |
|---|---|---|---|
| 2026-10-03 | Branch names in task files cut mid-word | Done by the Lead: all task files now use short whole-word names | `plans/tasks/` |
| 2026-10-03 | Many chats at once was too hard to run | Changed: one task at a time, every chat in the main folder, no worktree folders. Spike work T-02.2/4/7 dropped; tasks back to todo | `CLAUDE.md`, `docs/process/` |
| 2026-10-03 | Three chats per task is too much copy-paste | Changed: `/next` does a whole task in one chat; the Auditor is a sub-agent; the chat does the Lead's merge | `.claude/commands/next.md`, `CLAUDE.md`, `docs/process/` |
| 2026-10-03 | Whole MVP in 2–3 weeks, nothing cut | Accepted with risks named in `docs/plan.md`. Next epics now wait for the previous agent's batch-2 task, not its hold-out and acceptance; live tests likewise | `docs/plan.md`, T-07.1, T-12.1, T-14.1, T-16.1, T-18.3–5 |
| 2026-10-03 | Guard must fail closed fully (from T-02.2) | Done by the Lead: in-script timer (5 s) + `\|\| exit 2` + hook timeout 10 s; 2 new tests (hang, settings); live block checked. Architecture 4.8 wording still for T-02.8 | `tools/guard_holdout.py`, `.claude/settings.json`, `tools/tests/` |
| 2026-10-03 | T-02.4: plugin-hook repeat of T-02.2 runs `identity` and `crash-fixed` | Done in T-02.4 (answers 10–12) | `docs/spikes/T-02.4-plugin.md` |
