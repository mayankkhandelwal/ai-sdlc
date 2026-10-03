# Roadmap

Epic -> task -> sub-task. One chat = one task. Run `python tools/board.py` to see what is ready.
Status values: todo, doing, review, done, blocked, needs-human, skipped (skipped needs an ADR, e.g. Figma moved to v1.1).

| Epic | Title | Owner | Accepts | Tasks | Status |
|---|---|---|---|---|---|
| E-01 | [Setup](epics/E-01-setup.md) | Project lead | Project lead | 2/5 | doing |
| E-02 | [Week-1 spikes](epics/E-02-week-1-spikes.md) | Platform | Project lead | 4/8 | doing |
| E-03 | [Contracts](epics/E-03-contracts.md) | All owners | Project lead | 0/4 | todo |
| E-04 | [Platform foundations](epics/E-04-platform-foundations.md) | Platform | Platform owner (not the builder) or project lead | 0/9 | todo |
| E-05 | [AI checker and gating rubrics](epics/E-05-ai-checker-and-gating-rubrics.md) | Agents | Platform owner | 0/7 | todo |
| E-06 | [Walking skeleton](epics/E-06-walking-skeleton.md) | All owners | Project lead | 0/5 | todo |
| E-07 | [Requirement agent](epics/E-07-requirement-agent.md) | Agents | Project lead | 0/7 | todo |
| E-08 | [Critic agent](epics/E-08-critic-agent.md) | Agents | Project lead | 0/7 | todo |
| E-09 | [Question system and answer map](epics/E-09-question-system-and-answer-map.md) | Product | Agents owner | 0/7 | todo |
| E-10 | [BA agent and screen list](epics/E-10-ba-agent-and-screen-list.md) | Agents | Product owner | 0/7 | todo |
| E-11 | [Review page and approvals](epics/E-11-review-page-and-approvals.md) | Product | Platform owner | 0/6 | todo |
| E-12 | [Design Prompt agent and skill](epics/E-12-design-prompt-agent-and-skill.md) | Agents | Product owner | 0/7 | todo |
| E-13 | [Stitch adapter and screen checker](epics/E-13-stitch-adapter-and-screen-checker.md) | Platform | Agents owner | 0/7 | todo |
| E-14 | [Samples and feedback loop](epics/E-14-samples-and-feedback-loop.md) | Agents | Project lead | 0/7 | todo |
| E-15 | [Figma gate and Figma path](epics/E-15-figma-gate-and-figma-path.md) | Product | Project lead | 0/7 | todo |
| E-16 | [Full UI, package and commands](epics/E-16-full-ui-package-and-commands.md) | Platform | Project lead | 0/7 | todo |
| E-17 | [Evaluation and pilot](epics/E-17-evaluation-and-pilot.md) | Agents | Project lead | 0/5 | todo |
| E-18 | [Live project tests](epics/E-18-live-project-tests.md) | All owners | Project lead | 0/7 | todo |

Live project tests (E-18) run after phases 4–7; see `docs/plan.md`.

Agent epics (E-05, E-07, E-08, E-10, E-12, E-14) use the standard 7-task shape: design, build v1 and baseline, batch-1, batch-2 with regression, hold-out, audit, accept.
