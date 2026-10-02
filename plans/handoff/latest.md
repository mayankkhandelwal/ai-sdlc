# Handoff

- **Date (UTC):** 2026-10-02
- **Last task:** T-01.2 · Plan system: epics, tasks, audits, inbox — **done** (audit 8 PASS)
- **Branch:** merged into `main`
- **Who:** Claude (Builder), with the project lead

## Done

- T-01.1: context library; audit PASS (`plans/audits/T-01.1.md`)
- T-01.2: plans as epic → task → sub-task: 17 epics, 112 tasks, each with sub-tasks, done-when, proof and
  "needs from a person"; roles Lead / Builder / Auditor / Human; inbox; audit procedure; failure catalog
- `tools/board.py`: ready list; warns about missing proof, missing PASS audits, unknown dependencies, cycles
- The hold-out set now lives outside the repo (`HOLDOUT_DIR`); the old one is `eval/batch-3`.
  `tools/guard_holdout.py` stops accidental and obvious access (not a security boundary; limits in R2).
  `tools/tests/` has 10 passing tests
- T-01.2 needed 8 audits; the failed ones are kept in `plans/audits/` as a record of what was found

## Decided

- 3 levels only; the "main agent" is a Lead chat, not a program
- Agent epics: 7 tasks with baseline, regression rerun and the failure catalog
- Every epic's acceptance blocks v1 acceptance; dropped work is `skipped` with an ADR
- Acceptance by someone who did not build it
- The hold-out is protected mainly by being outside the repo; the guard catches accidents

## Next (run `python tools/board.py`)

- **People:**
  - T-01.3: push the repo to a private GitHub repo
  - T-01.4: review answer keys in batch-1, batch-2 and batch-3, and add 2–4 real documents
  - T-01.5: write the new hold-out set, in a Claude session started outside this project
- **Builders:** T-02.1 to T-02.7, the week-1 spikes, one chat each, from `main`
- Start a builder chat with: "Read `plans/handoff/latest.md` and `plans/tasks/T-02.1-spike-stitch-from-a-typescript-script.md`."

## Problems and open questions

- Answer keys are AI drafts until T-01.4
- Stitch account type (T-02.1); Langfuse cloud or self-hosted (T-02.6); evaluation API budget
- Four empty folders may exist in the default hold-out location from a blocked attempt (see T-01.5 notes)
