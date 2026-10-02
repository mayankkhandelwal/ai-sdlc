# E-10 · BA agent and screen list

- **Owner:** Agents
- **Accepted by:** Product owner (never only the person who built it)

## Tasks

| Task | Title | Role | Owner | Depends on |
|---|---|---|---|---|
| [T-10.1](../tasks/T-10.1-design.md) | Design | Builder | Agents | T-07.2 |
| [T-10.2](../tasks/T-10.2-build-v1-and-baseline.md) | Build v1 and baseline | Builder | Agents | T-10.1, T-01.4 |
| [T-10.3](../tasks/T-10.3-batch-1-test-and-fixes.md) | Batch-1 test and fixes | Builder | Agents | T-10.2 |
| [T-10.4](../tasks/T-10.4-batch-2-test-fixes-and-regression.md) | Batch-2 test, fixes and regression | Builder | Agents | T-10.3 |
| [T-10.5](../tasks/T-10.5-hold-out-run.md) | Hold-out run | Builder | Agents | T-10.4 |
| [T-10.6](../tasks/T-10.6-audit.md) | Audit | Auditor | another owner | T-10.5 |
| [T-10.7](../tasks/T-10.7-accept.md) | Accept | Human | Product owner | T-10.6 |

## Accepted

_Name and date when accepted._
