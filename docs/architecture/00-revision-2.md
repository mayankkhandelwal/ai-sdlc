REVISION 2

## What changed in revision 2

All audit suggestions accepted. Each line names the sections that changed.

| # | Change | Where |
|---|---|---|
| A | Stitch is called by one **TypeScript** script using Google's official SDK; all other scripts stay Python. The script reads the Stitch key from the OS keychain itself | 1.4, 1.6, 2.7, 3.0–3.7, 5.8, ADR-11, ADR-16 |
| B | Questions: still as many as needed, with defined gap importance, a **check-in after every 4 batches**, and an AI step that maps answers to questions for the user to confirm | 2.4, 2.10, 4.4, 5.5, ADR-24 |
| C | Figma: a **gated test** with pass marks. The frame builder writes a layout file; a script compiles it into Figma code; reading back uses the write tool, which has no daily limit | 2.7, 3.2, 4.7, 5.8, 6.10, ADR-23 |
| 1 | Guard hook **fails closed** by design: any error returns "deny"; no agent has the tool to start other agents | 3.4, 3.6, 4.8, 5.12, 6.3, ADR-19 |
| 2 | The state script checks its own conditions before moving on; the orchestrator rebuilds its view from the state on every run | 2.2, 3.6, 4.3, 5.1, ADR-20 |
| 3 | Quotes matched after text normalisation; tables cited by cell; IDs kept stable across versions; "convention" items for standard features | 2.1, 2.3, 2.4, 2.10, 5.4, ADR-21 |
| 4 | Failures routed by type instead of "retry, then stronger model" | 2.9, 4.5, 4.6, ADR-22 |
| 5 | Crash safety: job and node IDs saved before waiting; safe file writes; project lock | 2.1, 2.7, 2.9, ADR-25 |
| 6 | Full folder tree, complete record list, every file versioned | 2.1, 2.10 |
| 7 | 17 contradictions between parts fixed | Throughout |
| 8 | Runtime facts: agents run in the background; resume message via system message; usage from telemetry; plugin command names tested | 4.3, 4.8, 6.10 |
| 9 | Project commands: go, continue, reopen, cancel, purge; every human gate writes an approval | 2.2, 2.11 |
| 10 | Windows support: paths, encoding, line endings, credential manager, UTC times | 2.1, 3.7 |
| 11 | Design-system record that grows with the project; tolerance bands for tokens | 2.7, 2.8, 6.2, ADR-26 |
| 12 | Additions: cross-project memory, accessibility checks, languages, platform question early, sample data, confidence per item, version differences in review | 2.6, 2.10, 2.12, ADR-27 |
| 13 | One Stitch usage formula; Figma limits in the cost model; evaluation calibrates gating judges first and uses an approved API budget | 6.4, 6.5 |
| 14 | Week-1 tests and the Figma gate pass marks | 6.10 |
