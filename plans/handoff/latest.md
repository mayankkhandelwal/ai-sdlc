# Handoff

- **Date (UTC):** 2026-10-03
- **Last change:** Working method changed to **one task at a time** (Lead)
- **Branch:** `main` (no other branches)
- **Who:** Claude (Lead), with the project lead

## Done

- T-01.1: context library; audit PASS (`plans/audits/T-01.1.md`)
- T-01.2: plan system: 18 epics, 119 tasks, roles, inbox, audits, failure catalog; audit PASS
- Running many chats at once was too hard to manage, so it was stopped. The spike chats T-02.2, T-02.4
  and T-02.7 were archived, their worktrees and branches deleted and their work dropped. Those tasks are
  `todo` again
- Every chat now opens in `D:/AI-Job/AI_SDLC`; no worktree folders (`CLAUDE.md`, `docs/process/names.md`,
  `docs/process/how-we-work-with-claude.md`, start guide)
- Branch names in all task files are short whole-word names

## Decided

- One task at a time: Lead → `T-xx.y Builder` → `T-xx.y Auditor` → Lead merges → next task
- Running tasks in parallel again needs an ADR first
- Kept from the dropped T-02.2 chat: a crashing or timed-out hook lets the call through (in `plans/inbox.md`).
  The redone T-02.2 must prove it again

## Next

- **Builder, first task:** T-02.2 (guard hook spike). It needs nothing from a person
- Then, one at a time: T-02.4, T-02.7; then T-02.1, T-02.3, T-02.5, T-02.6 once their keys and files are
  ready; then T-02.8
- **People, any time:** T-01.3 (protect `main`, invite owners), T-01.4 (review answer keys, add real
  documents), T-01.5 (write the hold-out outside the project)

## Problems and open questions

- Answer keys are AI drafts until T-01.4
- Stitch account type (T-02.1); Langfuse cloud or self-hosted (T-02.6); evaluation API budget
- An old empty hold-out folder may still exist in `D:/AI-Job/`; delete it by hand (T-01.5)
