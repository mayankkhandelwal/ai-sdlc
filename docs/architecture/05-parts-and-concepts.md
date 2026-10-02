PART 5

## Parts and concepts

Fourteen parts, each explained for learning: the concept behind it, why it's built this way, what else was considered and why not, what we give up, how it can fail, how to test it, and what to learn next. The exact steps are in Parts 2–4; this part explains the thinking.

| Block | Answers |
|---|---|
| Concept | The general idea, reusable in other projects |
| Why this way | The reason it fits this system |
| Alternatives | Other designs considered, and why each was not chosen |
| Trade-offs | What we give up by choosing this |
| Failure modes | How it can go wrong, and the defence for each |
| How to test | What proves it works |
| Learn next | Topics to study |

5.1

### Orchestrator and state script

Steps: 2.2 · Runtime: 4.3

Code decides the order of steps; AI works only inside a step.

*Concept*

Orchestrator–worker pattern with a finite state machine. One coordinator, many focused workers, and a fixed map of allowed moves.

*Why this way*

Approvals can't be skipped, every path can be tested, and the project resumes exactly where it stopped.

*Alternatives*

- **One big agent in one conversation:** its memory fills up, it skips steps, and it can't resume
- **An AI planner choosing the next step:** unpredictable and hard to test
- **A workflow engine (Temporal, DBOS):** too heavy for a local plugin; a v2 option

*Trade-offs*

Less flexible: a new path needs a code change. More design work upfront.

*Failure modes → defence*

- State file damaged → rebuild from record files and hashes
- Command calls the wrong script → guard hook allows only listed scripts; state script rejects illegal moves
- The orchestrator (an AI) drifts over a long session and believes a check passed → `advance` checks the check-result files and hashes itself; the view is rebuilt from the state on every run
- Two sessions on one project → lock file with heartbeat

*How to test*

A unit test for every allowed move and every illegal one. Kill the run mid-step and check that resume works with nothing lost.

*Learn next*

`State machines` `Orchestrator–worker pattern` `Workflow orchestration` `Idempotency` 5.2

### Checker: rules + AI

Rubrics: 4.4

Exact checks by code first; meaning checks by a separate AI second.

*Concept*

Hybrid validation. Deterministic validators plus LLM-as-judge, with the judge calibrated against human labels.

*Why this way*

Rules are exact and free but can't judge meaning. AI can judge meaning but can be wrong and uses the subscription. Together they cover each other.

*Alternatives*

- **Rules only:** misses vague, unsupported or untestable items
- **AI only:** uses more of the subscription, gives different answers on reruns, proves nothing exactly
- **A person checks everything:** slow; people are kept for approvals

*Trade-offs*

Extra time and usage per step. A judge can still be wrong in a consistent way.

*Failure modes → defence*

- Judge too lenient → yes/no per item, fresh context, calibration set
- Rule too strict, false failures → review rule failures in traces each week

*How to test*

Files with planted defects for each rule. For each rubric, about 50 hand-labelled items; the judge must agree with people well enough (for example, kappa ≥ 0.6) before it's trusted.

*Learn next*

`JSON Schema` `LLM-as-judge` `Judge calibration` `Cohen's kappa` 5.3

### Document reader

Steps: 2.3

A script converts the document; AI only checks the result and describes images.

*Concept*

Deterministic preprocessing and chunking: turn messy input into clean, addressable pieces before any AI reads it.

*Why this way*

Converting a file has one right answer, so code does it the same way every time. Section IDs make exact citations possible.

*Alternatives*

- **Give the whole file to the model:** page limits, no stable section IDs, more usage
- **An OCR or document-AI service:** another provider and cost; not needed in v1
- **Embeddings and vector search:** unnecessary for one document; a v2 option

*Trade-offs*

Python must be installed. Complex layouts, such as multi-column PDFs, may convert badly.

*Failure modes → defence*

- Tables broken → table-count rule + AI conversion check
- Scanned PDF without text → stop and ask for another format
- Hidden instructions → injection scan; sections marked untrusted

*How to test*

A set of about 10 documents of different shapes (tables, images, long, multi-column, DOCX and PDF). Compare section and table counts with the originals.

*Learn next*

`Document parsing` `Chunking strategies` `pandoc` `PDF text extraction` 5.4

### Requirement agent + critic

Steps: 2.4 · Card: 4.7

Every requirement quotes its source word for word; a second agent hunts for what's missing.

