*Independent audit · devil's-advocate method · 3 reviewers*

# MVP AI Architecture Audit

An independent review of the [MVP AI Architecture](https://claude.ai/artifact/7nMt2vxxvNAoVzBdshZKnM), all six parts. Three reviewers who did not write the document read it separately: an AI architect, a platform fact-checker who checked every technical claim against official documentation, and a principal engineer looking for contradictions and running a pre-mortem.

Method: say what the design gets right first, then challenge it with a pre-mortem ("it failed three months in; why?"), inversion ("what would guarantee failure?") and questioning of assumptions, then give a verdict. Facts link to official sources; everything else is the reviewers' judgment.

*Verdict*

**All three reviewers: ship with changes.** The skeleton is sound and better than most: code owns the state, records are versioned and never overwritten, screens are checked by reading their code, feedback goes through a decisions log, and safety has several layers. The problems are where the design assumes that AI, documents or outside tools behave neatly.

**8 issues block the build.** Most are cheap to fix on paper now. Two of them need your decision: how Stitch is called, and how the question loop ends. The platform check also found some good news: hooks *can* tell which agent made a call, so the per-agent permission matrix can really be enforced.

**AI architect**

Ship with changes. Weak spots: quote matching on messy documents, an AI orchestrator trusted to follow the state rules, retries that push agents to invent, no limit on questions, the Figma builder.

**Platform fact-check**

Most claims correct. Wrong or partly wrong: the Stitch SDK is TypeScript only; plugin secrets don't reach scripts run through Bash; a crashed hook lets everything through; Figma read limits of 200 calls a day.

**Consistency + pre-mortem**

Ship with changes. 17 contradictions between parts, mostly drafting drift. Missing: full folder layout, record list, crash safety for outside calls, locking, project commands.

### What is genuinely strong (keep it)

- State machine owned by code, with idempotency keys and versioned records
- Rules checks before AI checks; exact quote matching by code
- Screen presence checked by parsing code or layers; vision only for the look
- Decisions log rebuilt each round instead of patching the prompt
- Layered safety: tool lists, guard hook, untrusted markers, outgoing scan
- Agent cards that list failure modes and required tests before building
- Honest about what isn't known yet

*Needs your decision*

## Three choices

Blocking

### A · How Stitch is called (ADR-11, ADR-16)

Stitch's only official SDK is **TypeScript**, and it is a wrapper around Stitch's MCP endpoint. So "a Python script calls Stitch" has no official path. Separately, plugin secrets (the Stitch key) are not passed to scripts that run through the Bash tool. The platform check also couldn't find an official paid Stitch plan; please confirm what your account is.

*Recommended*

**One TypeScript script for Stitch** using the official SDK; every other script stays Python. Key read from the OS keychain by the script itself

*Option 2*

**Stitch-caller agent** using Stitch's MCP from the plugin's `.mcp.json`; key passed through plugin settings. Simpler setup, but AI makes the calls

*Option 3*

**Python MCP client** talking to Stitch's endpoint. Keeps all-Python, but it's unofficial; needs a day-1 test

Raised by: platform fact-check (verified), consistency review

Blocking

### B · How the question loop ends

You chose "ask as many questions as needed". The reviewers found the stop rule can loop forever: the critic checks a fixed gap list every round, so it nearly always finds a "gap", and "important" isn't defined. Also, a script can't understand messy answers like "same as Q3" or one answer covering three questions.

*Recommended*

**Keep "as many as needed", add a check-in:** define gap importance; after every 4 batches, ask "continue or use suggestions?"; an AI step maps answers to questions and the user confirms

*Option 2*

**Hard caps:** about 7 questions per batch, about 4 batches; then suggestions are used

*Option 3*

**No change:** unlimited, user stops it; risk of endless rounds

Raised by: AI architect, consistency review

Blocking for Figma

### C · How the Figma path is protected

You want both tools, and that stays. But the Figma path is the most likely reason the project slips. A 30-screen project needs about 450–1,200 Figma calls. On the Professional plan, Figma's **read** tools are limited to 200 calls a day, and the plan reads back after every step. Custom fonts are documented inconsistently. Limiting calls to one file may not be checkable, and building real Figma components isn't planned.

*Recommended*

**Keep Figma, gate it:** a 1–2 week test with clear pass marks (calls per screen, quality score, fonts). The agent writes a layout file; a script turns it into Figma calls. Read back through the write tool, which has no limit

*Option 2*

**Figma through Stitch:** Stitch designs, then the design is moved into Figma (Figma has a tool that turns web pages into layers). Must be tested; Stitch's own export isn't available to code

*Option 3*

**No change:** the agent builds frames directly, with high usage and rate-limit risk

Raised by: all three reviewers (rate limit verified)

*Blocking fixes · no decision needed*

## Fix before building

Critical

### 1 · The guard hook lets everything through if it crashes

*What's wrong*

The document says the guard "fails closed". In Claude Code, a hook that crashes (exit code 1) lets the action proceed. Only an explicit "deny" blocks. Also, sub-agents can start other sub-agents by default.

*Fix*

- Wrap all guard logic so any error returns "deny"
- Keep its timeout short
- Leave the `Agent` tool out of every agent's tool list
- Test: force a crash, confirm the call is blocked

Part 5.12, 4.8 · platform fact-check (verified). Good news: the hook does receive the calling agent's type and ID, so the permission matrix in 3.4 can be enforced.

High

### 2 · "AI never moves the state" isn't true yet

*What's wrong*

The orchestrator is the main Claude session. It decides when checks passed and calls `advance`. Over days and many rounds, its memory fills up and can be compacted, and it could skip a check or advance on an old result.

*Fix*

- `mvp-state advance` checks its own conditions: check results exist, their hashes match the current records, approvals exist where needed
- Every `/mvp` rebuilds the orchestrator's working view from `mvp-state status`, not from chat history

Parts 3.6, 4.3, 5.1 · AI architect

High

### 3 · Exact quote matching breaks on real documents, and IDs aren't stable

*What's wrong*

- PDF text has ligatures, hyphenation, smart quotes and headers in mid-sentence; tables become pipe text
- Implied features (login, password reset) have no quote, so each becomes a question
- Each rerun writes a new requirement; nothing keeps `REQ-12` the same, so answers, comments and approvals lose their links

*Fix*

- Normalise text before matching (Unicode, hyphens, quotes, headers)
- Cite tables by cell, e.g. `DOC-3.2/T1/R4`; store character positions
- Add a "convention" status for standard features, confirmed in one answer
- Agent gets the previous version and must keep IDs; a rule checks it

Parts 2.4, 2.10, QG1 · AI architect

High

### 4 · Retries treat every failure as the model's fault

*What's wrong*

- If the client's own text is vague, retrying pushes the agent to invent specifics, which breaks the "never invent" goal
- A stronger model doesn't fix unclear instructions or missing information
- Three agents already use the strongest model, so "rung 2" doesn't exist for them
- Parts 2.9 and 4.5 describe different ladders

*Fix: route by failure type, in one place (2.9)*

- Format error → retry
- Quote not found → script gives the closest real text
- Source is vague → ask the user
- Judge disagrees with itself → mark for a person
- Model chosen by a setting in the task brief, not a second agent file

Parts 2.9, 4.4, 4.5 · AI architect, consistency review

High

### 5 · Crashes during Stitch or Figma calls make duplicates

*What's wrong*

If Claude Code closes while waiting for Stitch, or halfway through a Figma frame, the plan has nothing saved to know what was already created. The "0 duplicate screens" goal fails.

*Fix*

- Save the Stitch job ID and the Figma node IDs before waiting
- One idempotency key per Figma section
- Write files safely: temp file, then rename
- A lock file so two sessions can't run one project

Parts 2.7, 2.9 · consistency review

High

### 6 · Folder layout, record list and state format are incomplete

*What's wrong*

- Only some folders are named; gaps, questions, answers, feedback, issues and the package have no path, so the guard hook can't enforce paths
- Records like tokens, samples, image descriptions, messages and issues aren't in the record list
- Some files are edited in place (answers, logs, questions, review page), which breaks the hash rule

*Fix*

- Publish the full folder tree with each agent's write paths
- Complete the record list and the `state.json` format
- Version every file: e.g. `questions-b3.md`, `feedback-r2.md`; hash log lines

Parts 2.1, 2.10, 3.2 · consistency review

*Platform fact-check*

## What the document got right and wrong

| Claim | Verdict | What's true |
|---|---|---|
| Plugin parts: commands, agents, skills, hooks, MCP file, `bin/` scripts on the path | Correct | Docs now prefer skills over commands for new plugins |
| Plugin secret (Stitch key) available to scripts | Partly | Stored in the OS credential store; given to hooks and MCP config, **not** to commands run through Bash |
| Private marketplace from git, pinned versions | Correct | — |
| Agent file fields and model names | Correct | Full model IDs also allowed |
| Sub-agents can't ask the user questions | Correct | — |
| Agents never start each other | Partly | They can by default; remove the `Agent` tool |
| Agents run one after another | Partly | In interactive sessions they run in the background by default; wait for completion or turn background off |
| Frame builder limited to Figma tools | Partly | Tool list can name Figma tools; limiting to one file only through the hook, if the file key is visible |
| Guard hook knows which agent called and can block | Correct | Receives agent type and ID; can deny with a reason |
| Guard fails closed | Wrong | A crash lets the action proceed |
| Validation hook sends errors back to the agent | Correct | The file is already written at that point |
| Agent-finished hook reports usage | Partly | No usage field; get it from telemetry or the transcript |
| Session-start hook shows a message to the user | Partly | Must use the "system message" field |
| Bash limited to `mvp-*` scripts | Partly | Plugins can't ship permission rules; must be enforced by the guard hook |
| Langfuse from hooks | Correct | Official Claude Code integration exists; pin its SDK version. Claude Code's telemetry export could replace much of the trace script |
| Figma write: Full seat, beta, about 20 KB, no images | Correct | Will become a paid, usage-based feature |
| Figma fonts must be uploaded | Unclear | Figma's two documents disagree; test it |
| Figma limits | Missing | Professional plan: 200 read calls a day, 15 a minute; write calls exempt |
| Stitch callable from a Python script | Partly | Official SDK is TypeScript only; it wraps Stitch's MCP endpoint |
| Stitch generate, edit, export HTML and image | Correct | Calls wait up to about 5 minutes by default |
| Stitch paid plan and quota | Unverified | Only third-party sources; free Labs product with monthly caps |
| Stitch to Figma export by code | Likely wrong | Not in the SDK; Figma's own web-to-layers tool is a possible route |
| PDF read 20 pages at a time; no DOCX | Correct | Page ranges need the poppler tool installed, also on Windows |

*Contradictions between parts*

## Drafting drift to clean up

| Where | Conflict | Fix |
|---|---|---|
| 2.2 vs MVP Flow page | Different state lists | 2.2 is the master list; update the Flow page |
| Part 3 vs 1.5, 1.6, 1.9 | Stitch called by script vs. by MCP | Settle decision A, then align all diagrams |
| 2.9 vs 4.5 | Different retry ladders; continue vs. stop | One ladder by failure type, in 2.9 only |
| 4.5 vs 4.6 | "Stronger model" for agents already on the strongest | Model as a setting; more effort instead |
| 3.4 vs P1 | Orchestrator has no Figma access but runs the Figma test | Test runs through the frame builder |
| 3.4 vs 4.7 | Frame builder writes a file but has no write tool | Give it write to its path only, or a script fetches the layers |
| S2b vs S11 | Samples use tokens that only exist after "Go" | Samples use style message values |
| R6, S8 vs 3.4 | AI checker writes records it isn't allowed to | Script builds records from checker output |
| 3.6 vs R7, U6, D6, P7, S6 | "Scripts never call AI" vs. mixed script + AI steps | Orchestrator runs the AI part; label actors clearly |
| 4.7 vs M3 | Critic output has no AI check | Add a gap-value rubric, or note the exception |
| 2.2 vs 2.5 | Requirement change from samples goes to the wrong state | Go to requirement drafting; mark samples stale |
| 3.4 vs P4 | Design Prompt agent can't read answers | Add answers to its reads |
| 2.1 vs mutable files | "Never overwritten" vs. answers, logs, review page | Version them (blocking fix 6) |
| U3 vs U6 | Items need a question ID before questions exist | Agent drafts the question; builder assigns IDs |
| 2.10 vs 3.2 | Record list incomplete | Complete it (blocking fix 6) |
| MVP Flow vs 6.5 | 60–90 vs. about 45 Stitch generations | One formula including fix loops and final edits |
| MVP Flow vs R2 | When Stitch and Figma connections are tested | Follow R2 |

*Pre-mortem*

## "Three months in, it failed. Why?"

| Most likely cause | Early warning | Prevention |
|---|---|---|
| The Figma path swallowed the team | A form screen needs more than 40 calls, or scores below 3/5 | Decision C: a gated test with pass marks |
| The Stitch call assumption was wrong | No working script call by day 3 | Decision A on day 1, with the fallback designed |
| Usage limits made full runs impossible | Stage 2 alone uses more than 30% of a Max window; escalations on more than 20% of runs | Measure in week 1; normalise quotes; check samples of items; cap retries per project |
| Resume broke in edge cases | Kill-mid-step tests are flaky | Blocking fixes 5 and 6 |
| Evaluation never got ready, so nothing was "done" | Fewer than 12 gold documents by week 4 | Calibrate only the support and testable judges first; start labelling in week 1 |

*Not blocking · improve during the build*

## Worth fixing, and what an expert would add

### Improve

- **Consistency:** 1–2 samples don't show tables, pop-ups or empty states. Keep a growing design-system record (tokens + components); use tolerance bands instead of a 100% match; confirm Stitch accepts a reference screen
- **Evaluation workload:** 10 rubrics × 50 labels ≈ 500 labels. Calibrate the 4 gating judges first; define how gold items are matched; report averages with spread
- **Evaluation budget:** a "small API budget" conflicts with ADR-01; approve it explicitly or run evaluation on subscriptions
- **Cost model:** add retries, usage windows, Figma read limits; one Stitch formula
- **Project commands:** cancel, reopen a stage, purge, "Go", continue after budget pause; every human gate writes an approval record
- **Tool switch:** store tool and Figma file key in state; switching tools invalidates samples
- **Windows:** path normalisation in the guard, Python launcher, UTF-8 and line endings, credential manager, UTC times
- **Model pinning:** subscription uses model aliases; pinning may not be possible in v1

### An expert would add

- Memory across projects: reusable design systems, glossaries and past answers as defaults
- An accessibility step: contrast and touch-size checks on tokens
- Languages: output language, right-to-left, longer text, non-English documents end to end
- Better approval experience: differences between versions, partial approval, inline comments
- Ask early: mobile, web or both, and screen sizes
- Realistic sample data in screen messages
- A confidence note per item, so reviewers check the risky ones first

*Week 1*

## Hands-on tests that settle the open points

| Test | Settles |
|---|---|
| Call Stitch from a script (TypeScript SDK, or Python to the MCP endpoint): generate, edit, get HTML; time and quota | Decision A |
| Figma: one form screen; calls per screen; does reading back through the write tool avoid the daily limit; does an uploaded font render; is the file key visible to the hook; can seat type be read without a test frame | Decision C |
| Stitch to Figma route through Figma's web-to-layers tool | Decision C option 2 |
| Guard hook: agent type names for plugin agents and the main session; force a crash and confirm it blocks | Blocking fix 1 |
| A `bin/` Python script on Windows; confirm plugin secrets are absent in Bash | Decision A, scripts |
| Background vs. foreground agents; naming exact Figma tools in a tool list | Runtime design |
| Whether `/mvp` works as a plugin command name or must be `/mvp:mvp` | Commands |
| Langfuse hook with a pinned SDK; optional Claude Code telemetry to Langfuse | Tracing |
| Quote matching on 3 real PDFs after normalisation: share found word for word | Blocking fix 3 |
| One full project on Max: usage per stage | Cost model, usage risk |

*Sources checked by the platform reviewer (2 Oct 2026)*

- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Plugins reference](https://code.claude.com/docs/en/plugins-reference)
- [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Permissions](https://code.claude.com/docs/en/permissions)
- [Tools reference](https://code.claude.com/docs/en/tools-reference)
- [Monitoring and telemetry](https://code.claude.com/docs/en/monitoring-usage)
- [Langfuse Claude Code integration](https://langfuse.com/integrations/other/claude-code)
- [Figma write to canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)
- [Figma MCP rate limits](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)
- [Figma MCP server FAQs](https://help.figma.com/hc/en-us/articles/39252411778583)
- [Figma MCP server guide](https://github.com/figma/mcp-server-guide)
- [Google Stitch SDK](https://github.com/google-labs-code/stitch-sdk)
