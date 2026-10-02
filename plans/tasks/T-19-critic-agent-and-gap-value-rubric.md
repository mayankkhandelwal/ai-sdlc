# T-19 · Critic agent and gap-value rubric

- **Phase:** 4 Understand
- **Owner:** Agents
- **Depends on:** T-18
- **Status:** todo
- **Branch:** `t-19-critic-agent-and-gap-value-rub`

## Goal

Fixed gap list with importance levels; gap-value check.

## Read only these

- `docs/architecture/02-low-level-flow.md (U5, U5b)`
- `docs/architecture/05-parts-and-concepts.md (5.4)`

## Produce

- plugin/agents/critic-agent.md
- rubric gap-value

## Done when

- 3-batch test (eval/README.md): batch-1 fixed, batch-2 fixed, hold-out pass; 3 runs per document; finds planted gaps

## Tests

- eval batches

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