*Concept*

Grounded generation with verifiable citations, plus the generator–critic pattern.

*Why this way*

A wrong requirement spreads into stories, screens and the whole design. This is where errors are cheapest to stop.

*Alternatives*

- **Cite by section ID only:** models invent plausible IDs; nothing proves support
- **The same agent reviews itself:** same blind spots; tends to approve its own work
- **No critic, rely on user review:** users miss what isn't written

*Trade-offs*

Quotes make records longer. Marking inferred items creates more questions for the user.

*Failure modes → defence*

- Quote paraphrased → exact match fails → the script returns the closest real text as a hint
- Real quote fails because of PDF quirks (ligatures, hyphenation, smart quotes, headers) → match on normalised text; tables cited by cell
- Standard features with no quote (login, password reset) → "convention" items, confirmed in one question
- IDs renumbered on a rerun, breaking links → agent gets the previous version; a rule checks IDs are stable
- Critic lists generic gaps → fixed gap list, importance levels, gap-value rubric
- Vague client wording → becomes a question, never a retry that invents detail

*How to test*

Synthetic documents with planted requirements and planted gaps; the agents must find all of them. Injected-instruction documents must change nothing.

*Learn next*

`Grounding / citations` `Hallucination control` `Critic / reflection patterns` `Requirements engineering` 5.5

### Question system

Steps: U6–U9

Ask everything the agents need, in plain batches, and keep every answer as a source.

*Concept*

Elicitation with human-in-the-loop. Answers become first-class sources that later items can cite.

*Why this way*

Guessing is the biggest source of wrong output. Plain words, "why I'm asking" and suggestions let non-technical people answer well.

*Alternatives*

- **Ask one by one in chat:** slow, and answers get lost in the conversation
- **One big form:** overwhelming; people skip questions
- **Don't ask, assume:** fast but often wrong

*Trade-offs*

More of the user's time upfront, and waiting between batches.

*Failure modes → defence*

- Duplicate or already-answered questions → duplicates rubric
- Endless rounds → gap importance levels; check-in after every 4 batches
- Messy answers ("same as Q3", one answer for three questions, answers in chat) → AI answer map, confirmed by the user
- User edits a question's text → the block hash changes and the user is warned
- Blank answers → question stays open

*How to test*

Test users rate each question's clarity. Count questions the document already answered (target 0).

*Learn next*

`Requirements elicitation` `Survey and question design` `Human-in-the-loop` 5.6

### BA agent + screen list

Steps: 2.5 · Card: 4.7

Stories, testable criteria and an approved screen list, all linked to each other.

*Concept*

Behaviour-driven development (Given/When/Then) with a traceability matrix: requirement → story → criterion → screen.

*Why this way*

The criteria define "done", and the screen list sets the design's size and cost. Both are cheap to fix before screens exist.

*Alternatives*

- **No screen list:** the design step guesses which screens exist
- **Screens first, then stories:** loses the link back to requirements

*Trade-offs*

A larger approval package for the user to read.

*Failure modes → defence*

- Screens missing error or empty states → states rule
- Stories beyond scope → scope rubric
- Orphan screens → link rule

*How to test*

100% coverage on the test set; testability judged by the calibrated rubric.

*Learn next*

`BDD / Gherkin` `User story mapping` `Traceability matrix` 5.7

### Design Prompt agent

Steps: 2.6 · Card: 4.7

One style message for the whole project, one message per screen.

*Concept*

Meta-prompting with templates; separating global instructions from local ones.

*Why this way*

Short messages stay within tool limits, every screen gets full attention, one screen can be redone alone, and a style change happens in one place.

*Alternatives*

- **One prompt for all screens:** hits limits; later screens lose detail
- **Free-form prompt per screen:** every screen looks different

*Trade-offs*

The style message is repeated in every call, which uses more of the tools' input.

*Failure modes → defence*

- Generic style ("modern, clean") → checklist forces concrete values
- Message too long → length rule
- Criterion dropped → every criterion tagged by ID and checked

*How to test*

Same brief, 3 runs: messages should be stable and every criterion included.

*Learn next*

`Meta-prompting` `Prompt templates` `Design briefs` `Agent skills` 5.8

### Design adapters: Stitch script and Figma frame builder

Containers: 3.1 · Contract: 3.6 · Gate: 6.10

Two very different tools behind one interface: generate, edit and resume.

*Concept*

