# Names

One naming rule for everything, so nothing gets lost or mixed up. `EE` = epic number, `N` = task number
(task `T-02.2` → `EE` = 02, `N` = 2). Folder locations come from `tools/paths.json`.

We run **one task at a time**, so every chat opens in the main project folder. There are no task
worktree folders (if we ever run tasks in parallel again, that needs an ADR first).

## Folders

| What | Name and place |
|---|---|
| Main project: every chat opens here | `D:/AI-Job/AI_SDLC/` |
| Work folder for this project's extras | `D:/AI_SDLC_work/` (outside `D:/AI-Job`) |
| Hold-out set (no project chat opens it) | `D:/AI_SDLC_work/AI_SDLC_holdout/` |

Nothing for this project is created inside `D:/AI-Job/` except the main project folder, and nothing
extra is created inside the main project folder.

## Git

| What | Name | Example |
|---|---|---|
| Task branch | `t-EE-N-<short-name>` (the name in the task file) | `t-02-2-spike-guard-hook` |
| Create it (Builder, at start) | `git switch main` then `git switch -c t-EE-N-<short-name>` | — |
| Merge it (Lead, after PASS) | `git switch main` then `git merge --no-ff t-EE-N-<short-name>` | — |
| Commit message | What changed, in general words; never a test document or client name | "Critic now asks about error paths in multi-step approvals" |

## Files

| What | Name | Example |
|---|---|---|
| Task | `plans/tasks/T-EE.N-<slug>.md` | `plans/tasks/T-02.2-spike-guard-hook-identity-and-fail-closed.md` |
| Epic | `plans/epics/E-EE-<slug>.md` | `plans/epics/E-02-week-1-spikes.md` |
| Task handoff | `plans/handoff/T-EE.N.md` | `plans/handoff/T-02.2.md` |
| Overall handoff (Lead only) | `plans/handoff/latest.md` | — |
| Passed audit | `plans/audits/T-EE.N.md` | `plans/audits/T-02.2.md` |
| Failed audit (kept) | `plans/audits/T-EE.N-audit-K-fail.md` | `plans/audits/T-02.2-audit-1-fail.md` |
| Spike result | `docs/spikes/T-EE.N-<topic>.md` | `docs/spikes/T-02.2-guard.md` |
| Live test report | `docs/live-tests/L<n>.md` | `docs/live-tests/L1.md` |
| Decision record | `docs/adr/ADR-NN-<slug>.md` | `docs/adr/ADR-28-…md` |
| Evaluation results | `eval/results/<agent>/<YYYY-MM-DD>/` | `eval/results/requirement-agent/2026-11-02/` |

## Chats

**Opening any chat in the Claude app:** folder `D:/AI-Job/AI_SDLC`, the app's **worktree** box
**unticked** (ticking it makes the app create a copy inside the project; `.claude/worktrees/` is in
`.gitignore` as a safety net). Name the chat as soon as it opens.

| Chat | Name | When |
|---|---|---|
| Lead | `Lead` | Always open; says the next task, merges after PASS |
| Builder for a task | `T-EE.N Builder` | New chat for each task |
| Auditor for a task | `T-EE.N Auditor` | New chat after the Builder finishes |
| Fix after a failed audit | `T-EE.N Builder fix K` | New chat after audit K fails |
| Hold-out writer | `Hold-out writer` | Opened in the hold-out folder, never the project |

Close (archive) the Builder and Auditor chats once the Lead has merged the task.
