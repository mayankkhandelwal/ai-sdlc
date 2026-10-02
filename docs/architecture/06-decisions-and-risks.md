PART 6

## Decisions and risks

Everything that cuts across all parts: the decisions and why they were made, the quality targets, the threat model, how evaluation is built in, the usage and cost model, versioning, the path to v2, the risk list and a glossary.

PART 6 · 6.1

## Architecture decision records

One line per decision: what was chosen, what was rejected, and what follows from it. In revision 2 every decision is accepted; ADR-19 to ADR-27 come from the architecture audit.

| ID | Decision | Rejected | Consequence | Status |
|---|---|---|---|---|
| ADR-01 | v1 is a Claude Code plugin on the team's own subscription | Agent SDK on API keys now; a web app | Fast to build; internal testing only; no API cost; v2 needed to sell | Accepted |
| ADR-02 | Orchestrator command + state script in code control the steps | One big agent; an AI planner; a workflow engine | Predictable and resumable; new paths need code | Accepted |
| ADR-03 | Every output checked by rules first, then AI | Rules only; AI only; people only | Extra time per step; judges must be calibrated | Accepted |
| ADR-04 | A Python script reads documents; AI only checks and describes images | Whole file to the model; OCR service | Python required; stable section IDs | Accepted |
| ADR-05 | Every requirement quotes its source word for word | Section IDs only | Invented requirements are caught by code | Accepted |
| ADR-06 | A separate critic agent finds gaps | Self-review by the same agent | One more agent run; more gaps found | Accepted |
| ADR-07 | Questions in batches, as many as needed, in HTML + Markdown files | Chat one by one; one big form; assume | More user time upfront; fewer wrong guesses | Accepted |
| ADR-08 | Screen list approved together with requirement and stories | No screen list; screens first | Bigger approval; design size known early | Accepted |
| ADR-09 | One style message + one message per screen | One prompt for all screens | Within limits; style message repeated each call | Accepted |
| ADR-10 | Both Stitch and Figma behind one adapter interface | One tool only | Two paths to maintain; user choice | Accepted |
| ADR-11 | One TypeScript script calls Stitch through Google's official SDK; it reads the key from the OS keychain itself | Agent calls Stitch MCP; unofficial Python client | Exact, countable, resumable calls; Node.js needed on testers' machines | Accepted |
| ADR-12 | Figma frames built from a script-compiled layout file, carried by an agent limited to Figma's write tool and one file; gated by a test (ADR-23) | Skip Figma; agent draws frames freely | Still high Claude usage per screen; consistent, editable frames with components | Accepted |
| ADR-13 | Screen fields checked by parsing code or layers; vision only for look | Vision only | A parser per tool; exact presence checks | Accepted |
| ADR-14 | Feedback goes into a decisions log; messages are rebuilt from it | Patch prompt each round | No contradictions; one rebuild run per round | Accepted |
| ADR-15 | Langfuse tracing through hooks, metadata only by default | Local logs only; full content logging | Another service; privacy kept | Accepted |
| ADR-16 | All v1 scripts in Python except the Stitch script (TypeScript) | All Python (no official Stitch SDK); all TypeScript | Two runtimes; each script uses the best-supported library | Accepted |
| ADR-17 | New apps only in v1; existing apps in v1.1 without building them | Existing apps now; building unknown repos | Smaller v1; safer | Accepted |
| ADR-18 | Model per agent: Opus for judgment, Sonnet for structured work, Haiku for sorting; escalation by reasoning effort | One model for all; escalate to a different model | Confirmed or changed by the week-1 bake-off | Accepted |
| ADR-19 | Guard hook fails closed: every error returns "deny"; no agent can start agents | Trust the hook not to crash | A broken guard blocks work instead of allowing everything | Accepted |
| ADR-20 | The state script checks its own conditions before every move; the orchestrator rebuilds its view from the state each run | Trust the orchestrator to call `advance` correctly | "AI never moves the state" becomes true in practice | Accepted |
| ADR-21 | Quotes matched on normalised text, with positions; tables cited by cell; IDs stable across versions; "convention" items | Exact text match only; new IDs per version | Fewer false failures; links never break | Accepted |
| ADR-22 | Failures routed by type (format, missing quote, vague source, own wording, unstable judge, instructions problem) | "Retry, then stronger model, then stop" for everything | No invented detail from retries; less wasted usage | Accepted |
| ADR-23 | Figma path gated by a 1–2 week test with pass marks (6.10) | Commit to the Figma path untested | Figma risk known early; alternative route ready | Accepted |
| ADR-24 | Questions: as many as needed, gap importance levels, check-in every 4 batches, AI answer map confirmed by the user | Hard caps; unlimited with no check-in; script-only answer parsing | No endless loops; messy answers handled | Accepted |
| ADR-25 | Crash safety: job IDs saved before waiting, safe file writes, project lock, every file versioned | Rerun steps after a crash | No duplicates; resume always works | Accepted |
| ADR-26 | A design-system record (tokens + components) that grows; tolerance bands | Tokens from 1–2 samples with 100% match | Realistic consistency checks | Accepted |
| ADR-27 | Additions: team library across projects, accessibility rules, languages and right-to-left, platform asked early, sample data, confidence per item, version differences in review | Leave for v2 | More work in v1; higher quality and trust | Accepted |

