# Docs

| Folder / file | What it is |
|---|---|
| `architecture/` | **Master** architecture (revision 2), one file per part. Wins over everything else (rule R6) |
| `mvp-flow.md` | The same design as a step-by-step flow, for reading and learning |
| `adr/` | One file per decision; `README.md` is the index |
| `contracts/` | File formats and interfaces (frozen in T-09) |
| `spikes/` | Results of small platform tests |
| `process/how-we-work-with-claude.md` | The working cycle, prompts, git, testing method |
| `rules.md` | The fixed rules with reasons and enforcement |
| `audits/` | The two expert audits |
| `reference/` | The original HTML pages (for viewing only; the Markdown files are the source of truth) |

The architecture parts:

| File | Part |
|---|---|
| `architecture/00-revision-2.md` | What changed in revision 2 |
| `architecture/01-high-level-flow.md` | Scope, goals, quality scenarios, constraints, context, trust, high-level flow |
| `architecture/02-low-level-flow.md` | IDs and files, state machine, every step, failures, records, commands, team library |
| `architecture/03-system-diagram.md` | Containers, components, trust boundaries, permissions, data, contracts, deployment |
| `architecture/04-agent-runtime.md` | Agent anatomy, context, one run, checks, failure routing, models, agent cards, hooks, traces |
| `architecture/05-parts-and-concepts.md` | Learning cards for 14 parts, learning path |
| `architecture/06-decisions-and-risks.md` | ADRs, quality targets, threats, evaluation, cost, versioning, v2 path, risks, glossary, week-1 tests |
