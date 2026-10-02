# T-13 · Rules checks and schemas

- **Phase:** 2 Foundations
- **Owner:** Platform
- **Depends on:** T-09
- **Status:** todo
- **Branch:** `t-13-rules-checks-and-schemas`

## Goal

mvp-check for every record: schema, IDs, stable IDs, links, quotes, coverage, tokens, accessibility.

## Read only these

- `docs/architecture/02-low-level-flow.md (2.3–2.8 rules rows)`
- `docs/contracts/`

## Produce

- plugin/bin/mvp-check

## Done when

- Planted-defect files fail with exact errors

## Tests

- One defect file per rule

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