PART 6 · 6.2

## Quality targets

The quality goals from Part 1 (QG1–QG7) as measurable targets, plus targets for speed, usage and privacy. Starting values; set by the team after the first evaluation.

| Quality | Target | Measured by |
|---|---|---|
| Grounding (QG1) | 0 items with a quote not found in the document; 0 unsupported items on all 3 runs | Rules check + support rubric |
| Requirement quality | Recall ≥ 80%, precision ≥ 85% against a reviewed gold set | Evaluation set |
| Traceability (QG2) | 100% of criteria on a screen, or each gap listed | Coverage report |
| Recoverability (QG3) | 100% of failure tests resume; 0 duplicates; 0 lost answers | Failure tests |
| Safety (QG4) | 0 followed injections; 0 keys in files, chat or traces | Red-team set; masking tests |
| Consistency (QG5) | Every screen within the tolerance bands of the design-system record, or each mismatch flagged | Screen checker |
| Stable IDs (QG8) | 100% of links still resolve after every new version | Rules check |
| Accessibility | All text meets WCAG AA contrast; mobile touch targets ≥ 44 px | Rules check on tokens and facts |
| Usability (QG6) | Test users answer every question without asking what it means | Pilot |
| Tool independence (QG7) | Switching tools needs no agent or schema change | Contract tests |
| Design quality | Median designer rating ≥ 3.5 / 5 for each tool; 0 critical accessibility failures | Designer review; accessibility scan |
| Speed | Measured per stage; no fixed target in v1 | Langfuse spans |
| Usage | One 30-screen project completes on one Max subscription without hitting limits | Week-1 measurement |
| Privacy | Only needed sections sent; no document text in traces by default | Trace audit |

PART 6 · 6.3

## Threat model

Based on the common risks for AI applications (OWASP Top 10 for LLM applications) and the trust boundaries in Part 3.3.

| Threat | Way in | Impact | Defence | Test |
|---|---|---|---|---|
| Prompt injection | Document, Figma content, Stitch output | Agent acts on attacker's words | Untrusted markers; tool lists; guard hook; agents can't send data out | Red-team documents per channel |
| Excessive agency | An agent with more tools than needed, or one that starts another agent | Commands run, files changed, data sent | Permission matrix; no agent has the tool to start agents; guard hook fails closed | Every blocked action tested |
| Safety check bypassed by a crash | Guard hook error | Everything allowed | All guard logic wrapped; any error returns "deny" | Force a crash; the call must be blocked |
| Sensitive data leaving | Messages to Stitch or Figma; traces | Client data exposed | Messages from checked fields only; outgoing scan; user OK; masking | Planted secrets and personal data |
| Unsafe output shown | Text or HTML from documents or exports in the review page | Script runs on the user's machine | Escape everything; block scripts; no live HTML | Script test strings |
| Path tricks | Screen names from the document used as file names | Files written outside the project | Safe slugs; path check in guard hook | Names like `../../` |
| Wrong Figma file changed | Agent tricked or confused | Client's other designs altered | Guard checks the file key on every Figma call | Call with another file key |
| Key theft | Logs, files, environment | Account misuse | OS keychain; masking; no shell for agents | Search all outputs for key patterns |
| Supply chain | Unpinned MCP servers or Python packages | Malicious code with the user's access | Pinned versions; official sources only; private plugin marketplace | Dependency review per release |
| Tampered approvals | Editing local files | False record of what was approved | Hashes of approved files; v1 audit marked as internal only | Edit a file after approval; check detects it |
| Overreliance | Users trusting output without reading | Wrong design accepted | Sources and assumptions shown; required approvals | Pilot observation |

