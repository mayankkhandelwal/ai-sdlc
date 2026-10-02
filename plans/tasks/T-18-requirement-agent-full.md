# T-18 · Requirement agent (full)

- **Phase:** 4 Understand
- **Owner:** Agents
- **Depends on:** T-14, T-17
- **Status:** todo
- **Branch:** `t-18-requirement-agent-full`

## Goal

Quotes with positions, table cells, convention items, confidence, stable IDs, draft questions.

## Read only these

- `docs/architecture/02-low-level-flow.md (2.4)`
- `docs/architecture/04-agent-runtime.md (4.1, 4.7)`
- `docs/architecture/05-parts-and-concepts.md (5.4)`

## Produce

- plugin/agents/requirement-agent.md

## Done when

- 3-batch test (eval/README.md): batch-1 fixed, batch-2 fixed, hold-out pass; 3 runs per document

## Tests

- eval batches; generality check

## Skills to use

- mattpocock-skills:writing-for-agents
- superpowers:test-driven-development

## Rules to remember

- R1: nothing specific to any test document in agent, skill or prompt files
- R2: never open `eval/holdout/`
- R3: rules first, AI only for judgment

## Plan (filled in step 2 of the cycle)

_To be written at the start of the task._

## Notes and results

_Add findings, decisions (with ADR links) and the general problems fixed._
