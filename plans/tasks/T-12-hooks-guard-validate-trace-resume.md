# T-12 · Hooks: guard, validate, trace, resume

- **Phase:** 2 Foundations
- **Owner:** Platform
- **Depends on:** T-03, T-09
- **Status:** todo
- **Branch:** `t-12-hooks-guard-validate-trace-res`

## Goal

Guard (per-agent permissions, fails closed), quick schema validation, masked trace events, resume message.

## Read only these

- `docs/architecture/04-agent-runtime.md (4.8)`
- `docs/architecture/03-system-diagram.md (3.4)`

## Produce

- plugin/hooks/

## Done when

- Every permission-matrix rule tested; crash blocks

## Tests

- Red-team cases for each rule

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
