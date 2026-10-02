# T-01 · Review test documents and add real ones

- **Phase:** 0 Setup
- **Owner:** Human (all)
- **Depends on:** T-00
- **Status:** todo
- **Branch:** `t-01-review-test-documents-and-add-`

## Goal

People review the AI-written answer keys and add 2–4 real, anonymised briefs from past projects.

## Read only these

- `eval/README.md`
- `eval/batch-1/*/answer-key.md`
- `eval/batch-2/*/answer-key.md`

## Produce

- Corrected answer keys
- 2–4 real documents with answer keys and banned terms

## Done when

- Every batch-1 and batch-2 key marked 'reviewed by <name>'
- Hold-out keys reviewed by someone who will not build agents

## Tests

- —

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
