# AI-SDLC · Design-First MVP

A multi-agent **Claude Code plugin** (v1) that turns **one project document** into an approved
requirement, user stories, a screen list and a full UI design in **Google Stitch or Figma**.
v1 is for internal testing on the team's own Claude subscription with non-confidential documents.
v2 becomes a SaaS product on API keys. Team: 3 engineers, owners of **Agents**, **Platform**, **Product**.

## Hard rules (always follow; full text and reasons in `docs/rules.md`)

1. **Build for any project.** Agents, skills and prompts must work for ANY project document.
   Never put anything specific to a test document into agent, skill or prompt files.
   Fix the general cause, never the single case. `python tools/check_generality.py` must pass.
2. **Never read the hold-out set.** It lives outside this repo (folder given by `HOLDOUT_DIR`); only
   `python tools/eval_score.py` reads it, and only summary scores are shown. Never tune on it.
3. **Code for exact work, AI for judgment.** Rules checks run before AI checks.
4. **One chat = one task.** Start from `plans/handoff/latest.md` and one task file. End by updating
   the handoff and `plans/roadmap.md`, then commit.
5. **If it isn't in the repo, it doesn't exist.** Decisions go in `docs/adr/`; changes go in `docs/`.
6. **The architecture is the master.** `docs/architecture/` wins over every other page or chat.
   Changing it needs an ADR.
7. **Check facts before deciding.** Platform behaviour is proven by a small spike first.
8. **Say when an idea is wrong.** Give the reason and a better option; the user decides.
9. **Safety in code.** Every agent has an explicit tool list. No keys in files, chat or logs.
10. **An agent is done only after the 3-batch test** (`eval/README.md`).
11. **Read only what the task file lists.** Prefer one section file over a whole folder.

## Map

| Need | Read |
|---|---|
| Where we stopped, what's next | `plans/handoff/latest.md` |
| The whole plan: why, phases, testing, live projects | `docs/plan.md` |
| What's ready, doing, in review | `python tools/board.py` |
| Epics and status | `plans/roadmap.md`, `plans/epics/E-xx-*.md` |
| One task: sub-tasks, done-when, proof | `plans/tasks/T-xx.y-*.md` |
| New work waiting to be sorted | `plans/inbox.md` |
| Audits | `plans/audits/` (procedure in `README.md`) |
| General failure types found so far | `plans/failure-catalog.md` |
| How we work with Claude (cycle, skills, git) | `docs/process/how-we-work-with-claude.md` |
| Rules in full | `docs/rules.md` |
| Architecture (master), split in parts | `docs/architecture/00-…06-*.md` |
| What we build, in flow form | `docs/mvp-flow.md` |
| Decisions | `docs/adr/` |
| File formats and interfaces | `docs/contracts/` |
| Test documents and method | `eval/README.md` (batch-1, batch-2, batch-3; the hold-out is outside the repo) |
| Expert audits of the design | `docs/audits/` |
| Original HTML pages (reference only) | `docs/reference/` |

## Roles

Every chat has one role (full method in `docs/process/how-we-work-with-claude.md`):
- **Lead:** plans, sorts the inbox, picks ready tasks. Never writes product code.
- **Builder:** does one task and records proof.
- **Auditor:** fresh context; checks done-when against proof; never fixes.
- **Human:** reviews answer keys, approves plans, accepts epics, decides disagreements.

Epic → task → sub-task. Agent epics use 7 tasks: design, build v1 + baseline, batch-1, batch-2 + regression,
hold-out, audit, accept. An epic is accepted by someone who did not build it.

## Many chats at once

Several chats may run in parallel, one task each. Each task chat works in **its own git worktree**
(a sibling folder such as `../AI_SDLC-t-02-2`) on its own branch, and writes only:
its task file, its own handoff `plans/handoff/T-xx.y.md`, and the files the task produces.
**Only the Lead** edits `plans/handoff/latest.md` and `plans/roadmap.md`, and merges branches after
their audit passes.

## Starting a chat

Read `plans/handoff/latest.md`, the task file, and `plans/handoff/T-xx.y.md` if it exists, then only the
files the task lists. Say your role and task before doing anything. Set the task's status to `doing`.

## Ending a chat

1. Fill the task's **Proof** section; tick sub-tasks; set status `review` (or `done` for Human tasks).
2. Write `plans/handoff/T-xx.y.md` from `plans/templates/handoff.md` (done / decided / next / problems).
3. Run `python tools/check_generality.py` and `python tools/board.py`.
4. Commit on the task's branch. Then an Auditor chat audits it, and the Lead merges it.

## Commands

- `python tools/check_generality.py` — blocks test-document terms in agent, skill and prompt files
- `python tools/board.py [E-xx]` — ready, doing, review, blocked and warnings
- `python -m unittest discover -s tools/tests` — tests for the plan and safety tools
- `tools/guard_holdout.py` runs automatically as a project hook on every tool call (rule R2)
- Git hooks live in `.githooks/` (`git config core.hooksPath .githooks` is set)