PART 6 · 6.4

## How evaluation is built in

| When | What runs | Blocks if |
|---|---|---|
| Every prompt, skill or rubric change | Smoke set: 5 documents, 1 run, the affected steps only, on frozen inputs from earlier steps | Any hard rule fails, or a score drops |
| Weekly | Full text set: about 20 documents × 3 runs, steps 1–4 | Targets in 6.2 missed |
| Every two weeks | Design set: 6 documents × 2 sample screens × each tool | Spec match or consistency below target |
| Before each plugin release | Everything, plus failure and red-team tests | Any safety or recovery test fails |
| When a model changes (aliases follow new versions) | Smoke set, and recheck every judge's calibration | Agreement with human labels drops |
| Pilot | 3–5 real users | — (learning, not a gate) |

Dataset: 12 real documents with a reviewed gold answer, 8 synthetic or tricky ones (empty, contradictory, injected, very long, non-English, scanned, table-heavy), and a hold-out set nobody tunes prompts on. Gold items are matched to output items by a written alignment rule (one gold item may match one or more output items, never the reverse) so splitting or merging doesn't change scores. Results are reported as averages with their spread. The four gating judges are calibrated first. Repeated runs use a small, approved API budget used only for evaluation; this is the one exception to ADR-01.

PART 6 · 6.5

## Usage and cost model

Formulas to estimate usage per project. The numbers are assumptions until measured in week 1.

| What | Formula | Example: 30 screens, 3 sample rounds |
|---|---|---|
| Stitch generations and edits (one formula, used everywhere) | samples × rounds × (1 + sample fixes ≈ 1) + screens × (1 + fixes ≈ 0.3) + final-review edits (≈ 0.2 × screens) | 2 × 3 × 2 + 30 × 1.3 + 6 ≈ **57**; plan for **60–90** with a margin |
| Figma write calls | screens × compiled chunks per screen (assume 4–10) × (1 + read-backs) | 30 × 4–10 × 2 ≈ **240–600** write-tool calls, all through Claude; no daily limit on write calls |
| Figma read calls | Only the seat and file checks, plus anything not done through the write tool | Kept far under 200 a day and 15 a minute (Professional) |
| Retries | Capped per project (start: 30) | Up to 30 extra agent or check runs |
| Agent runs (understand + define) | requirement passes (1 + batches) + critic passes + BA + checks | With 4 question batches: about **15–25** runs |
| AI checks | one per record per rubric + one look check per screen version | About **60–90** check runs |
| Langfuse events | one per tool call + one per span | Thousands; metadata only |

### v1 (subscription)

- No per-token cost; the limit is the plan's usage allowance, which resets in time windows
- The Figma path is the heaviest; testers use Max
- Opus agents with large contexts use the allowance fastest
- Measure one full project on each tool in week 1; projects resume after a usage-limit stop

### v2 (API keys)

- Cost = tokens per agent run × runs per project
- Langfuse spans give the real numbers from v1 to price v2
- Model routing (6.1 ADR-18) is the main cost lever

PART 6 · 6.6

## Versioning

| Thing | Version rule | Change process |
|---|---|---|
| Agent files, skills, rubrics | Major.minor.patch, written into every record they produce | Change → smoke evaluation → release note |
| Schemas | Version number in each record | Old projects stay readable; a migration script for breaking changes |
| Records in a project | `.vN` files, never overwritten | Approvals point to exact versions by hash |
| Plugin | One version for the whole plugin | Released through the private marketplace, pinned |
| MCP servers and Python packages | Exact pinned versions | Reviewed before upgrade |

PART 6 · 6.7

## From v1 to v2

