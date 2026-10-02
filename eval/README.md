# Evaluation

How every agent is tested before it counts as done.

## Test documents

| Folder | Documents | Use |
|---|---|---|
| `batch-1/` | 4 | Build and fix |
| `batch-2/` | 4 | Check that fixes were general; fix again |
| `holdout/` | 4 | Final pass/fail only. **Never opened in a chat** (rule R2) |

Each document folder has:

- `document.md` (and sometimes `document.docx`): the client brief the agents read
- `answer-key.md`: the expected roles, requirements with quotes, gaps, contradictions, traps and
  screens. **Draft written by an AI, must be reviewed by a person** before scores count
- `banned-terms.txt`: terms that must never appear in agent, skill or prompt files (rule R1)

The 12 documents cover 12 different industries and deliberately vary in quality: well written,
short and vague, meeting notes, contradictions, tables, hidden injection text, other languages,
very long.

Agents under test **never read `answer-key.md`**. Only the scoring script compares output with it.

## The 3-batch method

1. **Batch-1:** run the agent on all 4 documents, 3 runs each. Read the failures and traces.
   Fix the **general** cause.
2. **Batch-2:** run on 4 new documents, 3 runs each. Problems here show whether the batch-1 fixes
   were general. Fix again.
3. **Hold-out:** run once (3 runs each). Only the summary score is shown. Pass = the agent is done.
   Fail = back to step 2 with fresh documents. Hold-out documents that were looked at move to batch-2,
   and new hold-out documents are written.

## Rules

- Run each document **3 times**, because AI output varies. Report the average and the worst run.
  Hard rules (no invented requirement, no followed injection) must hold on **all** runs.
- Every result is saved in `results/<agent>/<date>/`, so changes can be compared.
- Before every fix: "Would this help a document from a completely different industry?"
- Add documents from new industries every few weeks, and retire old ones to keep the set fresh.

## What a person must do

1. **Review every `answer-key.md` in batch-1 and batch-2**: correct the expected requirements, gaps
   and screens. A teammate who will not build the agents reviews the hold-out keys.
2. **Add 2–4 real documents** from past projects (anonymised, with permission). Real briefs are
   messier than written ones.
3. **Label calibration items** for the AI judges: about 50 per gating rubric (support, testable,
   scope, look), marking each as correct or not.
4. **Rate sample screens** as a designer (1–5) during the design stages.
5. **Rotate documents** every few weeks with new industries.
