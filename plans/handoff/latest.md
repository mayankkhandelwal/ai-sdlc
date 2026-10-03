# Handoff

- **Date (UTC):** 2026-10-03
- **Last change:** T-02.1 Stitch spike merged (audit PASS on the 2nd try)
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

## Decided

- One task at a time per person; no worktree folders; the chat asks before `git push`
- With 2–3 people, each runs `/next agents`, `/next platform` or `/next product` on their own computer
- ADR-11 confirmed with notes. For T-02.8: Stitch screens cannot be read back (no job ID) so ADR-25 "resume" fails
  for Stitch; Stitch renames fields; keychain reader proven on Windows only; the SDK says it is not officially supported
- Project `.mcp.json` (Stitch MCP server, key from `${STITCH_API_KEY}`, no key in the file) is on `main` for the
  comparison only; every session will offer it. Remove or keep in T-02.8. Never put the key in a `.env` file
- Kept from the dropped T-02.2 chat: a crashing or timed-out hook lets the call through (in `plans/inbox.md`).
  The redone T-02.2 must prove it again

## Next

- **`/next` order this week:** T-02.2, T-02.4, T-02.7 (need nothing), then T-02.1, T-02.5, T-02.6, T-02.3
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
