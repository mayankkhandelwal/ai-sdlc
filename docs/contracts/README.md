# Contracts

File formats and interfaces shared between the three owners. They are frozen in epic **E-03** (tasks T-03.1 to T-03.4),
after the week-1 spikes, and changed only through a pull request reviewed by all three owners.

| Contract | Defined in architecture | File to write in E-03 |
|---|---|---|
| Folder tree and write paths | 2.1 | `folder-tree.md` |
| State format (`state.json`, lock) | 2.2, 2.10 | `state.schema.json` |
| Every record (requirement, gaps, questions, answers, answer map, storyset, screen list, routing, brief, messages, layout, job, facts, tokens, components, issues, decisions, approvals, coverage) | 2.10 | `<record>.schema.json` |
| Agent result | 3.6 | `agent-result.schema.json` |
| State script commands | 3.6 | `mvp-state.md` |
| Rules check and AI check results | 3.6 | `check-result.schema.json` |
| Design adapter (`generate`, `edit`, `resume`) | 3.6 | `design-adapter.md` |
| Layout file (Figma) | 3.6, S2b | `layout.schema.json` |
| Question and feedback files | U7, D5 | `question-file.md` |
| Trace event | 3.6 | `trace-event.schema.json` |
