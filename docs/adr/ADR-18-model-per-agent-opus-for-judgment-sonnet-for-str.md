# ADR-18 · Model per agent: Opus for judgment, Sonnet for structured work, Haiku for sorting; escalation by reasoning effort

- **Status:** Accepted
- **Source:** `docs/architecture/06-decisions-and-risks.md` (6.1); audits in `docs/audits/`

## Decision

Model per agent: Opus for judgment, Sonnet for structured work, Haiku for sorting; escalation by reasoning effort

## Rejected options

One model for all; escalate to a different model

## Consequences

Confirmed or changed by the week-1 bake-off

## Notes

- 2026-10-03, T-02.7 bake-off (`docs/spikes/T-02.7-models.md`, 18 runs on 2 batch-1 documents): **confirmed
  with notes.** Opus is confirmed for requirement-agent and critic-agent (best coverage, every quote exact, every
  planted contradiction, most key gaps). Sonnet held every hard rule and was the fastest, but it covered less;
  it is kept for structured work, still to be proven per agent. Haiku broke the word-for-word quote rule and missed a
  planted contradiction, and it was not faster: use it only for short, closed sorting questions with a code
  check after it, never for extraction or judgment. Wording change to 4.6 goes through T-02.8.
