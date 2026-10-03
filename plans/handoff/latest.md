# Handoff

- **Date (UTC):** 2026-10-03
- **Last change:** T-02.2 guard hook spike merged (audit PASS on the 1st try)
- **Branch:** `main` (no other branches)
- **Who:** Claude (Builder + Lead via `/next`), with the project lead

## Done

- T-01.1: context library; audit PASS (`plans/audits/T-01.1.md`)
- T-01.2: plan system: 18 epics, 119 tasks, roles, inbox, audits, failure catalog; audit PASS
- Spike work from the parallel chats (T-02.2, T-02.4, T-02.7) was dropped; those tasks are `todo` again
- New way of working: open a new chat in `D:/AI-Job/AI_SDLC` and type `/next`. One chat does the whole
  task: plan → build → Auditor sub-agent → merge → this handoff
- Plan: whole MVP built and batch-tested in 3 weeks, proof with real people in weeks 4–5 (`docs/plan.md`).
  Next epics wait for the previous agent's batch-2 task, not its hold-out and acceptance
- Task guide page: `docs/reference/task-guide.html` (all 119 tasks in plain words)

- T-02.1: Stitch works through `@google/stitch-sdk` with the key read from the keychain by the script:
  3 screens (52–64 s each) + 1 edit (28 s), HTML and PNG. Result: `docs/spikes/T-02.1-stitch.md`; audit PASS
  (`plans/audits/T-02.1.md`)
- T-02.2: the guard hook sees the caller (`agent_type`, `agent_id`; none for main) and can deny per agent (JSON
  deny or exit 2). A hook that crashes (exit 1), is missing (127) or times out **lets the call through**;
  `|| exit 2` on the command + a timer in the script that exits 2 first block all three. Result:
  `docs/spikes/T-02.2-guard.md`; audit PASS (`plans/audits/T-02.2.md`)

## Decided

- One task at a time per person; no worktree folders; the chat asks before `git push`
- With 2–3 people, each runs `/next agents`, `/next platform` or `/next product` on their own computer
- ADR-11 confirmed with notes. For T-02.8: Stitch screens cannot be read back (no job ID) so ADR-25 "resume" fails
  for Stitch; Stitch renames fields; keychain reader proven on Windows only; the SDK says it is not officially supported
- Project `.mcp.json` (Stitch MCP server, key from `${STITCH_API_KEY}`, no key in the file) is on `main` for the
  comparison only; every session will offer it. Remove or keep in T-02.8. Never put the key in a `.env` file
- ADR-19 confirmed with a build change (fail closed = `try/except` → exit 2 + `|| exit 2` + in-script timer).
  4.8 (and maybe 3.4) wording changes go through T-02.8. Hold-out guard fix stays in the inbox for the Lead

## Next

- **`/next` order this week:** T-02.4 (add the plugin-hook repeat from the inbox), T-02.7 (need nothing), then T-02.1, T-02.5, T-02.6, T-02.3
  as their needs arrive, then T-02.8, E-03, E-04, E-06
- **Needs ready:** Stitch key: ready (Windows Credential Manager `ai-sdlc/stitch`; Workspace account, 400 left)
- **People, days 1–2 (these set the 3-week date):**
  - Langfuse keys and cloud or self-hosted (T-02.6), 3 real PDF briefs (T-02.5),
    Figma Full seat and test file (T-02.3)
  - T-01.4: review answer keys in batch-1, batch-2, batch-3 and add 2–4 real documents (blocks every agent build)
  - T-01.5: write the hold-out outside the project
  - T-01.3: invite the other owners; T-18.1: past project briefs for live test L1 (end of week 1)

## Problems and open questions

- Answer keys are AI drafts until T-01.4
- Claude usage limits during batch tests; evaluation API budget
- An old empty hold-out folder may still exist in `D:/AI-Job/`; delete it by hand (T-01.5)
