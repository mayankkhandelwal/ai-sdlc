# E-05 · AI checker and gating rubrics

- **Owner:** Agents
- **Accepted by:** Platform owner (never only the person who built it)

## Tasks

| Task | Title | Role | Owner | Depends on |
|---|---|---|---|---|
| [T-05.1](../tasks/T-05.1-design.md) | Design | Builder | Agents | T-04.9 |
| [T-05.2](../tasks/T-05.2-build-v1-and-baseline.md) | Build v1 and baseline | Builder | Agents | T-05.1, T-01.4 |
| [T-05.3](../tasks/T-05.3-batch-1-test-and-fixes.md) | Batch-1 test and fixes | Builder | Agents | T-05.2 |
| [T-05.4](../tasks/T-05.4-batch-2-test-fixes-and-regression.md) | Batch-2 test, fixes and regression | Builder | Agents | T-05.3 |
| [T-05.5](../tasks/T-05.5-hold-out-run.md) | Hold-out run | Builder | Agents | T-05.4 |
| [T-05.6](../tasks/T-05.6-audit.md) | Audit | Auditor | another owner | T-05.5 |
| [T-05.7](../tasks/T-05.7-accept.md) | Accept | Human | Platform owner | T-05.6 |

## Accepted

_Name and date when accepted._
