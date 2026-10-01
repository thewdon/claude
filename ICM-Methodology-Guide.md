---
title: "Interpretable Context Methodology (ICM): An AI-Consumable Specification of Jake Van Clief's Folder-and-File Workflow Method"
aliases: ["ICM", "Model Workspace Protocol", "MWP", "folder structure as agent architecture", "Clief Notes method", "Map / Rooms / Tools"]
method_author: "Jake Van Clief (with David McDermott). Eduba; Clief Notes community"
compiled: 2026-10-01
document_version: 0.2
intended_reader: "An AI agent that will design, build, restructure, validate, or operate ICM workspaces, skills, and workflows"
---

# ICM: Folder Structure as Agent Architecture

> One agent, reading the right files at the right moment, does the work a multi-agent framework would do. Numbered folders carry order. Nesting carries scope. A small file at the root says where everything lives. Plain markdown carries the state.

---

## 0. How to Use This Document

### 0.1 Purpose

This is a specification of the method Jake Van Clief teaches for doing AI work with **folders and plain markdown files instead of agent frameworks**. It is written for an AI agent to use as an operating manual. The agent should be able to:

| Goal | Go to |
|---|---|
| Decide whether a task needs a workspace at all, and which kind | §3 |
| Understand the non-negotiable rules | §4 |
| Build a simple workspace for ongoing work (the Foundations tier) | §6, §17.1 |
| Build a staged pipeline workspace (the formal ICM tier) | §7 to §12, §17.2 |
| Pick among the six workspace forms | §18 |
| Restructure an existing folder into ICM shape | §17.3 |
| Write each file correctly | §8 to §11, templates in §21 |
| Run a workspace session after session | §12, §13 |
| Write prompts inside the system | §14 |
| Write new skills in the same style | §16 |
| Validate any workspace | §19 |
| Avoid known mistakes | §20 |

### 0.2 Normative keywords

- **MUST / MUST NOT**: a hard rule. The source says "no exceptions" or "never", or a validation check fails without it.
- **SHOULD / SHOULD NOT**: a strong default the source states, with known legitimate exceptions.
- **MAY**: an allowed option.
- Every rule has a stable ID (for example `R-L2-03`) so later skills and checklists can cite it.

### 0.3 Source tags

Each rule ends with source tags. Authority runs from highest (top) to lowest (bottom).

| Tag | Source | Fidelity |
|---|---|---|
| `[A]` | `github.com/RinDig/icm-architect`: Jake's Claude skill (`SKILL.md`, `references/core.md`, `forms.md`, `system-map.md`, `reference-integrity.md`, `assets/templates/`). Jul to Aug 2026. Newest and most distilled statement of the method. | Verbatim, read in full |
| `[R]` | `github.com/RinDig/Interpretable-Context-Methodology`: `_core/CONVENTIONS.md` (15 patterns), `_core/templates/`, `_core/placeholder-syntax.md`, four example workspaces. Feb to Jun 2026. | Verbatim, read in full |
| `[P]` | Paper: Van Clief & McDermott, *Interpretable Context Methodology: Folder Structure as Agentic Architecture*, arXiv:2603.16021 (v1 17 Mar 2026 titled "Model Workspace Protocol"; v2 18 Mar 2026 renamed ICM, otherwise the same text). | Full text, from mirrors |
| `[M]` | Paper and repo: Van Clief, McDermott, Kumar, *The Cost of Remembering: Filesystem Memory Against Long Context on LongMemEval* (Aug 2026), `github.com/RinDig/cost-of-remembering`. ICM applied to agent memory. | Full text |
| `[F]` | Clief Notes Skool classroom, **The Foundation** lessons 1.2 to 5.1. Jake's own lesson text, which he says covers the same ground as the videos. | Community transcriptions and clippings of the lesson text; very likely verbatim |
| `[PB]` | Clief Notes classroom, **Implementation Playbooks** and **Building Your Stack** lessons. | Clippings of the lesson text |
| `[O]` | `github.com/RinDig/Content-Agent-Routing-Promptbase` ("Eduba Content System"): the production system ICM grew out of (Feb 2026). | Verbatim; superseded where it conflicts |
| `[V]` | Jake's YouTube channel (@JEVanClief). | Titles and search snippets only (transcripts were unreachable) |
| `[SS]` | Jake's Substack ("Clief Notes"), Skool posts, LinkedIn, TikTok. | Search snippets only |
| `[X]` | Third-party practitioners and write-ups. | Interpretation, lowest authority |
| `[I]` | Inference by the compiler of this document. | Strongly implied, not stated |

### 0.4 Precedence when sources disagree

The method moved fast between February and August 2026. When sources conflict:

1. Use `[A]` for structure, naming, and invariants.
2. Use `[R]` for detailed patterns `[A]` does not cover: checkpoint and audit tables, questionnaires, placeholders, value validation, specs-as-contracts, bundled skills.
3. Use `[P]` for rationale, scope, evidence, and future directions.
4. Use `[F]` and `[PB]` for the beginner tier, everyday practice, prompting, sessions, and planning.
5. Use `[M]` for memory and knowledge workspaces.
6. Use `[O]` only for history, or where it is the only source for an idea.
7. Treat `[V]`, `[SS]`, `[X]` as supporting color, never as the sole basis for a MUST.

Every known conflict and its resolution is listed in §23.

### 0.5 The method in one paragraph

One AI agent, reading the right files at the right moment, replaces a multi-agent framework. **Numbered folders carry sequencing. Folder hierarchy carries context scoping. Plain markdown files carry state. One folder's `output/` is the next folder's input.** A small root file (`CLAUDE.md`) says where everything is and routes each task to the right place. Each working folder has a `CONTEXT.md` that says what to read, what to do, what to write, and what a human checks. Stable rules (the factory) live apart from per-run work (the product). A human can open and edit every intermediate file before the next step reads it. Local scripts do the mechanical work that needs no AI. [P][R][A]

---

## 1. Core Thesis and Mental Models

### 1.1 The central observation

> "If the prompts and context for each stage of a workflow already exist as files in a well-organized folder hierarchy, you do not need a coordination framework to manage multiple specialized agents. You need one orchestrating agent that reads the right files at the right moment." [P §1]

> "Stage sequencing is the folder numbering. Context scoping is the folder hierarchy. State management is the files on disk. Coordination between stages is one folder's output being another folder's input." [P §3.2][R][A]

> "Claude is the intelligence. Your folders and context files are the orchestration." [F 4.5]

### 1.2 The problem the folders solve [F 3.1]

> "Most people open Claude or ChatGPT, type something, get a response, and start over... You are burning tokens on stuff that does not matter. You cannot edit what the AI produces at each step. And every conversation starts from zero. The folder structure fixes all of that."

Three failures, three fixes:

| Failure | Fix |
|---|---|
| Every conversation starts from zero | Persistent files carry identity, context, and progress |
| Everything gets dumped into one context window ("an AI writing a blog post is also reading your video production notes") | Separate areas; load only what the task needs |
| No chance to edit between steps | Each step writes a file a human can change before the next step |

### 1.3 Framework vs ICM control surfaces [P Table 1]

| Operation | Framework approach | ICM approach |
|---|---|---|
| Change stage order | Edit orchestration code, redeploy | Rename or reorder folders |
| Modify a prompt | Edit agent configuration in code | Edit a markdown file |
| Add or remove a stage | Write a new agent class, update the orchestrator | Add or delete a folder |
| Inspect intermediate state | Add logging, build a dashboard | Open the folder, read the files |
| Hand off to another person | Document the environment, dependencies, setup | Copy the folder |
| Who can make changes | A developer | Anyone with a text editor |
| Error recovery mid-pipeline | Built-in retry, fallback, exception handling | Manual re-run of the failed stage |
| Conditional branching | Programmatic routing on agent output | A human decides between stages |
| Concurrent execution | Native parallel agents | Sequential by design |
| External services | Programmatic API calls, auth | Local scripts or MCP connections |

ICM wins the first six rows. Frameworks win the last four. State both honestly. [P][A]

### 1.4 The five design principles [P §3.1][R][A core]

| # | Principle | Borrowed from | What it means in practice |
|---|---|---|---|
| 1 | **One stage, one job** | McIlroy (Unix), Parnas (information hiding) | A stage that fetches does not also filter. A stage that filters does not also format. A stage that researches does not also write. Each reads a defined input, transforms it, writes a defined output. |
| 2 | **Plain text as the interface** | Kernighan & Pike | Stages talk through markdown and JSON. No binary formats, no databases in the loop, no proprietary serialization. Anyone with a text editor can inspect or change any artifact. |
| 3 | **Layered context loading** | Context engineering; "lost in the middle" | Load only what the current stage needs: "prevention rather than compression". Reference material and working artifacts arrive as structurally separate context. |
| 4 | **Every output is an edit surface** | Horvitz (mixed initiative), Shneiderman (direct manipulation) | Each intermediate output is a file a human can open, edit, and save before the next stage. The next stage reads whatever is there. |
| 5 | **Configure the factory, not the product** | Continuous delivery | Set up preferences, brand, style, and structure once. Every run produces a new deliverable from the same configuration. |

### 1.5 Mental models (use these to make design calls)

| Model | Statement | Design implication | Source |
|---|---|---|---|
| **Map / Rooms / Tools** | The root file is the floor plan on the wall. Each workspace is a room with its own context. Tools (skills, MCP) are wired into the rooms that need them. | Root file orients and routes only; detail lives in rooms; tools are scoped per room. | [F 3.1, 4.5] |
| **The library** | "The workspace is a library. The routing files are the catalog: small, stable, they point at everything and store almost nothing... One librarian, one model, walks the building, and the question decides which shelf gets walked to. Nobody photocopies the library into a backpack; that is what context-stuffing is." | Routing files hold pointers, never payload. Load by walking, not dumping. | [A] |
| **Factory vs product** | Layer 3 is the factory (stable, configured once). Layer 4 is the product (new each run). The recipe vs the ingredients. Also a warning: "They built the factory without ever making a product." | Keep stable rules and per-run artifacts in separate folders. Do not over-build before real use. | [P][R][A][F 3.3] |
| **The folder is memory, the prompt is direction** | Identity and context live in files. The task and its constraints go in each prompt. | Put what persists in files; put what changes in the prompt. | [F 1.2, 1.3] |
| **Stateless model, stateful workspace** | "Claude is stateless. Your workspace is stateful. The workspace is the memory." | Persist plans, progress, and decisions to disk. Every session can start clean. | [PB 2.4] |
| **The new hire** | CLAUDE.md is "an onboarding document for a new hire. Except the new hire reads the entire thing in two seconds and follows every word." | Write for a smart outsider: facts, conventions, what to avoid. | [F 4.4] |
| **Mad Libs (1953)** | The model fills in blanks without seeing the story, the way it sees only what is in its context window. | Control the story it can see. Structured context changes output fundamentally. | [V][F 2.3 via 4.2] |
| **Unix pipeline** | "Programs that do one thing. Output of one becomes input of another. Plain text as universal interface. Human-readable intermediate state." | One stage, one job. Text handoffs. | [P §1, §7] |
| **Multi-pass compiler** | Each stage is a pass that produces an intermediate representation. Re-run only the stale passes. | Stage outputs must be complete, readable artifacts. Re-run selectively. | [P §4.2, §6.1] |
| **Literate programming** | The instruction file and the documentation are the same artifact. | Write CONTEXT.md so a human can read it as docs and an agent can follow it as instructions. | [P §3.3] |
| **Glass box** | "It was never opaque in the first place." | Observability is free. Do not build dashboards. | [P §5.3][R] |
| **Index lookup vs table scan** | Reading all history to answer one question is a full table scan. Reading a catalog then two or three files is an index lookup. | Any question should resolve through the entry file, one index, and one or two leaves. | [M] |
| **Make / Codd** | Files are both the work and the coordination. A fact lives in one place and is pointed at from everywhere else, because copies drift. | No orchestration layer. One home per fact. Generated indexes. | [P][M] |
| **Worse is Better** | "ICM trades the flexibility of a programmatic orchestrator for the portability, inspectability, and editability of plain files. That tradeoff is the point." | Prefer the simplest structure that works. | [P §3.2] |
| **Orchestration vs intelligence** | A 100K-star "agent" product contains no AI of its own; it is orchestration around a model. | Most "agent" value is organization, which folders provide. | [V "Clawdbot"][F 4.5] |
| **"The machine is smart"** | "Being smart is not the hard part." "Productionize your opinion, not just your process": bake your judgment calls, ordering, and checks into files. "If your value lives in a clever prompt, you are racing the labs, and you will lose." Engelbart: intelligence depends on organization. | Encode judgment and arrangement, not cleverness. | [SS] |
| **The abstraction ladder** | Every layer of computing started unreliable; "one line of Python triggers 12,000 lines of code". AI is the next rung. | "AI is probabilistic" is not a reason to avoid it; build structure around it. Work at the right layer. | [SS][V] |
| **Inverted U of constraints** | "Too few constraints and you get chaos, too many and you get stiff output." | Give "creative room within clear boundaries". | [PB 1.1] |
| **60/30/10** | A Vault course: "the business methodology for deciding where AI fits". Secondary descriptions: about 60% existing infrastructure or traditional queries, 30% rule-based logic, 10% AI. | Most of a workflow is not AI. Use scripts and rules first; reserve the model for judgment. | [SS title][X percentages] |

### 1.6 Who does what: agent, scripts, human

| Actor | Does | Does not |
|---|---|---|
| **One orchestrating agent** | Reads the routing files, runs one stage or task at a time, writes outputs to files, runs audits, presents checkpoints | Load the whole workspace; decide branching on its own; learn from old outputs |
| **Sub-agents (optional)** | Do delegated sub-tasks inside a stage; their prompts are filled from the same CONTEXT.md and reference files | Coordinate with each other through code |
| **Local scripts** | Mechanical work that needs no AI: fetching, moving files, formatting, emailing, rendering, transcribing, rebuilding indexes | Make judgment calls |
| **Human** | Reviews every stage output; edits files directly; decides branches between stages; approves restructures; fixes recurring problems at the source | Re-answer setup questions every run |

> "The folder hierarchy is both the human's control surface and the model's orchestration logic." [P §4.1]

---

## 2. Glossary

| Term | Definition |
|---|---|
| **Workspace** | A self-contained folder holding one ICM system: entry file, routing, rooms or stages, factory material, setup. It still works after being copied, zipped, or committed to git. [P §3.4] In the Foundations tier, "workspace" also means one *area of work* (a room) inside a project, such as `script-lab/`. [F 3.1] Context makes clear which is meant. |
| **Entry file (Layer 0, "the Map")** | `CLAUDE.md` (Claude Code) or `AGENTS.md` (other agents) at the root. Answers "where am I, where does everything live, where do I go for task X" and nothing else. [A][F] |
| **Room** | A workspace area for one kind of work, with its own `CONTEXT.md`. [F 3.1] |
| **Root CONTEXT.md (Layer 1)** | Workspace-level routing. Maps the task to the stage that handles it and lists shared resources. In icm-architect form it is "the pipeline in one screen". [P][R][A] |
| **Stage** | One numbered folder doing one job in a sequence. Contains `CONTEXT.md`, `references/`, `output/`. [P][R][A] |
| **Stage contract (Layer 2)** | A stage's `CONTEXT.md`: Inputs, Process, Outputs, plus optional Checkpoints and Audit, and a Human check. "The control point of the entire system." [P §3.2] |
| **Inputs table** | The part of a contract that names exactly which files, and which sections of them, to load. It makes context selection "explicit, editable, and auditable". [P §3.2] |
| **Routing table** | A table in the entry file: task → where to go → what to read (→ which skills). "The most important pattern in the whole system." [F 3.1] |
| **Reference material (Layer 3, factory)** | Stable rules and knowledge: voice, design system, conventions, templates, skills. Configured once. The model internalizes it as constraints. [P][R] |
| **Working artifacts (Layer 4, product)** | Per-run content: earlier stage outputs and user source material. The model processes it as input. [P][R] |
| **Handoff** | Stage N writes to its `output/`; stage N+1 reads it. [R] |
| **Edit surface** | Any intermediate output file a human may edit before the next step runs. [P] |
| **Review gate / Human check** | The point between stages where a person reads the output before anything moves on. [P Fig. 4][A] |
| **Checkpoint** | A pause inside a stage, between process steps, where the agent shows options or a draft and the human picks a direction. [R] |
| **Audit** | A pass/fail checklist the agent runs after the process and before writing to `output/`. [R] |
| **Trigger** | A keyword the entry file recognizes, such as `setup` or `status`. [R] |
| **Questionnaire** | `setup/questionnaire.md`: one-time onboarding that configures the factory. [R][A] |
| **Placeholder** | A literal `{{SCREAMING_SNAKE_CASE}}` token in a template file, replaced during `setup`. [R] |
| **Conditional section** | `{{?NAME}} ... {{/NAME}}` wrapped around a whole section, removed if the user does not need it. [R] |
| **Skill** | A folder (`SKILL.md` plus optional `rules/`, `scripts/`) that gives domain knowledge. It is wired into the rooms or stages that need it, or bundled into `skills/`. [R][F] |
| **Form** | One of six workspace shapes (Pipeline, Umbrella, Record library, Knowledge bundle, Context map, System map), chosen by the repeating unit of work. [A] |
| **Walk test** | Validation by walking the workspace cold, as an agent with no memory. [A] |
| **Catalog / Contract / Factory / Product / Dead** | The five roles every file gets during a restructure. [A] |
| **Canonical source** | The single authoritative file for a fact. Everything else points to it. [R] |
| **PRD** | A product requirements document written before building; "stateful prompting" that persists as context. [PB] |
| **PROGRESS.md** | A root file holding current status, the last session, decisions made, and open questions. [PB 2.4] |
| **Edit-source principle** | "Editing the output fixes this run. Editing the source fixes every future run." [P §6.3] |