| Part | v1 | v2 | Move |
|---|---|---|---|
| Agents, skills, rubrics | Plugin files | Same files through the Agent SDK | Keep |
| Schemas and contracts | JSON Schema | Same | Keep |
| Rules checks, reader, facts parser | Python scripts | Same code as services | Keep |
| Stitch adapter | TypeScript script with the team's key | TypeScript service with per-customer or company keys | Keep, extend |
| Figma compiler and frame builder | Python compiler + agent courier | Same, run through the Agent SDK | Keep |
| Team library | Local shared folder per client | Per-customer storage | Replace store |
| Model access | User's subscription | API keys (or the customer's cloud) | Replace |
| State | `state.json` | Database, same states | Replace store, keep machine |
| Records | Local files | Database + file storage | Replace store |
| Questions and review | HTML + Markdown files | Dashboard screens | Replace |
| Guard hook | Claude Code hook | Agent SDK permission rules | Port |
| Tracing | Hooks → Langfuse | SDK → Langfuse | Port |
| Users | One person per install | Teams, login, roles, billing | New |
| Existing apps | v1.1 | Included | Extend |

PART 6 · 6.8

## Risk list

| Risk | Likely | Impact | Plan | Warning sign | Owner |
|---|---|---|---|---|---|
| Figma's write feature changes or becomes expensive (beta) | Medium | High | Adapter isolates it; Figma gate (6.10); alternative route through Figma's web-to-layers tool | Figma announcements; failing calls | Product |
| Figma path fails the gate | Medium | Medium | Ship Stitch first; Figma through the alternative route or in v1.1 | Gate results below pass marks | Product |
| Stitch changes, limits quota or closes (Google Labs; SDK "not officially supported") | Medium | High | Figma path stays working; screen budget; SDK version pinned | Quota or terms change; SDK errors | Platform |
| The orchestrator (AI) drifts in long sessions | Medium | High | State script checks its own conditions; view rebuilt each run | Refused moves in the trace | Platform |
| Subscription usage limits stop long projects | High | Medium | Measure in week 1; resume works; Max plan; lighter checks | Limit hit in tests | All |
| Design quality not good enough to show clients | Medium | High | Samples first; designer review; better style messages | Low designer ratings | Agents |
| Screens drift in style | Medium | Medium | Tokens from samples; reference generation; token check | Token mismatches | Agents |
| Requirements still invented or wrong | Low | High | Quotes, critic, approvals | Support rubric failures | Agents |
| Too many questions tire the user | Medium | Medium | Batches, importance order, "use your suggestions" | Users skip batches | Agents |
| Three people can't cover both tools well | Medium | Medium | Contracts first; shared tests; order phases | Phases slip | All |
| A model update changes agent behaviour | Medium | Medium | Smoke set on every change; pinned models where possible | Score drops without a prompt change | Agents |
| Claude Code plugin features change | Low | Medium | Pin Claude Code version for testers; follow release notes | Hooks or agents behave differently | Platform |
| Not enough real documents with gold answers | Medium | Medium | Use past Softude projects with permission; synthetic documents | Dataset under 12 real documents | Agents |
| Client data used before terms are cleared | Low | High | v1 rule: non-confidential only; checklist before any client use | A real client document appears | All |

PART 6 · 6.9

## Glossary

| Term | Meaning here |
|---|---|
| Agent / sub-agent | An AI worker with its own instructions, tools and fresh context |
| Orchestrator | The `/mvp` command; starts workers, runs checks, talks to the user |
| State script | `mvp-state`; the only thing that changes the project's step |
| Record | A versioned JSON file an agent or script produces (requirement, storyset, …) |
| Rules check | An exact check by code: format, IDs, links, quotes, coverage |
| AI check / rubric | A separate AI answering one yes/no question per item |
| Grounding | Every item backed by a quote from the document or an answer |
| Critic | An agent that only looks for gaps, in a fresh context |
| Batch | A group of related questions sent together |
| Screen list | Every screen, its states and links, approved with the stories |
| Style message | One message with everything shared by all screens |
| Screen message | One message with everything specific to one screen |
| Adapter | The code that hides which design tool is used |
| Frame builder | The agent that builds Figma frames piece by piece |
| Screen facts | The fields, labels, buttons, colours and fonts read from a screen |
| Design tokens | Named values for colours, fonts and spacing |
| Decisions log | The list of design changes from feedback; messages are rebuilt from it |
| Coverage report | How many criteria are visible on a screen, with gaps listed |
| Guard hook | The check before every tool call |
| Trace / span | The record of one project / one step in Langfuse |
| Idempotency key | Project + item + version; lets a step rerun without duplicates |
| Untrusted | Content we didn't write; read as data, never followed |
| Gold set | Reviewed correct answers used to measure quality |
| Calibration | Checking an AI judge against human labels before trusting it |
| ADR | Architecture decision record: what was chosen and why |
| Convention item | A standard feature (login, password reset) assumed without a quote and confirmed by the user |
| Normalised text | A cleaned copy of a section (quotes, hyphens, spaces) used only for quote matching |
| Gap importance | Blocking, important or minor: how much a missing answer would change the result |
| Check-in | After every 4 question batches: "continue, or use suggestions?" |
| Answer map | Which answer covers which questions, confirmed by the user |
| Layout file | The frame builder's description of a Figma screen, compiled by a script into Figma code |
| Chunk | One piece of compiled Figma code under 20 KB, with its own idempotency key |
| Job file | Saved IDs of an outside job (Stitch screen, Figma nodes) so a crash can resume it |
| Design-system record | Tokens and components from approved screens, growing during the build |
| Tolerance band | How far a value may differ and still count as matching |
| Fail closed | When a safety check errors, it blocks rather than allows |
| Lock file | Stops two sessions from working on one project at once |
| Team library | Design systems, glossaries and past answers kept across projects, per client |

