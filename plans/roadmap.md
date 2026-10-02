# Roadmap

All tasks. One chat = one task. Status: todo / doing / done / blocked.
Phases run in order; tasks inside a phase can run in parallel when their dependencies are done.

| ID | Task | Phase | Owner | Depends on | Status |
|---|---|---|---|---|---|
| T-00 | [Set up the context library](tasks/T-00-set-up-the-context-library.md) | 0 Setup | Platform | — | done |
| T-01 | [Review test documents and add real ones](tasks/T-01-review-test-documents-and-add-real-ones.md) | 0 Setup | Human (all) | T-00 | todo |
| T-02 | [Spike: Stitch from a TypeScript script](tasks/T-02-spike-stitch-from-a-typescript-script.md) | 1 Spikes | Platform | T-00 | todo |
| T-03 | [Spike: guard hook identity and fail-closed](tasks/T-03-spike-guard-hook-identity-and-fail-closed.md) | 1 Spikes | Platform | T-00 | todo |
| T-04 | [Spike: Figma write tool (starts the Figma gate)](tasks/T-04-spike-figma-write-tool-starts-the-figma-gate.md) | 1 Spikes | Product | T-00 | todo |
| T-05 | [Spike: plugin skeleton behaviour](tasks/T-05-spike-plugin-skeleton-behaviour.md) | 1 Spikes | Platform | T-00 | todo |
| T-06 | [Spike: quote matching on real PDFs](tasks/T-06-spike-quote-matching-on-real-pdfs.md) | 1 Spikes | Agents | T-00 | todo |
| T-07 | [Spike: Langfuse and usage numbers](tasks/T-07-spike-langfuse-and-usage-numbers.md) | 1 Spikes | Platform | T-00 | todo |
| T-08 | [Spike: model bake-off](tasks/T-08-spike-model-bake-off.md) | 1 Spikes | Agents | T-00 | todo |
| T-09 | [Freeze contracts](tasks/T-09-freeze-contracts.md) | 1 Spikes | All | T-02, T-03, T-04, T-05 | todo |
| T-10 | [Plugin skeleton and commands](tasks/T-10-plugin-skeleton-and-commands.md) | 2 Foundations | Platform | T-09 | todo |
| T-11 | [State script mvp-state](tasks/T-11-state-script-mvp-state.md) | 2 Foundations | Platform | T-09 | todo |
| T-12 | [Hooks: guard, validate, trace, resume](tasks/T-12-hooks-guard-validate-trace-resume.md) | 2 Foundations | Platform | T-03, T-09 | todo |
| T-13 | [Rules checks and schemas](tasks/T-13-rules-checks-and-schemas.md) | 2 Foundations | Platform | T-09 | todo |
| T-14 | [AI checker and gating rubrics](tasks/T-14-ai-checker-and-gating-rubrics.md) | 2 Foundations | Agents | T-09 | todo |
| T-15 | [Document reader](tasks/T-15-document-reader.md) | 2 Foundations | Platform | T-06, T-09 | todo |
| T-16 | [Evaluation runner and scorer](tasks/T-16-evaluation-runner-and-scorer.md) | 2 Foundations | Agents | T-09 | todo |
| T-17 | [Walking skeleton (thin end-to-end)](tasks/T-17-walking-skeleton-thin-end-to-end.md) | 3 Skeleton | All | T-10, T-11, T-13, T-15 | todo |
| T-18 | [Requirement agent (full)](tasks/T-18-requirement-agent-full.md) | 4 Understand | Agents | T-14, T-17 | todo |
| T-19 | [Critic agent and gap-value rubric](tasks/T-19-critic-agent-and-gap-value-rubric.md) | 4 Understand | Agents | T-18 | todo |
| T-20 | [Question system](tasks/T-20-question-system.md) | 4 Understand | Product | T-18, T-19 | todo |
| T-21 | [Answer map](tasks/T-21-answer-map.md) | 4 Understand | Agents + Product | T-20 | todo |
| T-22 | [BA agent and screen list](tasks/T-22-ba-agent-and-screen-list.md) | 4 Understand | Agents | T-18 | todo |
| T-23 | [Review page and approvals](tasks/T-23-review-page-and-approvals.md) | 4 Understand | Product | T-22 | todo |
| T-24 | [Design skill and Design Prompt agent](tasks/T-24-design-skill-and-design-prompt-agent.md) | 5 Design | Agents | T-22 | todo |
| T-25 | [Stitch adapter (full)](tasks/T-25-stitch-adapter-full.md) | 5 Design | Platform | T-02, T-24 | todo |
| T-26 | [Screen facts and screen checker](tasks/T-26-screen-facts-and-screen-checker.md) | 5 Design | Platform + Agents | T-25 | todo |
| T-27 | [Samples, feedback and decisions log](tasks/T-27-samples-feedback-and-decisions-log.md) | 5 Design | Agents + Product | T-26 | todo |
| T-28 | [Figma gate decision](tasks/T-28-figma-gate-decision.md) | 5 Design | Product | T-04, T-24 | todo |
| T-29 | [Figma frame builder and compiler](tasks/T-29-figma-frame-builder-and-compiler.md) | 5 Design | Product | T-28 | todo |
| T-30 | [Full UI build](tasks/T-30-full-ui-build.md) | 6 Full flow | Platform + Agents | T-27 | todo |
| T-31 | [Final approval, package and team library](tasks/T-31-final-approval-package-and-team-library.md) | 6 Full flow | Product | T-30 | todo |
| T-32 | [Project commands](tasks/T-32-project-commands.md) | 6 Full flow | Platform | T-11 | todo |
| T-33 | [Full evaluation](tasks/T-33-full-evaluation.md) | 7 Evaluate | Agents | T-31 | todo |
| T-34 | [Failure and red-team tests](tasks/T-34-failure-and-red-team-tests.md) | 7 Evaluate | Platform | T-31 | todo |
| T-35 | [Pilot with real users](tasks/T-35-pilot-with-real-users.md) | 7 Evaluate | All | T-33, T-34 | todo |

Agent tasks (T-14, T-18, T-19, T-22, T-24, T-29) are done only after the 3-batch test in `eval/README.md`.
