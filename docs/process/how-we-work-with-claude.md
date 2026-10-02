# How we work with Claude

This is the working method for every task. It keeps context small, keeps decisions in the repo and
keeps the agents general.

## 0. The plan system

```
Lead (planning chat)      keeps the roadmap, sorts the inbox, picks the next task, reads audits
  └─ Epic (plans/epics/)  one per agent or part, with its owner and acceptor
       └─ Task (plans/tasks/)   one chat each: sub-task checklist, done-when, proof
            └─ Audit (plans/audits/)  fresh-context check of the proof
```

| Role | Who | Does | Never does |
|---|---|---|---|
| **Lead** | A planning chat, started when needed | Keeps `plans/roadmap.md`, sorts `plans/inbox.md`, picks ready tasks (`python tools/board.py`), reads audit results | Write product code |
| **Builder** | A new chat per task, one task at a time | One task: plan, test first, build, record proof | Change other tasks or the plan |
| **Auditor** | A fresh chat or sub-agent, never the builder | Checks done-when against proof, reruns tests, writes the audit file | Fix things |
| **Human** | The team | Approves plans, reviews answer keys, accepts epics, decides disagreements | — |

**Status flow:** `todo` → `doing` → `review` → `done`; also `blocked`, `needs-human`, and `skipped`
(work dropped on purpose, e.g. the Figma path moved to v1.1; needs an ADR).

**Branches:** every task works on its own branch; after its audit passes, it is merged to `main`.
New chats always start from an up-to-date `main`.

**Ready rule:** a task can start only when every task it depends on is `done`. `tools/board.py` lists ready tasks.

**Done rule:** every sub-task ticked, proof recorded, tests pass, generality check passes, docs and ADRs
updated, roadmap and handoff updated, committed. Then an audit.

**One task doing per person** at a time.

**Acceptance:** the epic's acceptor accepts, never only the person who built it. The project lead
accepts cross-cutting epics and every architecture change.

**New work:** goes into `plans/inbox.md`. The Lead sorts it into a task, an epic, or "no / later".
Nothing is built straight from the inbox.

**Agent epics** use 7 tasks: design → build v1 and baseline → batch-1 → batch-2 with regression →
hold-out → audit → accept. Every batch task adds general failure types to `plans/failure-catalog.md`,
and every later agent's design task reads it first.

## 1. The cycle for every task

| Step | What happens | Skill or tool to use |
|---|---|---|
| 0. Start | New chat. Read `plans/handoff/latest.md` and the task file. Set status `doing`. Create the task branch | `CLAUDE.md` start steps |
| 1. Understand | Read only the files the task lists. Restate the goal and "done when" in 3 lines | `agent-ready-repo:intent` |
| 2. Plan | Write a short plan in the task file: steps, files to change, tests. Review it before coding | `superpowers:writing-plans`, `agent-ready-repo:plan-eng-review` |
| 3. Test first | Write the failing test. For agents: pick the evaluation batch and expected checks | `superpowers:test-driven-development` |
| 4. Build | The smallest change that passes. One concern at a time | `superpowers:executing-plans`, `agent-ready-repo:implement` |
| 5. Verify | Run tests. For agents: run the batch, read 2–3 traces in Langfuse | `superpowers:verification-before-completion` |
| 6. Review | Fresh-context review: a teammate, or a review sub-agent | `code-review`, `superpowers:requesting-code-review` |
| 7. Finish | Record proof; update docs and ADRs if anything changed; run the generality check; set status `review`; commit; update roadmap and handoff; close the chat | `superpowers:finishing-a-development-branch`, `agent-ready-repo:document-release` |
| 8. Audit | A fresh chat or sub-agent audits the task; pass → `done`, fail → back to `doing` | `plans/audits/README.md` |

When something breaks: reproduce it, find the real cause, fix it, and add a test so it can't return
(`agent-ready-repo:investigate`, `superpowers:systematic-debugging`).

## 2. Prompts to paste

**Start of a task chat** (new chat in `D:/AI-Job/AI_SDLC`, named `T-xx.y Builder`)

