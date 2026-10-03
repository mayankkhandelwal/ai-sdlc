# How we work with Claude

This is the working method for every task. It keeps context small, keeps decisions in the repo and
keeps the agents general.

## 0. The plan system

```
/next chat               picks the next ready task, builds it, has it audited, merges, hands off
  └─ Epic (plans/epics/)  one per agent or part, with its owner and acceptor
       └─ Task (plans/tasks/)   one chat each: sub-task checklist, done-when, proof
            └─ Audit (plans/audits/)  fresh-context check of the proof
```

| Role | Who | Does | Never does |
|---|---|---|---|
| **Lead** | The end of each `/next` chat; a planning chat only when the plan changes | Merges after PASS, keeps `plans/roadmap.md` and `plans/handoff/latest.md`, sorts `plans/inbox.md` | Write product code |
| **Builder** | The `/next` chat, one task at a time | One task: plan, test first, build, record proof | Change other tasks or the plan |
| **Auditor** | A sub-agent started by the `/next` chat, fresh context | Checks done-when against proof, reruns tests, writes the audit file | Fix things |
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
| 0. Start | New chat, `/next`. Read `plans/handoff/latest.md` and the task file. Set status `doing`. Create the task branch | `/next` |
| 1. Understand | Read only the files the task lists. Restate the goal and "done when" in 3 lines | `agent-ready-repo:intent` |
| 2. Plan | Write a short plan in the task file: steps, files to change, tests. Review it before coding | `superpowers:writing-plans`, `agent-ready-repo:plan-eng-review` |
| 3. Test first | Write the failing test. For agents: pick the evaluation batch and expected checks | `superpowers:test-driven-development` |
| 4. Build | The smallest change that passes. One concern at a time | `superpowers:executing-plans`, `agent-ready-repo:implement` |
| 5. Verify | Run tests. For agents: run the batch, read 2–3 traces in Langfuse | `superpowers:verification-before-completion` |
| 6. Review | Fresh-context review: a teammate, or a review sub-agent | `code-review`, `superpowers:requesting-code-review` |
| 7. Finish | Record proof; update docs and ADRs if anything changed; run the generality check; set status `review`; commit; update roadmap and handoff; close the chat | `superpowers:finishing-a-development-branch`, `agent-ready-repo:document-release` |
| 8. Audit and merge | An Auditor sub-agent audits the task; pass → merge and `done`, fail → fix and audit again | `plans/audits/README.md` |

When something breaks: reproduce it, find the real cause, fix it, and add a test so it can't return
(`agent-ready-repo:investigate`, `superpowers:systematic-debugging`).

## 2. Running a task: `/next`

Open a new chat in `D:/AI-Job/AI_SDLC` (the app's worktree box unticked), name it after the task once
you know it (`T-02.2`), and type:

> /next

The steps it follows are in `.claude/commands/next.md`: pick the first ready task → read only what it
needs → branch → plan → wait for "go" → build → proof → **Auditor sub-agent** → fix until PASS → merge
into `main` → update roadmap and handoff → ask before pushing. Then close the chat and open a new one
for the next task. `/next T-02.4` runs a given task; `/next agents` picks a task from one area.

**Human tasks:** `/next` lists what the person must do and stops; do them by hand.

**When the chat feels long or confused**

> Stop. Write the current state into `plans/handoff/T-xx.y.md` and commit. I'll start a new chat.

Then in a new chat: `/next T-xx.y` continues from that handoff.

**Changing the plan** (new epics, reordering, sorting the inbox): a separate chat that says
"You are the Lead" and names the change. It never writes product code.

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
- **One task at a time per person.** Every chat opens in `D:/AI-Job/AI_SDLC` (the app's worktree box
  unticked). The `/next` chat creates the task branch, and merges it into `main` after the Auditor
  sub-agent's PASS. No worktree folders. With more people, each works on their own computer and own
  area (`/next agents`, `/next platform`, `/next product`), so two people never take the same task.
- Pushing to GitHub: the chat asks first. Before starting, `/next` pulls the latest `main`.
- The Auditor sub-agent is the review before merging; the epic's audit and acceptance tasks are the
  second check. The pre-commit hook runs the generality check.
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
