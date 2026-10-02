# T-14 · AI checker and gating rubrics

- **Phase:** 2 Foundations
- **Owner:** Agents
- **Depends on:** T-09
- **Status:** todo
- **Branch:** `t-14-ai-checker-and-gating-rubrics`

## Goal

ai-checker agent; rubrics support, clarity, testable, scope, look; calibration sets.

## Read only these

- `docs/architecture/04-agent-runtime.md (4.4)`
- `docs/architecture/05-parts-and-concepts.md (5.2)`

## Produce

- plugin/agents/ai-checker.md
- plugin/skills/rubrics/

## Done when

- Each gating rubric agrees with ~50 human labels well enough to trust

## Tests

- Calibration sets; generality check

## Skills to use

- mattpocock-skills:writing-for-agents

## Rules to remember

- R1: nothing specific to any test document in agent, skill or prompt files
- R2: never open `eval/holdout/`
- R3: rules first, AI only for judgment

## Plan (filled in step 2 of the cycle)

_To be written at the start of the task._

## Notes and results

_Add findings, decisions (with ADR links) and the general problems fixed._