> You are the Builder for T-xx.y. Run `git switch main`, then create the task's branch from its task file
> with `git switch -c <branch>`. Read `plans/handoff/latest.md`, `plans/tasks/T-xx.y-….md`, and
> `plans/handoff/T-xx.y.md` if it exists. Then read only the files that task lists. Tell me the goal, the
> done-when and your plan before changing anything.

**End of a task chat**

> We're finishing T-xx.y. Fill its Proof, set its status to review, write `plans/handoff/T-xx.y.md` from the
> template, run `python tools/check_generality.py`, and commit on the task branch. Stay on the branch. Don't edit
> `plans/roadmap.md` or `plans/handoff/latest.md`; the Lead does that.

**Lead chat** (named `Lead`, kept open)

> You are the Lead. Read `plans/handoff/latest.md`, run `python tools/board.py`, and read `plans/inbox.md`.
> If the last task's audit passed, merge its branch into `main`, mark it done, update `plans/roadmap.md` and
> `plans/handoff/latest.md`, and commit. Then tell me the one next task and give me its Builder prompt.
> Don't write product code.

**Audit chat** (new chat, named `T-xx.y Auditor`, after the Builder finished)

> You are the Auditor for T-xx.y. Stay on the current branch. Read `plans/audits/README.md` and the task file. Check every done-when
> item against the proof, rerun the tests and the generality check, and write `plans/audits/T-xx.y.md`.
> Don't fix anything. Commit the audit file on this branch.

**When the chat feels long or confused**

> Stop. Write the current state into `plans/handoff/T-xx.y.md` and commit. I'll start a new chat.

## 3. Keeping context small

- One chat = one task. Start a new chat for the next task.
- Big searches and reviews go to a sub-agent, which returns only the conclusion.
- Read one section file instead of a whole folder.
- Refer to items by ID (`REQ-12`, `ADR-21`) instead of pasting their text.
- If Claude starts repeating itself, forgetting rules or mixing up details, write the handoff and
  start fresh. Don't argue with a tired context.

## 4. Git

- `main` is always working. No direct commits to `main` except the context library itself.
- One branch per task: `t-07-2-build-v1-and-baseline`.
- **One task at a time.** Every chat opens in `D:/AI-Job/AI_SDLC` (the app's worktree box unticked).
  The Builder creates the task branch there; the Auditor works on the same branch; the Lead merges it
  into `main` after PASS. The next task starts only after that merge. No worktree folders are used
  (running tasks in parallel again would need an ADR). Names are in `docs/process/names.md`.
- A Builder writes only its own task file, its own handoff (`plans/handoff/T-xx.y.md`) and the files its
  task produces. Only the Lead edits `plans/roadmap.md` and `plans/handoff/latest.md`.
- Merge through a pull request, reviewed by another owner. The pre-commit hook runs the
  generality check.
- Commit messages say the general problem fixed, not the test document: "Critic now asks about
  error paths in multi-step approvals", not "fix b1-02".

## 5. Testing agents: the 3-batch method

Full method in `eval/README.md`. In short:

1. Build the agent. Run it on **batch-1** (4 documents × 3 runs). Fix the general causes.
2. Run on **batch-2** (4 new documents × 3 runs). Shows whether the fixes were general. Fix again.
3. Run once on the **hold-out** with `python tools/eval_score.py` (4 unseen documents × 3 runs; summary
   only). Pass = done. Fail = back to step 2. If hold-out content was ever seen, those documents move into
   the repo as a new batch and a new hold-out set is written outside the repo (rule R2).

Before every fix, ask: "Would this help a document from a completely different industry?"

## 6. Decisions

- Any choice that changes the architecture gets an ADR in `docs/adr/` (template there).
- Claude says clearly when it thinks an idea is wrong, with the reason and a better option.
  The user decides, and the decision is written down.

## 7. Who does what (owners)

| Owner | Area |
|---|---|
| Agents | Agent and skill files, rubrics, AI parts of checks, evaluation |
| Platform | Plugin, state script, guard and other hooks, rules checks, reader, Stitch script, tracing |
| Product | Question files and answer map, review page, Figma frame builder and compiler, team library |

Anyone can work in any area; the owner reviews changes to it.
