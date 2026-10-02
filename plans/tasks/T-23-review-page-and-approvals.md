# T-23 · Review page and approvals

- **Phase:** 4 Understand
- **Owner:** Product
- **Depends on:** T-22
- **Status:** todo
- **Branch:** `t-23-review-page-and-approvals`

## Goal

Escaped review page with sources, confidence, version differences, feedback routing, approval records.

## Read only these

- `docs/architecture/02-low-level-flow.md (D4–D7, routing table)`
- `docs/architecture/05-parts-and-concepts.md (5.11)`

## Produce

- plugin/bin/mvp-review
- routing

## Done when

- XSS test strings never run; approvals recorded with hashes

## Tests

- Security tests

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
