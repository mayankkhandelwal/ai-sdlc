# Handoff

- **Date (UTC):** 2026-10-02
- **Task:** T-01.2 · Plan system: epics, tasks, audits, inbox
- **Branch:** `t-01-2-plan-system` (merge to `main` after its audit passes)
- **Who:** Claude (Builder), with the project lead

## Done in this chat

- T-01.1: context library (first commit); audit PASS (`plans/audits/T-01.1.md`)
- T-01.2: plans as epic → task → sub-task: 17 epics, 112 tasks, each with sub-tasks, done-when, proof
  and "needs from a person"; roles Lead / Builder / Auditor / Human; inbox; audit procedure; failure catalog
- `tools/board.py`: ready list; warns about missing proof, missing PASS audits, unknown dependencies, cycles
- Four audits of T-01.2 failed (8, 4, 3 findings, then 7 guard bypasses out of 51 attempts); all fixed
- **Structural change for rule R2:** the hold-out set now lives outside the repo (`HOLDOUT_DIR`). The old
  in-repo set is kept as `eval/batch-3`. `tools/guard_holdout.py` blocks every tool call that points at the
  outside folder, including writes; `tools/tests/` has 7 passing tests
- New task **T-01.5**: a person writes the new hold-out in a separate Claude session started outside this project

## Decided

- 3 levels only; the "main agent" is a Lead chat, not a program
- Agent epics: 7 tasks with baseline, regression rerun and the failure catalog
- Every epic's acceptance blocks v1 acceptance; dropped work is `skipped` with an ADR
- Acceptance by someone who did not build it
- The hold-out is protected by being outside the repo, not by pattern matching alone

## Next step (exact)

- After T-01.2's audit passes: merge `t-01-2-plan-system` into `main`
- People: **T-01.3** push to GitHub; **T-01.4** review answer keys (batch-1, 2, 3); **T-01.5** write the hold-out outside
- Builders: **T-02.1 to T-02.7** (week-1 spikes), one chat each, from `main`
- Start a builder chat with: "Read `plans/handoff/latest.md` and `plans/tasks/T-02.1-spike-stitch-from-a-typescript-script.md`."

## Problems and open questions

- Answer keys are AI drafts until T-01.4
- Stitch account type (T-02.1); Langfuse cloud or self-hosted (T-02.6); evaluation API budget

## Files changed

- `plans/`, `eval/` (holdout → batch-3, README), `tools/board.py`, `tools/guard_holdout.py`,
  `tools/check_generality.py`, `tools/tests/`, `.claude/settings.json`, `CLAUDE.md`, `docs/rules.md`,
  `docs/process/how-we-work-with-claude.md`
