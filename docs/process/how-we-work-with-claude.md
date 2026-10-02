# How we work with Claude

This is the working method for every task. It keeps context small, keeps decisions in the repo and
keeps the agents general.

## 1. The cycle for every task

| Step | What happens | Skill or tool to use |
|---|---|---|
| 0. Start | New chat. Read `plans/handoff/latest.md` and the task file. Create the task branch | `CLAUDE.md` start steps |
| 1. Understand | Read only the files the task lists. Restate the goal and "done when" in 3 lines | `agent-ready-repo:intent` |
| 2. Plan | Write a short plan in the task file: steps, files to change, tests. Review it before coding | `superpowers:writing-plans`, `agent-ready-repo:plan-eng-review` |
| 3. Test first | Write the failing test. For agents: pick the evaluation batch and expected checks | `superpowers:test-driven-development` |
| 4. Build | The smallest change that passes. One concern at a time | `superpowers:executing-plans`, `agent-ready-repo:implement` |
| 5. Verify | Run tests. For agents: run the batch, read 2–3 traces in Langfuse | `superpowers:verification-before-completion` |
| 6. Review | Fresh-context review: a teammate, or a review sub-agent | `code-review`, `superpowers:requesting-code-review` |
| 7. Finish | Update docs and ADRs if anything changed; run the generality check; commit; update roadmap and handoff; close the chat | `superpowers:finishing-a-development-branch`, `agent-ready-repo:document-release` |

When something breaks: reproduce it, find the real cause, fix it, and add a test so it can't return
(`agent-ready-repo:investigate`, `superpowers:systematic-debugging`).

## 2. Prompts to paste

**Start of a chat**

> Read `plans/handoff/latest.md` and `plans/tasks/T-xx-….md`. Then read only the files that task lists.
> Tell me the goal, the done-when and your plan before changing anything.

**End of a chat**

> We're finishing T-xx. Update its status in `plans/roadmap.md`, rewrite `plans/handoff/latest.md`
> using the template, run `python tools/check_generality.py`, and commit on the task branch.

**When the chat feels long or confused**

> Stop. Write the current state into `plans/handoff/latest.md` and commit. I'll start a new chat.

## 3. Keeping context small

- One chat = one task. Start a new chat for the next task.
- Big searches and reviews go to a sub-agent, which returns only the conclusion.
- Read one section file instead of a whole folder.
- Refer to items by ID (`REQ-12`, `ADR-21`) instead of pasting their text.
- If Claude starts repeating itself, forgetting rules or mixing up details, write the handoff and
  start fresh. Don't argue with a tired context.

## 4. Git

- `main` is always working. No direct commits to `main` except the context library itself.
- One branch per task: `t-18-requirement-agent`.
- Parallel work: each owner uses their own git worktree (`superpowers:using-git-worktrees`), so
  sessions never touch each other's files.
- Merge through a pull request, reviewed by another owner. The pre-commit hook runs the
  generality check.
- Commit messages say the general problem fixed, not the test document: "Critic now asks about
  error paths in multi-step approvals", not "fix b1-02".

## 5. Testing agents: the 3-batch method

Full method in `eval/README.md`. In short:

1. Build the agent. Run it on **batch-1** (4 documents × 3 runs). Fix the general causes.
2. Run on **batch-2** (4 new documents × 3 runs). Shows whether the fixes were general. Fix again.
3. Run once on the **hold-out** (4 unseen documents × 3 runs). Pass = done.
   Fail = back to step 2 with fresh documents; the hold-out documents that were looked at move to
   batch-2 and new hold-out documents are written.

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
