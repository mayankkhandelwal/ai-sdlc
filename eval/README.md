# Evaluation

How every agent is tested before it counts as done.

## Test documents

| Set | Where | Documents | Use |
|---|---|---|---|
| `batch-1/` | this repo | 4 | Build and fix |
| `batch-2/` | this repo | 4 | Check that fixes were general; fix again |
| `batch-3/` | this repo | 4 | Extra set for more fixing and regression checks (the first hold-out, retired because it was in the repo) |
| **hold-out** | **outside this repo** (`HOLDOUT_DIR`) | 4 | Final pass/fail only. **Never opened in a chat** (rule R2) |

Each document folder has:

- `document.md` (and sometimes `document.docx`): the client brief the agents read
- `answer-key.md`: the expected roles, requirements with quotes, gaps, contradictions, traps and
  screens. **Draft written by an AI, must be reviewed by a person** before scores count
- `banned-terms.txt`: terms that must never appear in agent, skill or prompt files (rule R1)

The 12 in-repo documents cover 12 different industries and deliberately vary in quality: well written,
short and vague, meeting notes, contradictions, tables, hidden injection text, other languages,
very long. The hold-out covers 4 more industries.

Agents under test **never read `answer-key.md`**. Only the scoring script compares output with it.

## The 3-batch method

1. **Batch-1:** run the agent on all 4 documents, 3 runs each. Read the failures and traces.
   Fix the **general** cause.
2. **Batch-2:** run on 4 new documents, 3 runs each. Problems here show whether the batch-1 fixes
   were general. Fix again. Rerun batch-1 to check nothing got worse. Batch-3 can be used for a
   further round if needed.
3. **Hold-out:** `python tools/eval_score.py` runs it (3 runs each) and shows only the summary score.
   Pass = the agent is done. Fail = back to step 2. If hold-out content was ever seen, those documents
   move into the repo as a new batch, and a new hold-out set is written.

## The hold-out set

- It lives **outside this repo**, in a folder named by the `HOLDOUT_DIR` environment variable. Set it in
  the environment Claude Code starts from (so the guard hook sees it), or use the default location the
  hook expects (a sibling folder of the repo). The project lead knows where it is.
- It is written by **a person**, in a **separate Claude session started outside this project folder**,
  ideally a teammate who will not build agents (task T-01.5). The project hook `tools/guard_holdout.py`
  blocks obvious and accidental attempts by sessions in this project to read or write it; it does not
  stop deliberate code that walks parent folders (see the known limits in `docs/rules.md`, R2).
- Its `banned-terms.txt` files are still read by `tools/check_generality.py` (rule R1).

## Rules

- Run each document **3 times**, because AI output varies. Report the average and the worst run.
  Hard rules (no invented requirement, no followed injection) must hold on **all** runs.
- Every result is saved in `results/<agent>/<date>/`, so changes can be compared.
- Before every fix: "Would this help a document from a completely different industry?"
- Add documents from new industries every few weeks, and retire old ones to keep the set fresh.

## What a person must do

1. **Review every `answer-key.md` in batch-1, batch-2 and batch-3** (task T-01.4): correct the expected
   requirements, gaps and screens.
2. **Write the hold-out set** outside the repo (task T-01.5), or have a teammate who won't build agents
   write it, and review its keys there.
3. **Add 2–4 real documents** from past projects (anonymised, with permission). Real briefs are
   messier than written ones.
4. **Label calibration items** for the AI judges: about 50 per gating rubric (support, testable,
   scope, look), marking each as correct or not.
5. **Rate sample screens** as a designer (1–5) during the design stages.
6. **Rotate documents** every few weeks with new industries.
