# E-13 · Stitch adapter and screen checker

- **Owner:** Platform
- **Accepted by:** Agents owner (never only the person who built it)

## Tasks

| Task | Title | Role | Owner | Depends on |
|---|---|---|---|---|
| [T-13.1](../tasks/T-13.1-design.md) | Design | Builder | Platform | T-02.8, T-12.2 |
| [T-13.2](../tasks/T-13.2-stitch-adapter.md) | Stitch adapter | Builder | Platform | T-13.1 |
| [T-13.3](../tasks/T-13.3-screen-facts-parser.md) | Screen facts parser | Builder | Platform | T-13.2 |
| [T-13.4](../tasks/T-13.4-screen-checker-and-look-rubric.md) | Screen checker and look rubric | Builder | Agents | T-13.3 |
| [T-13.5](../tasks/T-13.5-failure-tests.md) | Failure tests | Builder | Platform | T-13.4 |
| [T-13.6](../tasks/T-13.6-audit.md) | Audit | Auditor | another owner | T-13.5 |
| [T-13.7](../tasks/T-13.7-accept.md) | Accept | Human | Agents owner | T-13.6, T-12.7 |

## Accepted

_Name and date when accepted._
