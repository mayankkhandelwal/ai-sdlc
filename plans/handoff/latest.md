# Handoff

- **Date (UTC):** 2026-10-02
- **Task:** T-01.2 · Plan system: epics, tasks, audits, inbox
- **Branch:** main
- **Who:** Claude (Builder), with the project lead

## Done in this chat

- T-01.1: context library (first commit)
- T-01.2: plans restructured as epic → task → sub-task: 17 epics, 109 tasks, each with sub-task
  checklist, done-when and a proof section
- Roles Lead / Builder / Auditor / Human, ready and done rules, inbox, audit procedure, failure catalog
- `tools/board.py` shows ready tasks and warns about missing proof or audits

## Decided

- 3 levels only (epic → task → sub-task); the "main agent" is a Lead chat, not a program
- Agent epics use 7 tasks, with a baseline before tuning, a batch-1 regression rerun, and the failure catalog
- Acceptance: the area owner, the project lead for cross-cutting work, never only the builder

## Next step (exact)

- People: **T-01.3** push to a private GitHub repo; **T-01.4** review answer keys and add real documents
- Builders: **T-02.1 to T-02.7** (week-1 spikes), one chat each, in parallel
- Start a builder chat with: "Read `plans/handoff/latest.md` and `plans/tasks/T-02.1-spike-stitch-from-a-typescript-script.md`."

## Problems and open questions

- Answer keys are AI drafts until T-01.4
- Stitch account type (T-02.1); Langfuse cloud or self-hosted (T-02.6); evaluation API budget

## Files changed

- `plans/` (roadmap, epics, tasks, inbox, audits, failure catalog, handoff), `tools/board.py`,
  `CLAUDE.md`, `docs/process/how-we-work-with-claude.md`
