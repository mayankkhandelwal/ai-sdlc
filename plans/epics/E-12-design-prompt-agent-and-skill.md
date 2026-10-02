# E-12 · Design Prompt agent and skill

- **Owner:** Agents
- **Accepted by:** Product owner (never only the person who built it)

## Tasks

| Task | Title | Role | Owner | Depends on |
|---|---|---|---|---|
| [T-12.1](../tasks/T-12.1-design.md) | Design | Builder | Agents | T-10.7 |
| [T-12.2](../tasks/T-12.2-build-v1-and-baseline.md) | Build v1 and baseline | Builder | Agents | T-12.1, T-01.4 |
| [T-12.3](../tasks/T-12.3-batch-1-test-and-fixes.md) | Batch-1 test and fixes | Builder | Agents | T-12.2 |
| [T-12.4](../tasks/T-12.4-batch-2-test-fixes-and-regression.md) | Batch-2 test, fixes and regression | Builder | Agents | T-12.3 |
| [T-12.5](../tasks/T-12.5-hold-out-run.md) | Hold-out run | Builder | Agents | T-12.4 |
| [T-12.6](../tasks/T-12.6-audit.md) | Audit | Auditor | another owner | T-12.5 |
| [T-12.7](../tasks/T-12.7-accept.md) | Accept | Human | Product owner | T-12.6 |

## Accepted

_Name and date when accepted._
