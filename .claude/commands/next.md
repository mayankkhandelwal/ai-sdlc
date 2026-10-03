---
description: Do the next ready task from start to merge (build, independent audit, merge, handoff)
argument-hint: "[task ID like T-02.2, or an area: agents | platform | product]"
---

You run ONE task from start to finish in this chat. Argument: `$ARGUMENTS` (empty = first ready task).
Keep the user's simple English. Show short status lines, not long reports.

## 1. Pick the task

1. Run `git status`. If there are uncommitted changes or the current branch is not `main`, stop and tell
   the user what you found. Otherwise run `git pull --ff-only` (if a remote exists).
2. Run `python tools/board.py`. Pick the task:
   - argument is a task ID → that task (stop if it is not ready);
   - argument is an area → the first ready task whose owner matches that area;
   - empty → the first ready task with role **Builder** or **Auditor** that needs nothing from a person;
     if none, the first one whose need `plans/handoff/latest.md` marks as ready; if none, ask the user
     which need is ready.
3. If the only ready tasks are **Human** tasks, list them with what the person must do (from each task
   file's "Needs from a person" and sub-tasks) and stop.

## 2. Start

1. Read `plans/handoff/latest.md`, the task file, and `plans/handoff/T-xx.y.md` if it exists. Then read
   **only** the files the task lists (rule R11).
2. Say in 3 lines: your role, the task, its goal and done-when.
3. Create the branch named in the task file: `git switch -c <branch>`. Set the task's status to `doing`.
4. Show a short plan (steps, files, tests). If the task needs something from a person that is missing,
   say exactly what and stop. Otherwise **wait for the user to say "go"**.

## 3. Build

Follow `docs/process/how-we-work-with-claude.md` section 1 (test first, smallest change, verify).
Never put anything specific to a test document into agent, skill or prompt files (rule R1).
Never open the hold-out folder (rule R2).

When finished: fill the task's **Proof**, tick sub-tasks, set status `review`, write
`plans/handoff/T-xx.y.md` from `plans/templates/handoff.md`, run `python tools/check_generality.py`
and the tests, and commit on the branch.

For an **Auditor** task (an epic's audit): skip building; go straight to step 4 and audit the whole epic.

## 4. Independent audit (a sub-agent, fresh context)

Start a **general-purpose sub-agent** in the foreground with this prompt (fill in the ID and file):

> You are the Auditor for T-xx.y. You did not build it. Read `plans/audits/README.md` and
> `plans/tasks/<task file>`. Check every done-when item against the proof, rerun the task's tests and
> `python tools/check_generality.py`, and write `plans/audits/T-xx.y.md` with PASS or FAIL using the
> template. Don't fix anything. Don't commit. Reply with PASS or FAIL and the missing items.

- **FAIL:** rename its file to `plans/audits/T-xx.y-audit-K-fail.md`, fix the missing items, commit, and
  audit again with a new sub-agent. After 3 failed audits, stop and ask the user.
- **PASS:** commit the audit file on the branch.

## 5. Merge and hand off (the Lead's job, done here)

1. `git switch main`, `git merge --no-ff <branch>`, `git branch -d <branch>`.
2. Set the task's status to `done`. Update its epic's count and status in `plans/roadmap.md`.
3. Update `plans/handoff/latest.md`: last task, what was done or decided, the next ready task.
4. Add any new work you found to `plans/inbox.md` (never build it now).
5. Run `python tools/board.py`, commit on `main`.
6. **Ask the user before `git push`.**
7. Tell the user in 3 lines: what was done, what's next, and "open a new chat and type `/next`".
