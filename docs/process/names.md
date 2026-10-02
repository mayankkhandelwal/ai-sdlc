# Names

One naming rule for everything, so nothing gets lost or mixed up. `EE` = epic number, `N` = task number
(task `T-02.2` → `EE` = 02, `N` = 2). Folder locations come from `tools/paths.json`.

## Folders

| What | Name and place | Example |
|---|---|---|
| Main project (main branch, Lead chat) | `D:/AI-Job/AI_SDLC/` | — |
| Work folder for this project's extras | `D:/AI_SDLC_work/` (outside `D:/AI-Job`) | — |
| One worktree per task | `D:/AI_SDLC_work/worktrees/t-EE-N/` | `D:/AI_SDLC_work/worktrees/t-02-2/` |
| Hold-out set (no chat opens it) | `D:/AI_SDLC_work/AI_SDLC_holdout/` | — |

Nothing for this project is created inside `D:/AI-Job/` except the main project folder, and nothing
extra is created inside the main project folder.

## Git

| What | Name | Example |
|---|---|---|
| Task branch | `t-EE-N-<short-name>` | `t-02-2-spike-guard-hook` |
| Create a task worktree | `git worktree add D:/AI_SDLC_work/worktrees/t-EE-N -b t-EE-N-<short-name> main` | see the start guide |
| Remove it after merge | `git worktree remove D:/AI_SDLC_work/worktrees/t-EE-N` | — |
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

Give every Claude chat a name when you open it, so you always know which window does what.

| Chat | Name | Opened in |
|---|---|---|
| Lead | `Lead` | `D:/AI-Job/AI_SDLC/` |
| Builder for a task | `T-EE.N Builder` | its worktree folder |
| Auditor for a task | `T-EE.N Auditor` | the same worktree folder, new session |
| Fix after a failed audit | `T-EE.N Builder fix K` | the same worktree folder, new session |
| Hold-out writer | `Hold-out writer` | the hold-out folder, never the project |

Example: three spike chats open at once are named `T-02.2 Builder`, `T-02.4 Builder`, `T-02.7 Builder`.