Ports and adapters (hexagonal architecture), with deterministic edges: code produces what is sent to outside services wherever possible.

*Why this way*

The rest of the system doesn't care which tool is used. The TypeScript Stitch script uses Google's official SDK and sends exactly the checked message. For Figma, the AI only carries chunks a script compiled from a checked layout file.

*Alternatives*

- **A Python script for Stitch:** no official Python SDK; would need an unofficial client
- **An agent calls Stitch's MCP:** the AI could change the message; harder to count and resume
- **The agent draws Figma frames freely:** fragile layouts, many more calls, no real components
- **Stitch, then Figma's web-to-layers tool:** tested in week 1 as an alternative Figma route; Stitch's own Figma export isn't available to code

*Trade-offs*

Two runtimes (Python and Node.js). Two code paths to maintain. The Figma path still uses much more Claude usage than Stitch.

*Failure modes → defence*

- Stitch quota runs out → budget check before each screen
- Crash while waiting → job IDs saved in `job.json` first; resume, don't restart
- Figma frame half-built → one idempotency key per chunk; resume from the next chunk
- Figma read limit (200 a day) → read back through the write tool
- Wrong Figma file → guard hook checks the file key
- Figma path not good enough → the gate in 6.10 decides before more is built on it

*How to test*

Contract tests: the same screen message through both adapters must return valid screen facts. Simulate quota and rate-limit errors.

*Learn next*

`Adapter pattern` `Hexagonal architecture` `MCP` `API rate limits` `Figma auto layout` 5.9

### Screen facts and screen checker

Steps: S3–S6, F4–F6

Read each screen's code or layers into one format, then check it exactly.

*Concept*

Normalise, then compare. Structural checks (what is there) are separated from perceptual checks (how it looks).

*Why this way*

Vision models miss small labels and sometimes see things that aren't there. Code reading HTML or layers is exact.

*Alternatives*

- **Vision only:** unreliable for presence checks
- **A person checks every screen:** slow; people review the final result instead

*Trade-offs*

A parser per tool; generated HTML structure varies.

*Failure modes → defence*

- Field with unusual markup missed → planted-defect tests
- Colours almost the same, or arbitrary values in generated HTML → tolerance bands (for example ΔE ≤ 2, ± 2 px)
- Poor contrast or tiny buttons → accessibility rules on tokens and facts

*How to test*

About 30 screens with planted defects; measure how many defects are caught (recall) and how many alarms are false (precision).

*Learn next*

`HTML / DOM parsing` `Design tokens` `Precision and recall` `Multimodal evaluation` 5.10

### Feedback loop and full UI

Steps: S8–S11, F1–F9

Feedback becomes decisions; messages are rebuilt from them; approved samples guide every other screen.

*Concept*

Single source of truth (the decisions log), rebuilt declaratively, plus reference-based generation.

*Why this way*

Patching a prompt round after round piles up contradictions. Text alone drifts between screens; approved samples hold the style.

*Alternatives*

- **Patch the prompt each round:** contradictions after a few rounds
- **Regenerate everything each round:** loses good parts; uses quota

*Trade-offs*

Each rebuild is an agent run. The decisions log must be read correctly.

*Failure modes → defence*

- Comment misunderstood → user confirms the labels
- Screens drift → design-system record (tokens + components) with tolerance bands
- Samples don't show tables, pop-ups or empty states → new components are added to the design-system record as they appear
- An earlier decision lost → rebuild always reads the whole log

*How to test*

A 3-round feedback scenario: every comment applied, and no earlier decision undone.

*Learn next*

`Event sourcing` `Single source of truth` `Design systems` `Iterative refinement` 5.11

### Review page

Component: mvp-review

One static page where the user reads everything with its sources.

*Concept*

Static generation with safe output encoding.

*Why this way*

Long records are hard to read in chat. One page shows requirement, stories, screens and coverage together.

*Alternatives*

- **Review in chat:** hard to read and compare
- **A web app:** a server to run; that's v2

*Trade-offs*

Read-only: comments go in `feedback-rN.md` or chat.

*Failure modes → defence*

- Script hidden in document or export text → escape everything; block scripts; never show live HTML
- Out of date → rebuilt on every state change

*How to test*

Documents containing script and HTML test strings; nothing must run.

*Learn next*

`Output encoding` `Content Security Policy` `XSS` 5.12

### Guard hook and safety

Matrix: 3.4 · Hooks: 4.8

Every tool call is checked against what that part is allowed to do.

