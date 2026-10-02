# The plan

The one plan for building the Design-First MVP (v1). Task-level detail lives in `plans/`; this file
explains the whole journey: why there is one plan, the phases, when each part is tested, and when the
system meets a live project.

## Why one plan

| Reason | What it means in practice |
|---|---|
| **One source of truth** | Every chat and every person reads the same `plans/` files. Nobody works from a memory of a chat |
| **Order stays safe** | Dependencies are written down, so a task never starts on unfinished work. Tasks run one at a time |
| **Nothing gets forgotten** | Every part of the architecture maps to a task; a task the board doesn't list doesn't happen |
| **Progress is measurable** | `python tools/board.py` shows done, doing and ready at any moment |
| **"Done" means proven** | Every task has done-when and proof; audits check it against the plan |
| **Changes are controlled** | New ideas go to `plans/inbox.md`; the Lead turns them into tasks. Nothing is built "on the side" |
| **The plan can change** | If a spike or a live test proves something wrong, the plan and the ADRs change, in one commit |

## The phases

Estimates assume 3 engineers and Claude chats running one task at a time. They are a guide; order matters more
than dates.

| Phase | Weeks (estimate) | Epics | Result | Live test after it |
|---|---|---|---|---|
| 0 · Setup | done | E-01 | Repo, rules, plan, test documents | — |
| 1 · Spikes | 1–2 | E-02 | Platform facts proven; ADRs updated (T-02.8) | — |
| 2 · Contracts | 2 | E-03 | File formats and interfaces frozen | — |
| 3 · Foundations | 3–4 | E-04, start E-05 | Plugin, state, hooks, checks, reader, scorer | — |
| 4 · Skeleton | 5 | E-06 | Thin path: document → 1 Stitch screen | **L1 · Shadow** |
| 5 · Understand | 6–9 | E-05, E-07, E-08, E-09, E-10, E-11 | Requirement, critic, questions, stories, review page | **L2 · Assisted** |
| 6 · Design | 10–13 | E-12, E-13, E-14, E-15 (gate) | Design messages, Stitch, samples and feedback, Figma decision | **L3 · Design** |
| 7 · Full flow | 14–15 | E-16 | Full UI, package, commands, usage test | **L4 · End to end** |
| 8 · Evaluate and pilot | 16–18 | E-17 | Full evaluation, red-team, pilot with 3–5 users, v1 accepted | Pilot |

## When testing happens

| Kind of test | When | With what | Who |
|---|---|---|---|
| **Unit and rules tests** | Every build task | Planted-defect files, test inputs | Builder chat |
| **Batch tests** | Every agent epic (tasks .3–.5) | batch-1, batch-2 (+ batch-3), then the hold-out | Builder chat; scorer for the hold-out |
| **Audits** | Every task before "done" | The task's proof | A fresh Auditor chat |
| **Live project tests** | After phases 4, 5, 6 and 7 (L1–L4) | Real project briefs | The team, with Claude |
| **Full evaluation** | Phase 8 | All sets, 3 runs each, per design tool | Agents owner |
| **Pilot** | Phase 8 | 3–5 real users, real non-confidential projects | The team |

Test documents are not enough on their own: written briefs are cleaner than real ones, and only real
use shows whether the output saves time. That is why live tests start in phase 4, not at the end.

## Live project tests (epic E-18)

A **live project** is a real project brief from Softude's work: a past project, or a current one, used
with permission.

| Test | After | Mode | What happens | Pass when |
|---|---|---|---|---|
| **L1 · Shadow** | Skeleton (E-06) | Shadow: nothing goes to a client | Run the skeleton on 1–2 **past** projects; compare with what the team actually produced | Runs end to end; a list of what was missed or wrong, sorted by general failure type |
| **L2 · Assisted** | Understand stage (E-07 to E-11) | Shadow, then assisted | On a **current** project, the BA runs the agents alongside normal work; the team checks every item before using any | The BA rates requirements and stories useful; time saved measured; no invented requirements |
| **L3 · Design** | Design stage (E-12 to E-14, gate E-15) | Assisted | Samples and feedback rounds on a current project; a designer reviews | Designer rating ≥ 3.5/5; feedback rounds ≤ 3; samples usable as a starting point |
| **L4 · End to end** | Full flow (E-16) | Assisted | One current project from document to approved design and package | Completes; team says they would use it again; usage fits the plan |

**Before any live test (T-18.1):**

- Team or Enterprise Claude seats for anyone handling client documents (not Pro/Max)
- The client's permission, or a non-confidential or internal project
- Personal data and secrets removed from the document
- Stitch's terms checked for client data; Figma AI training turned off
- The project chosen is not in any test set

**After every live test:**

- Write `docs/live-tests/L-n.md`: what was measured, what went wrong, what to change
- Add failures to `plans/failure-catalog.md` **in general words only** (rule R1): never the client, the
  product or its domain terms
- Turn changes into items in `plans/inbox.md`; the Lead plans them
- With permission, anonymise the brief and add it to the test documents as a new real document

## Milestones

| Milestone | When it's reached |
|---|---|
| M-1 · Facts proven | T-02.8 done |
| M-2 · Contracts frozen | T-03.4 done |
| M-3 · Skeleton runs | T-06.5 done |
| M-4 · Understand stage accepted | E-07 to E-11 accepted and L2 done |
| M-5 · Design stage accepted | E-12 to E-14 accepted, Figma gate decided, L3 done |
| M-6 · Full flow accepted | E-16 accepted and L4 done |
| M-7 · v1 accepted | T-17.5 done |

## How the plan changes

- New work → `plans/inbox.md` → the Lead adds tasks or epics → `python tools/board.py` shows them.
- A spike, audit or live test that proves something wrong → update the ADR and architecture in the same
  commit, then the affected tasks.
- Dropped work → status `skipped`, with an ADR.
