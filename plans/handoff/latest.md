# Handoff

- **Date (UTC):** 2026-10-03
- **Last change:** `/next` (one chat per task) and the 3-week plan (Lead)
- **Branch:** `main` (no other branches)
- **Who:** Claude (Lead), with the project lead

## Done

- T-01.1: context library; audit PASS (`plans/audits/T-01.1.md`)
- T-01.2: plan system: 18 epics, 119 tasks, roles, inbox, audits, failure catalog; audit PASS
- Spike work from the parallel chats (T-02.2, T-02.4, T-02.7) was dropped; those tasks are `todo` again
- New way of working: open a new chat in `D:/AI-Job/AI_SDLC` and type `/next`. One chat does the whole
  task: plan → build → Auditor sub-agent → merge → this handoff
- Plan: whole MVP built and batch-tested in 3 weeks, proof with real people in weeks 4–5 (`docs/plan.md`).
  Next epics wait for the previous agent's batch-2 task, not its hold-out and acceptance
- Task guide page: `docs/reference/task-guide.html` (all 119 tasks in plain words)

## Decided

- One task at a time per person; no worktree folders; the chat asks before `git push`
- With 2–3 people, each runs `/next agents`, `/next platform` or `/next product` on their own computer
- Kept from the dropped T-02.2 chat: a crashing or timed-out hook lets the call through (in `plans/inbox.md`).
  The redone T-02.2 must prove it again

## Next

- **`/next` order this week:** T-02.2, T-02.4, T-02.7 (need nothing), then T-02.1, T-02.5, T-02.6, T-02.3
  as their needs arrive, then T-02.8, E-03, E-04, E-06
- **Needs ready:** none yet. When one arrives, write it here (e.g. "Stitch key: ready")
- **People, days 1–2 (these set the 3-week date):**
  - Stitch API key (T-02.1), Langfuse keys and cloud or self-hosted (T-02.6), 3 real PDF briefs (T-02.5),
    Figma Full seat and test file (T-02.3)
  - T-01.4: review answer keys in batch-1, batch-2, batch-3 and add 2–4 real documents (blocks every agent build)
  - T-01.5: write the hold-out outside the project
  - T-01.3: invite the other owners; T-18.1: past project briefs for live test L1 (end of week 1)

## Problems and open questions

- Answer keys are AI drafts until T-01.4
- Claude usage limits during batch tests; evaluation API budget
- An old empty hold-out folder may still exist in `D:/AI-Job/`; delete it by hand (T-01.5)