---

## 3. Deciding What to Build

### 3.1 Decision procedure (run this first)

```
START: a human describes some work.

Q1. Is it a one-off?
    YES -> Do it in chat. No files. STOP.
Q2. Does it repeat but fit in one saved prompt or one skill?
    YES -> Write a saved prompt or a skill (see §16). Do not build a workspace. STOP. [A]
Q3. Has the process actually repeated, or is it ongoing work the person does regularly?
    NO  -> Do not build yet. "A workspace for a thing done twice is scaffolding, not architecture." STOP. [A]
Q4. Is it ongoing work across several kinds of tasks (writing, production, clients, code areas),
    with no fixed sequence?
    YES -> TIER 1: Simple workspace (Map / Rooms / Tools). See §6, build with §17.1.
Q5. Is it a repeating sequence that produces a deliverable each run, where a human
    should check each step?  (sequential + reviewable + repeatable)
    YES -> TIER 2: Pipeline workspace. See §7 to §12, build with §17.2.
Q6. Is the repeating unit something else (a record, a body of knowledge, an organization,
    a codebase later agents will edit, several pipelines sharing one brand)?
    YES -> TIER 3: choose a Form (§18) and build with §17.2.
Q7. Does it need real-time agent-to-agent loops, many simultaneous users, or automated
    branching on AI output mid-run?
    YES -> ICM is the wrong tool for that part. Use a framework there (§3.4).
```

Tiers nest. A Tier 1 room can grow a Tier 2 pipeline inside it once a sequence inside the room starts repeating. [I, consistent with A "forms compose"]

### 3.2 The three-part test for a pipeline [P §5.1][R]

Use a pipeline when the workflow is:

- **Sequential**: step 2 follows step 1.
- **Reviewable**: a human should check each step's output.
- **Repeatable**: the same pipeline runs regularly (weekly, daily) with different input.

Typical fits: content production, research and analysis, monitoring and digests, reporting, training material, course decks, policy analysis, client deliverables, literature reviews, audits, curriculum development, code documentation. [P][R] "Same structure, different content" across research, finance, and engineering procedures. [SS TikTok]

### 3.3 The ladder: do not over-structure

> "The ladder runs: chat → saved prompt/skill → folders + one agent. Only climb when the rung below is genuinely automated and repeating. A workspace for a thing done twice is scaffolding, not architecture." [A]

- **R-SCOPE-01** If the whole job fits in one saved prompt, say so and MUST NOT build a workspace. [A]
- **R-SCOPE-02** MUST NOT build a pipeline before the process has actually repeated. [A]
- **R-SCOPE-03** "Three real stages beat seven imagined ones." MUST NOT create folders for stages that do not exist yet, empty "misc" buckets, or speculative depth. [A]
- **R-SCOPE-04** The first version of a simple workspace SHOULD take about 15 minutes. "If it took longer, you over-built." Let the structure grow from use, not from planning. [F 3.3]
- **R-SCOPE-05** "The moment it starts feeling heavy or complicated, something went wrong." [F 3.3]
- **R-SCOPE-06** Use the simplest tool that solves the problem. Jake's tool ladder: (1) Claude Projects, (2) Cowork, (3) VS Code + Claude Code ("where most people should land"), (4) a custom front-end. "If you're not sure whether you need a custom front-end, you probably don't." [PB Stack 1.1]

### 3.4 Where ICM loses (state these honestly) [P §5.2][A core]

| Situation | Why ICM is the wrong tool |
|---|---|
| Real-time multi-agent collaboration (agents answering each other in tight loops) | Needs message-passing infrastructure; file handoffs are too slow |
| High concurrency (many users hitting one pipeline at once) | Needs queueing, state isolation, deployment; ICM is local-first |
| Automated mid-pipeline branching on AI output | A human choosing 3a vs 3b between stages is natural; the system branching on its own "pushes ICM toward becoming the framework it replaced" |

> "The claim is not that ICM replaces frameworks everywhere. The claim is that for sequential, human-reviewed, repeatable workflows, which is most knowledge work, the framework is more complexity than the problem requires, and that complexity costs opacity, fragility, and developer dependency." [A][P]

Frameworks are not "bad": they fit complex, concurrent systems. [P]

### 3.5 ICM and MCP are complementary [P §2.2][R]

MCP handles tool and data access. ICM handles how context is structured and delivered across stages. An ICM stage MAY use MCP connections; the folder decides what context the agent has while it does. Scope tools per room or stage (§15.3).

---

## 4. The Invariants (the non-negotiable core)

The titles are verbatim from icm-architect `[A]`; the paper and repo reinforce each one. Every ICM workspace of any form MUST obey all ten, at every level of nesting.

| ID | Invariant | Rule |
|---|---|---|
| **INV-01** | **One folder, one job** | Each folder does a single step or holds a single kind of thing, and states its own purpose in a file inside itself. "The structure is the documentation." |
| **INV-02** | **A small, stable entry file** | `CLAUDE.md` (or `AGENTS.md`) at the root answers "where am I, where does everything live, where do I go for task X", and nothing else. Under ~60 lines. It routes; it never holds content. |
| **INV-03** | **Numbering encodes order** | `01_`, `02_`, ... where sequence matters. Renaming folders reorders the pipeline; that is the point. |
| **INV-04** | **Every folder-level contract is explicit** | A `CONTEXT.md` per working folder: what it reads (inputs), what it does (process), what it writes (outputs), what a human checks. |
| **INV-05** | **Factory vs product** | Reference material (rules, voice, schemas, templates; stable across runs) lives structurally apart from working artifacts (outputs, drafts; new every run). |
| **INV-06** | **Every output is an edit surface** | Intermediate outputs are plain files a human can open, edit, and save before the next step reads them. Nothing moves forward until a person has read the last output. |
| **INV-07** | **Load only what the step needs** | An agent doing a step reads its contract, its references, and its inputs, not the whole workspace. 2,000 to 8,000 tokens per step is the healthy range. |
| **INV-08** | **Plain text, linkable, queryable** | Markdown plus YAML frontmatter. Links (`[[wikilinks]]` or relative paths) make it a graph; frontmatter labels make it queryable. One home per fact; a link beats a copy. |
| **INV-09** | **The filesystem is the state machine** | Status is derived by scanning what exists in output folders. Generated indexes (file maps, logs) are rebuilt by script, never hand-edited. |
| **INV-10** | **Instantiate by copying** | A new unit of work is a copy of a template folder, not a blank page. Templates live in `_templates/`. |

Library rules that support the invariants [A core][M][F]:

- **R-LIB-01 The catalog holds no books.** Routing files point at everything and store almost nothing. A growing routing file is absorbing payload: move it to a shelf and leave a pointer.
- **R-LIB-02 One home per fact.** "Duplication is how structures rot." [A] "One fact, one location." [F 4.5]
- **R-LIB-03 Generated indexes are never hand-edited.** An index built from frontmatter by a script cannot drift; a hand-curated one always does. If an index matters, script it and schedule the rebuild. Head generated files with a marker such as `<!-- GENERATED by <script> from <source>. Do not edit. -->`. [A][M]
- **R-LIB-04 The structure is the documentation.** Explanations go in that folder's `CONTEXT.md`, "not in a wiki elsewhere and not in anyone's head". "A new collaborator should understand the whole pipeline by reading the CONTEXT files top to bottom, without running anything." [A][P §3.3]
- **R-LIB-05 Method and instance live apart.** A structure's blank, reusable template is a different artifact from any filled-in deployment. Once a structure proves out, extract the template before it tangles with the data. [A]
- **R-LIB-06 Working sessions end in artifacts.** A workshop, interview, or planning call that produces only slides or vibes has failed the structure. It should end in files the structure can shelve. "Conversations are disposable. The thinking is not." [A][F 4.3]
- **R-LIB-07 New sessions start clean.** Because CLAUDE.md is read fresh and routing sends the agent to the right room, nothing bleeds over from a previous task. [F 4.5]
- **R-LIB-08 Same quality for everyone.** "When the context lives in files, not in someone's head, anyone who opens the folder gets the same Claude experience." [F 4.5]

---

## 5. The Context Layers

### 5.1 Two views of the same architecture

Jake teaches the layers two ways. They describe the same thing at different resolutions.

| Teaching model (Foundations) [F 3.1] | Formal model (paper, repo, architect) [P][R][A] | What lives there |
|---|---|---|
| **Layer 1, The Map** | **L0** `CLAUDE.md` | Identity, folder map, naming conventions, routing table |
| **Layer 2, The Rooms** | **L1** root `CONTEXT.md` + **L2** room or stage `CONTEXT.md` | What this area or stage is for, its process, what to load |
| **Layer 3, The Tools** | Part of **L3** (skills, MCP) | Skills and tools wired into the rooms that need them |
| (reference docs a room points to) | **L3** reference material: `references/`, `_shared/`, brand and design folders | Voice, design system, conventions, templates |
| (drafts, outputs) | **L4** working artifacts: `output/`, source material | This run's inputs and products |

The video covers "the three most important layers"; the paper defines five. [F 3.1]

### 5.2 The five layers in detail

Agents read down the layers and stop as soon as they have what they need. [R][O]

| Layer | File / location | Question | Role | Loaded | Size |
|---|---|---|---|---|---|
| **L0** | `CLAUDE.md` at root | Where am I? | Catalog (identity, routing) | Always (Claude Code auto-loads it) | ~800 tokens [P][R]; 300 to 800 [A]; under ~60 lines [A][M]; 30 to 50 lines [PB 3.2] |
| **L1** | Root `CONTEXT.md` | Where do I go? | Catalog (task routing, shared resources) | On entry | ~300 [P][R]; 200 to 500 [A] |
| **L2** | Stage or room `CONTEXT.md` | What do I do? | **The control point** (contract) | Per task | 200 to 500 tokens; under 80 lines |
| **L3** | `references/`, `_shared/` (or `shared/`, `_config/`, `brand-vault/`, `design-system/`), `skills/` | What rules apply? | Factory (stable) | Selectively, as Inputs say | 500 to 2,000 tokens |
| **L4** | Earlier stages' `output/`, user source material | What am I working with? | Product (per run) | Selectively, as Inputs say | Varies; "rarely exceeds a few thousand tokens when the previous stage has done its job of condensing and structuring" [P] |

