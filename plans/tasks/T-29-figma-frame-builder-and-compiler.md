# T-29 · Figma frame builder and compiler

- **Phase:** 5 Design
- **Owner:** Product
- **Depends on:** T-28
- **Status:** todo
- **Branch:** `t-29-figma-frame-builder-and-compil`

## Goal

Layout file, mvp-figma-compile, frame builder courier, facts from layers. Only if the gate passed.

## Read only these

- `docs/architecture/02-low-level-flow.md (S2b)`
- `docs/architecture/05-parts-and-concepts.md (5.8)`

## Produce

- plugin/agents/frame-builder-agent.md
- plugin/bin/mvp-figma-compile

## Done when

- 3-batch test (eval/README.md): batch-1 fixed, batch-2 fixed, hold-out pass; 3 runs per document (design subset)

## Tests

- Contract tests vs Stitch facts; crash test

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