*Concept*

Defence in depth with least privilege, enforced at one policy point.

*Why this way*

Agents get every tool by default. Instructions like "don't do X" can be overridden by injected text; a hook can't be talked out of its rules.

*Alternatives*

- **Instructions only:** can be overridden by injected text
- **Detect attacks only:** misses new kinds of attack

*Trade-offs*

Legitimate actions can be blocked; allow lists need maintenance.

*Failure modes → defence*

- Hook bug allows too much → a test for every rule
- Hook crashes → in Claude Code a crashing hook lets the action through, so the guard wraps all its logic and returns "deny" on any error; tested by forcing a crash
- An agent starts another agent to escape its limits → the tool to start agents is in no agent's list, and the guard denies it
- Paths written differently on Windows → paths normalised before checking

*How to test*

Red-team documents that try to run commands, fetch the web, write outside the project, or touch another Figma file. Every attempt must be blocked.

*Learn next*

`OWASP Top 10 for LLM apps` `Prompt injection` `Least privilege` `Defence in depth` 5.13

### Langfuse tracing

Structure: 4.9

See what every agent and script did, how long it took and where it failed.

*Concept*

Observability with traces and spans, plus data minimisation.

*Why this way*

AI systems fail quietly: a weak question, a dropped field, a slow tool. Traces show exactly where, and which prompt version caused it.

*Alternatives*

- **Local log file only:** hard to search and compare across projects
- **Log full content:** privacy risk

*Trade-offs*

Another service to run. Masking can hide details you'd want when debugging.

*Failure modes → defence*

- Langfuse unreachable → events kept in `run-log.jsonl` and sent later; the flow never waits for it
- A secret slips into an event → masking tests

*How to test*

One project end to end: every step has a span. No key or document text appears in any event.

*Learn next*

`LLM observability` `OpenTelemetry` `Traces and spans` `Data minimisation` 5.14

### Evaluation and testing

Cards: 4.7

Test each agent as it's built, the whole flow after, and measure quality on a fixed set of documents.

*Concept*

Eval-driven development: every prompt change is measured against a fixed dataset before it's used.

*Why this way*

AI output varies between runs, and a change that fixes one case can break three others. Only measurement shows the truth.

*Alternatives*

- **Manual spot checks:** no trend, easy to fool yourself
- **One run per document:** results are mostly noise

*Trade-offs*

Time to build the dataset and labels; an approved API budget used only for repeated evaluation runs. To keep the labelling workload realistic, the four gating judges are calibrated first.

*Failure modes → defence*

- Prompts tuned to the test documents only → keep a hold-out set nobody tunes on
- Judges drift → recheck calibration when a model changes

*How to test*

This is the testing: about 20 documents, 3 runs each, results per step and per design tool, plus failure tests.

*Learn next*

`Eval datasets` `Golden sets` `Regression testing for prompts` `Hold-out sets` `pass@k` PART 5 · 5.15

## Learning path

The order to learn the concepts above, so each builds on the last.

| Step | Topics | Used in |
|---|---|---|
| 1 | Agent loop, tool calling, Claude Code sub-agents, hooks, skills | Everything |
| 2 | Context engineering, structured output, JSON Schema | 4.2, 5.2 |
| 3 | State machines, idempotency, orchestrator–worker pattern | 5.1 |
| 4 | Grounding and citations, critic patterns, hallucination control | 5.4 |
| 5 | Requirements elicitation, BDD, traceability | 5.5, 5.6 |
| 6 | Meta-prompting, prompt templates, agent skills | 5.7 |
| 7 | MCP, adapter pattern, rate limits | 5.8 |
| 8 | HTML parsing, design tokens, multimodal evaluation | 5.9, 5.10 |
| 9 | Prompt injection, least privilege, output encoding | 5.11, 5.12 |
| 10 | LLM observability, OpenTelemetry | 5.13 |
| 11 | LLM-as-judge, calibration, eval datasets, regression testing | 5.2, 5.14 |

*Concept and why · Part 5*

**Why write down alternatives**

A design without its rejected options looks arbitrary. Writing "we considered X and didn't choose it because Y" stops the same debate coming back, and teaches the reasoning.

**Why write down failure modes before building**

Each failure mode with its defence becomes a test. Problems found on paper are the cheapest to fix.

**Reuse it when**

You design any system: for each part, write the concept, why, alternatives, trade-offs, failures and tests.