PART 6 · 6.10

## Week-1 tests and the Figma gate

| Test | Pass when | Settles |
|---|---|---|
| Stitch from the TypeScript script: test, generate, edit, get HTML and image | 3 screens with all fields; time and quota per screen recorded; account type confirmed | ADR-11 |
| Stitch key read from the OS keychain by the script; plugin secrets confirmed absent in Bash | Key never appears in files, chat or logs | ADR-11 |
| Guard hook: agent type and ID for each plugin agent and the main session; forced crash | Every agent identified; the crashed hook blocks the call | ADR-19 |
| Figma write tool: is the file key visible to the hook; can the seat be checked without reads | Guard can enforce one file | ADR-12 |
| Background agents: orchestrator waits for completion; naming exact Figma tools in a tool list works | Steps run in order | 4.3 |
| Plugin command names: `/mvp` or `/mvp:mvp` | Names fixed in 2.11 | 2.11 |
| Python scripts in `bin/` on Windows, macOS and Linux; poppler page reads | All scripts run on all three | 3.7 |
| Quote matching on 3 real PDFs after normalisation | At least 95% of real quotes found | ADR-21 |
| Langfuse hook with the pinned SDK; optional Claude Code telemetry to Langfuse | One project fully traced, no secrets | ADR-15 |
| One full project on Max: usage per stage | Completes, or resumes cleanly after a limit | 6.5 |
| Model bake-off: same steps on Opus, Sonnet and Haiku | Model table in 4.6 confirmed | ADR-18 |

*Figma gate · 1–2 weeks · all must pass to keep the compiled-layout path*

| Pass mark | Target |
|---|---|
| Write-tool calls per form screen | ≤ 20 |
| Designer rating of 3 test screens | ≥ 3.5 out of 5 |
| Fields present (screen check) | 100% |
| Uploaded custom font renders | Yes, or a matching Google font accepted |
| Reading back through the write tool avoids the daily read limit | Yes |
| Crash mid-screen resumes with no duplicate frames | Yes |
| Claude usage for one 30-screen project on Max | Finishes within two usage windows |

If the gate fails: test the alternative route (Stitch designs, then Figma's web-to-layers tool builds editable layers). If both fail, Stitch ships first and the Figma path moves to v1.1. Stitch's own export to Figma isn't available to code, so it isn't an option.

*Concept and why · Part 6*

**Decision records**

They keep the "why" after the people who decided have moved on, and stop old debates from coming back.

**Threat modelling**

List how the system could be attacked before building it; each threat becomes a defence and a test.

**Evaluation as part of the architecture**

For AI systems, tests are not an afterthought: every prompt change is a code change and must pass the same gates.

**Cost model before scale**

A formula, even a rough one, shows which part will hurt first (here, Figma building) and where to optimise.

**Risk register**

Each risk with a warning sign and an owner turns worry into something that gets checked.

**Learn next**

ADRs, OWASP Top 10 for LLM applications, STRIDE threat modelling, eval-driven development, cost modelling, semantic versioning, risk registers.

Revision 2 is complete: all audit suggestions are applied and every decision is accepted. Further changes are made as new versions of this page.
