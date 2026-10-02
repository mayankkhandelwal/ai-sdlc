# T-16 · Evaluation runner and scorer

- **Phase:** 2 Foundations
- **Owner:** Agents
- **Depends on:** T-09
- **Status:** todo
- **Branch:** `t-16-evaluation-runner-and-scorer`

## Goal

Run an agent on a batch × 3 runs, compare with answer keys, save results; hold-out shows summary only.

## Read only these

- `eval/README.md`
- `docs/architecture/06-decisions-and-risks.md (6.4)`

## Produce

- tools/eval_run.py
- tools/eval_score.py

## Done when

- Scores saved in eval/results/; hold-out prints summary only

## Tests

- Dry run with a fake agent output

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
