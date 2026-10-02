# E-07 · Requirement agent

- **Owner:** Agents
- **Accepted by:** Project lead (never only the person who built it)

## Tasks

| Task | Title | Role | Owner | Depends on |
|---|---|---|---|---|
| [T-07.1](../tasks/T-07.1-design.md) | Design | Builder | Agents | T-05.7, T-06.5 |
| [T-07.2](../tasks/T-07.2-build-v1-and-baseline.md) | Build v1 and baseline | Builder | Agents | T-07.1, T-01.4 |
| [T-07.3](../tasks/T-07.3-batch-1-test-and-fixes.md) | Batch-1 test and fixes | Builder | Agents | T-07.2 |
| [T-07.4](../tasks/T-07.4-batch-2-test-fixes-and-regression.md) | Batch-2 test, fixes and regression | Builder | Agents | T-07.3 |
| [T-07.5](../tasks/T-07.5-hold-out-run.md) | Hold-out run | Builder | Agents | T-07.4 |
| [T-07.6](../tasks/T-07.6-audit.md) | Audit | Auditor | another owner | T-07.5 |
| [T-07.7](../tasks/T-07.7-accept.md) | Accept | Human | Project lead | T-07.6 |

## Accepted

_Name and date when accepted._
