# E-15 · Figma gate and Figma path

- **Owner:** Product
- **Accepted by:** Project lead (never only the person who built it)

## Tasks

| Task | Title | Role | Owner | Depends on |
|---|---|---|---|---|
| [T-15.1](../tasks/T-15.1-run-the-figma-gate.md) | Run the Figma gate | Builder | Product | T-02.3, T-12.2 |
| [T-15.2](../tasks/T-15.2-gate-decision.md) | Gate decision | Human | Project lead | T-15.1 |
| [T-15.3](../tasks/T-15.3-layout-compiler.md) | Layout compiler | Builder | Product | T-15.2 |
| [T-15.4](../tasks/T-15.4-frame-builder-agent.md) | Frame builder agent | Builder | Product | T-15.3 |
| [T-15.5](../tasks/T-15.5-design-subset-batch-tests.md) | Design-subset batch tests | Builder | Product | T-15.4 |
| [T-15.6](../tasks/T-15.6-audit.md) | Audit | Auditor | another owner | T-15.5 |
| [T-15.7](../tasks/T-15.7-accept.md) | Accept | Human | Project lead | T-15.6 |

## Accepted

_Name and date when accepted._
