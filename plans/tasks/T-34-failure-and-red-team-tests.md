# T-34 · Failure and red-team tests

- **Phase:** 7 Evaluate
- **Owner:** Platform
- **Depends on:** T-31
- **Status:** todo
- **Branch:** `t-34-failure-and-red-team-tests`

## Goal

Crashes, limits, two sessions, edited questions, injection on every channel, key leaks.

## Read only these

- `docs/architecture/06-decisions-and-risks.md (6.3)`
- `docs/architecture/02-low-level-flow.md (2.9)`

## Produce

- test suite

## Done when

- All failure and safety tests pass

## Tests

- Red-team set

## Skills to use

- security-review

## Rules to remember

- R1: nothing specific to any test document in agent, skill or prompt files
- R2: never open `eval/holdout/`
- R3: rules first, AI only for judgment

## Plan (filled in step 2 of the cycle)

_To be written at the start of the task._

## Notes and results

_Add findings, decisions (with ADR links) and the general problems fixed._
