# AI-SDLC · Design-First MVP

A multi-agent **Claude Code plugin** (v1) that turns **one project document** into an approved
requirement, user stories, a screen list and a full UI design in **Google Stitch or Figma**.
v1 is for internal testing on the team's own Claude subscription with non-confidential documents.
v2 becomes a SaaS product on API keys. Team: 3 engineers, owners of **Agents**, **Platform**, **Product**.

## Hard rules (always follow; full text and reasons in `docs/rules.md`)

1. **Build for any project.** Agents, skills and prompts must work for ANY project document.
   Never put anything specific to a test document into agent, skill or prompt files.
   Fix the general cause, never the single case. `python tools/check_generality.py` must pass.
2. **Never read `eval/holdout/`.** Only the scoring script may open it. Never tune on it.
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
| All tasks and status | `plans/roadmap.md` |
| One task's goal, inputs, done-when | `plans/tasks/T-xx-*.md` |
| How we work with Claude (cycle, skills, git) | `docs/process/how-we-work-with-claude.md` |
| Rules in full | `docs/rules.md` |
| Architecture (master), split in parts | `docs/architecture/00-…06-*.md` |
| What we build, in flow form | `docs/mvp-flow.md` |
| Decisions | `docs/adr/` |
| File formats and interfaces | `docs/contracts/` |
| Test documents and method | `eval/README.md` (never `eval/holdout/`) |
| Audits | `docs/audits/` |
| Original HTML pages (reference only) | `docs/reference/` |

## Starting a chat

Read `plans/handoff/latest.md`, then the task file named there, then only the files the task lists.
Say which task you are on before doing anything.

## Ending a chat

1. Update the task's status in `plans/roadmap.md`.
2. Rewrite `plans/handoff/latest.md` (done / decided / next / problems).
3. Run `python tools/check_generality.py`.
4. Commit on the task's branch.

## Commands

- `python tools/check_generality.py` — blocks test-document terms in agent, skill and prompt files
- Git hooks live in `.githooks/` (`git config core.hooksPath .githooks` is set)
