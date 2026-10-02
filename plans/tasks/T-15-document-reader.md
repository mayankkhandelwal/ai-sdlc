# T-15 · Document reader

- **Phase:** 2 Foundations
- **Owner:** Platform
- **Depends on:** T-06, T-09
- **Status:** todo
- **Branch:** `t-15-document-reader`

## Goal

mvp-read: DOCX/PDF/MD to sections, table cells, images, normalised copy, language, injection pattern scan.

## Read only these

- `docs/architecture/02-low-level-flow.md (2.3)`

## Produce

- plugin/bin/mvp-read

## Done when

- All 8 batch-1/2 documents convert; section and table counts match

## Tests

- Converter tests on batch-1 and batch-2 documents

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