L0 to L2 together come to about 1,300 to 1,600 tokens. A full stage context runs **2,000 to 8,000 tokens**. A monolithic prompt for the same pipeline runs **30,000 to 50,000** (about 42k in the paper's figure, against about 4.9k, 5.5k, and 5.6k for the three ICM stages). [P §3.2] The origin system measured about 4,000 tokens to write a script with routing against 15,000+ without, and about 500 to render. [O]

### 5.3 Why reference (L3) and working (L4) material are kept apart

> "Layer 3 material needs to be internalized as constraints and patterns: the model should write like this, use these colors, follow these conventions. Layer 4 material needs to be processed as input: the model should transform this research into a script... Mixing persistent rules with per-run artifacts in an undifferentiated context window forces the model to sort them on its own. Separating them in the folder structure means the model receives already-organized context." [P §3.2]

| | Layer 3: Reference | Layer 4: Working |
|---|---|---|
| Changes between runs | No | Yes |
| Example files | `voice.md`, `design-system.md`, `conventions.md` | `research-output.md`, `script-draft.md` |
| Model should | Internalize as constraints | Process as input |
| Configured during | Workspace setup (once) | Pipeline execution (each run) |
| Folder location | `references/`, `_shared/`, `_config/`, `shared/`, `skills/` | `output/` |
| Analogy | The recipe | The ingredients |

[P Table 2][A]

### 5.4 Layer rules

- **R-LAY-01** No agent reads everything. Each task reads only as deep as it needs (a rendering stage may need only L0 to L2; a writing stage reads to L4). [P][R]
- **R-LAY-02** L0 to L2 are the catalog: small, stable, no content payload. [A]
- **R-LAY-03** L2's Inputs section makes context selection explicit instead of leaving it to the agent's judgment. Without it, the agent loads everything or guesses. [P][A]
- **R-LAY-04** Large L3 collections MUST get their own internal `CONTEXT.md` router: Layer 1 routing applied again inside Layer 3. "The hierarchy is self-similar at every depth; apply it inside any folder that grows past easy scanning." Examples: `brand-vault/CONTEXT.md`, `design-system/CONTEXT.md`. [P fn4][R][A]
- **R-LAY-05** "Every token of irrelevant context is a token of diluted attention. Loading more context does not make output better. It makes it worse." [R] "When you load 15,000 tokens into an agent that needs 4,000 of them, the extra 11,000 aren't neutral. They're noise." [O]
- **R-LAY-06** "The context window is working memory, not storage." [R][O] "200K tokens sounds huge until you fill it with irrelevant files." [F 4.5] (A token is "roughly three quarters of a word". [F 3.1])
- **R-LAY-07 Token discipline.** If a stage's context grows past about 8k tokens: (a) split the stage, (b) tighten the Inputs list, or (c) push detail down into an L3 file the contract points at but does not inline. [A][R]
- **R-LAY-08** Each stage SHOULD condense and structure its output so the next stage's L4 stays small. [P][I]
- **R-LAY-09** Every token in CLAUDE.md is paid on every prompt. "A 200-line CLAUDE.md costs you on every single prompt." [PB 3.2][O]
- **R-LAY-10** Tables and structured data are already token-efficient. Keep them as tables. [F 1.3]

---

## 6. Tier 1: The Simple Workspace (Foundations)

This is what Jake teaches first in Clief Notes. Use it for ongoing work split by kind of task, with no fixed sequence of stages. [F]

### 6.1 The three-file first folder [F 1.2, 3.1]

"Three files. Five minutes." Name the folder after the work. Use `.md` (plain `.txt` also works).

```
my-first-workspace/
├── CLAUDE.md      who Claude is working for and how to behave
├── CONTEXT.md     what you are working on right now
└── REFERENCES.md  background material Claude should know about but does not need to act on directly
```

- `CLAUDE.md`: Identity ("You are helping [NAME] with [WHAT YOU DO]"), folder structure (for example `/drafts`, `/final`, `/references`), and rules ("Write in plain, clear language"; "Ask clarifying questions before making assumptions"; "When you are unsure, say so"; "Read this file first on every new task"; "Ask before creating files outside of /drafts").
- `CONTEXT.md`: What we are building (2 to 3 sentences), What good looks like, What to avoid.
- `REFERENCES.md`: Examples of good work, relevant links, notes.

Three ways to load it: Claude Code (`cd` into the folder, run `claude`); a Claude Project (upload the files as Project Knowledge); or paste them at the top of the first message. [F 1.2]

### 6.2 Map / Rooms / Tools [F 3.1, 3.2, 4.5]

When the work spans several kinds of tasks, split it into rooms (workspaces), one per kind of work, under one Map.

```
my-project/
├── CLAUDE.md            THE MAP: what this is, folder structure, naming conventions, routing table
├── writing-room/
│   └── CONTEXT.md       THE ROOM: what it is for, its process, its files, its skills
├── production/
│   └── CONTEXT.md
└── community/
    └── CONTEXT.md
```

**The Map (`CLAUDE.md`)**, read first every time. It holds what the project is, the folder structure, naming conventions, where things go, and the **routing table**:

> "This is the most important pattern in the whole system. Inside it, you put a simple table that tells the AI: for this task, read these files, skip those files, you might need these skills. Without this, the AI either reads everything and wastes tokens, guesses wrong about what matters, or produces work you cannot edit along the way." [F 3.1]

| Task | Go to | Read | Skills |
|---|---|---|---|
| Write or brainstorm | `/script-lab` | `CONTEXT.md` | (none) |
| Build or produce | `/production` | `CONTEXT.md` | frontend-design |
| Publish or repurpose | `/distribution` | `CONTEXT.md` | (none) |

**A Room (`CONTEXT.md`)** describes what the room is for, its process ("first I do this, then I do that"), what files live there and how they are organized, which skills or tools to use, and what good work looks like. "Plain English. Short documents. A few paragraphs." Under a page. A room CONTEXT.md may point to separate reference files when there is a lot of material. [F 3.1, 3.2] "You say 'go to writing room, let's start making something' and the AI immediately reads the context file", loads the voice and style, and asks what to build. [F 3.1]

**The Tools (skills, MCP servers)** are wired into the rooms that need them, never loaded everywhere. "You can reference 15, 20, or 100 skills in a project, but each workspace only loads the ones it needs." [F 3.1]

### 6.3 Rules for the simple workspace

**Boundaries**

- **R-T1-01** Separate kinds of work into separate rooms so unrelated material never shares a context window. [F 3.1]
- **R-T1-02** Start with 2 to 3 rooms (4 at most). [F 3.2, 3.3]
- **R-T1-03 The mental-mode test.** A room boundary is a change of mental mode. "If you find yourself wishing Claude would 'forget' what it was just doing and focus on something else, that is a workspace boundary." "Drafting and editing are the same mental mode at different stages. That is one workspace with a process inside it." [F 3.2, 3.3]
- **R-T1-04** "If you are not sure whether something deserves its own workspace, it does not." Make it a subfolder. [F 3.3]
- **R-T1-05** One folder per client, each with its own CONTEXT.md. "Never reference one client's information in another client's workspace." Onboarding a client means copying the structure, writing a new CONTEXT.md, and adding one routing row. [F 3.2]

**Inside a room**

- **R-T1-06** More than 8 to 10 files at one level means subfolders. Group by room (what kind of work) first, then by stage or type. "The folder structure is the architecture." [F 3.3]
- **R-T1-07** Use stage or status subfolders inside a room: `ideas/ drafts/ final/`; `briefs/ specs/ builds/ output/`; `intake/ deliverables/ communications/`. [F 3.2]
- **R-T1-08 Naming conventions replace databases.** Put type, status, version, and date in filenames and document the convention in CLAUDE.md, so the agent can find files by name: `api-auth-guide_draft.md`, `topic-name_final.md`, `2026-03-launch-week.md`, `YYYY-MM-platform-topic.md`, `demo_v2.md`, `feature-name_spec.md`, `YYYY-MM-DD-decision-title.md`. "You can say 'pull my demo v2 and build a spec from it'... No SQL. No vector database." [F 3.1, 3.2]
- **R-T1-09** Shared templates live in their own room (`templates/`), and work starts by copying from it: "Proposals always start from /templates and get customized in the client folder." [F 3.2]
- **R-T1-10** Workspace-wide rules belong in CLAUDE.md, for example "Deliverables go in /client-[name]/deliverables, drafts stay in working folders." [F 3.2]

**The Map**

- **R-T1-11** CLAUDE.md is "a routing file... not a project brief... not a style guide... not a brain dump." Identity, folder structure, routing table, naming conventions: "That is it." [F 3.3]
- **R-T1-12** It SHOULD fit on one screen. "If your CLAUDE.md is longer than 40-50 lines, you have context files hiding inside it. Pull them out." Aim for 30 to 50 lines. [F 3.3][PB 3.2]
- **R-T1-13** MUST include a routing table (Task | Go to | Read, plus Skills when tools are in use), one row per kind of work. Routing that works "sometimes" is the problem. [F 3.3]
- **R-T1-14** Detail for a subfolder MAY go in a folder-level `README.md` or `CONTEXT.md`, so the root stays lean. [PB 3.2]

**Room context files**

- **R-T1-15 Describe the work, not the AI.** "Claude responds to context about the work far more than context about itself." Spend about 80% of a context file on the project, audience, what has been done, what good looks like, and what to avoid, and 20% or less on behavioral instructions. "If your context file reads like a personality quiz, rewrite it." [F 3.3]
- **R-T1-16** Specific audience facts beat role labels: "mid-market HR directors who... are skeptical of AI claims" beats "you are a senior copywriter". [F 3.3]
- **R-T1-17** Every context file SHOULD include "What good looks like" and "What to avoid". [F 1.2]
- **R-T1-18 Keep context alive.** Context files are "working notes, not finished documents". Update them when the project changes; it is "the single highest-leverage habit in the whole system". A "Last updated" line helps. When Claude seems to "get worse", suspect stale context first. [F 3.2, 3.3, 4.4]
- **R-T1-19** Keep reference material (examples, links, style guides) separate from instructions: "anything Claude should have access to but does not need to act on directly". [F 1.2]

**Building it** [F 3.2, 3.3]

1. List 2 to 4 rooms, using the mental-mode test.
2. Write one `CONTEXT.md` per room, under a page.
3. Write `CLAUDE.md`: rooms, routing table, naming conventions.
4. Start working, and adjust. "The first version will not be perfect." Add what is missing after a few days; fix what is wrong after a week. "The best folder setups in the community were all built incrementally."

The smallest experiment: two folders, each with its own CLAUDE.md. Run the same kind of task in each and watch the behavior differ; then join them under one routing table. [F 4.5]

**When it gets messy**: ask the agent to "Clean up this project folder and update CLAUDE.md to reflect the structure." [PB 1.3]

### 6.4 A single code project's CLAUDE.md [F 4.4]

For one project, about 15 lines is enough, written in about 10 minutes: overview (2 to 3 sentences), tech stack (or document types), how to run things (or how to use these files), key conventions, what to avoid. "Write it for a smart person who just joined your project." "A mediocre CLAUDE.md beats no CLAUDE.md every time." Test it by moving it out and comparing the outputs. It works for non-code folders too.

```markdown
# My Web App

React 18 + Express + PostgreSQL + TypeScript

## Commands
npm run dev | npm run api | npm test

## Conventions
Functional components only. Routes in src/api/.
All database queries go through src/db/queries/.

## Avoid
No class components. Don't modify db/migrations directly.
Don't use Moment.js (we use date-fns).
```

### 6.5 Graduating from Tier 1 to Tier 2

When a sequence inside a room starts repeating (for example script → spec → build → render), turn that room into a pipeline with numbered stage folders, contracts, and `output/` handoffs (§7). Keep the Map routing to it. The origin system did exactly this: an umbrella of rooms (brand-vault, script-lab, topic-engine, animation-studio...) where animation-studio held `workflows/01-scripts → 02-specs → 03-builds → 04-renders`. [O][I]

---

## 7. Tier 2: Pipeline Workspace Structure and Naming

### 7.1 Canonical pipeline skeleton

```
workspace-name/
├── CLAUDE.md                  L0: identity, folder map, routing, triggers
├── CONTEXT.md                 L1: the pipeline in one screen (or task routing)
├── setup/
│   └── questionnaire.md       configures the factory once
├── _shared/                   L3 factory: voice.md, rules.md, design-system.md, definition-of-done.md
│   └── CONTEXT.md             only if the folder grows past easy scanning
├── _templates/                blank starters; new work is a copy
├── skills/                    L3: bundled domain skills (optional)
│   └── skill-name/SKILL.md
└── stages/
    ├── 01_research/
    │   ├── CONTEXT.md         L2: stage contract
    │   ├── references/        L3: stage-specific reference
    │   └── output/            L4: this run's artifact, handed to 02
    ├── 02_script/
    │   ├── CONTEXT.md
    │   ├── references/
    │   └── output/
    └── 03_production/
        ├── CONTEXT.md
        ├── references/
        └── output/
```

[P Fig. 2][A forms][R]

The ICM repo's workspaces use an equally valid variant: `stages/01-script/`, `shared/` for cross-stage files, and a named context folder such as `brand-vault/` or `design-system/` with its own `CONTEXT.md`. Pick one style per workspace and hold it. [R]

### 7.2 Where things go

| Material | Location |
|---|---|
| Identity, folder map, routing table, triggers | `CLAUDE.md` |
| Task routing, shared-resource index, pipeline overview | root `CONTEXT.md` |
| Stage-specific rules, templates, formats, tool setup guides | `stages/NN_name/references/` |
| Cross-stage reference (voice, brand, design, platform specs, definition of done) | `_shared/` (or `shared/`) |
| Brand, voice, or design collections big enough to need routing | a dedicated folder (`brand-vault/`, `design-system/`, `_config/`) with its own `CONTEXT.md` |
| Domain skills | `skills/<skill-name>/` (§15) |
| Blank templates for new units of work | `_templates/` |
| Generated indexes, logs | `_index/` |
| Schema, the workspace's own rules (graph forms) | `_meta/schema.md` |
| Superseded or dead files | `_archive/` (never silently delete) |
| Secrets | `.env` (gitignored), with `env-template.md` listing variables with empty values |
| Per-run metadata (project name, topic, audience) | written by the entry stage to its own `output/`, carried forward |
| Plans and progress across sessions | `PRD.md` / `docs/prd.md`, `PROGRESS.md` at the root (§13) |

### 7.3 Naming rules

- **R-NAME-01** Stage folders MUST carry a zero-padded two-digit order prefix. Default `NN_kebab-name` (`01_research`) [A][P]; variant `NN-kebab-name` (`01-script`) [R]. One style per workspace.
- **R-NAME-02** Folders and files use lowercase kebab-case with no spaces. [R][A]
- **R-NAME-03** Meta and system folders take an underscore prefix so they sort to the top: `_meta/`, `_system/`, `_shared/`, `_config/`, `_templates/`, `_index/`, `_archive/`. "Underscore = 'about the workspace, not of the work.'" [A]
- **R-NAME-04** Ordered files inside a folder MAY use an ordinal-only prefix (`00-tracker.md`, `00_START-HERE.md`). [A]
- **R-NAME-05** Output artifacts: `[topic-slug]-[artifact-type].md` (`hello-world-script.md`, `hello-world-spec.md`). [R]
- **R-NAME-06** Typed content files MAY prefix their type (`data-customer-list.md`). [A]
- **R-NAME-07** For records and nodes, choose kebab-case slugs (machine-facing) or Title Case (where a person browses daily, as in an Obsidian vault). Pick one per workspace and write it into the schema: "drift between schema and files is the most common decay." [A]
- **R-NAME-08** Templates are blank, named for what they produce, and live together (`_templates/pilot-brief.md`). [A]
- **R-NAME-09** Placeholders are `{{SCREAMING_SNAKE_CASE}}` and descriptive (`{{BRAND_NAME}}` not `{{BN}}`). Related ones share a prefix (`{{PRIMARY_COLOR}}`, `{{SECONDARY_COLOR}}`). [R]
- **R-NAME-10** The entry file is `CLAUDE.md` for Claude Code and `AGENTS.md` for other agents. If both exist, one is generated from the other or is a one-line pointer. MUST NOT keep two hand-maintained copies. [A]
- **R-NAME-11** Date-bearing files SHOULD use sortable dates (`YYYY-MM-DD-...`, `...-2022-10.md`). [F 3.2][M]
- **R-NAME-12** Renumbering is a feature: renaming folders reorders the pipeline. Every input path that names a renamed folder MUST be edited in the same change. [A]
- **R-NAME-13** Alternative branches a human chooses between MAY be sibling stages, such as `03a_...` and `03b_...`. [P §5.2][I]
- **R-NAME-14** Every folder that should persist but starts empty gets a `.gitkeep`. [R]
- **R-NAME-15** Status and version MAY live in filenames: `[PILLAR]-[slug]-[draft|review|final].md`, `T-[id]-[slug]-v[version].mp4`. ID systems used everywhere (pillar codes, topic codes) belong in L0. [O]
- **R-NAME-16** A naming convention MAY double as an ID scheme: `ht10-second-brain` = type + counter + slug. [A]

---

## 8. File Spec: The Entry File (`CLAUDE.md`, L0, the Map)

### 8.1 Purpose

Answer "where am I, where does everything live, where do I go for task X", and nothing else. It is auto-loaded into every conversation, so every line costs tokens on every task. [A][R][PB 3.2]

### 8.2 Required content

| Section | Content | Tier | Source |
|---|---|---|---|
| Title + one sentence | What this workspace is and what leaves it | all | [A][R] |
| Identity (one line) | Who the work is for: "You are helping [NAME] with [WHAT]" | Tier 1 | [F 1.2] |
| Folder map | Tree or table: folder → what it holds | all | [R][A][F] |
| Routing table | Task (or "what just happened") → where to go → what to read (→ skills) → where to stop | all | [F][R][A] |
| Naming conventions | File patterns, ID schemes | all | [F 3.1][O] |
| Triggers | `setup`, `status`, plus workspace-specific keywords, and what each does | Tier 2 | [R] |
| What to Load | Task → Load These → Do NOT Load | Tier 2, recommended | [R] |
| Stage handoffs note | "Each stage writes its output to its own output/ folder. The next stage reads from there. If you edit an output file, the next stage picks up your edits." | Tier 2 | [R] |
| The one rule | "Nothing moves to the next stage until a person has read the output of the last one." | Tier 2 | [A] |
| Workspace-wide rules | A few lines at most ("Never reference one client's information in another client's workspace") | optional | [F 3.2] |

### 8.3 Rules

- **R-L0-01** MUST route, never hold content: no definitions, rule sets, examples, or voice guidance. [A][R][F]
- **R-L0-02** SHOULD stay under about 60 lines (300 to 800 tokens); Jake's lessons say one screen, 30 to 50 lines. Treat 80 lines as the outer limit. [A][M][F][PB]
- **R-L0-03** MUST NOT contain placeholders, because it has to work before onboarding runs. [R]
- **R-L0-04** A repo or umbrella root `CLAUDE.md` routes into sub-workspaces. "Navigate into a workspace folder and that workspace's CLAUDE.md takes over." [R]
- **R-L0-05** Route by task, or by "what just happened" (If | Go to | Then stop at). [A][F]
- **R-L0-06** In the What to Load table, list what NOT to load for each task (other stages' references, unneeded skills, prior runs). It gives the agent "permission to not look". [R][X]
- **R-L0-07** "The map states only what rarely changes; details live in each pipeline." [A]
- **R-L0-08** In memory and knowledge workspaces, include a numbered "How to answer a question" procedure: read this file, follow it to the index or folder, read only the leaves you need. [M]
- **R-L0-09** A "When you first start working" sequence MAY be included: read this file → identify your task → go to the workspace → read its CONTEXT.md → do the work → consult other workspaces only through cross-references. [O]

---

## 9. File Spec: Root `CONTEXT.md` (L1)

Two accepted shapes. Choose one per workspace.

- **Shape A, "the pipeline in one screen"** [A]: a one-line flow; one table `Stage | Job | Input | Output | Human check`; one line naming where the factory lives and one naming where the product lives; and the status rule ("a stage is COMPLETE when its `output/` holds an artifact; a placeholder that only keeps the empty folder in git does not count").
- **Shape B, task routing** [R]: a one-sentence description; a `Task Type | Go To | Description` table; a `Resource | Location | Contains` table of shared resources (context folders, shared files, skills).

Rules:

- **R-L1-01** Routing only. The purity rules for stage contracts apply (§10.4). [R][A]
- **R-L1-02** Routing tables MUST NOT contain placeholders. [R]
- **R-L1-03** SHOULD list every shared resource with its location, so stages point at it instead of copying it. [R]
- **R-L1-04** In Tier 1 there is usually no root CONTEXT.md. The Map routes directly to each room's CONTEXT.md. [F]

---

## 10. File Spec: Stage `CONTEXT.md` (L2, the Stage Contract)

### 10.1 Purpose

The contract for one stage: what it reads, what it does, what it writes, and what a human checks. "Simple enough that a non-technical user can read it and understand what is happening. Structured enough that an agent can follow it reliably. Every stage follows this exact shape. No exceptions." [R Pattern 1]

### 10.2 Section order (unified superset)

This merges the repo `[R]` and icm-architect `[A]` shapes. Delete the optional sections a stage does not need.

| # | Section | Status | Source |
|---|---|---|---|
| 1 | `# NN_stage-name: the job in five words` (repo form: `# Stage 01: Script Writing`) | required | [A][R] |
| 2 | One sentence: "One job: ..." | required | [A][R] |
| 3 | `## Inputs` | required | [P][R][A] |
| 4 | `Do NOT load:` line | strongly recommended (required in [A]) | [A] |
| 5 | `## Process` | required | [P][R][A] |
| 6 | `## Checkpoints` | required for creative stages | [R] |
| 7 | `## Audit` | required for creative and build stages | [R] |
| 8 | `## Outputs` | required | [P][R][A] |
| 9 | `## Human check` | required (in [A]) | [A] |
| 10 | `## Verify` | optional, proposed in the paper | [P §6.2] |

### 10.3 Section rules

**Inputs**

- **R-L2-IN-01** List every file the agent needs by exact relative path. [R][A]
- **R-L2-IN-02** Label or split inputs into **Working (this run)** (L4) and **Reference (every run)** (L3). The paper writes `Layer 4 (working)` and `Layer 3 (reference)`. [P][A]
- **R-L2-IN-03 Route to sections, not just files.** Name the section ("'Hard Constraints' through 'What the Voice Is NOT'"). Write "Full file" when the whole file is needed. [R Pattern 4] The origin system called this "the highest-leverage pattern in the whole system... same principle as database views." "A 150-line file might have only 60 lines of actionable rules for a specific stage." [O][R]
- **R-L2-IN-04** Table form: `Source | File/Location | Section/Scope | Why` [R]. List form: `- Working (this run): ../01_research/output/research.md` [A]. Either works.
- **R-L2-IN-05** The working input names the previous folder's real name: "renumbering the pipeline means editing this path." [A]
- **R-L2-IN-06** User input appears as a row with Source `User` and Location `(conversation)` or `(uploaded files or pasted text)`. [R]
- **R-L2-IN-07** Reference a skill as `| Skill | ../../skills/[name]/SKILL.md | Index, then load rules as needed | [what it provides] |`. [R]
- **R-L2-IN-08** Placeholders MAY appear in Inputs values (for example `Platform matching {{PRIMARY_PLATFORM}}`), never in routing structure. [R]
- **R-L2-IN-09** Inputs MUST NOT point at earlier runs' `output/` files to learn patterns (Docs over outputs, R-QUAL-01). [R]

**Do NOT load**

- **R-L2-DNL-01** Name anything an eager agent would wrongly pull in: other stages' references, prior runs, the whole `_shared` folder, skills this stage does not need. [A][R]

**Process**

- **R-L2-PR-01** Numbered steps. Each step is one concrete action. [R]
- **R-L2-PR-02** "Be specific enough that two different agents following these steps would produce structurally similar outputs." [R template]
  - Too vague: "Write the script." Good: "Write the full script in one pass, then audit against the voice hard constraints and value brief."
  - Too vague: "Generate ideas." Good: "Propose 3-5 concept angles, each as a single sentence. Tag each with its value type and format."
- **R-L2-PR-03** Keep it short. Constraints live in L3 files and are not restated here. "Contracts that restate reference material (point instead)" is a named failure. [A]
- **R-L2-PR-04** MAY restate hard limits worth repeating: length, count, format ("Keep under 90 seconds spoken"). [A]
- **R-L2-PR-05** Mark checkpoint steps inline: `**[Checkpoint N]** -- Present X to the human for Y`. [R]
- **R-L2-PR-06** The second-to-last step is usually "Run the audit checks below. If any fail, revise before saving." The last is "Save to output/". [R]
- **R-L2-PR-07** In the entry stage, step 1 collects per-run metadata conversationally (name, topic, audience, scope) and writes it to `output/[slug]-meta.md`. [R]
- **R-L2-PR-08** Frame process steps as production ("read X, produce Y"), not exploration ("help me explore X"). [X][I]

**Outputs**

- **R-L2-OUT-01** Table form `Artifact | Location | Format` [R], or list form `- script_draft.md → output/` [A][P].
- **R-L2-OUT-02** Every output MUST be consumed by a downstream stage or be the final deliverable. [R]
- **R-L2-OUT-03** SHOULD say that the output is the human's edit surface and the next stage reads whatever is there. [R][A]

**Human check**

- **R-L2-HC-01** Exactly one human check, stated as something a person *does*, not a vague "review". Examples: "Read the draft aloud." "Verify the numbers against X." "Confirm the argument order survived from research." Close with: "Edit in place; the next stage reads whatever is here." [A]

**Verify (proposed)**

- **R-L2-VER-01** Where final output can drift from earlier decisions, a stage MAY carry a Verify section naming which earlier outputs to check for consistency and against what criteria. The agent runs the checks and flags discrepancies before the human reviews. Today this exists as an "audit file" that makes the agent trace the spec back to the script and re-verify the timing of each phrase. It catches "frame count discrepancies, visual density mismatches, and pacing breaks at scene boundaries". [P §6.2]

### 10.4 Purity and size

- **R-L2-01 CONTEXT.md is routing, not content.** It answers three questions: what is this folder, what do I load, what is the process. "No definitions. No rules. No extended examples. No voice guidelines." [R Pattern 6]
- **R-L2-02** "If you find yourself writing more than a one-sentence description in a CONTEXT.md, that content belongs in a separate file that the CONTEXT.md points to." [R]
- **R-L2-03** Allowed sections only: title, description, Inputs, Do NOT load, Process, Checkpoints, Audit, Outputs, Human check (and Verify). [R WB check 6][A]
- **R-L2-04** 25 to 80 lines. MUST be under 80. [R]
- **R-L2-05** Warning signs of an over-large CONTEXT.md: more than 80 lines, code examples, "Why it works" sections, information duplicated from another CONTEXT.md. [O]
- **R-L2-06** It doubles as human documentation (literate programming). [P]

(Tier 1 room CONTEXT.md files are looser: what the room is for, its process, its files, its skills, what good looks like, what to avoid. Same limits: under a page, no payload. [F])

---

## 11. Stage Design Rules

### 11.1 Where to cut stages

- **R-STG-01 One stage, one job.** If a stage does two jobs, split it. [P][A]
- **R-STG-02 Cut where the human naturally pauses to check.** "Their pauses become stage boundaries. Their 'I always check X before Y' become human gates. Their 'it always has to sound like / follow Z' becomes factory reference material." [A]
- **R-STG-03 Surface the judgment call before the expensive work.** "Surfacing the judgment call (an outline, a structural plan) as an editable file before the expensive downstream work is the whole trick. Correction is cheapest at the earliest gate." [A][P §4.3] Put a boundary right after any decision that determines everything downstream.
- **R-STG-04** Give each stage a focused, scoped task, not "a monolithic instruction to do everything in a single pass". [P §3.3]
- **R-STG-05** Prefer tightly scoped stages (clear instructions, limited reference material, a specific output format). They produce more consistent results than broad ones. "The structure of the context delivery... may matter as much as the content of the context itself." [P §5.4]
- **R-STG-06** Mechanical steps that need no AI become local scripts called from the stage (§15.2). [P]
- **R-STG-07** Classify every stage: **creative** (writing, design, ideation), **build** (code, assembly), or **linear** (extract, convert, render, validate). Creative stages need checkpoints and audits. Build stages need audits. Linear stages MAY run straight through. [R]
- **R-STG-08** The point of stages is optionality: "The AI can automate all four or you can get deeply involved at any step. That is the whole point of having it broken into stages." [PB 1.1]
- **R-STG-09** Some steps are faster by hand (timing nudges in a video editor): "a video editor task, not an AI task." Leave them to the human tool. [PB 1.1]
- **R-STG-10** Start short. Prove the pipeline on a small deliverable (a 30-second animation) before scaling to a large one (10 minutes). [PB 1.1]
- **R-STG-11** Prefer reusable components and templates so the agent assembles proven parts instead of inventing them each run (a component library, a slide-pattern library). [PB 1.1][R]

### 11.2 Checkpoints (inside a stage) [R Pattern 11]

- **R-CHK-01** Creative stages MUST have at least one checkpoint.
- **R-CHK-02** "The agent completes a full unit of work, presents options or a draft, and the human redirects before the next unit begins. Checkpoints go between process steps, not within them."
- **R-CHK-03** Table: `After Step | Agent Presents | Human Decides`. Step numbers MUST point at real process steps.
- **R-CHK-04** Good checkpoint patterns: show 3 to 5 options (angles, concepts) to choose from; show a brief (concept, value slots, format, hook, close) for confirmation before drafting; show an extraction or plan for a completeness check.
- **R-CHK-05** Delete the Checkpoints section if the stage runs straight through.

### 11.3 Audits (before writing output) [R Pattern 12]

- **R-AUD-01** Creative and build stages MUST have an Audit table `Check | Pass Condition`.
- **R-AUD-02** It runs after the process and before writing to `output/`. "If any check fails, the agent revises before saving to output/."
- **R-AUD-03** "Each check should be specific enough that pass/fail is unambiguous." Good: "Em-dash count: zero"; "The tension lands within 2-3 seconds"; "Every chunk traces back to a specific source"; "Word count within ±10% of budget". Bad: "Quality is good".
- **R-AUD-04** Audits catch problems before they spread downstream. They are each stage's quality floor.

### 11.4 Value validation (content stages) [R Pattern 13]

- **R-VAL-01** Content workspaces define their value types once in a reference file. Examples: NOVEL, USABLE, QUESTION-GENERATING, INTERESTING; for courses, TEACHES, PRACTICES, CHALLENGES.
- **R-VAL-02** Before the main creative work, at a checkpoint, the agent and human lock which value types this piece will deliver. Minimum 2. "Two strong value slots are better than four weak ones. Three is ideal."
- **R-VAL-03** The audit checks the output delivers the locked slots. This prevents "interesting but doesn't DO anything" output.

### 11.5 Specs are contracts (spec → build splits) [R Pattern 10][PB 1.1]

- **R-SPEC-01** Spec stages define WHAT the output must achieve and WHEN things happen, not HOW to build it.
- **R-SPEC-02** A spec contains (animation example): a beat map with approximate durations, narration, and mood; a visual philosophy (what a muted viewer should understand); 2 to 3 key moments that MUST land, and why; audio sync points; color flow.
- **R-SPEC-03** A spec MUST NOT contain implementation choices: frame numbers, component names, pixel positions, spring configs, prop definitions, code.
- **R-SPEC-04** The split: "spec = WHAT/WHEN, design system = quality floor, builder = HOW." "Creative freedom means choosing how to implement those requirements, not whether to implement them." [R]
- **R-SPEC-05** The spec is "the most important file in the entire workflow... a contract between the voiceover and the animation." "Putting code-level detail in the spec actually constrained Claude and made the animations worse." [PB 1.1]
- History: the origin system wrote specs as "code blueprints" and called that "the biggest single improvement". v2 reversed it, because prescribing HOW "removes creative freedom from the build stage and produces rigid, uncreative output". Follow the contract form. [O][R]

### 11.6 Docs over outputs [R Pattern 14]

- **R-QUAL-01** Agents MUST NOT read previous `output/` files to learn patterns. Reference docs are the authority on how to build. "Early outputs are the worst outputs. If future agents learn from them, quality never improves." Build-stage contracts SHOULD carry the line "Do not read other output/ files to learn patterns."
- **R-QUAL-02** Examples placed next to a rule MUST agree with it, because "a model copies examples before a model follows rules." [X, crediting Jake's own audit]

### 11.7 Shared constants (code workspaces) [R Pattern 15]

- **R-CONST-01** Configurable values (colors, fonts, timing, layout) live in one shared file that every build output imports (`import { COLORS, FONTS } from "../constants"`). The questionnaire fills it once. This is canonical sources applied to code.
- **R-CONST-02** Non-code workspaces keep shared values in reference docs instead.

---

## 12. Reference Material, Routing, and Running a Pipeline

### 12.1 Reference files (L3)

- **R-REF-01** Reference files MUST be under 200 lines. Split longer ones. [R]
- **R-REF-02** Reference files hold the rules, definitions, examples, and templates that CONTEXT.md files may not. [R]
- **R-REF-03 "Write for machines, store for humans."** Source docs explain why each rule exists; the routing layer pulls out only the what. A file MAY carry a "Strategic Rationale" section that section routing usually skips. [O][R]
- **R-REF-04** Design-system references SHOULD include **Recipes** (copy-and-adapt patterns), an **Anti-Patterns** table (`Error | Why It Fails`), and a **Production Checklist** the build audit references. [R]
- **R-REF-05** Tool setup guides go in the `references/` of the stage that uses the tool, or in `_shared/` if several stages need it. Write them for someone who has never installed the tool: what it is (one sentence), install steps, how to verify, how the workspace uses it. Tools bundled inside skills need no separate guide. [R Pattern 7]
- **R-REF-06** Brand and identity folders are READ-ONLY during runs: "It's the DNA." Downstream stages MUST NOT overwrite them. In a conflict, the brand file wins. [O][R]
- **R-REF-07** Use the person's real assets (their brand, their voice, their examples), not sample templates. "The value only shows up when the system reflects your actual brand." [PB Claude Design]

### 12.2 Voice file structure [R]

A voice file (`voice-rules.md` or `_shared/voice.md`) has five parts:

1. **Hard Constraints**: "These are errors. If the output contains any of these, rewrite." A numbered list. Jake's own include: no filler transitions ("Now let's talk about..."), no recap summaries at the end of sections, no hype language ("game changing", "revolutionary"), and never em dashes.
2. **Sentence Rules**: a `Wrong | Right` table of verbatim examples ("They invested significant time in infrastructure development." → "They spent six months building a custom pipeline.").
3. **Pacing**: the rhythm ("setup, dense, dense, breath, dense").
4. **What the Voice Is NOT**: named anti-patterns with Bad and Good examples: not performative (never announce credentials), not antithetical ("not X, but Y" at most once per piece), not rhetorically questioning.
5. **Strategic Rationale**: why the choices fit the audience. Usually not loaded.

Rule: **examples over descriptions**. "Examples are pattern-matchable. Descriptions require interpretation and produce weaker constraints." [R]

### 12.3 One-way references [R Pattern 3][O]

- **R-XREF-01** "Every folder points outward to what it needs. No folder points back." If stage 03 references stage 02's component registry, stage 02 references nothing in stage 03. A brand folder serving several stages references no stage.
- **R-XREF-02** Before adding a reference, ask: "Does the target file already reference my folder? If yes, restructure."
- **R-XREF-03** The dependency graph MUST be a DAG. This keeps reference growth linear instead of N-squared.
- **R-XREF-04** If B would need to point back at A, you probably need a third location C that both reference. [O]
- **R-XREF-05** A later stage MAY read an earlier stage's `references/` file instead of copying it. A workspace MAY point at a sibling workspace's skill instead of bundling it twice. [R]

### 12.4 Canonical sources [R Pattern 5][A][F]

- **R-CANON-01** Every piece of information has ONE home. Other files point there.
- **R-CANON-02** Smell test: search the workspace for a specific phrase. If two files hold it and both are meant to be authoritative, make one a pointer.
- **R-CANON-03** A pointer file MAY stand in for a copy, stating "This file is a pointer, not a copy. Do not duplicate content from X here." [R]
- **R-CANON-04** When removing a duplicate, leave a link where the copy was if anything referenced it. [A]
- **R-CANON-05** Map the information architecture before writing prompts: what exists, where each piece canonically lives, and which tasks need which pieces. [O]

### 12.5 Recursive routing

- **R-ROUTE-01** Any folder that grows past easy scanning gets its own `CONTEXT.md` router. [A][P]
- **R-ROUTE-02** "Each level has its own small catalog, and no level's catalog describes the internals of the level below; it links down and stops." [A]
- **R-ROUTE-03** A folder's `CONTEXT.md` SHOULD say what does NOT belong there and point to where it lives ("Plans/events live in [[../plans/CONTEXT.md]] instead"). [M]

### 12.6 Handoffs

- **R-RUN-01** Stage N writes `stages/NN_name/output/[slug]-[artifact].md`. Stage N+1's Inputs reads it by exact path. "No state management. No orchestration layer. Just files in predictable places." [R Pattern 2]
- **R-RUN-02** The handoff chain MUST be unbroken: stage N's output location matches stage N+1's input reference. [R]
- **R-RUN-03** Each stage output MUST be a complete, readable artifact that "captures the work done so far and provides everything the next stage needs to continue." [P §3.3]
- **R-RUN-04** The entry stage collects per-run metadata (project name, topic, audience), writes it to its `output/`, and it is copied forward through each stage's output. It is never a setup placeholder. Any stage MAY be the entry point; if so, it collects the metadata itself. [R]
- **R-RUN-05** A stage MAY read more than its immediate predecessor (a validation stage reads stages 03 and 04). Declare it in Inputs. [R]
- **R-RUN-06** Tell the agent where to put every output: a named file in a named folder, never only the chat. ("Save the result as summary.md in this folder.") [F 4.2]

### 12.7 Human review between stages

- **R-HUM-01** "Nothing moves to the next stage until a person has read the output of the last one." [A]
- **R-HUM-02** At each gate the human may: proceed; edit the output file directly, then proceed; re-run the previous stage with different input; or abandon the run. [P §5.3]
- **R-HUM-03** Editing an output is "the primary way to steer the pipeline." [R]
- **R-HUM-04** Branching decisions belong to the human, made between stages. [P]
- **R-HUM-05 The U-curve.** Expect heavy editing at stage 1 (direction-setting, creative judgment), light editing in the middle (held in place by the upstream output and the reference material), and heavy editing at the last stage (alignment, closer to debugging). In the paper's practitioner group, 30 of 33 reported this, at roughly 92%, 30%, and 78% edit frequency across three stages. "Design the first and last outputs to be especially easy to edit." [P §4.5][A]
- **R-HUM-06** When an output is wrong, say what is wrong and iterate. Do not start over: "Starting over throws away all the context." [F 4.2]

### 12.8 Status: the filesystem is the state machine

- **R-STATE-01** The `status` trigger scans `stages/*/output/`. A stage is COMPLETE when its output folder holds an artifact other than `.gitkeep` (list the filenames); otherwise it is PENDING. Render an ASCII pipeline: [R]

```
Pipeline Status: [workspace-name]

  [01_research]  ------>  [02_script]  ------>  [03_production]
     COMPLETE               PENDING               PENDING
  (topic-brief.md)          (empty)               (empty)
```

- **R-STATE-02** "A placeholder that only keeps the empty folder in git does not count." [A]
- **R-STATE-03** In record and graph forms, status lives in frontmatter or a generated index log, never in a hand-kept tracker. [A]

### 12.9 Re-running and change propagation

- **R-RUN-07** Re-run only the stage that needs it. "If the research output is fine but the script needs rework, the practitioner re-runs stage 2 without touching stage 1." [P §6.1]
- **R-RUN-08** A stage's Inputs table declares its dependencies. A change to any of those files means the stage's output may be stale: re-run it and everything downstream. "Changed script? Regenerate spec. Changed spec? Rebuild composition." [P][O]
- **R-RUN-09** Flow is one-way. "Don't reverse-engineer earlier stages from later ones." [O]
- **R-RUN-10** When a later artifact becomes the source of truth (recorded audio over the script), say so in a "Source of truth at each stage" table, and re-derive everything downstream when it changes. "If the audio differs from the script, the audio wins." [R]
- **R-RUN-11** To start a fresh run, clear (or archive) the previous run's output folders. [R]
- **R-RUN-12** Error recovery is a manual re-run of the failed stage. [P]

### 12.10 The edit-source principle [P §6.3]

- **R-EDIT-01** "Editing the output fixes this run. Editing the source fixes every future run." Editing the output is "patching the binary"; it does not improve the compiler.
- **R-EDIT-02** One-off creative edits that cannot be reduced to a rule are legitimate output edits.
- **R-EDIT-03** Recurring edits are debugging information. If the same kind of edit happens in the same stage about three runs in a row, move it into the source: a contract amendment ("keep the opening under three sentences"), a stronger reference example, or a new constraint.
- **R-EDIT-04** When output is wrong, check the three possible sources in order: (a) the reference material is underspecified, (b) the stage contract stresses the wrong quality, (c) the previous stage's output framed things wrongly.
- **R-EDIT-05** "Every constraint you give is a mistake Claude will not make." Turn each recurring annoyance into a written constraint. [F 1.3]

### 12.11 Version control, portability, secrets

- **R-GIT-01** A workspace is a folder. Copy it, git it, zip it, sync it. No server, no deployment step. [P §3.4]
- **R-GIT-02** The ICM template repo gitignores stage outputs (`**/stages/*/output/*` except `.gitkeep`) so templates ship clean. A live deployment MAY commit outputs after each run to build "a version history of the entire production pipeline's behavior over time". Templates: do not commit outputs. Deployments: commit them if history matters. [R][P]
- **R-GIT-03** Handing off a workspace is copying the folder; the recipient edits prompts without a developer. [P]
- **R-SEC-01** Secrets live in `.env`, never in committed files. Confirm `.env` is in `.gitignore`. Provide `env-template.md` with empty values. Also gitignore `node_modules`, build output, and any private markdown (voice docs, client files); ask "would I be comfortable if a stranger read this file?" [R][PB 3.2]
- **R-SEC-02** Several agent sessions MAY work in one folder, kept coordinated by the shared CLAUDE.md. [PB 3.2]
- **R-SEC-03** Data with access limits SHOULD be marked (for example an `access_tier` frontmatter field) so private raw material does not leave the machine. [A forms]

---

## 13. Sessions, Memory, and Planning

### 13.1 The workspace is the memory [PB 2.4][PB Stack 1.3]

> "Claude is stateless. Your workspace is stateful. The workspace is the memory."

What to persist:

| Layer | What | When |
|---|---|---|
| Project definition ("what are we building") | PRD or spec, CLAUDE.md, the folder structure | Always |
| Progress markers ("where are we") | `PROGRESS.md` or `STATUS.md`: done, in progress, blocked | After meaningful milestones |
| Session notes ("why did we do that") | Key decisions and their reasons | When you would be frustrated to forget them |

- **R-SESS-01** Keep a `PROGRESS.md` at the project root with: Current Status, Last Session (date; completed, in progress, blocked, next), Decisions Made (with reasons), Open Questions. [PB 2.4]
- **R-SESS-02** Start a session with "Read CLAUDE.md and PROGRESS.md. What's the status? What should we work on next?" End it with "Update PROGRESS.md with what we accomplished and what's next." "This takes 30 seconds and saves you 10 minutes of re-orienting next time." [PB 2.4]
- **R-SESS-03** Before hitting token limits, write progress into files and start a fresh session. [PB][F 4.5]
- **R-SESS-04** After a session ends unexpectedly, check the files against the progress notes: "Don't assume the last task completed. Check." [PB 2.4]
- **R-SESS-05** Record decisions with their reasons: the reason "is what stops the argument happening twice". [X RyMac, consistent with PB]

### 13.2 Plan before you build [PB 3.3][PB Stack 1.1 to 1.3][F 4.3]

> "Spend your thinking before you spend your tokens." "15 minutes of thinking saves 90 minutes of building the wrong thing."

- **R-PLAN-01 Decide, then build.** "Desktop for decisions. Code for execution. If you try to decide and build at the same time, both suffer." [F 4.3]
- **R-PLAN-02** In planning chats, start with what you are trying to accomplish, not the thing you want produced. Prompt for thinking ("What am I not seeing?"). Push back on the first answer. [F 4.3]
- **R-PLAN-03 The pre-build sequence** [PB 3.3]:
  1. Analyze what already exists, in chat.
  2. Have the chat write a markdown briefing "for Claude to read, not for me". It carries the context from chat into Claude Code.
  3. First build prompt sets boundaries: the folder structure (including CLAUDE.md), the deployment target, the scope (what you are *not* building yet), the tech preference, and it ends with "ask me three questions to understand more" ("the most important line").
  4. Answer the questions.
  5. "Create a PRD file... Do not start building yet." Review and edit it.
- **R-PLAN-04** A whole project SHOULD take under 10 prompts: about 4 to 5 for planning and 2 to 3 for building. [PB 3.3]
- **R-PLAN-05** The PRD is "stateful prompting": persistent context the agent re-reads. Another session MAY audit it ("What's overcomplicated?"). When the agent drifts, point it back at the document. "Let it be smarter than your instructions when it makes sense." [PB Stack 1.1 to 1.3]
- **R-PLAN-06 The build process** [PB Stack 1.1]: define the need → research what exists ("Don't reinvent the wheel... Make the wheel yours") → map the existing structure → write the PRD → **build inside your workspace**, not in a separate folder, so the context is already there → work in sessions.

### 13.3 Memory workspaces built by the agent [M]

When the agent itself files knowledge over time (long-term memory, a "second brain"), see §18.7.

---

## 14. Prompting Inside the System [F 1.3][F 4.2]

### 14.1 The five-part prompt

"A prompt is an instruction set." Five parts: **Identity, Task, Context, Constraints, Output Format**. "You will not use all five every time. But knowing them means you always know which one is missing when the output is not right."

| Part | What it carries | Rule |
|---|---|---|
| **Identity** | Who Claude is right now | "The part most people skip... The output is always more generic without it." CLAUDE.md handles it at project level. |
| **Task** | A clear action, a defined scope, enough detail | **Stranger test**: "If you read your task out loud and a stranger could not start working on it without asking you five follow-up questions, the task is too vague." |
| **Context** | Audience, prior decisions, data | "If the output feels generic or off-target, the fix is almost always more context, not a better prompt." |
| **Constraints** | What to avoid, limits | "Every constraint you give is a mistake Claude will not make. Think about the last three times an AI output annoyed you. Those annoyances are constraints you did not set." |
| **Output Format** | The shape of the answer | "The difference between getting something you can use immediately and getting something you have to reformat for 20 minutes." |

Which parts to use:

| Task type | Parts |
|---|---|
| Simple | Task only |
| Creative | Identity + Task + Constraints + Output Format |
| Complex | All five |
| Ongoing (a workspace) | Identity and Context live in the folder files; Task and Constraints go in each prompt |

"The folder is memory. The prompt is direction."

### 14.2 Prompting rules

- **R-PROMPT-01 One clear ask per prompt.** Chunk large projects into steps with review between them. "If something goes wrong at step 3, you only redo step 3. This is the same principle behind the folder architecture." [F 1.3]
- **R-PROMPT-02 Feed large inputs in order.** Give the structure or table of contents first, then sections in order with a confirmation after each, then ask for the synthesis. [F 1.3]
- **R-PROMPT-03 Be specific, and name the output location.** [F 4.2]
- **R-PROMPT-04 Correct in place.** Say what is wrong; do not start over. [F 4.2]
- **R-PROMPT-05** Claude Code's working loop is **Read → Think → Write → Check → Adjust**. It is best for tasks that read and write files. Process many files in one prompt instead of many copy-pastes (15 meeting notes at about 2k tokens each is about 30k tokens, well inside the window). [F 4.2]
- **R-PROMPT-06** When teaching an agent a repeated task by demonstration, narrate the intent, not only the clicks: "The narration matters because it tells Claude your intent, not just the coordinates of your clicks." [PB 2.3]
- **R-PROMPT-07** One model, three interfaces: Desktop/claude.ai (conversation; cannot see your files), VS Code + Claude Code (editor; "what I use for almost everything"), the terminal (command line). "If you have ever felt like Claude kind of gets it but not quite, it is probably because you are working from a pasted excerpt instead of your actual project." "The folder becomes the app. Claude Code is the thing that runs it." [F 4.1]

---

## 15. Skills, Scripts, Tools, MCP, and Sub-agents

### 15.1 Skills in a workspace [R Pattern 9][F 3.1]

- **R-SKILL-01** Wire each skill into the rooms or stages that need it. Never load every skill everywhere. [F 3.1][R]
- **R-SKILL-02** A workspace MAY bundle skills into `skills/<name>/` (`SKILL.md`, optional `rules/`, `scripts/`) so it is self-contained without global installs. [R]
- **R-SKILL-03** Discovery, during workspace design: scan `~/.claude/skills/` and `~/.agents/skills/`, search public skill repos for the domain, show candidates, let the user choose. [R]
- **R-SKILL-04** Bundle by copying (local) or cloning (remote) into `skills/` during scaffolding. [R]
- **R-SKILL-05** Reference skills from Inputs as "Index, then load rules as needed": read `SKILL.md`, then only the rule files this step needs. "Claude does not read all of them at once. It reads the parts relevant to the current task." [R][PB 1.1]
- **R-SKILL-06** A skill REPLACES a custom reference doc that covers the same ground. Delete the duplicate and point at the skill. [R]
- **R-SKILL-07** Keep workspace-specific files (design system, brand, build conventions) beside skills, not inside them. [R]
- **R-SKILL-08** MUST NOT bundle skills about the agent tool itself (skill-creator, mcp-builder). Bundle only runtime domain knowledge. [R]
- **R-SKILL-09** Prefer CONTEXT.md and reference files before reaching for a skill, to save tokens. [O]
- **R-SKILL-10** A named folder with its own context is already "the agent" for that job. Most "I want an agent for X" requests are "I want the AI to keep X in mind", which is a reference file. [V "Stop Buying Agent Tools"][X]

### 15.2 Scripts for mechanical work

- **R-SCRIPT-01** "Local scripts handle the mechanical work that does not need AI at all": fetching data, moving files, formatting output, sending email, rendering, transcription, rebuilding indexes. [P][M]
- **R-SCRIPT-02** Scripts SHOULD offer a dry run before any expensive or external call (`--dry-run` before generating audio). [R][I]
- **R-SCRIPT-03** Generated files (indexes, tables, numbers) come only from scripts. "Do not type a number into a .tex file." Anything hand-copied eventually contradicts the data. [M]

### 15.3 Tools and MCP

- **R-TOOL-01** Scope tool definitions to individual stages or rooms. Load only the tools the current step needs; loading every tool definition up front slows agents and raises cost. [P §2.2][F]
- **R-TOOL-02** External services come in through local scripts or MCP connections, called from a stage. [P]

### 15.4 Sub-agents

- **R-SUB-01** One orchestrating agent runs the pipeline. It MAY hand sub-tasks inside a stage to faster sub-agents, and the folder structure drives the delegation: the orchestrator reads the stage's CONTEXT.md and L3 files to decide what to delegate and what context each sub-agent gets. "There is no separate orchestration framework." [P §4.1, §4.2] (The paper's setup: Claude Code with Opus orchestrating and Sonnet sub-agents.)
- **R-SUB-02** Sub-agents and plan mode are fine as tool features; the architecture stays the folder. [PB Stack 1.3][I]
- **R-SUB-03** The method is model-agnostic. It specifies folder structure, file formats, and naming, so any capable model can be pointed at the same files. A memory built by one vendor's model was read by another's at equal accuracy. [P][M][PB Claude Design]

---

## 16. Writing Skills in Jake's Style

The user's goal includes building skills. Jake's own skills (icm-architect, lecture-deck, whisper-beat-finder, elevenlabs-narration, remotion-scene-anatomy) share a consistent shape. This section is derived from those files. [A][R][I]

### 16.1 Skill anatomy

```
skill-name/
├── SKILL.md            the method on one page: what, when, procedure, rules, file index
├── references/         depth, one concern per file, read only when SKILL.md says so
├── rules/              (alternative to references/) one rule topic per file
├── assets/templates/   copyable starters the skill instantiates
└── scripts/            mechanical work (render, transcribe, check, build)
```

### 16.2 SKILL.md rules

- **R-SKW-01 Frontmatter `description` is a router.** It states what the skill does, lists concrete trigger situations and literal trigger phrases ("make this an ICM", "ICM this", "structure this for agents"), and says what it is NOT for ("Not for pitch decks that must be PowerPoint"). [A][lecture-deck]
- **R-SKW-02 Open with the method in one paragraph**, plus one governing metaphor if it helps (the library). [A][lecture-deck]
- **R-SKW-03 State the invariants or "the rules that make it good"** as a short bold-titled list. [A][lecture-deck]
- **R-SKW-04 Give a numbered procedure** ("When you get a request: 1... 7..."), with modes if the skill has more than one job (Build vs Restructure). [A][lecture-deck]
- **R-SKW-05 Include a validation step** the agent runs before delivering (walk test, render-and-look, register check). [A][lecture-deck]
- **R-SKW-06 Name guardrails and where the method loses**, honestly. [A]
- **R-SKW-07 End with a file index** that says when to read each reference ("Read when writing contracts or when a structural call is contested"). This is selective section routing applied to the skill itself. [A]
- **R-SKW-08 Push depth down.** SKILL.md stays one screen to a few screens; references hold detail; templates hold shapes; scripts hold mechanics. [A][R]
- **R-SKW-09 Skills that wrap a tool** follow: `## When to Use` (which stage, what it outputs, who reads the output) → `## What You Need` → defaults with reasons (for example why CPU over GPU) → `## How It Works` (numbered) → `## Scripts` → `## Output Format` (the exact table the next stage reads). [R whisper-beat-finder]
- **R-SKW-10** Skills MAY carry placeholders that the workspace's `setup` fills (`{{WHISPER_MODEL}}`). [R]

---

## 17. Procedures

### 17.1 Build a Tier 1 simple workspace (15 minutes)

1. Ask: what kinds of work does this person do in this project? Apply the mental-mode test (R-T1-03) to get 2 to 3 rooms.
2. Create the root folder named after the work, and one folder per room.
3. Write each room's `CONTEXT.md` (under a page, about 80% about the work): what it is for, its process, what files live there and how they are named, which skills or tools to use, what good looks like, what to avoid. Point to reference files instead of pasting long material.
4. Write `CLAUDE.md` (30 to 50 lines): identity line, rooms, routing table (Task | Go to | Read | Skills), naming conventions, a few workspace-wide rules.
5. Add subfolders only where a room already holds more than 8 to 10 files or has clear stages (drafts/final).
6. Start working. Revisit after a few days; update context files whenever the project changes.

### 17.2 Build a Tier 2 or Tier 3 workspace (Build mode) [A][R workspace-builder][P §4.4]

**Step 1. Extract the structure from dialogue.** "The structure is already in how the person describes the work; don't impose a shape, surface theirs." Ask a few questions at a time, not all at once: [A]

1. What is the repeating unit of work? (an episode, a client, a report, a person, a team?)
2. Walk me through one run, start to finish. Where do you stop and check something before continuing?
3. What stays the same every run (voice, rules, brand, schema), and what is new every run?
4. What does "done" look like? What artifact leaves the workspace?
5. Who else touches this, and what do they need to find without asking you?

Map the answers: pauses → stage boundaries; "I always check X before Y" → human gates; "it always has to sound like / follow Z" → factory reference material.

Then, for each stage, ask: what goes in, what comes out, what does the agent need to know? Also find: context shared across stages; user-specific values (→ placeholders); optional stages (→ conditionals); tools that need installing (→ setup guides); relevant skills (→ bundled). Present the workflow map for confirmation (checkpoint). [R 01-discovery]

**Step 2. Pick the form** (§18).

**Step 3. Map contracts and dependencies** [R 02-mapping]: write each stage's Inputs/Process/Outputs; map cross-references; pick canonical sources; draw the dependency graph and confirm it is a DAG; confirm every output is consumed or is the final deliverable; present the diagram and contracts (checkpoint).

**Step 4. Scaffold the smallest structure that carries the work** [A][R 03-scaffolding]: root `CLAUDE.md`; root `CONTEXT.md`; `setup/questionnaire.md` if the factory needs configuring; the factory folder (`_shared/`, or a brand/design folder with its own CONTEXT.md if large); `stages/NN_name/{CONTEXT.md, references/, output/}`; `skills/` if any; `_templates/` if units are created by copying; `.gitkeep` in every `output/`. Add a value framework for content workspaces and a constants file for code workspaces. Structure voice rules as Hard Constraints / Sentence Rules / Pacing, not a single description placeholder. Delete Checkpoints and Audit sections that do not apply. Do not create folders for stages that do not exist yet. If the job fits in one saved prompt, stop and say so.

**Step 5. Design the questionnaire** [R 04-questionnaire-design]: scan for every `{{` placeholder; split system-level values (→ questions) from per-run values (→ the entry stage collects them); write flat, all-at-once questions with defaults; examples over descriptions for voice; derived fields; yes/no for optional stages; a two-pass review for derived voice rules.

**Step 6. Validate** with §19. Fix the structure, then re-run the failed checks.

**Step 7. Run it once end to end.** At least one complete run MUST finish before the workspace counts as done. [R]

### 17.3 Restructure an existing folder (Restructure mode) [A]

1. **Inventory before touching.** List the tree. For each area, note what it is, when it was last touched, and what refers to it. Never delete or move anything in this pass.
2. **Find the hidden form.** Ask the owner, or infer and confirm: what is the repeating unit here? Where does work enter and leave? "The mess usually contains a real pipeline, library, or map that grew without a skeleton; extract it, don't replace it. Interview the folder the way you'd interview the person."
3. **Classify every file** into one role:
   - **Catalog**: identity or routing (becomes or feeds `CLAUDE.md` and index files)
   - **Contract**: describes how a step works (becomes a `CONTEXT.md`)
   - **Factory**: stable reference (→ `_shared/`, `_system/`, `references/`)
   - **Product**: run-specific artifacts (→ stage `output/` or record folders)
   - **Dead**: stale, duplicated, or superseded (→ propose `_archive/`, never delete silently). A file is Dead only after step 4 shows nothing depends on it. "Apparent disuse is not proof."
4. **Check reference integrity before proposing.** List what points at each file you plan to move: references inside the workspace; sibling-path `../` references (these break when folders regroup); symlinks; external consumers (other repos, deploy scripts, cron, issue trackers, agent configs). External consumers are a question for the human, not an endless grep. A file with a live referrer is held, or moved only if every referrer is updated in the same change.
5. **Propose before moving.** Show the target tree and a migration map (`old path → new path → role → referrers found`). Get approval. The reviewer approves against the reference report, not a hunch.
6. **Migrate: copy, verify, then remove.** First confirm the workspace root is tracked or backed up. Before any copy or rename, check whether the destination already exists **case-folded** (on Windows and macOS, `CLAUDE.md` → `CONTEXT.md` can silently overwrite an existing `context.md`); raise any collision at the approval gate. Copy, verify parity (file count + content hash; for zipped office formats compare unzipped content), and only then remove the original, leaving a pointer if anything referred to it. Write the entry file and contracts. De-duplicate toward one home per fact. Keep the method (blank template) apart from this instance.
7. **Validate with the walk test** (§19.1), including "does every reference that existed before the move still resolve?"

---

## 18. The Six Forms [A forms]

Choose by asking: **what is the repeating unit of work?**

| The unit is... | Form | Optimizes for |
|---|---|---|
| a run (same stages, new deliverable each time) | **Pipeline** | Repeatable production with review gates |
| several kinds of runs sharing one identity | **Umbrella** | Shared brand and voice across distinct pipelines |
| a record that accumulates (person, client, session) | **Record library** | Uniform shape and retrieval |
| the knowledge itself (claims, notes, evidence) | **Knowledge bundle** | Navigable knowledge, layered loading |
| an organization (teams, processes, data, handoffs) | **Context map** | The org as a graph; automation candidates |
| a folder later agents must edit (code, markdown, mixed) | **System map** | Change impact without reading the whole tree |

(The Tier 1 simple workspace is closest to an Umbrella of rooms, with no pipelines yet. [I])

### 18.1 Pipeline: the production line

Skeleton in §7.1. Defining moves: the handoff is `output/` → next input; each contract has load and do-NOT-load lists; `status` scans `stages/*/output/`; boundaries sit where the human pauses; expect the U-curve. Watch for: stages doing two jobs; contracts restating reference material; pipelines built before the process has repeated.

### 18.2 Umbrella: a portfolio of pipelines

```
workspace/
├─ CLAUDE.md               the map: what lives where, which pipeline for which job
├─ 01-pillars/             shared factory: positioning, pillars
├─ 02-brand-voice/         shared factory: voice, style
├─ 03-video-production/    a full Pipeline workspace (own CLAUDE.md)
├─ 04-scene-generation/    a full Pipeline workspace (own CLAUDE.md)
└─ 05-animation-studio/    a full Pipeline workspace (own CLAUDE.md)
```

Each sub-pipeline is self-contained with its own entry file and shares no state except the root reference layers. The root routes by task ("making a talking-head video → 03; animating a diagram → 05") and holds nothing else. A pipeline MAY host sibling patterns (two variants of one line, such as record-then-cut vs animation-first). Watch for: a stale root map (state only what rarely changes); shared reference copied into sub-pipelines (link up instead).

### 18.3 Record library: the unit is a record

```
workspace/
├─ 00_START-HERE.md        the map (identity + routing in one file)
├─ _index/                 catalog: log.md, one line per record, id + status
├─ _templates/
│  └─ record-template/     every record starts as a copy of this
├─ 01_reference/           factory: the method, rules, shared knowledge
└─ records/
   ├─ acme-corp/           each record has the same internal shape
   └─ jane-doe/
```

A new record is a copy, not a blank page; "the template is the schema". The index log is the declared source of truth: one line per record, with a small lifecycle (`briefed → active → archived`). The naming convention doubles as an ID scheme. Records may recurse (a record holding its own mini pipeline or knowledge bundle). Watch for: records drifting from the template (re-stamp them); the log absorbing content; half-created records (finish the stamp or archive it).

### 18.4 Knowledge bundle: the product is the knowledge

```
workspace/
├─ CLAUDE.md
├─ corpus/                 raw sources + _index.md checkbox manifest (state surface)
├─ extraction/             the factory: an ICM Pipeline whose output is the bundle
└─ bundle/                 the product:
   ├─ index.md             what's in here, layer by layer
   ├─ voice/  (layer A)    always-load essentials
   ├─ dispositions/ (B)    load-by-task
   └─ episodes/ (C)        evidence, loaded last, access-tiered
```

Every note carries typed YAML frontmatter (`type:`, `layer:`, `access_tier:`, `strength:`). Notes cross-link by relative path or wikilink; navigation is link-following, not folder-crawling; an unresolved link marks something worth writing, not an error. Reading protocol: the always-load layer first, task-relevant nodes second, evidence only when needed. Never read the whole bundle. `access_tier` gates what may leave the machine (abstracted patterns yes, raw private quotes no). Regenerating the bundle is a factory run, and every change appends to a log. Watch for: treating the bundle as a search index instead of a model (it answers "how does this think", not "find me the file"); frontmatter fields nobody queries (cut them); editing the product by hand instead of fixing the factory.

### 18.5 Context map: the organization as a graph

```
workspace/
├─ CLAUDE.md / AGENTS.md   entry (one generated from the other)
├─ FILE-MAP.md             GENERATED index; agents jump here, never crawl
├─ _meta/                  the rules: schema.md, maturity-levels.md, ritual docs
├─ teams/
│  └─ marketing/
│     ├─ Marketing.md      node card: In / Movement / Out / Edges
│     ├─ governance.md
│     ├─ jobs/             outcome nodes
│     ├─ processes/        workflow nodes (the workhorses)
│     └─ data/             data-<thing>.md asset nodes
├─ patterns/               cross-team patterns, written bottom-up only
└─ dashboards/             00-tracker.md ... live queries over frontmatter
```

A closed set of node types (team, job, process, data-asset, governance, pattern) is defined once in `_meta/schema.md`, and every node declares its `type:`. Process nodes carry scoring frontmatter: owner; `ai-level` (L0 manual, L1 copy-paste, L2 structured, L3 integrated); frequency; value 1 to 5; pain 1 to 5; `consumes:` and `produces:` as wikilinks to data assets. The links draw the org graph on their own, and value + pain ≥ 8 flags a pilot candidate. "The workshop is the data event": map live with the team, and every session ends in node files, not slides. "You don't point an agent at a legacy mess; you clean the shelf first." The librarian ritual per team: inventory → single source of truth → give it shape → catalogue → shelve by sensitivity → connect the agent. The human stays the approval gate; the agent drafts and proposes. A pattern needs three independent occurrences: "one team complaining is a gripe". Watch for: schema naming things the files stopped using; duplicate entry files; instance data tangled into the method; node types multiplying past what anyone queries.

### 18.6 System map: a body of work as an edit graph

```
subject/
├─ CLAUDE.md                 existing entry; add one row pointing at map/
└─ map/
   ├─ CLAUDE.md              catalog (generate AGENTS.md + routing.md)
   ├─ CONTEXT.md             universes + name collisions
   ├─ _meta/schema.md
   ├─ _templates/            object.md, process.md
   ├─ objects/               record library of nouns (object cards)
   ├─ processes/             real movements only (verb cards)
   └─ effects/CONTEXT.md     if you change X, open these cards
```

The subject tree stays authoritative. Cards cite `path:line` (code) or the owning file (markdown). Universes are live, leftover, and ghost (aspirations and dead types are ghost, not live). Slices are gated: inventory → catalog → nouns → verbs → impact index → re-verify; empty `processes/` or `effects/` folders are forbidden. Each card has "Hits / Does not hit", where "does not hit" names the obvious next noun that is the wrong one. Extra walk-test check: can a cold agent answer "what is X" and "what else moves if I change X" from `map/CLAUDE.md` plus one card? Watch for: copying behavior into cards; mapping intent docs as live; two hand-edited entry files; marking `verified` without a citation.

### 18.7 Memory variant: ICM as long-term agent memory [M]

A knowledge bundle or record library that the agent builds incrementally, one conversation at a time. The agent's invariants: one folder, one job, each with its own CONTEXT.md; a root CLAUDE.md under 60 lines that only routes; the catalog holds no books; one home per fact; generated indexes rebuilt by command; markdown + YAML frontmatter + wikilinks; and a structure where answering means reading the entry file, one index, and one or two leaves.

Extra rules:
- Reorganize as the picture develops: "a shape that suited ten conversations may not suit fifty."
- Do not copy sources verbatim. Record what matters.
- When adding a leaf, update the indexes above it (the folder CONTEXT.md and CLAUDE.md).
- When the place already exists, filing is "a matter of finding it instead of designing it".

Reader rules:
- Read the entry file first and follow it. Open only what you need.
- Ground every claim in something you actually read.
- Use frontmatter dates for timing. The most recent fact wins a conflict.
- Say plainly when the archive does not contain the answer, and do not accept a false premise.
- Before saying "not found", make an explicit search-exhaustiveness pass, because "a reader that has seen only what it opened cannot distinguish absent information from unfound information."

A relational or columnar store MAY sit underneath for data it is genuinely good at, with files above for the parts a person needs to read.

### 18.8 Composing forms

The forms nest because the invariants are recursive:
- a record library whose records are knowledge bundles;
- a pipeline that emits into a record library;
- an umbrella over pipelines that share one knowledge bundle as their factory;
- a context map whose team folders each grow a small pilot pipeline;
- a repo that hosts a system map beside a setup pipeline.

One rule stays absolute: each level has its own small catalog, and no level's catalog describes the internals of the level below. It links down and stops.

---

## 19. Validation

### 19.1 The walk test [A]

Walk the workspace cold, as an agent with no memory:

| # | Check | Pass condition |
|---|---|---|
| W1 | Open the root. Can you answer "where am I" and "where do I go for the current task"? | Within the entry file plus at most two more reads |
| W2 | Pick any stage or node. Does its contract name exact input paths, the job, the output, and the human check? | All four present |
| W3 | Can you state pipeline status purely by scanning `output/` folders (or node frontmatter)? | Yes |
| W4 | Is any routing file carrying content payload? | No (move it to a shelf, leave a pointer) |
| W5 | Is any fact stored in two places? | No (one home, link from the other) |
| W6 | After a restructure, does every reference that existed before still resolve? | Yes |
| W7 | Token check: entry file + one contract + its inputs | About 2k to 8k tokens |
| W8 | System map only: can a cold agent answer "what is X" and "what else moves if I change X" from `map/CLAUDE.md` plus one card? | Yes |

"If a step fails, fix the structure, not by explaining more, but by moving or splitting files until the walk works."

### 19.2 Structural checks [R 05-validation]

| # | Check | Pass condition |
|---|---|---|
| V1 | Cross-reference integrity | Every path in every Inputs table points to a real file |
| V2 | No circular dependencies | The reference graph is a DAG |
| V3 | Placeholder coverage | Every placeholder has a question; every question maps to a file containing its placeholder |
| V4 | Conditional validity | Every `{{?X}}...{{/X}}` wraps a complete section |
| V5 | Handoff chain | Stage N's output location equals stage N+1's input reference |
| V6 | CONTEXT.md purity | Only the allowed sections (R-L2-03) |
| V7 | Checkpoints in creative stages | At least one; step numbers valid |
| V8 | Audits in creative and build stages | Present, unambiguous, run before output is written |
| V9 | Contract purity in spec stages | No component names, frame numbers, props, spring configs |
| V10 | Line counts | CONTEXT.md under 80 lines; reference files under 200 |
| V11 | Naming | Lowercase kebab-case; zero-padded stage numbers; `.gitkeep` in empty `output/` |
| V12 | Tool prerequisites | Every system-level tool has a setup guide with install and verify steps; optional tools are asked about in the questionnaire |
| V13 | Quality scan | No em dashes (repo house style), no unexplained jargon, clean markdown |

### 19.3 Ongoing health checks

- **Cold-chat test**: open a brand-new session and ask a status question ("where does the busiest client stand?"). If it takes more than about two moves to find the answer, the hole is in the files. [X RyMac, consistent with W1]
- **Stale-context check**: if output quality "got worse", read the context files before blaming the model. [F 3.3]
- **CLAUDE.md test**: move CLAUDE.md out, run the same task, compare. [F 4.4]
- **Guard test**: "A guard that exists is not a guard that works. Only a planted mistake proves a guard." Plant a known error and confirm the audit catches it. [X 4R audit]
- **Rule-held-only-by-a-sentence check**: treat a rule that lives only in prose, with no audit check or structure enforcing it, as a finding. [X, crediting Jake's audit]

### 19.4 Ship checklist [R README]

- [ ] Built through the builder procedure, not assembled ad hoc
- [ ] `setup` runs cleanly and all placeholders resolve
- [ ] At least one end-to-end run completed
- [ ] No stage outputs committed (template repos)
- [ ] All CONTEXT.md under 80 lines; all reference files under 200
- [ ] Creative stages have at least one checkpoint and an audit
- [ ] No circular dependencies

### 19.5 Style guardrails [R]

- Plain English, no jargon: "If a term needs explaining, it is too specialized."
- Every markdown file readable by someone who knows markdown and git basics but has no deep engineering background.
- No em dashes in workspace files (repo convention; use `--`). Jake's voice rules treat em dashes as an error. icm-architect itself uses them, so this is a house-style choice.

---

## 20. Anti-patterns and Failure Modes

| # | Anti-pattern | Why it fails | Fix | Source |
|---|---|---|---|---|
| AP-01 | A multi-agent framework for a sequential, reviewed workflow | Overhead the problem does not need; opacity; developer dependency | One agent + folders | [P] |
| AP-02 | Context-stuffing ("photocopying the library into a backpack") | 30k to 50k token prompts; diluted attention | Layered loading; Inputs; Do NOT load | [P][A] |
| AP-03 | CLAUDE.md as brain dump, project brief, or style guide (over 40 to 60 lines) | Paid on every prompt; context files hiding inside it | Move content into room or reference files | [F 3.3][A] |
| AP-04 | No routing table, or routing that works "sometimes" | Inconsistent loading and output | One row per kind of work | [F 3.3] |
| AP-05 | Too many rooms | Upkeep outgrows the work | 2 to 3 rooms; mental-mode test | [F 3.3] |
| AP-06 | Context files that describe the AI instead of the work | The model responds to the work, not to personality | 80% work, 20% behavior | [F 3.3] |
| AP-07 | Never updating context | Claude seems to "get worse" | Update as you go; "Last updated" line | [F 3.3] |
| AP-08 | Everything in one flat folder | Wrong file picks | Subfolders beyond 8 to 10 files | [F 3.3] |
| AP-09 | Building the whole system before using it | "Built the factory without ever making a product" | 15-minute first version; grow from use | [F 3.3] |
| AP-10 | Routing files that carry payload; CONTEXT.md over 80 lines, with code or "why it works" sections | Bloat, staleness, duplication | Move payload to a shelf, leave a pointer | [A][R][O] |
| AP-11 | The same rule in two files | They drift | One home per fact, a pointer elsewhere | [R][A] |
| AP-12 | `CLAUDE.md` and `AGENTS.md` both hand-edited | Drift | Generate one, or a one-line pointer | [A] |
| AP-13 | Hand-edited generated indexes | They drift from the files | Rebuild by script | [A][M] |
| AP-14 | A schema naming things the files stopped using | Rot | Reconcile the same day | [A] |
| AP-15 | Circular references between folders | N-squared growth | One-way references; a third shared location | [R][O] |
| AP-16 | Stages that do two jobs | Muddy handoffs, weaker output | Split | [A] |
| AP-17 | Contracts restating reference material | Duplication, drift | Point instead | [A] |
| AP-18 | Vague process steps ("write the script") | Output you cannot reproduce | Concrete, one-action steps | [R] |
| AP-19 | A vague human check ("review") | Nobody knows what to verify | One concrete act | [A] |
| AP-20 | Specs that prescribe HOW (frame numbers, props, code) | Stiff, uncreative builds | Specs give WHAT and WHEN | [R][PB] |
| AP-21 | Agents learning from old outputs | Copies the earliest, worst work | Docs over outputs | [R] |
| AP-22 | Examples beside a rule that contradict it | Models copy examples before following rules | Make examples obey the rule | [X] |
| AP-23 | Setup questions asked every run; per-run details in setup | Friction; wrong layer | Setup once; entry stage collects per-run details | [R] |
| AP-24 | Asking for voice descriptions instead of examples | Weak, interpreted constraints | Ask for right and wrong example sentences | [R] |
| AP-25 | Inline conditional placeholders | Broken markdown after removal | Wrap whole sections only | [R] |
| AP-26 | Speculative stages, "misc" buckets, a workspace for a task done twice | Scaffolding, not architecture | The smallest structure that carries the work | [A] |
| AP-27 | Automated mid-pipeline branching | Turns ICM back into a framework | A human decides between stages | [P] |
| AP-28 | Moving files without checking referrers; silent deletes | Broken references | Reference-integrity gate; `_archive/` | [A] |
| AP-29 | Workshops ending in slides | Nothing for the structure to shelve | Every session ends in files | [A] |
| AP-30 | Patterns declared top-down | False structure | Three independent occurrences | [A] |
| AP-31 | Only ever fixing outputs | The same correction every run | Edit-source principle | [P] |
| AP-32 | Starting over when output is wrong | Throws away the context | Correct in place | [F 4.2] |
| AP-33 | Deciding and building at the same time | Both suffer | Plan in chat, build in Code | [F 4.3] |
| AP-34 | Losing progress between sessions | Re-explaining, missed details | PRD + PROGRESS.md | [PB 2.4] |
| AP-35 | Secrets or private files committed | Leaks | `.env` + `.gitignore` + the stranger test | [R][PB] |
| AP-36 | One client's information inside another client's room | Leakage, confusion | One isolated folder per client | [F 3.2] |
| AP-37 | Building a new tool in a separate folder from its context | The context is not there | Build inside the workspace | [PB Stack] |

---

## 21. Templates (copy-ready)

### 21.1 Tier 1 `CLAUDE.md` (the Map) [F 3.1, 3.2]

```markdown
# [Project Name]

You are helping [NAME] with [WHAT THEY DO], for [AUDIENCE].

## Workspaces
- /[room-1]: [what happens here]
- /[room-2]: [what happens here]
- /[room-3]: [what happens here]

## Routing
| Task | Go to | Read | Skills |
|------|-------|------|--------|
| [task type 1] | /[room-1] | CONTEXT.md | [skill or none] |
| [task type 2] | /[room-2] | CONTEXT.md | [skill or none] |
| [task type 3] | /[room-3] | CONTEXT.md | [skill or none] |

## Naming conventions
- Drafts: topic-name_draft.md
- Final: topic-name_final.md
- Published: YYYY-MM-platform-topic.md

## Rules
- Read this file first on every new task.
- Ask clarifying questions before making assumptions. When unsure, say so.
- [workspace-wide rule, e.g. never mix client information across folders]
```

### 21.2 Tier 1 room `CONTEXT.md` [F 1.2, 3.1, 3.2]

```markdown
# [Room Name]

Last updated: [YYYY-MM-DD]

## What this room is for
[One or two sentences about the work done here.]

## Process
First [step], then [step], then [step].

## What lives here
- ideas/  drafts/  final/   (naming: topic-name_draft.md, topic-name_final.md)
- Voice and style: see ../_shared/voice.md (load for writing tasks only)

## Skills and tools
- [skill name]: [when to use it]

## What good looks like
[Specific description or a pointer to an example.]

## What to avoid
[The mistakes and annoyances that keep happening.]
```

### 21.3 Tier 2 `CLAUDE.md` (icm-architect style) [A]

```markdown
# {Workspace name}

{One sentence: what this workspace is and what leaves it.}

Built on ICM: folders carry sequencing, hierarchy carries context, files carry state. The structure is the documentation. If something needs explaining, the explanation goes in that folder's CONTEXT.md.

## Where things live

| Folder | What it holds |
|---|---|
| `stages/` | the pipeline, in execution order |
| `_shared/` | factory: rules and reference that never change per run |
| `_templates/` | blank starters; new work is a copy, not a blank page |
| `setup/` | one-time factory configuration |

## Route by what just happened

| If | Go to | Then stop at |
|---|---|---|
| starting a new run | `stages/01_.../CONTEXT.md` | human reads the output |
| {previous stage} output approved | next numbered stage | human reads the output |
| asked for status | scan `stages/*/output/` | report what exists |
| setting up for a new user | `setup/questionnaire.md` | answers written to `_shared/` |

## The one rule

Nothing moves to the next stage until a person has read the output of the last one.
```

### 21.4 Tier 2 `CLAUDE.md` (ICM repo style, with triggers and What to Load) [R]

```markdown
# [Workspace Name]

[One sentence: what this workspace does.]

## Folder Map

[tree of the workspace with one-line descriptions]

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run onboarding questionnaire |
| `status` | Show pipeline completion for all stages |

## Routing

| Task | Go To |
|------|-------|
| [Task type 1] | `stages/01-[name]/CONTEXT.md` |
| [Task type 2] | `stages/02-[name]/CONTEXT.md` |

## What to Load

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| [Task 1] | [minimal file list] | [what to skip and why] |

## Stage Handoffs

Each stage writes its output to its own `output/` folder. The next stage reads from there. If you edit an output file, the next stage picks up your edits.
```

### 21.5 Root `CONTEXT.md` (the pipeline in one screen) [A]

```markdown
# {Workspace name}: the pipeline

The flow in one line: {plan it, make it, check it, ship it, in your workspace's words}.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| `01_{name}` | {five words} | {what it reads} | `output/{file}` | {what a person verifies} |
| `02_{name}` | {five words} | 01's output | `output/{file}` | {what a person verifies} |
| `03_{name}` | {five words} | 02's output | `output/{file}` | {what a person verifies} |

Factory (stable, every run): `_shared/{voice.md, rules.md, ...}`
Product (new each run): each stage's `output/`

Status is whatever exists: a stage is COMPLETE when its `output/` holds an artifact. A placeholder that only keeps the empty folder in git does not count.
```

### 21.6 Stage `CONTEXT.md` (unified superset) [A][R]

```markdown
# {NN}_{stage-name}: {the job in five words}

One job: {the single thing this stage does}.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Working (this run) | `../{NN-1}_{prev}/output/{slug}-{artifact}.md` | Full file | The artifact to transform |
| Reference (every run) | `../../_shared/voice.md` | "Hard Constraints" through "What the Voice Is NOT" | Tone rules |
| Reference (every run) | `references/{stage-guide}.md` | Full file | Structure for this stage |

Do NOT load: {other stages' references, prior runs, the whole _shared folder, unneeded skills}. Do not read other output/ files to learn patterns.

## Process

1. Read the inputs.
2. {One concrete action.}
3. **[Checkpoint 1]** Present {options or draft} to the human for {decision}.
4. {One concrete action, following the reference constraints.}
5. {Hard limits worth restating: length, count, format.}
6. Run the audit checks below. If any fail, revise before saving.
7. Save to output/.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | {what to show} | {what to choose} |

## Audit

| Check | Pass Condition |
|-------|---------------|
| {Check name} | {Unambiguous pass/fail condition} |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| {Name} | `output/{slug}-{artifact}.md` | {Format description} |

## Human check

{One concrete act: read it aloud / verify the numbers against X / confirm the order survived.} Edit the output in place; the next stage reads whatever is here.

<!-- Keep this file under 80 lines. Delete Checkpoints/Audit if the stage is linear. -->
```

### 21.7 Questionnaire [R][A]

```markdown
# Onboarding Questionnaire

<!-- Agent: read this when the user types "setup". Ask ALL questions in one pass.
     Replace placeholders in the listed files. Then scan the workspace for "{{".
     Rules: flat list, all at once, system-level only, derive don't ask,
     sensible defaults, ask once never again, examples over descriptions. -->

### Q1: Who is this for, and what does a finished deliverable look like?
- Placeholder: `{{DEFINITION_OF_DONE}}`
- Files: `_shared/definition-of-done.md`
- Type: free text
- Example: "A 60-90 second explainer for founders, ready to post."

### Q2: Paste two sentences that sound right, one that sounds wrong, and any error patterns you hate.
- Placeholder: `{{VOICE_RIGHT_EXAMPLE_1}}`, `{{VOICE_RIGHT_EXAMPLE_2}}`, `{{VOICE_WRONG_EXAMPLE_1}}`
- Files: `_shared/voice.md`
- Type: structured
- Derived: `{{VOICE_HARD_CONSTRAINT_1..3}}` (shown back for review in pass 2)

### Q3: Hard constraints that never bend (length, format, brand, compliance)?
- Placeholder: `{{HARD_RULES}}`
- Files: `_shared/rules.md`
- Type: free text
- Default: none

### Q4: What do you always check before anything ships?
- Placeholder: `{{HUMAN_CHECK_STAGE_NN}}`
- Files: each `stages/*/CONTEXT.md` Human check line
- Type: free text

### Q5: Do you need the {optional} stage?
- Type: yes/no
- If NO: Remove `stages/03_{name}/` entirely and the `{{?BUILD_STAGE}}` section

---

## After Onboarding

Tell the user what was configured and where to start. Scan the whole workspace for remaining `{{`. If any remain, ask for the missing information. Onboarding is complete only when none remain.
```

### 21.8 Voice rules skeleton [R]

```markdown
# Voice Rules: {{BRAND_NAME}}

## Hard Constraints
These are errors. If the output contains any of these, rewrite.
1. {{VOICE_HARD_CONSTRAINT_1}}
2. Filler transitions ("Now let's talk about..."). Just start the next thought.
3. Recap summaries at the end of sections.
4. Hype language ("game changing", "revolutionary").

## Sentence Rules
| Wrong | Right |
|-------|-------|
| {{VOICE_WRONG_EXAMPLE_1}} | {{VOICE_RIGHT_EXAMPLE_1}} |

## Pacing
{{VOICE_PACING_DESCRIPTION}}

## What the Voice Is NOT
**Not performative.** Bad: "As someone who works extensively in this field..." Good: "A company I worked with spent six months on this exact problem."
**Not antithetical.** "Not X, but Y" at most once per piece.
**Not rhetorically questioning.** Cut questions that exist only for effect.

## Strategic Rationale
(Why these choices work for {{TARGET_AUDIENCE}}. Usually not loaded.)
```

### 21.9 `PROGRESS.md` [PB 2.4]

```markdown
# Progress

## Current Status
[One or two lines: what is being built right now, what is next.]

## Last Session (YYYY-MM-DD)
- Completed:
- In Progress:
- Blocked:
- Next:

## Decisions Made
- [Decision] ([reason])

## Open Questions
- [Question]
```

### 21.10 Context-map process node [A]

```markdown
---
type: process
team: {team-slug}
owner: {name}
ai-level: L0   # L0 manual · L1 copy-paste · L2 structured · L3 integrated
frequency: {daily|weekly|monthly|ad-hoc}
value: 3       # 1-5, to the business
pain: 3        # 1-5, to the people doing it
consumes: ["[[data-{input-asset}]]"]
produces: ["[[data-{output-asset}]]"]
governance: internal   # internal · sensitive · external
---

# {Process name}

## Input → Movement → Output
## Now
## What is working / not working
## If we structure this
## What the human keeps checking
```

### 21.11 Memory entry-file seed [M]

```markdown
# User memory

Long-term memory for one user, built from their past conversations.

## Where things are

(Nothing yet. This file is the catalog. As you add folders, list them here
with one line each saying what they hold and when to go there.)

## How to answer a question about this user

1. Read this file to find the right area.
2. Follow it to the index or folder that covers it.
3. Read only the leaves you need.
```

---

## 22. Worked Examples (from Jake's repos and lessons)

### 22.1 Tier 1 trees [F 3.2]

**Content creator**
```
my-content-project/
├── CLAUDE.md                     routing + naming (topic-name_draft.md, topic-name_final.md, YYYY-MM-platform-topic.md)
├── script-lab/    CONTEXT.md  ideas/ drafts/ final/
├── production/    CONTEXT.md  briefs/ specs/ builds/ output/
└── distribution/  CONTEXT.md  platforms/ scheduling/ analytics/
```

**Freelancer / consultant**
```
my-consulting-practice/
├── CLAUDE.md                     active clients, internal rooms, routing, rules
├── client-alpha/  CONTEXT.md  intake/ deliverables/ communications/
├── client-beta/   CONTEXT.md  intake/ deliverables/ communications/
├── templates/     CONTEXT.md  proposals/ reports/ frameworks/
└── business-dev/  CONTEXT.md  pipeline/ outreach/ case-studies/
```
Rules in its CLAUDE.md: "Never reference one client's information in another client's workspace"; "Proposals always start from /templates and get customized in the client folder"; "Deliverables go in /client-[name]/deliverables, drafts stay in working folders."

**Developer**
```
my-app/
├── CLAUDE.md                     tech stack, rooms, routing (| Task | Go to | Read | Skills |), naming
├── planning/  CONTEXT.md  specs/ architecture/ decisions/
├── src/       CONTEXT.md  components/ services/ utils/ tests/
├── docs/      CONTEXT.md  api/ guides/ changelog/
└── ops/       CONTEXT.md  deploy/ monitoring/ scripts/
```
Naming: `feature-name_spec.md`, PascalCase components, `feature-name.test.ts`, `YYYY-MM-DD-decision-title.md`.

**Website project** [PB 3.2]: root `CLAUDE.md` (master routing, 30 to 50 lines); `docs/brand-voice.md`, `docs/design-tokens.md`, `docs/prd.md`; `src/components/README.md`, `src/pages/README.md`, `src/layouts/README.md` for folder-level detail; `.gitignore` for `.env`, `node_modules`, build output.

### 22.2 script-to-animation (Pipeline, 3 stages) [R][P §4.2]

```
script-to-animation/
├── CLAUDE.md, CONTEXT.md
├── setup/questionnaire.md          14 questions
├── brand-vault/{CONTEXT.md, identity.md, voice-rules.md}
├── shared/platform-specs.md
├── skills/{remotion-best-practices/, frontend-design/}
└── stages/
    ├── 01-script/   references: hook-system, script-templates, content-pillars, value-framework
    ├── 02-spec/     references: spec-format, animation-guide, component-registry, design-system
    └── 03-build/    references: build-conventions, remotion-setup   (optional, {{?BUILD_STAGE}})
```

- **01-script**: topic → pick the pillar → propose 3 to 5 angles tagged with value slots and format → **Checkpoint 1** → value brief (concept, 2+ value slots, format, hook, close) → **Checkpoint 2** → write the full script in one pass → audit (voice hard constraints; value delivery; tension lands within 2 to 3 seconds; the close is something you could say to a friend; no gap over 5 seconds without a retention beat; share test) → metadata header → `output/[topic-slug]-script.md`.
- **02-spec**: script → core visual metaphor → beats → beat map → visual philosophy → 2 to 3 key moments → audio sync → color flow → audit (mute test, one concept per beat, contract purity, key moments, 3+ sync points) → `output/[topic-slug]-spec.md`.
- **03-build**: spec + build conventions + Remotion skill (index, then rules) + `../02-spec/references/design-system.md` (a one-way cross-stage reference) → `output/[topic-slug]/{index.tsx, beats/*.tsx, constants.ts, assets/}` → audit (spec coverage, shared constants, platform specs, no hard cuts, mobile readability, safe zones).
- Its What to Load table excludes other stages' references and unneeded skills for each task (§21.4).

### 22.3 course-deck-production (Pipeline, 5 stages) [R][P §4.3]

01-extraction (the entry stage collects course metadata into `output/[course-slug]-meta.md`; chunks tagged by topic, complexity, and source; a checkpoint; audit for coverage, tag accuracy, citations, one concept per chunk) → 02-curriculum (modules and sessions, 2 to 3 objectives each) → 03-outline (15 to 25 slides per session from a slide-pattern library) → 04-generation (HTML per slide, html2pptx → `.pptx`; linear, no checkpoint) → 05-qa-delivery (thumbnail grids, a fix loop, `output/final/`, QA report, delivery manifest). The metadata travels forward through every stage's output, and any stage can be the entry point. The design reason: "By surfacing the structural plan as an editable markdown file before any slides are drafted, ICM lets the human course-correct at the point where correction is cheapest."

### 22.4 voice-driven-animation (Pipeline, 5 stages, 3 custom skills) [R]

01-research (3 to 7 primary sources, verbatim quotes for numbers, conflicts surfaced; a brief with Summary, Claims, Angle, Open Questions) → 02-script (word budget at about 150 to 170 wpm; a paste block for the TTS tool plus a beat-annotated copy with `<!-- BEAT N -- desc (~Ns) -->` markers; audit: at most one antithesis, zero em dashes, word count within ±10%, dry-run extract) → 03-voice (dry run → audio → transcript JSON → beat timings by phrase match, all by scripts) → 04-animate (a timing file and per-beat scenes) → 05-render (pre-flight, render, runtime within 5%, notes, a "When to Loop Back" table). Its "Source of Truth at Each Stage" table runs brief → script → audio ("if the audio differs from the script, the audio wins") → beat timings → composition.

### 22.5 workspace-builder (meta-pipeline, 5 stages) [R][P §4.4]

01-discovery → `workflow-map.md`; 02-mapping → `stage-contracts.md` + an ASCII dependency diagram; 03-scaffolding → the whole new workspace in `output/`; 04-questionnaire-design → `questionnaire.md`; 05-validation → `validation-report.md`. Its own setup asks four questions (the domain; the workflow in one sentence; who the users are and how skilled they are with AI; a rough stage count and which stages are skippable). These feed discovery rather than filling placeholders. "The builder enforces the same structural rules it was built with."

### 22.6 The origin system (Content-Agent-Routing-Promptbase) [O]

An umbrella of rooms under one CLAUDE.md:
- `brand-vault/` (READ-ONLY "DNA": who-jake-is, voice-and-tone, brand-story, content-pillars)
- `script-lab/` (hook system with 6 hook types, script templates; scripts sorted by format and pillar P1 to P5)
- `topic-engine/` (topic bank T-01 to T-50)
- `products-and-offers/`, `platform-playbook/`, `production-rhythm/`
- `animation-studio/` (`docs/` with a component registry and design system; `workflows/01-scripts → 02-specs → 03-builds/[active|complete] → 04-renders`)

Measured budgets:

| Task | With routing | Without |
|---|---|---|
| Write a script | ~4,000 tokens | 15,000+ |
| Generate a spec | ~5,000 tokens | 12,000+ |
| Research topics | ~2,500 tokens | 15,000+ |
| Plan the week | ~1,500 tokens | 15,000+ |
| Render | ~500 tokens | 15,000+ |

Its history:
1. A monolith that "worked for about two weeks".
2. A "distributed monolith" with duplicated info and drift.
3. The routing architecture.

### 22.7 Practitioner pattern: duplicate and adapt [P §4.5]

People with a working workspace for one format (short explainers) duplicate the folder, edit the stage prompts for another format (long-form essays), and run it, instead of rebuilding from scratch. This is a legitimate way to create a new workspace.

---

## 23. Conflicts Between Sources and How This Document Resolves Them

| Topic | Variant A | Variant B | Resolution |
|---|---|---|---|
| Stage folder separator | `01_research` [P][A] | `01-script` [R] | Default `NN_kebab-name`. Either is allowed; one per workspace. |
| Shared folder | `_shared/` [A] | `shared/` + `brand-vault/`/`design-system/`; `_config/` in diagrams [R][P] | Default `_shared/`. Named context folders are allowed when they need their own router. |
| Entry-file size | under ~60 lines [A][M]; 30 to 50 lines, one screen [F][PB] | ~800 tokens; repo files of 69 to 81 lines [R][P] | Target 30 to 60 lines; never over 80. |
| Number of layers | Three (Map / Rooms / Tools) [F] | Five (L0 to L4) [P][R][A] | The same architecture at two resolutions (§5.1). |
| Stage contract shape | Inputs table + optional Checkpoints and Audit [R] | Working/Reference list + Do NOT load + exactly one Human check [A] | The unified superset (§10.2). |
| Specs | Code blueprints [O] | Contracts: WHAT and WHEN only [R v2][PB] | Contracts. |
| Learning from outputs | Read one existing build [O] | Never [R v2] | Never. |
| Committing outputs | Gitignore outputs [R] | Commit after each run for history [P] | Templates: do not commit. Deployments: may commit. |
| Em dashes | Banned in the repo [R] | Used freely [A] | House style. Banned inside voice rules for Jake-style content. |
| Name | Model Workspace Protocol (MWP) [P v1][R early] | Interpretable Context Methodology (ICM) | ICM. |
| Questionnaire | Grouped categories, one voice description [early MWP] | Flat, all at once, examples [R v2] | Flat, all at once, examples. |
| Skills vs context files | "Prefer CONTEXT.md files first to save tokens" [O] | Bundle skills; skills replace reference docs [R] | Use reference files for workspace-specific knowledge. Use skills for reusable domain knowledge, wired per room or stage. |

---

## 24. Evidence and Claims (for calibration)

- **Token budgets**: the ICM stages ran about 4.9k, 5.5k, and 5.6k tokens, against about 42k monolithic for the same pipeline. [P Fig. 3]
- **Practitioners** (a 52-member invite-only community):
  - 30 of 33 reported the U-shaped editing pattern (about 92%, 30%, 78%).
  - Non-technical users edited CONTEXT.md successfully.
  - Three people with no coding experience built and ran workspaces that produced ten-minute animated videos.
  - People duplicate and adapt workspaces.
  - All of this is self-reported, not instrumented. [P §4.5, §4.6]
- **Memory study** (ICM folder memory against the whole history in context, on LongMemEval):
  - Accuracy did not differ significantly (0.744 vs 0.872, p = 0.227).
  - The folder read 97% fewer tokens and cost 95% less per query, breaking even after about 7 questions.
  - The same agent without the ICM conventions did significantly worse than long context (p = 0.021).
  - A memory built by one model was read by another vendor's model at equal accuracy and 96% lower cost. [M]
- **Community scale**: Clief Notes passed about 47,000 members in 2026. Jake has cited "30,000 people" building this way. [SS][X]
- **Honest limits**: there is no controlled comparison of staged vs monolithic quality yet; testing used a single model family; the community is self-selected; the benchmark cannot measure the properties ICM exists for (auditability, correction, collaboration). [P][M]
- **Open questions the authors name**: whether the hierarchy generalizes across model families; whether bigger context windows reduce the need for scoping (the human-interaction arguments remain either way); how sensitive output is to the order and formatting of context within a layer. [P §5.4]

---

## 25. Quick-Reference Card (for an agent mid-task)

1. **Does this need a workspace?** One-off → chat. Fits one prompt → a skill or saved prompt. Repeating, multi-part → a workspace.
2. **Which tier?** Ongoing kinds of work → Tier 1 (Map / Rooms / Tools). A repeating reviewed sequence → Tier 2 pipeline. Another repeating unit → Tier 3 form.
3. **Root CLAUDE.md**: 30 to 60 lines, routes only. Routing table: Task | Go to | Read | Skills.
4. **Rooms**: 2 to 3 to start, split by mental mode. CONTEXT.md under a page, 80% about the work. Update it as you go.
5. **Stages**: cut where the human pauses. Surface judgment calls as editable files before the expensive work.
6. **Each stage**: `CONTEXT.md` (Inputs with exact paths and sections, Do NOT load, numbered concrete Process, Checkpoints if creative, Audit if creative or build, Outputs, one concrete Human check) + `references/` + `output/`.
7. **Factory** (`_shared/`, `references/`, `skills/`) apart from **product** (`output/`).
8. **Budget**: 2k to 8k tokens per stage. Over budget → split, tighten, push down.
9. **One home per fact.** One-way references. Generated indexes by script.
10. **Limits**: CONTEXT.md under 80 lines; reference files under 200.
11. **Setup**: flat, all at once, system-level only, defaults, examples over descriptions, no `{{` left.
12. **Status** = scan `output/`. Nothing moves until a human has read the last output.
13. **Sessions**: read CLAUDE.md + PROGRESS.md at start; update PROGRESS.md at end. Plan in chat, build in Code.
14. **Prompts**: Identity, Task, Context, Constraints, Output Format. One ask per prompt. Correct in place.
15. **Recurring edits** → fix the source.
16. **Validate**: walk test; one full run end to end.

---

## 26. Sources and Coverage Notes

### 26.1 Primary sources

- Van Clief, J. & McDermott, D. (2026). *Interpretable Context Methodology: Folder Structure as Agentic Architecture*. arXiv:2603.16021. https://arxiv.org/abs/2603.16021
- Van Clief, J., McDermott, D. & Kumar (2026). *The Cost of Remembering: Filesystem Memory Against Long Context on LongMemEval*. https://github.com/RinDig/cost-of-remembering
- https://github.com/RinDig/icm-architect
- https://github.com/RinDig/Interpretable-Context-Methodology
- https://github.com/RinDig/Content-Agent-Routing-Promptbase
- https://github.com/RinDig/lecture-deck-skill (skill-writing style)
- Clief Notes (Skool): https://www.skool.com/cliefnotes. The Foundation, Implementation Playbooks, and Building Your Stack lesson text came from community transcriptions and clippings (`donroy26/Clief-Notes-Foundations-Tutor`, `Naxxy/workspace-builder-skill/_design/skool-references/`).
- YouTube: https://www.youtube.com/@JEVanClief ("Stop Building AI Agents. Use This Folder System Instead."; "You're Automating The Wrong Layer"; "Stop Buying Agent Tools. Your Folders Already Do This."; "How a 1953 Word Game Explains AI Memory"; "How One Line of Python Triggers 12,000 Lines of Code"; "Clawdbot (Moltbot) Has 100K Stars. It Has Zero AI.")
- Substack: https://jakevanclief.substack.com ("The Machine Is Smart."; "Augmenting Human Intellect"; "How One Line of Python Triggers 12,000 Lines of Code")

### 26.2 Coverage gaps (to fill later if access allows)

- No YouTube transcripts were retrievable. Video content comes through Jake's own written lesson companions, which say they cover the same ground, plus search snippets.
- Substack posts and Skool posts were seen only as search snippets.
- The "Abstraction Series" lessons (2.1 to 2.7: the Ladder, Video as Code, 60/30/10, Book / Movie / Video Game) and lesson 1.1 were not recovered beyond their titles and headline ideas.
- The Vault (premium) and Drawing Room (VIP) material was not accessible.
- The full text of the Ethics Engine paper (arXiv:2510.11742) was not retrieved; it is only tangential to the method.
