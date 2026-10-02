# Architecture decision records

One file per decision. New decisions use `TEMPLATE.md`. Changing the architecture needs an ADR in the same commit (rule R6).

| ID | Decision | Status |
|---|---|---|
| [ADR-01](ADR-01-v1-is-a-claude-code-plugin-on-the-team-s-own-sub.md) | v1 is a Claude Code plugin on the team's own subscription | Accepted |
| [ADR-02](ADR-02-orchestrator-command-state-script-in-code-contro.md) | Orchestrator command + state script in code control the steps | Accepted |
| [ADR-03](ADR-03-every-output-checked-by-rules-first-then-ai.md) | Every output checked by rules first, then AI | Accepted |
| [ADR-04](ADR-04-a-python-script-reads-documents-ai-only-checks-a.md) | A Python script reads documents; AI only checks and describes images | Accepted |
| [ADR-05](ADR-05-every-requirement-quotes-its-source-word-for-wor.md) | Every requirement quotes its source word for word | Accepted |
| [ADR-06](ADR-06-a-separate-critic-agent-finds-gaps.md) | A separate critic agent finds gaps | Accepted |
| [ADR-07](ADR-07-questions-in-batches-as-many-as-needed-in-html-m.md) | Questions in batches, as many as needed, in HTML + Markdown files | Accepted |
| [ADR-08](ADR-08-screen-list-approved-together-with-requirement-a.md) | Screen list approved together with requirement and stories | Accepted |
| [ADR-09](ADR-09-one-style-message-one-message-per-screen.md) | One style message + one message per screen | Accepted |
| [ADR-10](ADR-10-both-stitch-and-figma-behind-one-adapter-interfa.md) | Both Stitch and Figma behind one adapter interface | Accepted |
| [ADR-11](ADR-11-one-typescript-script-calls-stitch-through-googl.md) | One TypeScript script calls Stitch through Google's official SDK; it reads the key from the OS keychain itself | Accepted |
| [ADR-12](ADR-12-figma-frames-built-from-a-script-compiled-layout.md) | Figma frames built from a script-compiled layout file, carried by an agent limited to Figma's write tool and one file; gated by a test (ADR-23) | Accepted |
| [ADR-13](ADR-13-screen-fields-checked-by-parsing-code-or-layers-.md) | Screen fields checked by parsing code or layers; vision only for look | Accepted |
| [ADR-14](ADR-14-feedback-goes-into-a-decisions-log-messages-are-.md) | Feedback goes into a decisions log; messages are rebuilt from it | Accepted |
| [ADR-15](ADR-15-langfuse-tracing-through-hooks-metadata-only-by-.md) | Langfuse tracing through hooks, metadata only by default | Accepted |
| [ADR-16](ADR-16-all-v1-scripts-in-python-except-the-stitch-scrip.md) | All v1 scripts in Python except the Stitch script (TypeScript) | Accepted |
| [ADR-17](ADR-17-new-apps-only-in-v1-existing-apps-in-v1-1-withou.md) | New apps only in v1; existing apps in v1.1 without building them | Accepted |
| [ADR-18](ADR-18-model-per-agent-opus-for-judgment-sonnet-for-str.md) | Model per agent: Opus for judgment, Sonnet for structured work, Haiku for sorting; escalation by reasoning effort | Accepted |
| [ADR-19](ADR-19-guard-hook-fails-closed-every-error-returns-deny.md) | Guard hook fails closed: every error returns "deny"; no agent can start agents | Accepted |
| [ADR-20](ADR-20-the-state-script-checks-its-own-conditions-befor.md) | The state script checks its own conditions before every move; the orchestrator rebuilds its view from the state each run | Accepted |
| [ADR-21](ADR-21-quotes-matched-on-normalised-text-with-positions.md) | Quotes matched on normalised text, with positions; tables cited by cell; IDs stable across versions; "convention" items | Accepted |
| [ADR-22](ADR-22-failures-routed-by-type-format-missing-quote-vag.md) | Failures routed by type (format, missing quote, vague source, own wording, unstable judge, instructions problem) | Accepted |
| [ADR-23](ADR-23-figma-path-gated-by-a-1-2-week-test-with-pass-ma.md) | Figma path gated by a 1–2 week test with pass marks (6.10) | Accepted |
| [ADR-24](ADR-24-questions-as-many-as-needed-gap-importance-level.md) | Questions: as many as needed, gap importance levels, check-in every 4 batches, AI answer map confirmed by the user | Accepted |
| [ADR-25](ADR-25-crash-safety-job-ids-saved-before-waiting-safe-f.md) | Crash safety: job IDs saved before waiting, safe file writes, project lock, every file versioned | Accepted |
| [ADR-26](ADR-26-a-design-system-record-tokens-components-that-gr.md) | A design-system record (tokens + components) that grows; tolerance bands | Accepted |
| [ADR-27](ADR-27-additions-team-library-across-projects-accessibi.md) | Additions: team library across projects, accessibility rules, languages and right-to-left, platform asked early, sample data, confidence per item, version differences in review | Accepted |
