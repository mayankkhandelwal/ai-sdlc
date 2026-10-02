# T-11 · State script mvp-state

- **Phase:** 2 Foundations
- **Owner:** Platform
- **Depends on:** T-09
- **Status:** todo
- **Branch:** `t-11-state-script-mvp-state`

## Goal

States, allowed moves, advance conditions, lock, versions and hashes, resume, rebuild.

## Read only these

- `docs/architecture/02-low-level-flow.md (2.1, 2.2)`
- `docs/contracts/state.json`

## Produce

- plugin/bin/mvp-state

## Done when

- Every allowed and illegal move tested; refuses advance without checks or approvals

## Tests

- Unit tests per transition; kill-mid-step test; lock test

## Skills to use

- superpowers:test-driven-development

## Rules to remember

- R1: nothing specific to any test document in agent, skill or prompt files
- R2: never open `eval/holdout/`
- R3: rules first, AI only for judgment

## Plan (filled in step 2 of the cycle)

_To be written at the start of the task._

## Notes and results

_Add findings, decisions (with ADR links) and the general problems fixed._
