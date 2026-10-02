# T-25 · Stitch adapter (full)

- **Phase:** 5 Design
- **Owner:** Platform
- **Depends on:** T-02, T-24
- **Status:** todo
- **Branch:** `t-25-stitch-adapter-full`

## Goal

generate, edit, resume from job.json, quota counting, budget.

## Read only these

- `docs/architecture/02-low-level-flow.md (S1, S2a)`
- `docs/architecture/03-system-diagram.md (3.6 adapter)`

## Produce

- plugin/bin/mvp-stitch (TypeScript)

## Done when

- Crash mid-wait resumes with no duplicate

## Tests

- Contract tests; crash test

## Skills to use

- Default cycle in `docs/process/how-we-work-with-claude.md`

## Rules to remember

- R1: nothing specific to any test document in agent, skill or prompt files
- R2: never open `eval/holdout/`
- R3: rules first, AI only for judgment

## Plan (filled in step 2 of the cycle)

_To be written at the start of the task._

## Notes and results

_Add findings, decisions (with ADR links) and the general problems fixed._
