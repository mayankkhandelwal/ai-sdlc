*Audit · Design-First MVP · 6 independent reviews*

# Design-First MVP Audit

Six reviewers read the [Design-First MVP Flow](https://claude.ai/artifact/YCQjS3qjU4wgEBmYdhSDnb) independently: AI expert, AI engineer, security, product and UX, legal and compliance, and QA and evaluation. Below: what they agree on, which of your fixed decisions they challenge, and what must change before building.

Facts the reviewers checked against official docs are linked in Sources. Everything else is their judgment. The legal points are risks to check with counsel, not legal advice.

*Verdict*

**Keep the flow. Change the scope and harden it before building.** All six reviewers think the requirement half (steps 3–5) is well designed: grounding, human questions, coverage checked by code and partial regeneration. The design half (steps 6–9) depends on three things nobody has tested yet: that both design tools can generate screens from a prompt, that a text master prompt keeps screens consistent, and that a vision check can confirm a screen matches its spec.

Four reviewers independently recommend shipping **Google Stitch only** in v1. The full scope as written takes about **10–12 weeks**, not 7–8. With the cuts below, 7–8 weeks is realistic.

**AI expert**

Requirements: sound. Design consistency and vision checks: unproven. Add a screen inventory.

**AI engineer**

Plugin works. Sub-agents can't ask questions; Figma can't generate from a prompt. 10–12 weeks for full scope.

**Security**

Agents inherit all tools unless restricted. Builds on the user's laptop are dangerous. Restrict tools, don't rely on detection.

**Product and UX**

The v1 user and the surface don't match. Screens arrive too late. Traceability is the edge.

**Legal and compliance**

Pro and Max are consumer plans; use Team or Enterprise for customer data. Stitch terms unverified.

**QA and evaluation**

Metrics are the right kind, but ground truth, judges and the vision check need fixing. 3 runs per document.

*Needs your decision*

## Five decisions the reviewers challenge

These change things you fixed earlier, so they are yours to decide. Each card gives the reviewers' recommendation and what happens if you keep your original choice.

Critical

### D-A · Both Stitch and Figma in v1 (M7)

Figma's MCP can create and edit frames through code (`use_figma`), but it has no "generate a screen from a prompt". So the same master prompt cannot drive both tools: for Figma, Claude would have to build every frame itself. Writing needs a Full seat, the feature is in beta, and responses are capped at 20 KB.

*Recommended*

Stitch only in v1. Figma in v1.1, as an export target or "Claude builds frames from tokens"

*If you keep both*

Add 2–3 weeks, not 1; quality will differ per tool

*Check in week 1*

Generate 3 real screens on each tool

Raised by: AI engineer (verified), AI expert, Product, QA

High

### D-B · Running on Pro and Max subscriptions (M8)

Pro and Max are consumer plans. If the user's training setting is on, Anthropic may train on their sessions, including Claude Code, and keep data up to 5 years. Team, Enterprise and API are not trained on. Customer documents should not go through consumer accounts.

*Recommended*

Pro/Max allowed for internal tests with non-confidential documents only. Team or Enterprise required for customer work

*If you keep Pro/Max for all*

Customer data may be trained on; most enterprises and DPAs will block it

*Also*

Usage limits may stop a full run; measure one project on Pro and Max

Raised by: Legal (verified), AI engineer, AI expert

High

### D-C · Readiness check that builds the existing app (M2, step 2)

Building an unknown repo runs its install and build scripts. That is someone else's code running on the user's laptop. Docker "when available" isn't safe enough, and build-and-run across unknown stacks, especially on Windows, is a project of its own.

*Recommended*

v1 reads code and theme/CSS files only, plus screenshots the user uploads. No building. Build-and-run moves to v2

*If you keep building*

Docker becomes mandatory, hardened (no network, no host mounts); add about 1–2 weeks

*Saves*

About 1–2 weeks and the biggest security risk

Raised by: Security, AI engineer, Product

Critical

### D-D · Who the v1 user is

BAs, PMs and designers review stories and screens, and they don't work in Claude Code. Developers do, but they already have v0, Lovable and Figma Make. Setup (Claude plan, Stitch key, Figma, GitHub, Docker) and about 7 human steps before the first screen will lose evaluators.

*Recommended*

Your team runs v1 for the first 5 design partners (concierge mode). The v1 user is an agency's solution lead or presales engineer

*Also*

One merged questionnaire; the review page is the only place to review; first screen within about 15 minutes

*If you keep self-serve*

Plan for a guided `/mvp:setup`, a setup video, and lower take-up

Raised by: Product

High

### D-E · The 7–8 week estimate

The full scope as written (both adapters, Docker readiness, review page with comments, the evaluation set) is about 10–12 weeks.

*Recommended*

Accept D-A and D-C to stay at 7–8 weeks, with week 8 as buffer and pilot

*If you keep full scope*

Plan for 10–12 weeks

*Week by week*

See the build order below

Raised by: AI engineer, Product

*Must fix · no decision needed*

## Changes to the design

These fix things that are wrong or missing without changing your decisions.

### How the plugin works

Critical**Sub-agents can't ask the user questions**

The question tool is removed inside sub-agents. Agents return `needs_input` with their questions; the main `/mvp` command asks the user, saves the answers as sources, and starts the agent again.

Steps 3, 6, 8 · verified High**Nothing enforces the JSON schemas**

A hook runs a bundled validator after each agent writes its file; errors go back to the agent, max 2 retries.

All steps · verified High**Plugin agents ignore their own MCP and hook settings**

Declare Stitch, Figma and GitHub in the plugin's `.mcp.json` and hooks at plugin level; limit each agent with its `tools` list.

Foundations · verified Medium**An LLM shouldn't run the state machine**

A small `mvp-state` script in the plugin's `bin/` folder handles steps, versions and approvals; the command calls it.

States · judgment Medium**v2 parts are mixed into v1**

Remove `runAgent()`, Langfuse and pgvector from v1; label them v2. In v2 the SDK's `query()` loads the same plugin folder.

Steps 3, 7, 9 · verified Medium**DOCX can't be read; PDFs read 20 pages at a time**

Bundle a DOCX converter (mammoth or pandoc) behind a script; read PDFs in page ranges; drop OCR from v1.

Step 1 · verified for PDF Medium**Stitch quotas aren't published and generation is slow**

Generate screens one after another with polling; set a screen budget per project.

Steps 7, 9 · partly verified

### AI design

Critical**A text master prompt won't keep screens consistent**

After "Go", take the tokens and components from the approved samples' exported code. Generate later screens in the same Stitch project with the approved sample as reference, or in edit/variant mode. Then check colours, fonts and navigation against the sample in code.

Steps 6, 7, 9 High**Vision check is the wrong tool for "are all fields there"**

Check fields, labels and buttons by parsing the exported HTML against the screen spec; use vision only for layout and style. Measure the checker on about 30 screens with planted defects.

Steps 7, 9 High**No screen inventory**

Add a `ScreenInventory` record: every screen, its states and the navigation map. The user approves it as part of the requirement approval in step 5, not as an extra step.

Steps 4–6 Medium**A citation existing doesn't mean it supports the item**

Require a quoted span from the source and check in code that it appears in that section. Show "inferred" items to the user as assumptions to confirm.

Step 3 Medium**Self-critique in the same context finds little**

Run a separate critic in a fresh context with a fixed list of gap types (actors, error paths, permissions, data lifecycle, vague words). It outputs issues only.

Steps 3, 6 Medium**Patching the prompt every round builds up contradictions**

Rebuild the master prompt each round from the design decisions log. Show the user how each comment was classified and the prompt diff; edit screens instead of regenerating them.

Step 8

### Product

High**Make traceability the centre of the product**

Generating screens from prompts is common; linking every screen element to an acceptance criterion and a source paragraph, with a coverage report ("38/40 criteria visible"), is not. Put that at the centre of the review page and the demo.

Review page, step 9 Medium**Fewer human steps**

Merge requirement and design questions into one questionnaire; up to 2 sample rounds; final approval optional.

Steps 3, 6, 8, 10 Medium**Add business success measures**

Time to first screen ≤ 15 minutes; BA hours saved ≥ 50%; at least 3 of 5 partners use it again; at least 1 paid pilot.

Evaluation Medium**Stories need to reach Jira**

Export stories as CSV for Jira or Azure DevOps in v1; a full integration can come later.

Step 10

*Where reviewers agree and disagree*

## Consensus and disagreements

### All or most agree

- The requirement half is well designed; keep it
- "Feedback changes the prompt, not just the picture" plus samples before the full build is the right loop
- Ship one design tool first (Stitch)
- Don't build unknown repos in v1
- Remove v2 infrastructure from v1
- LLM judges and the vision check must be calibrated against human labels
- Check Stitch's data terms in week 1

### Disagreements, resolved

- **More steps or fewer?** The AI expert adds a screen inventory approval; Product wants fewer steps. Resolved: the inventory goes inside the existing requirement approval.
- **Questions before or after the first screen?** Product wants a screen first; AI design wants questions first for quality. This is a value choice: a fast draft screen with defaults, then questions, is an option for you to try with partners.
- **Self-serve or run for partners?** This is a business choice (D-D).

*Security baseline for v1*

## Minimum before anyone uses it

### Agents and tools

- Every agent has an explicit `tools` list; agents without one get every tool, including Bash
- A hook blocks Bash, web fetch and writes outside `.agent-mvp/`
- Plugin code, not the model, writes files and makes MCP calls
- All outside content (document, repo, Figma, Stitch, text in images) is treated as data, with an injection test for each
- Screen names become safe file names; no paths outside the project

### Data and secrets

- Messages to Stitch or Figma are built only from validated fields, scanned for secrets and personal data, and the first one is shown to the user
- Stitch key stored through the plugin's sensitive setting (OS keychain)
- GitHub token read-only on one repo
- `review.html`: escape everything, strict content policy, sandboxed previews, no remote images
- `.agent-mvp/` added to `.gitignore`; logs hold metadata only; a purge command
- MCP servers pinned to exact versions, from official sources only

*Compliance*

## Before customer data, and before selling

### Before customer data in v1

- Team or Enterprise seats only
- Client contract allows AI sub-processors: Anthropic, Google, Figma
- Stitch's own terms reviewed, or Stitch off for that client
- Figma content training off (on by default for Starter and Professional)
- Personal data and secrets removed from documents
- Local transcript retention set; Claude Code's feedback upload turned off

### Before selling v2

- Anthropic commercial terms or an Enterprise agreement; Bedrock or Vertex for customer-cloud installs
- Written confirmation from Google and Figma on commercial use and resale
- India DPDP Act duties (most apply from about May 2027); GDPR if selling in the EU
- Customer terms: no copyright promise on purely AI-made output
- SOC 2 or ISO 27001 plan; published sub-processor list
- Product name without "Claude" or "Anthropic"
- A plan for Stitch being discontinued

*Evaluation, revised*

## How to prove the MVP works

| Area | Change |
|---|---|
| Dataset | About 20 documents: 12 real with a reviewed "gold" answer, 8 synthetic or tricky (empty, contradictory, injected, very long, non-English, scanned) |
| Ground truth | Two reviewers merge human and model items and mark each valid or not; report recall and precision |
| Repeat runs | 3 runs per document; report the average and the worst; hard rules must hold on all 3 |
| LLM judges | Each judge checked against about 50 human labels before it's trusted; different prompt or model from the generator |
| Design quality | Spec match by a separate checker; accessibility and contrast scan; designer rating; side-by-side with human designs |
| Feedback | Comment classifier accuracy ≥ 90% on 60 labelled comments; share of comments actually fixed |
| Regression runs | A small API budget for evaluation only, run headless with a pinned model |
| Failure tests | Kill mid-step, rate limits, usage limit mid-build, corrupted state: must resume with no duplicate screens |
| Pilot | 3–5 real users in weeks 6–8: rounds, time saved, share of requirement items approved unedited |

*Week 1*

## Check these before building

| Check | Decides |
|---|---|
| Generate 3 real screens on Stitch and on Figma through MCP | D-A: one tool or two |
| Consistency across 8 screens: master prompt alone vs. with an approved reference sample | How step 9 generates screens |
| Field check by HTML parsing vs. vision, on screens with planted defects | How steps 7 and 9 check screens |
| Sub-agent returns questions → main session asks → agent resumes, including after closing Claude Code | How questions work |
| Schema validation hook blocks and retries a bad output | Output safety |
| One full project on Pro and on Max: time and usage limits | D-B |
| The same plugin folder runs through the Agent SDK with an API key | The v2 path |
| Stitch's terms and privacy notice, from the primary source | Whether customer data may use Stitch |
| Quoted citations on 3 real documents: share that appear word for word | Grounding approach |

*Build order with the recommended cuts*

## 8 weeks, three owners

| Week | Agents | Platform | Product |
|---|---|---|---|
| 1 | Model bake-off, schemas, collect evaluation documents | Plugin skeleton, MCP connection checks, `mvp-state` script, week-1 checks | Review page wireframe |
| 2 | Requirement agent with the question round trip | PDF/DOCX reader, section index, validation hook | First-run setup check |
| 3 | BA agent, screen inventory, coverage check | Run-log hooks, resume | Review page: requirement and stories |
| 4 | Design skill, Design Prompt agent | Stitch adapter: generate, poll, export | Approval flow, diffs |
| 5 | Screen checker, feedback classifier | Sample loop, versioning | Samples next to their stories |
| 6 | Full-UI coverage and consistency checks | Journey batching, screen budget | Traceability view, handoff package, CSV export |
| 7 | Everyone: evaluation runs, injection and failure tests, code-only readiness check |  |  |
| 8 | Buffer and design-partner pilot. Figma starts after this |  |  |

*Sources the reviewers checked*

- Claude Code sub-agents: [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)
- Plugins reference: [code.claude.com/docs/en/plugins-reference](https://code.claude.com/docs/en/plugins-reference)
- Agent SDK plugins: [code.claude.com/docs/en/agent-sdk/plugins](https://code.claude.com/docs/en/agent-sdk/plugins)
- Agent SDK structured outputs: [code.claude.com/docs/en/agent-sdk/structured-outputs](https://code.claude.com/docs/en/agent-sdk/structured-outputs)
- Claude Code legal and compliance: [code.claude.com/docs/en/legal-and-compliance](https://code.claude.com/docs/en/legal-and-compliance)
- Claude Code data usage: [code.claude.com/docs/en/data-usage](https://code.claude.com/docs/en/data-usage)
- Anthropic consumer terms: [anthropic.com/legal/consumer-terms](https://www.anthropic.com/legal/consumer-terms)
- Publishing plugins: [code.claude.com/docs/en/plugins/publish](https://code.claude.com/docs/en/plugins/publish)
- Figma MCP server FAQs: [help.figma.com](https://help.figma.com/hc/en-us/articles/39252411778583-Figma-MCP-server-FAQs)
- Figma AI content training: [help.figma.com](https://help.figma.com/hc/en-us/articles/17725942479127)
- Stitch SDK: [github.com/google-labs-code/stitch-sdk](https://github.com/google-labs-code/stitch-sdk)
- Google Labs privacy notice: [labs.google/fx/privacy](https://labs.google/fx/privacy) (does not name Stitch; Stitch's own terms still to be read)
- India DPDP Rules 2025: [pib.gov.in](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)
- US Copyright Office on AI: [copyright.gov/ai](https://copyright.gov/ai/)
