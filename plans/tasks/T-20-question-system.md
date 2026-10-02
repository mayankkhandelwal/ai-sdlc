# T-20 · Question system

- **Phase:** 4 Understand
- **Owner:** Product
- **Depends on:** T-18, T-19
- **Status:** todo
- **Branch:** `t-20-question-system`

## Goal

Question builder, batch files (HTML + MD), check-in every 4 batches, answer extraction, edit warnings.

## Read only these

- `docs/architecture/02-low-level-flow.md (U6–U10, stop table)`
- `docs/mvp-flow.md (Question system)`

## Produce

- plugin/bin/mvp-questions
- question templates

## Done when

- Non-technical tester answers a batch without help

## Tests

- Parsing tests for messy answers

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
