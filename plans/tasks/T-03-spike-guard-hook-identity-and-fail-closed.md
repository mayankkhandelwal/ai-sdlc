# T-03 · Spike: guard hook identity and fail-closed

- **Phase:** 1 Spikes
- **Owner:** Platform
- **Depends on:** T-00
- **Status:** todo
- **Branch:** `t-03-spike-guard-hook-identity-and-`

## Goal

Prove the guard hook sees agent type and ID, can deny, and blocks when it crashes.

## Read only these

- `docs/architecture/04-agent-runtime.md (4.8)`
- `docs/architecture/03-system-diagram.md (3.4)`

## Produce

- docs/spikes/T-03-guard.md

## Done when

- Agent type values recorded for plugin agents and main session
- Forced crash blocks the call

## Tests

- Hook test script

## Skills to use

- plugin-authoring
- claude-code-guide agent

## Rules to remember

- R1: nothing specific to any test document in agent, skill or prompt files
- R2: never open `eval/holdout/`
- R3: rules first, AI only for judgment

## Plan (filled in step 2 of the cycle)

_To be written at the start of the task._

## Notes and results

_Add findings, decisions (with ADR links) and the general problems fixed._
