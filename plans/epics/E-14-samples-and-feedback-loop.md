# E-14 · Samples and feedback loop

- **Owner:** Agents
- **Accepted by:** Project lead (never only the person who built it)

## Tasks

| Task | Title | Role | Owner | Depends on |
|---|---|---|---|---|
| [T-14.1](../tasks/T-14.1-design.md) | Design | Builder | Agents | T-13.7 |
| [T-14.2](../tasks/T-14.2-build-v1-and-baseline.md) | Build v1 and baseline | Builder | Agents | T-14.1, T-01.4 |
| [T-14.3](../tasks/T-14.3-batch-1-test-and-fixes.md) | Batch-1 test and fixes | Builder | Agents | T-14.2 |
| [T-14.4](../tasks/T-14.4-batch-2-test-fixes-and-regression.md) | Batch-2 test, fixes and regression | Builder | Agents | T-14.3 |
| [T-14.5](../tasks/T-14.5-hold-out-run.md) | Hold-out run | Builder | Agents | T-14.4 |
| [T-14.6](../tasks/T-14.6-audit.md) | Audit | Auditor | another owner | T-14.5 |
| [T-14.7](../tasks/T-14.7-accept.md) | Accept | Human | Project lead | T-14.6 |

## Accepted

_Name and date when accepted._
