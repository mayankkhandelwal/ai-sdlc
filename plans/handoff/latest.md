# Handoff

- **Date (UTC):** 2026-10-02
- **Task:** T-00 · Set up the context library
- **Branch:** main (first commit)
- **Who:** Claude, with the project lead

## Done in this chat

- Designed the MVP (flow, architecture revision 2, two audits); all decisions accepted
- Created this repo: `CLAUDE.md`, `docs/rules.md`, working method, architecture as Markdown parts,
  27 ADR files, contracts index, roadmap with 36 tasks and one file per task
- Wrote 12 test documents (batch-1, batch-2, hold-out) with draft answer keys and banned terms
- Added `tools/check_generality.py`, the pre-commit hook, and a Claude setting that blocks reading the hold-out

## Decided (with ADR links)

- All decisions are in `docs/adr/README.md` (ADR-01 to ADR-27)
- Fixed rules R1–R11 in `docs/rules.md` (most important: R1 build for any project, R2 hold-out unseen)

## Next step (exact)

- **T-01 (people):** review the answer keys in `eval/batch-1` and `eval/batch-2`; add 2–4 real documents
- **T-02 to T-08 (week-1 spikes):** can start in parallel, one chat each
- First thing in the next chat: "Read `plans/handoff/latest.md` and `plans/tasks/T-02-spike-stitch-from-a-typescript-script.md`"

## Problems and open questions

- Answer keys are AI drafts; scores don't count until people review them
- Stitch account type still to confirm (T-02)
- Langfuse cloud or self-hosted (T-07)
- An approved small API budget for evaluation runs (ADR-01 exception, architecture 6.4)

## Files changed

- Whole repository (first commit)
