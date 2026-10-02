PART 2

## Low-level flow

Every step of the six stages: who does it, what it reads, what it writes, which state it leaves the project in, and what happens when it fails. Numbers such as timeouts and retry counts are starting values to tune during testing.

| Actor | Meaning |
|---|---|
| ORCH | The `/mvp` command (orchestrator). The only actor that talks to the user |
| SCRIPT | Plugin code: state script, reader, rules checks, adapters, file writers. No AI decisions |
| AGENT | A sub-agent doing AI work in a fresh context |
| AI-CHECK | A separate checker agent judging meaning, in a fresh context |
| USER | The person running the project |

PART 2 · 2.1

## IDs and file rules

Every item gets a stable ID so it can be linked, checked, commented on and traced. Files are never overwritten; each change makes a new version.

### ID scheme

- `DOC-3.2` document section
- `REQ-12` requirement item
- `GAP-4` gap found by the critic
- `Q-17` question · `ANSWER-17` its answer
- `JRN-2` journey · `STORY-8` story · `CRIT-8.3` criterion
- `SCR-apply-leave` screen (safe slug)
- `DEC-5` design decision · `APR-3` approval

### File rules

- Name pattern: `<record>.v<N>.json`, plus a `.md` copy for people
- **Every** file is versioned, including ones people edit: `questions-b3.md`, `feedback-r2.md`; logs hash each line
- `state.json` points to the current version of each record
- Every file write records a SHA-256 hash in `state.json`
- Safe writes: write to a temp file, then rename
- One session per project: `.agent-mvp/lock` with session ID and heartbeat
- Slugs: lowercase letters, digits and hyphens only, max 60 characters
- No path may leave the project folder; paths normalised (Windows `\`, case, short names, links)
- Text files UTF-8; line endings handled either way; all times UTC
- `.agent-mvp/` is added to `.gitignore` on the first run

### Stable IDs and citations

- An agent writing a new version gets the previous one and must keep existing IDs; new items get new IDs; removed items are marked `removed`, never reused
- A rules check confirms no ID changed meaning between versions
- Quotes carry the exact text **and** character positions in the section
- Tables are cited by cell: `DOC-3.2/T1/R4` (section, table, row)

*Full folder tree (each agent may write only its marked paths)*

```
project/
  .agent-mvp/
    state.json  lock  run-log.jsonl  queue.json        mvp-state only
  01-document/  original.v1.*  index.vN.json  sections/  images/  images.vN.json
  02-questions/ questions.vN.json  questions-bN.html  questions-bN.md
                answers.vN.json  answer-map-bN.json
  03-requirement/ requirement.vN.json(.md)  gaps.vN.json      requirement-agent, critic-agent
  04-stories/   storyset.vN.json(.md)  screen-list.vN.json     ba-agent
  05-review/    review-vN.html  feedback-rN.md  routing-rN.json  approvals.jsonl
  06-design/    brief.vN.json  style-message.vN.md  screens/SCR-*.vN.md
                samples.json  decisions.jsonl                   design-prompt-agent
  07-samples/   round-N/SCR-*/  (image, export, facts, layout, job.json)
  08-design-system/ tokens.vN.json  components.vN.json
  09-full-ui/   JRN-*/SCR-*/  coverage.vN.json
  issues/       <record>-<rubric>.vN.json                     ai-checker
  package/                                                     mvp-package
```

Shared memory across projects lives outside the project folder, in the team's library (2.12).

PART 2 · 2.2

## State machine

The state script owns this. An agent can never change the state; it only returns a result. The orchestrator asks the script to move, and `mvp-state advance` **checks its own conditions** before it moves: the check-result files for the current record versions exist and passed, their hashes match, and an approval record exists wherever the move needs one. If any condition fails, the move is refused, whatever the orchestrator believes.

```mermaid
stateDiagram-v2
  [*] --> uploaded
  uploaded --> reading
  reading --> requirement_drafting : sections pass checks
  reading --> failed_input : unreadable file
  requirement_drafting --> critic_review : requirement passes checks
  critic_review --> needs_input_req : questions open
  needs_input_req --> requirement_drafting : answers read
  critic_review --> stories_drafting : stop rule met
  stories_drafting --> awaiting_requirement_approval : stories pass checks
  awaiting_requirement_approval --> requirement_drafting : requirement change
  awaiting_requirement_approval --> stories_drafting : story or screen change
  awaiting_requirement_approval --> design_setup : approved
  design_setup --> needs_input_design : design questions open
  needs_input_design --> design_setup : answers read
  design_setup --> awaiting_send_ok : messages pass checks
  awaiting_send_ok --> samples_generating : user ok
  samples_generating --> awaiting_sample_feedback : samples checked
  awaiting_sample_feedback --> design_setup : feedback
  awaiting_sample_feedback --> requirement_drafting : requirement change, samples marked stale
  awaiting_sample_feedback --> full_generating : Go (approval recorded)
  full_generating --> paused_budget : budget reached
  paused_budget --> full_generating : user continues
  full_generating --> awaiting_final_approval : all screens checked
  awaiting_final_approval --> full_generating : screen changes
  awaiting_final_approval --> done : approved
  done --> [*]
  note right of uploaded : Any waiting state can go to cancelled (/mvp:cancel). /mvp:reopen moves back to an earlier stage and marks later records stale
```

| State | What runs | Waiting for | Leaves to |
|---|---|---|---|
| uploaded | File checks, project folder | — | reading |
| reading | Reader script, rules + AI check, injection scan | — | requirement_drafting, failed_input |
| requirement_drafting | Requirement agent, rules + AI check | — | critic_review |
| critic_review | Critic agent, question builder | — | needs_input_req, stories_drafting |
| needs_input_req | Nothing | User answers in `questions-bN.md`, then confirms the answer map | requirement_drafting |
| stories_drafting | BA agent, rules + AI check, review page | — | awaiting_requirement_approval |
| awaiting_requirement_approval | Nothing | Comments or `/mvp:approve` | requirement_drafting, stories_drafting, design_setup |
| design_setup | Tool choice, Design Prompt agent, rules + AI check | — | needs_input_design, awaiting_send_ok |
| needs_input_design | Nothing | User answers | design_setup |
| awaiting_send_ok | Outgoing scan done | User OK on the first outgoing message | samples_generating |
| samples_generating | Adapter, screen facts, screen check, fix loop | — | awaiting_sample_feedback |
| awaiting_sample_feedback | Nothing | Feedback or `/mvp:go` | design_setup, requirement_drafting, full_generating |
| full_generating | Adapter per journey, checks, coverage | — | awaiting_final_approval, paused_budget |
| paused_budget | Nothing | User decision on budget (`/mvp:continue`) | full_generating |
| awaiting_final_approval | Nothing | Screen comments or approval | full_generating, done |
| done | Package written | — | — |
| failed_input | Nothing | A new document | — |
| cancelled | Nothing | — | — (files kept until `/mvp:purge`) |

PART 2 · 2.3

## Stage 1 · Read

| Step | Actor | Does | Reads | Writes |
|---|---|---|---|---|
| R1 | ORCH | User runs `/mvp:start <file>`. Check type (PDF, DOCX, MD) and size (start: ≤ 50 MB, ≤ 300 pages). Create project folder | File path | `state.json` = uploaded |
| R2 | SCRIPT | Connection check: Python + packages, Langfuse keys. Stitch and Figma are checked later, when the user picks one | Environment, keychain | `run-log.jsonl` |
| R3 | SCRIPT | Copy original, hash it | File | `01-document/original.v1.*` |
| R4 | SCRIPT | Convert to Markdown (DOCX: mammoth/pandoc; PDF: page by page, with poppler). Remove page headers and footers; join hyphenated words; split by heading; give IDs; keep tables with cell addresses; extract images; detect the document's language | Original | `sections/DOC-*.md`, `images/`, `index.v1.json` |
| R4b | SCRIPT | Make a normalised copy of each section for quote matching: Unicode NFKC, straight quotes, single spaces, no soft hyphens | Sections | `sections/DOC-*.norm.txt` |
| R5 | SCRIPT | Rules check: no empty sections, unique IDs, table count and page count match the original | Index, sections | Check result |
| R6 | ORCH → AI-CHECK, then SCRIPT | The orchestrator runs the checker to compare 3 sampled pages with the original and describe each image; a script turns the checker's output into the record | Original pages, sections, images | `images.v1.json` (written by script) |
| R7 | SCRIPT, then ORCH → AI-CHECK | Injection scan: a script runs the pattern list; the orchestrator runs the injection rubric on suspicious text; the script marks sections `untrusted: true` | Sections | Index flags, warning to user |
| R8 | SCRIPT | Advance state | Check results | `state.json` = requirement_drafting |

**Fails:** wrong type or too large → tell the user, stay in uploaded. Scanned PDF with no text → failed_input, ask for another format. Rules check fails → retry conversion once with the other converter, then failed_input.

PART 2 · 2.4

## Stage 2 · Understand

| Step | Actor | Does | Reads | Writes |
|---|---|---|---|---|
| U1 | ORCH | Start Requirement agent with its instructions and the section index; it may only read `01-document/` and `answers` | Index | — |
| U2 | AGENT | Write each item: type, text, quote, source (section, or table cell), character positions, status (*stated* / *inferred* / *answered* / *convention*), confidence (high / medium / low) with a one-line why, and a draft question for inferred items. On reruns it gets the previous version and keeps existing IDs | Sections, answers, previous version, team library | `03-requirement/requirement.vN.json` |
| U3 | SCRIPT | Rules: schema valid; IDs unique and stable versus the previous version; each quote found in the normalised section text at its positions; table cells exist; inferred items have a draft question; convention items name the standard feature | Requirement, normalised sections | Check result |
| U3b | SCRIPT | If a quote isn't found: find the closest real text in that section and return it to the agent as a hint (not a free retry) | Normalised sections | Hint for the agent |
| U4 | ORCH → AI-CHECK | Rubrics *support* and *clarity*. Vague wording that is in the client's own text is not sent back to the agent; it becomes a question (2.9) | Requirement, cited sections | Issues file |
| U5 | AGENT | Critic, fresh context, fixed gap list: every user type, error cases, permissions, data life cycle, limits, vague words, languages. Each gap gets an importance: **blocking** (design would be wrong without it), **important** (a screen or rule would change), **minor** (wording or detail) | Requirement, sections | `gaps.vN.json` |
| U5b | ORCH → AI-CHECK | Rubric *gap-value*: is each gap real, specific and not already answered? | Gaps, answers | Issues file |
| U6 | SCRIPT, then ORCH → AI-CHECK | Question builder: the script collects draft questions from inferred items, gaps and convention items, removes exact duplicates and assigns `Q-` IDs; the duplicates rubric removes same-meaning ones and ones the document answers; group by topic; blocking first. All convention items go into one question ("we assumed these standard features; untick any you don't want") | Requirement, gaps, answers | `02-questions/questions.vN.json` |
| U7 | SCRIPT | Write batch N as `questions-bN.html` and `questions-bN.md`. Each question sits under a `### Q-n` heading; the script stores a hash of each question block | Questions | Two files; state = needs_input_req |
| U8 | USER | Types answers under each question (or in chat), runs `/mvp` to say "ready" | Question files | `questions-bN.md` |
| U9 | SCRIPT | Extract text: everything from `Answer:` to the next heading belongs to that question; warn if a question's text was edited (hash changed); chat answers are saved into the file first | `questions-bN.md` | Raw answers |
| U9b | ORCH → AI-CHECK | Rubric *answer-map*: link each answer to the questions it answers (handles "same as Q3" and one answer covering several), and flag answers that contradict the document or change scope | Raw answers, questions, requirement | Answer map |
| U9c | USER | Confirms the answer map in one step (shown in chat and in the batch file); corrects anything wrong | Answer map | `answers.vN.json`, `answer-map-bN.json` |
| U10 | ORCH | Rerun the Requirement agent with the confirmed answers; repeat until the stop rule is met. Answering a question again creates a new answer version that replaces the old one | All above | requirement.v(N+1) |

*Decision table · when to stop asking*

| Blocking or important gaps open? | Batches since last check-in | User's choice at check-in | Result |
|---|---|---|---|
| None (only minor or none) | — | — | **Stop**; minor gaps listed in the review as assumptions |
| Yes | Fewer than 4 | — | Ask the next batch |
| Yes | 4 | Continue | Ask the next batch; counter resets |
| Yes | 4 | Use suggestions | **Stop**; the rest use suggestions, marked as assumptions with low confidence |
| — | Any | User says "use your suggestions" at any time | **Stop** as above |

Batches have no fixed size, but each batch covers one topic and blocking questions always come first. The check-in after every 4 batches shows how many questions remain and how many are blocking, so the user can decide with the facts in front of them.

PART 2 · 2.5

## Stage 3 · Define

| Step | Actor | Does | Reads | Writes |
|---|---|---|---|---|
| D1 | AGENT | BA agent: roles, journeys, stories, criteria (Given/When/Then incl. errors), screen list with states and links; links criterion → screen | Requirement | `04-stories/storyset.vN.json`, `screen-list.vN.json` |
| D2 | SCRIPT | Rules: schema; IDs stable versus the previous version; every in-scope requirement has ≥ 1 story; every story has ≥ 1 criterion; every criterion points to a screen; every screen has ≥ 1 story and its states; every link points to a real screen; every screen has realistic sample data | Storyset, screen list, requirement | Check result |
| D3 | ORCH → AI-CHECK | Rubrics *testable* (per criterion) and *scope* (per story) | Storyset, requirement | Issues file |
| D4 | SCRIPT | Build `review-vN.html` (all text escaped): requirement, stories, screen list, sources, assumptions, **confidence per item** (low-confidence items first), and **what changed since the last version** | All records | Review page; state = awaiting_requirement_approval |
| D5 | USER | Writes comments by ID in `feedback-rN.md` or chat (saved into the file), or runs `/mvp:approve`; may approve parts and comment on others | Review page | `feedback-rN.md` |
| D6 | SCRIPT, then ORCH → AI-CHECK | Script reads IDs; the *label* rubric sorts each comment; route by the table below; comments marked processed | Feedback | `routing-rN.json` |
| D7 | SCRIPT | On approve: record approver, time, stage and the hash of every approved file. A later change marks this approval stale | Current versions | `approvals.jsonl`; state = design_setup |

*Decision table · where a comment goes*

| Comment is on | Kind (AI decides, user can correct) | Goes to | Redone |
|---|---|---|---|
| `REQ-*` | Change of meaning | Requirement agent | That item, then only the stories linked to it |
| `REQ-*` | Wording only | Requirement agent | That item's text |
| `STORY-*` or `CRIT-*` | Any | BA agent | Those stories and their screen links |
| `SCR-*` in screen list | Add, remove, merge, change states | BA agent | Screen list and affected criterion links |
| No ID | Unclear | ORCH asks the user which item it is about | Nothing until clarified |

PART 2 · 2.6

## Stage 4 · Prepare design

| Step | Actor | Does | Reads | Writes |
|---|---|---|---|---|
| P1 | ORCH | Ask: Stitch or Figma? For Figma, also ask for the target file link. Test that connection: Stitch through `mvp-stitch test` (lists projects); Figma through the frame builder (account and seat check, one tiny write in the target file). Save the tool and Figma file key in `state.json`. Changing tool later goes back here and marks samples stale | Keychain, MCP | `state.json`: tool, file key |
| P2 | AGENT | Design Prompt agent loads the design skill; marks each checklist item answered (with source), taken from the team library, or missing. The checklist asks early: **web, mobile or both, and screen sizes**; output language and right-to-left; accessibility needs | Storyset, screen list, answers, skill, team library | `06-design/brief.vN.json` |
| P3 | SCRIPT | Missing items go through the question system (same as U6–U9) | Brief | Questions; state = needs_input_design |
| P4 | AGENT | Write style message (with colour, font and spacing values); write one screen message per screen with criterion IDs tagged inline and realistic sample data in the output language; pick samples (main screen + one form) | Brief, answers, screen list | `style-message.vN.md`, `screens/SCR-*.vN.md`, `samples.json` |
| P5 | SCRIPT | Rules: every criterion of each screen appears by ID in its message; style + longest screen message under the tool's limit; slugs safe; **accessibility**: text and background colours meet contrast (WCAG AA), touch targets at least 44 px on mobile; right-to-left set when the language needs it | Messages, screen list | Check result |
| P6 | ORCH → AI-CHECK | Rubric *contradiction*: conflicts between style and screen messages; anything unclear for a designer | Messages | Issues file |
| P7 | SCRIPT, then ORCH → AI-CHECK | Outgoing scan: secret and personal-data patterns (script), then confidential content (rubric). Remove or ask | Messages | Scan result |
| P8 | ORCH | Show the first outgoing message; wait for OK | First message | state = awaiting_send_ok → samples_generating |

PART 2 · 2.7

## Stage 5 · Samples and feedback

| Step | Actor | Does | Reads | Writes |
|---|---|---|---|---|
| S1 | SCRIPT | For each sample, idempotency key = project + screen + message version. If a finished result exists for that key, skip; if a `job.json` exists without a result, resume that job instead of starting a new one | `state.json`, `job.json` | — |
| S2a | SCRIPT (TypeScript) | **Stitch:** `mvp-stitch generate` uses Google's official SDK. It writes the project and screen IDs to `job.json` **before** waiting, waits for the result (SDK default about 5 minutes, then checks again), fetches image + HTML, counts the generation against the quota | Messages, keychain | `07-samples/round-N/SCR-*/` |
| S2b-1 | AGENT | **Figma:** the frame builder writes a **layout file** for the screen: frames, auto layout, components, text, sizes, all from the style message values (or design-system tokens after "Go"). Checked against its schema | Messages, design-system record | `layout.json` |
| S2b-2 | SCRIPT | `mvp-figma-compile` turns the layout file into small Figma code chunks (each under 20 KB), one per section, each with its own idempotency key; uses components and variables where they exist | Layout file | Code chunks |
| S2b-3 | AGENT | The frame builder sends each chunk to Figma's write tool exactly as compiled, saves the returned node IDs to `job.json` after each chunk, and reads the result back **through the write tool** (no daily limit), not through read tools | Chunks | Frame in Figma; layer tree file |
| S3 | SCRIPT | Screen facts: parse HTML (Stitch) or layer tree (Figma) into fields, labels, buttons, texts, colours, fonts | Export | `facts.json` |
| S4 | SCRIPT | Rules: every item in the screen message present in facts; colours, fonts and spacing within tolerance of the style message; contrast check | Facts, messages | Check result |
| S5 | ORCH → AI-CHECK | Rubric *look* (vision): layout clear, nothing broken or overlapping | Image | Issues file |
| S6 | ADAPTER (script or frame builder) | Fix loop: missing or wrong → edit that screen with a fix note, max 2 times, then flag in the review | Issues | New screen version |
| S7 | SCRIPT | Review page with samples next to stories, coverage and the differences from the previous round | All | state = awaiting_sample_feedback |
| S8 | ORCH → AI-CHECK, then USER | Rubric *label*: style (all screens), one screen, or requirement change. Show the labels; user corrects if wrong | `feedback-rN.md` | `routing-rN.json` |
| S9 | SCRIPT | Append each change to the decisions log (one line, one hash) | Routing | `decisions.jsonl` |
| S10 | AGENT | Rebuild the style message from the brief + the whole decisions log; update affected screen messages; show the difference | Brief, decisions | New message versions → back to S1, round N+1 |
| S11 | SCRIPT | On `/mvp:go`: record the approval; freeze the style message version; create the **design-system record** from the approved samples: tokens (colours, fonts, spacing, navigation) and the components seen so far | Approved samples | `08-design-system/tokens.v1.json`, `components.v1.json`; state = full_generating |

**Round limit:** default 3 sample rounds. After that the review page suggests a designer review; the user can still continue. Samples use the style message's values directly; tokens only exist after "Go".

PART 2 · 2.8

## Stage 6 · Full UI and approval

| Step | Actor | Does | Reads | Writes |
|---|---|---|---|---|
| F1 | SCRIPT | Order journeys; within a journey, follow screen links | Screen list | Build queue in `state.json` |
| F2 | SCRIPT | Budget check before each screen: project screen budget, remaining Stitch quota, Figma read-call limits, Claude usage seen so far. Over → paused_budget | Usage counters | — |
| F3 | ADAPTER | Generate with the frozen messages and the design-system record; Stitch uses an approved sample as reference if the SDK accepts one (week-1 check); Figma reuses the components | Messages, design system, sample | `09-full-ui/JRN-*/SCR-*/` |
| F4 | SCRIPT | Screen facts + rules (S3–S4) plus token match within tolerance bands (for example colour difference ΔE ≤ 2, spacing ± 2 px). New components seen are added to `components.vN.json` | Facts, design system | Check result |
| F5 | ORCH → AI-CHECK | Rubric *look* (S5) | Image | Issues file |
| F6 | ADAPTER | Fix loop (S6) | Issues | New version or flag |
| F7 | SCRIPT | Coverage report: criteria visible / total, with gaps listed | All facts, storyset | `coverage.vN.json` |
| F8 | USER | Comments on single screens (→ edit just those, back to F4) or `/mvp:approve`; the approval is recorded with file hashes | Review page | Feedback or approval |
| F9 | SCRIPT | Write the package: requirement, stories, screen list, messages, decisions, design system, design links, coverage, approvals. Offer to save the design system and glossary to the team library | All | `package/`; state = done |

PART 2 · 2.9

## Failures, retries and errors

This is the single place that defines what happens on failure. Failures are routed by **type**: retrying only helps when the agent made a fixable mistake. Retrying when the source itself is unclear would push the agent to invent.

*Routing by failure type*

| Failure type | Route | Limit | Then |
|---|---|---|---|
| Format: invalid JSON, missing field, wrong schema | Same agent with the exact errors | 2 retries | Same agent with more reasoning effort, 1 try; then stop and show the user |
| Quote not found | Script gives the closest real text in that section as a hint | 1 retry | Item becomes *inferred* with a question |
| Source text is vague or contradictory (the client's own words) | No retry. A question to the user | — | Next batch |
| Agent's own wording is vague, or a rule is missed | Same agent with the issues | 2 retries | More reasoning effort, 1 try; then a warning in the review |
| Judge not stable (passes and fails on reruns of the same item) | No retry. Marked for a person in the review | Judge rerun up to 3 times; 2 of 3 decides | Shown as "needs a person" |
| Instructions problem (same failure on many items or projects) | No retry. Logged for the team to fix the agent file | — | Seen in Langfuse; fixed through the change process (6.6) |

"More reasoning effort" replaces "a stronger model" because three agents already start on the strongest model. Each project also has a cap on total retries (start: 30); reaching it pauses the project and shows the user why.

*Errors and what the user sees*

| What fails | Detected by | Action | User sees |
|---|---|---|---|
| Rules check fails | SCRIPT | Routed by type (above) | Nothing, unless it still fails: "REQ-12 quote not found in DOC-3.2" |
| AI check finds issues | AI-CHECK | Routed by type (above) | Remaining issues shown in the review as warnings |
| Agent returns no file or invalid JSON | SCRIPT | Format route | Error message after the format route ends |
| Guard hook itself errors | Hook | Returns "deny" (fail closed) | "Action blocked by safety check" with the reason |
| Another session holds the project lock | mvp-state | Refuse to start; lock expires if its heartbeat stops for 10 minutes | "Project is open in another session" |
| Crash while waiting for Stitch or building in Figma | Next `/mvp` | Read `job.json`; resume the same job or the next Figma section; never start a duplicate | "Resuming SCR-… from where it stopped" |
| Stitch or Figma error, rate limit or timeout | Adapter | Wait 5 s, 20 s, 60 s; 3 tries | "Stitch is not responding; try again later" with the screen name |
| Stitch result not ready after the SDK wait plus one more check (about 10 min in total) | Adapter | Keep the job ID in `job.json`; mark the screen as pending; continue with the next; check pending jobs again on the next run | Pending screens listed |
| Figma read-call limit reached | Adapter | Should not happen (read back goes through the write tool); if it does, pause Figma work until the next day | "Figma daily limit reached; continuing tomorrow" |
| Claude usage limit reached | ORCH | Save state; stop | "Usage limit reached. Run /mvp again later to continue from SCR-…" |
| Claude Code closed mid-step | Next `/mvp` | The unfinished step is rerun; idempotency keys stop duplicates | "Resuming at …" |
| `state.json` damaged | SCRIPT on load | Rebuild from the latest valid record files and their hashes | "State rebuilt from files" |
| Hidden instruction found | Injection scan | Section marked untrusted; never followed | Warning with the section ID |
| Secret or personal data in an outgoing message | Outgoing scan | Block send; ask to remove or confirm | The flagged text, masked |

PART 2 · 2.10

## Main records, field by field

| Record | Key fields |
|---|---|
| state | project_id, stage, state, tool, figma_file_key, record pointers[ name, version, sha256 ], approvals[], build queue, usage counters, retry count, schema version |
| lock | session_id, started, heartbeat |
| index | language, sections[ id, heading, file, norm_file, pages, chars, tables[ id, rows ], untrusted ], images[ file, page ] |
| images | items[ file, page, description ] (built by script from checker output) |
| requirement | version, items[ id, type (goal, user, scope_in, scope_out, rule, nfr), text, quote, source (section or table cell), start, end, status (stated, inferred, answered, convention, removed), confidence, why, draft_question ] |
| gaps | items[ id, gap_type, importance (blocking, important, minor), about, why_it_matters, draft_question ] |
| questions | items[ id, batch, topic, text, why, options[], from (REQ / GAP / brief / convention), importance, block_hash, status (open, answered, suggest) ] |
| answers | items[ id, question_ids[], text, suggest, supersedes, time ] |
| answer-map | batch, links[ answer_id, question_ids[] ], conflicts[], scope_changes[], confirmed_by, time |
| storyset | roles[], journeys[ id, role, steps[] ], stories[ id, journey, as_a, i_want, so_that, req_ids[], confidence, criteria[ id, given, when, then, screen_id ] ] |
| screen-list | platform (web, mobile, both), sizes[], screens[ id, name, purpose, role, states[], links_to[], story_ids[], sample_data ] |
| routing | round, comments[ id, item_id, label, route, processed ] |
| brief | tool, language, rtl, accessibility, checklist[ item, status, value, source ], samples[] |
| style-message / screen-message | version, text, criterion_ids[] (screen only), built_from (brief version, decision IDs) |
| layout (Figma) | screen_id, frames[ id, layout, children[] ], components_used[], text[], sizes |
| job | screen_id, tool, idempotency key, stitch_project_id, stitch_screen_id, figma_node_ids[], chunks_done[], status |
| facts | screen_id, version, fields[ label, type ], buttons[], texts[], colours[], fonts[], spacing[], nav[] |
| tokens / components | colours[], fonts[], spacing[], radius[], nav; components[ name, used_on[], figma_component_id ] |
| issues | record, version, rubric, items[ id, issue, severity ], judge_runs |
| decisions | id, round, from_comment, scope (style / screen), screen_id, change, time, line hash |
| approvals | id, stage (requirement, send, go, final), by, time, files[ path, version, sha256 ], stale |
| coverage | criteria_total, criteria_visible, gaps[ crit_id, screen_id, reason ] |

Full JSON schemas are written in week 1 and agreed by all three owners. Every record carries `version`, `schema_version` and `created_by` (which agent or script, with its version). All times are UTC.

PART 2 · 2.11

## Project commands

| Command | Does |
|---|---|
| /mvp:start <file> | New project from one document |
| /mvp | Continue: rebuilds its view from `mvp-state status`, then runs the next step. Also means "my answers are ready" |
| /mvp:status | Where the project is, what it waits for, usage so far |
| /mvp:approve [ids] | Approve the current stage, or only some items |
| /mvp:go | Approve the samples and build the full UI |
| /mvp:continue | Continue after a budget pause |
| /mvp:reopen <stage> | Go back to an earlier stage; later records and approvals marked stale |
| /mvp:cancel | Stop the project; files kept |
| /mvp:purge | Delete the project's files after a confirmation step |

Week 1 checks whether plugin commands appear as `/mvp` or need a longer name such as `/mvp:mvp`; the names above may change to fit.

PART 2 · 2.12

## Team library: memory across projects

### What it keeps

- Approved design systems (tokens and components) per client
- Glossaries of client terms
- Past answers to common questions, offered as defaults
- Lists of standard ("convention") features by app type

### How it is used

- Saved only when the user agrees at the end of a project (F9)
- Agents read it; only a script writes it
- Defaults from the library are shown as suggestions, never applied silently
- Stored outside project folders, per client, so one client's data never reaches another's project

*Concept and why · Part 2*

**State machine owned by code**

Agents return results; only the script moves the state. That makes every path testable and stops an agent from "deciding" to skip an approval.

**Immutable, versioned files**

Never overwrite; always add a new version. You can always see what changed, approvals point to exact versions by hash, and a damaged state can be rebuilt from files.

**Idempotency keys**

A step identified by project + item + version can be rerun safely: if the result exists, it is skipped. This is what makes resume possible without duplicate screens or double usage.

**Decision tables**

Writing "if this and that, then do this" as a table shows every case, including the ones nobody thought of. Each row becomes a test.

**Retries with backoff and limits**

Retry quickly first, then wait longer, then stop. Without a limit, a failing step loops forever and burns usage.

**Fail safe**

When unsure (no ID on a comment, secret in a message, budget reached), stop and ask instead of guessing.

**Route failures by type**

A retry fixes an agent's mistake, but not missing information or a vague source. Sorting failures first stops the system from "fixing" a problem by inventing an answer.

**Write the job down before waiting**

Saving an outside job's ID before waiting for it is what makes a crash harmless: the next run picks up the same job instead of starting a second one.

**Learn next**

arc42 runtime view, state machines, idempotency, exponential backoff, JSON Schema, decision tables.
