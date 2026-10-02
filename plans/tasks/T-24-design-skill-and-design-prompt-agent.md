# T-24 · Design skill and Design Prompt agent

- **Phase:** 5 Design
- **Owner:** Agents
- **Depends on:** T-22
- **Status:** todo
- **Branch:** `t-24-design-skill-and-design-prompt`

## Goal

Checklist (platform first), style message, screen messages, sample choice, accessibility and outgoing scan.

## Read only these

- `docs/architecture/02-low-level-flow.md (2.6)`
- `docs/architecture/05-parts-and-concepts.md (5.7)`

## Produce

- plugin/skills/design-prompt/
- plugin/agents/design-prompt-agent.md

## Done when

- 3-batch test (eval/README.md): batch-1 fixed, batch-2 fixed, hold-out pass; 3 runs per document; every criterion in its screen message

## Tests

- eval batches

## Skills to use

- anthropic-skills:skill-creator
- mattpocock-skills:writing-for-agents

## Rules to remember

- R1: nothing specific to any test document in agent, skill or prompt files
- R2: never open `eval/holdout/`
- R3: rules first, AI only for judgment

## Plan (filled in step 2 of the cycle)

_To be written at the start of the task._

## Notes and results

_Add findings, decisions (with ADR links) and the general problems fixed._
