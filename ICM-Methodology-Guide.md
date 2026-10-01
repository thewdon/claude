---
title: "Interpretable Context Methodology (ICM): An AI-Consumable Specification of Jake Van Clief's Folder-and-File Workflow Method"
aliases: ["ICM", "Model Workspace Protocol", "MWP", "folder structure as agent architecture", "Clief Notes method", "Map / Rooms / Tools"]
method_author: "Jake Van Clief (with David McDermott). Eduba; Clief Notes community"
compiled: 2026-10-01
document_version: 0.3
intended_reader: "An AI agent that will design, build, restructure, validate, or operate ICM workspaces, skills, and workflows"
---

# ICM: Folder Structure as Agent Architecture

> One agent, reading the right files at the right moment, does the work a multi-agent framework would do. Numbered folders carry order. Nesting carries scope. A small file at the root says where everything lives. Plain markdown carries the state.

**Document layout.**
- **Part I, the Operating Core (§0 to §20)**, is what an agent needs while working.
- **Part II, the Reference Appendix (§A1 to §A7)**, holds the rationale, worked examples, the source conflicts, the evidence, the extensions register, the rule index, and the sources.

An agent mid-task SHOULD stay in Part I.

---

# PART I: OPERATING CORE

## 0. How to Use This Document

### 0.1 Entry points

| You were asked to... | Start at | Then |
|---|---|---|
| Decide whether something needs a workspace, and which kind | §1 | the section it routes to |
| Build a simple workspace for ongoing work (Foundations tier) | §5 | §15.1, validate with §17 |
| Build a staged pipeline (formal ICM tier) | §6 to §9 | §15.2, then §10 setup, then validate with §17 |
| Build another form (record library, knowledge bundle, context map, system map, umbrella) | §16 | §15.2 with the form's interview add-on |
| Restructure an existing folder, repo, drive, or vault | §15.3 | §16 to pick the form, then §17 |
| Write a skill | §14 | §15.4, §17.6 |
| Run setup / onboarding for a workspace | §10 | §15.5 |
| Start or continue a run | §9 | §11 for sessions |
| Write prompts inside a workspace | §12 | |
| Check limits and thresholds | §3 | |
| Review a workspace for problems | §17, §18 | |

### 0.2 Normative keywords

- **MUST / MUST NOT**: the source states it as non-negotiable ("no exceptions", "never", "every stage follows this exact shape").
- **MUST (validation)**: the source says "should", but Jake's own validation stage fails a workspace without it. Treat it as MUST when shipping.
- **SHOULD / SHOULD NOT**: a strong default with legitimate exceptions.
- **MAY**: allowed.
- **INFO**: rationale, a definition, or an observed effect that the other rules rely on. It cannot be checked on its own.
- Rule IDs follow the form `R-<AREA>-NN`. They are stable, so skills and checklists can cite them. §A6 indexes them.

### 0.3 Source tags

| Tag | Source | Fidelity |
|---|---|---|
| `[A]` | `github.com/RinDig/icm-architect`, Jake's Claude skill (Jul to Aug 2026): `SKILL.md`, `references/{core, forms, system-map, reference-integrity}.md`, `assets/templates/`. The newest, most distilled statement of the method. | Verbatim, read in full |
| `[R]` | `github.com/RinDig/Interpretable-Context-Methodology` (Feb to Jun 2026): `_core/CONVENTIONS.md` (15 patterns), `_core/templates/`, `_core/placeholder-syntax.md`, four example workspaces including their reference files. | Verbatim, read in full |
| `[P]` | Van Clief & McDermott, *Interpretable Context Methodology: Folder Structure as Agent Architecture*, arXiv:2603.16021. The PDF says "Agent", the arXiv listing says "Agentic". v1 (17 Mar 2026) was titled "Model Workspace Protocol"; v2 (18 Mar 2026) renamed it, with the same text. | Full text, from mirrors |
| `[M]` | Van Clief, McDermott, Kumar, *The Cost of Remembering: Filesystem Memory Against Long Context on LongMemEval* (Aug 2026), `github.com/RinDig/cost-of-remembering`. | Full text |
| `[F]` | Clief Notes (Skool) classroom, **The Foundation** lessons 1.2 to 5.1. Jake's lesson text, which he says "cover[s] the same ground" as the videos. | Community transcriptions and clippings of the lesson text |
| `[PB]` | Clief Notes classroom, **Implementation Playbooks** and **Building Your Stack** (cited as `PB Stack x.y`). | Clippings of the lesson text |
| `[O]` | `github.com/RinDig/Content-Agent-Routing-Promptbase`, the "Eduba Content System", the production system ICM grew out of (Feb 2026). | Verbatim; superseded where it conflicts |
| `[V]` | YouTube (@JEVanClief). | Titles and search snippets only |
| `[SS]` | Substack ("Clief Notes"), Skool posts, LinkedIn, TikTok. | Search snippets only |
| `[X]` | Third-party practitioners and write-ups. | Interpretation; lowest authority |
| `[I]` | Inference by this document's compiler. | Strongly implied, not stated |
| `[EXT]` | **Extension**: a convention this document adds to close a gap found when an agent tried to build from the method. It is NOT Jake's. Adopt it, change it, or drop it. All are listed in §A5. | Ours |

### 0.4 Precedence when sources disagree

1. `[A]` for structure, naming, and invariants.
2. `[R]` for detailed patterns `[A]` lacks (checkpoints, audits, questionnaires, placeholders, value validation, specs-as-contracts, bundled skills, reference-file shapes).
3. `[P]` for rationale, scope, evidence, future directions.
4. `[F]` / `[PB]` for the beginner tier, everyday practice, prompting, sessions, planning.
5. `[M]` for memory and knowledge workspaces.
6. `[O]` only for history, or where it is the only source.
7. `[V]`, `[SS]`, `[X]` never as the sole basis for a MUST.
8. `[EXT]` fills gaps only. It MUST NOT override a sourced rule.

Every known conflict and its resolution is in §A3.

### 0.5 The method in one paragraph

One AI agent, reading the right files at the right moment, replaces a multi-agent framework. **Numbered folders carry sequencing. Folder hierarchy carries context scoping. Plain markdown files carry state. One folder's `output/` is the next folder's input.** A small root file (`CLAUDE.md`) says where everything is and routes each task. Each working folder has a `CONTEXT.md` that says what to read, what to do, what to write, and what a human checks. Stable rules (the factory) live apart from per-run work (the product). A human can open and edit every intermediate file before the next step reads it. Local scripts do the mechanical work that needs no AI. [P][R][A]

> "Stage sequencing is the folder numbering. Context scoping is the folder hierarchy. State management is the files on disk. Coordination between stages is one folder's output being another folder's input." [P §3.2][R][A]

> "Claude is the intelligence. Your folders and context files are the orchestration." [F 4.5]

### 0.6 Core vocabulary (full glossary in §A1.6)

| Term | Meaning |
|---|---|
| **Workspace** | A self-contained folder holding one ICM system. It still works copied, zipped, or committed. [P] |
| **Room** | A Tier 1 area for one kind of work, with its own `CONTEXT.md` (Jake also calls these "workspaces"). [F] |
| **Stage** | A numbered folder doing one job in a sequence: `CONTEXT.md` + `references/` + `output/`. [P][R][A] |
| **Entry file / the Map / L0** | Root `CLAUDE.md` (or `AGENTS.md`): where am I, where is everything, where do I go. [A][F] |
| **Contract / L2** | A stage's `CONTEXT.md`: Inputs, Process, Outputs, Human check. "The control point." [P][A] |
| **Factory / L3** | Stable reference material: voice, rules, design system, templates, skills. [P] |
| **Product / L4** | Per-run working artifacts: inputs and outputs of this run. [P] |
| **Checkpoint** | A pause *inside* a stage, between process steps, for human steering. [R] |
| **Human check / gate** | The single act a person performs on a stage's saved output before the next stage reads it. [A] |
| **Audit** | A pass/fail list the agent runs before saving output. [R] |
| **Form** | One of six workspace shapes, chosen by the repeating unit of work. [A] |
| **Walk test** | Validation by walking the workspace cold, with no memory. [A] |

---

## 1. Decision Procedure (run this first)

### 1.1 Classify the request

| Request type | Signals | Go to |
|---|---|---|
| **Build** | "set up", "build me a workspace / system / workflow for X" | §1.2 |
| **Restructure** | an existing folder, repo, drive, or vault: "organize", "clean up", "ICM this", "map this repo" | §15.3 (then §16 for the form) |
| **Skill** | "make a skill / command that does X" | §1.2 step D2, then §14 |
| **Run** | a workspace exists: "start a new run", "next stage", "status" | §9 |
| **Setup** | "setup", a new user for an existing workspace | §10 |

### 1.2 Build decision table (evaluate in order; stop at the first match)

| Step | Question | If YES | Source |
|---|---|---|---|
| D0 | Does any part need real-time agent-to-agent loops, many simultaneous users, or automated branching on AI output mid-run? | Keep that part out of ICM and use a framework for it. Continue with the rest. | [P §5.2][A] |
| D1 | Is it a one-off? | Do it in chat. No files. STOP. | [A] |
| D2 | Does it repeat, and fit in one saved prompt or one skill? A [EXT] threshold for "fits": about one screen of instructions, no state carried between runs, no human review needed between steps. | Write a saved prompt or a skill (§14). Do not build a workspace. STOP. | [A]; threshold [EXT] |
| D3 | Is it repeating already, or is it ongoing work the person does regularly? "Weekly or more often" and "3-15 steps" that "are the same each time" are good signs. Fewer than 3 steps is faster done by hand; more than 15 "gets fragile" unless split. | If NO (planned, imagined, or done twice), do not build yet: "A workspace for a thing done twice is scaffolding, not architecture." Offer a saved prompt and revisit after real repetitions. STOP. | [A][PB 2.3] |
| D4 | Is it ongoing work across several *kinds* of task (writing, analysis, clients, code areas) with no fixed sequence? | **Tier 1: Rooms** (§5). | [F] |
| D5 | Is it a repeating sequence producing a deliverable each run, where a human should check the key steps (sequential + reviewable + repeatable)? | **Tier 2: Pipeline** (§6 to §9). | [P §5.1][R] |
| D6 | Is the repeating unit something else (several pipelines sharing one brand; a record that accumulates; a body of knowledge; an organization; a codebase or vault later agents will edit)? | **Tier 3: another form** (§16). | [A] |

Typical pipeline fits [P][R]: content production, research and analysis, monitoring and digests, reporting, training material and course decks, policy analysis, client deliverables, literature reviews, audit procedures, curriculum development, and code documentation. The method carries across domains (research papers, finance, procedural engineering documents): "same structure, different content." [SS TikTok]

Tiers and forms line up as follows: **Tier 1 = Rooms** (closest to an Umbrella with no pipelines yet [I]); **Tier 2 = the Pipeline form**; **Tier 3 = the other five forms**. Tiers nest: a room grows a pipeline inside it once a sequence in that room starts repeating (§5.6). [I]

### 1.3 Before building anything

- **R-SCOPE-01** If the whole job fits in one saved prompt, say so. MUST NOT build a workspace. [A]
- **R-SCOPE-02** MUST NOT build a pipeline before the process has actually repeated. [A]
- **R-SCOPE-03** "Three real stages beat seven imagined ones." MUST NOT create folders for stages that do not exist yet, empty "misc" buckets, or speculative depth. [A]
- **R-SCOPE-04** A Tier 1 first version SHOULD take about 15 minutes. "If it took longer, you over-built." Let structure "grow from use, not from planning". [F 3.3]
- **R-SCOPE-05 (INFO)** "The moment it starts feeling heavy or complicated, something went wrong." [F 3.3]
- **R-SCOPE-06 (SHOULD)** Use the simplest tool that solves the problem. Tool ladder: Claude Projects → Cowork → VS Code + Claude Code ("where most people should land") → custom front-end ("If you're not sure whether you need a custom front-end, you probably don't."). [PB Stack 1.1] A simple one-page site can skip Claude Code entirely. [PB 3.3]
- **R-SCOPE-07 (SHOULD)** "You can't write requirements for emergent behavior." For client or enterprise work, loop Discovery → Observation → Production. Prototype with simple tools, and measure real use before a big build. [SS]
- **R-SCOPE-08 (SHOULD)** Much "AI isn't good enough" frustration "is actually a context architecture problem". Check the structure before blaming the model. [O]
- **R-SCOPE-09 (SHOULD)** Decide where AI fits at all. Jake's 60/30/10 framing: about 60% traditional or database work, 30% rule-based logic, 10% AI. Use scripts and rules first, and save the model for judgment. [SS snippet; a different [X] breakdown exists, see §A3]
- **R-SCOPE-10 (SHOULD)** If the person "make[s] different decisions based on what [they] see", keep that step manual or break it into smaller pieces. [PB 2.3]

### 1.4 Where ICM loses (state these honestly) [A core][P §5.2]

| Situation | Why ICM is the wrong tool |
|---|---|
| Real-time multi-agent collaboration | It needs message-passing infrastructure; file handoffs are too slow. |
| High concurrency (many users on one pipeline) | It needs queueing, state isolation, deployment. ICM is local-first. |
| Automated mid-pipeline branching | A human choosing 3a or 3b between stages is natural. The system branching on its own "pushes ICM toward becoming the framework it replaced". |

> "The claim is not that ICM replaces frameworks everywhere. The claim is that for sequential, human-reviewed, repeatable workflows — most knowledge work — the framework is more complexity than the problem requires, and that complexity costs opacity, fragility, and developer dependency." [A core]

The paper's version: "for a large and common class of workflows, the existing tools provide more complexity than the problem requires, and that complexity has real costs: opacity, fragility, developer dependency, and overhead that slows iteration." [P §5.2] Frameworks fit complex, concurrent systems. [P]

MCP is complementary: it handles tool and data access, while ICM handles how context is structured across stages. A stage MAY use MCP. [P §2.2][R]

---

## 2. The Invariants

The ten titles are verbatim from icm-architect `[A]`. Each is reinforced by `[P]` and `[R]`.

| ID | Invariant | Rule |
|---|---|---|
| **INV-01** | **One folder, one job** | Each folder does a single step or holds a single kind of thing, and states its own purpose in a file inside itself. "The structure is the documentation." |
| **INV-02** | **A small, stable entry file** | `CLAUDE.md` (or `AGENTS.md`) at the root answers "where am I, where does everything live, where do I go for task X", and nothing else. It routes; it never holds content. Limits are in §3. |
| **INV-03** | **Numbering encodes order** | `01_`, `02_`, ... where sequence matters. Renaming folders reorders the pipeline; that is the point. |
| **INV-04** | **Every folder-level contract is explicit** | A `CONTEXT.md` per working folder: what it reads, what it does, what it writes, what a human checks. |
| **INV-05** | **Factory vs product** | Reference material (stable across runs) lives structurally apart from working artifacts (new every run). |
| **INV-06** | **Every output is an edit surface** | Intermediate outputs are plain files a human can open, edit, and save before the next step reads them. Nothing moves forward until a person has read the last output. |
| **INV-07** | **Load only what the step needs** | A step reads its contract, its references, and its inputs, not the whole workspace. |
| **INV-08** | **Plain text, linkable, queryable** | Markdown plus YAML frontmatter. Links make it a graph; frontmatter makes it queryable. One home per fact; a link beats a copy. |
| **INV-09** | **The filesystem is the state machine** | Status is derived from what exists. Generated indexes are rebuilt by script, never hand-edited. |
| **INV-10** | **Instantiate by copying** | A new unit of work is a copy of a template folder, not a blank page. Templates live in `_templates/`. |

### 2.1 Which invariants apply to which tier [I]

Jake's Tier 1 teaching predates the invariants and does not use all of them, so applicability is scoped here.

| Invariant | Tier 1 Rooms | Tier 2 Pipeline | Tier 3 Forms |
|---|---|---|---|
| INV-01 | MUST: each room's `CONTEXT.md` states its purpose. Leaf subfolders (`drafts/`, `final/`) are exempt. | MUST | MUST |
| INV-02 | MUST (with the Tier 1 allowance in R-L0-02) | MUST | MUST |
| INV-03 | Only where a room has a real sequence | MUST for stages | Where order matters |
| INV-04 | Looser room form (§7.4) | MUST (full contract, §7.3) | Per form |
| INV-05 | SHOULD: reference files apart from working files | MUST | MUST |
| INV-06 | SHOULD (work is written to files) | MUST | MUST |
| INV-07 | MUST (routing table) | MUST | MUST |
| INV-08 | SHOULD | MUST | MUST |
| INV-09 | n/a | MUST | MUST |
| INV-10 | When units repeat (clients, projects) | When units are instantiated | MUST for record forms |

"Working folder" means a folder where the agent does a step or that holds one kind of thing. Data leaves (`output/`, `references/`, `drafts/`, a record's internal folders) inherit their purpose from the parent's `CONTEXT.md` or the template, and need no file of their own. [EXT]

### 2.2 Library rules [A core][M][F]

- **R-LIB-01 The catalog holds no books (MUST).** Routing files point at everything and store almost nothing. A growing routing file is absorbing payload: move the payload to a shelf and leave a pointer.
- **R-LIB-02 One home per fact (MUST).** "Duplication is how structures rot." [A] "One fact, one location." [F 4.5] The sanctioned exceptions are in §8.4.
- **R-LIB-03 Generated indexes are never hand-edited (MUST).** "A file map built from frontmatter by a script cannot drift; a hand-curated one always does. If an index matters, script it and schedule the rebuild." Head each generated file with a marker such as `<!-- GENERATED by <script> from <source>. Do not edit. -->`. [A][M]
- **R-LIB-04 (SHOULD) The structure is the documentation.** Explanations go in that folder's `CONTEXT.md`, "not in a wiki elsewhere and not in anyone's head". "A new collaborator should understand the whole pipeline by reading the CONTEXT files top to bottom, without running anything." [A][P §3.3]
- **R-LIB-05 Method and instance live apart (SHOULD).** The blank, reusable template is a different artifact from any filled-in deployment. "When a structure proves out, extract the template before it tangles with the data." [A]
- **R-LIB-06 Working sessions end in artifacts (SHOULD).** A workshop, interview, or planning call "that produces only slides or vibes has failed the structure". "Conversations are disposable. The thinking is not." [A][F 4.3]
- **R-LIB-07 (INFO) New sessions start clean.** CLAUDE.md is read fresh and routing sends the agent to the right room, so nothing bleeds over from a previous task. [F 4.5]
- **R-LIB-08 (INFO) Same quality for everyone.** "When the context lives in files, not in someone's head, anyone who opens the folder gets the same Claude experience." [F 4.5]
- **R-LIB-09 (INFO) Change the labels, keep the architecture.** "You change the labels and the context. The architecture holds." "The layers do not change. The labels do." [F 3.1, 3.2]

---

## 3. Limits and Thresholds (canonical table)

This is the one home for every number. Other sections point here. "Hard" marks a validation failure; "target" marks a soft goal. Being *under* a target is fine.

| Item | Target | Hard limit | Unit | Source |
|---|---|---|---|---|
| Root `CLAUDE.md` | 30 to 50 lines ("fit on one screen"); 300 to 800 tokens | ~60 lines. Over 40 to 50 lines means "context files hiding inside it". | lines / tokens | [F 3.3][PB 3.2][A][M]; ~800 tokens [P][R] |
| Single-project `CLAUDE.md` (code) | ~15 lines, written in ~10 minutes | same as above | lines | [F 4.4] |
| Root `CONTEXT.md` (L1) | ~300 tokens (200 to 500) | under 80 lines [I, by analogy] | tokens | [P][R][A] |
| Stage `CONTEXT.md` (L2) | 200 to 500 tokens; 25 to 80 lines | **under 80 lines** | lines | [R][P][A] |
| Room `CONTEXT.md` (Tier 1) | "a few paragraphs", "under a page" | 80 lines [EXT] | lines | [F 3.1, 3.2] |
| Reference file (L3) | 500 to 2,000 tokens loaded per stage | **under 200 lines**; split if longer | lines | [R][P] |
| A stage's full context (entry + contract + references + inputs) | 2,000 to 8,000 tokens | over ~8k means split, tighten, or push down | tokens | [P][A] |
| Monolithic prompt (anti-pattern) | n/a | 30,000 to 50,000 tokens is the thing to avoid | tokens | [P] |
| Orientation reads | entry file + at most 2 more reads | | reads | [A walk test] |
| Memory lookup | entry file + one index + one or two leaves | | reads | [M] |
| Files at one folder level | 8 to 10 | more means subfolders | files | [F 3.3] |
| L3 folder needing an `_index.md` | about 10 files | | files | [X] |
| Rooms to start | 2 to 3 ("you can always add more") | | rooms | [F 3.3]; "2-4 major areas" [F 3.2] |
| Stages | "three real stages"; 3 to 5 is the "sweet spot" [X] | | stages | [A][X] |
| Concept options at a checkpoint | 3 to 5 | | options | [R] |
| Value slots per piece | 2 minimum; "three is ideal when the concept supports it" | 2 | slots | [R] |
| Automation candidate | weekly or more often, 3 to 15 consistent steps | under 3 steps: do it by hand; over 15: fragile, so split | steps | [PB 2.3] |
| Prompts per project | under 10 (4 to 5 planning, 2 to 3 build) | over 12: review what could be combined or front-loaded | prompts | [PB 3.3] |
| Pattern declaration (context map) | 3 independent occurrences | | occurrences | [A] |
| Recurring edit → fix the source | about 3 runs in a row (proposed) | | runs | [P §6.3, proposed] |
| Pilot candidate (context map) | value + pain ≥ 8 | | score | [A] |
| SKILL.md body | one to a few screens (Jake's run about 50 to 115 lines) | | lines | [I from A, lecture-deck] |
| Token rule of thumb | "roughly three quarters of a word" per token | | | [F 3.1] |

---

## 4. The Context Layers

### 4.1 Two views of the same architecture

| Teaching model (Foundations) [F 3.1] | Formal model [P][R][A] | What lives there |
|---|---|---|
| **Layer 1, The Map** | **L0** `CLAUDE.md` | Identity, folder map, naming conventions, routing table |
| **Layer 2, The Rooms** | **L2** room or stage `CONTEXT.md` (plus **L1** root `CONTEXT.md` in Tier 2; usually absent in Tier 1) | What the area or stage is for, its process, what to load |
| **Layer 3, The Tools** | part of **L3**: skills, MCP | Skills and tools wired into the rooms that need them |
| (reference docs a room points to) | **L3** reference: `references/`, `_shared/`, brand and design folders | Voice, design system, conventions, templates |
| (drafts, outputs) | **L4** working: `output/`, `input/`, source material | This run's inputs and products |

The video covers "the three most important layers"; the paper defines five. [F 3.1]

### 4.2 The five layers

Agents read down the layers and stop as soon as they have what they need. [R][O]

| Layer | Location | Question | Role | Loaded |
|---|---|---|---|---|
| **L0** | root `CLAUDE.md` | Where am I? | Catalog: identity, routing ("the DNS of the system" [O]) | Always (Claude Code auto-loads it) |
| **L1** | root `CONTEXT.md` | Where do I go? | Catalog: task routing, shared resources ("a load balancer. Directs traffic, doesn't do work." [O]) | On entry |
| **L2** | stage or room `CONTEXT.md` | What do I do? | **The control point**: the contract | Per task |
| **L3** | `references/`, `_shared/` (or `shared/`, `_config/`, `brand-vault/`, `design-system/`), `skills/` | What rules apply? | Factory (stable) | Selectively, per Inputs |
| **L4** | `input/`, earlier stages' `output/`, user material | What am I working with? | Product (per run) | Selectively, per Inputs |

Sizes are in §3. L0 to L2 together come to about 1,300 to 1,600 tokens. In the paper's example, the three stages took about 4.9k, 5.5k, and 5.6k tokens, against about 42k for one monolithic prompt. [P Fig. 3] The origin system measured about 4,000 tokens for a script with routing, 15,000+ without, and about 500 to render. [O]

### 4.3 Why reference (L3) and working (L4) material are kept apart

> "Layer 3 material needs to be internalized as constraints and patterns: the model should write like this, use these colors, follow these conventions. Layer 4 material needs to be processed as input... Mixing persistent rules with per-run artifacts in an undifferentiated context window forces the model to sort them on its own. Separating them in the folder structure means the model receives already-organized context." [P §3.2]

| | Layer 3: Reference | Layer 4: Working |
|---|---|---|
| Changes between runs | No | Yes |
| Example files | `voice.md`, `design-system.md`, `conventions.md` | `research-output.md`, `script-draft.md` |
| The model should | Internalize as constraints | Process as input |
| Configured during | Workspace setup (once) | Pipeline execution (each run) |
| Folder location | `references/`, `_config/`, `shared/` [P]; also `_shared/` [A], `skills/` [R] | `output/` [P]; `input/` [EXT] |
| Analogy | "The recipe" | "The ingredients" |

### 4.4 Layer rules

- **R-LAY-01 (MUST)** No agent reads everything. Each task reads only as deep as it needs: a rendering stage may need only L0 to L2; a writing stage reads to L4. [P][R]
- **R-LAY-02 (MUST)** L0 to L2 are the catalog: small, stable, no content payload. [A]
- **R-LAY-03 (MUST)** L2's Inputs section makes context selection explicit, editable, and auditable instead of leaving it to the agent's judgment. Without it the agent "would either load everything in the workspace or rely on its own judgment about what matters". [P][A]
- **R-LAY-04 (SHOULD)** An L3 collection that grows past easy scanning gets its own internal `CONTEXT.md` router: L1 routing applied again inside L3. "The hierarchy is self-similar at every depth." The router shape is in §7.6. [P fn4 "can include"][R][A]
- **R-LAY-05 (INFO)** "Every token of irrelevant context is a token of diluted attention. Loading more context does not make output better. It makes it worse." [R] "When you load 15,000 tokens into an agent that needs 4,000 of them, the extra 11,000 aren't neutral. They're noise." [O]
- **R-LAY-06 (INFO)** "The context window is working memory, not storage." [R][O] "200K tokens sounds huge until you fill it with irrelevant files." [F 4.5]
- **R-LAY-07 Token discipline (SHOULD).** If a stage's context grows past about 8k tokens: (a) split the stage, (b) tighten the Inputs list, or (c) push detail down into an L3 file the contract points at but does not inline. [A][R]
- **R-LAY-08 (SHOULD)** Each stage condenses and structures its output, so the next stage's L4 stays small. [P][I]
- **R-LAY-09 (INFO)** Every token in CLAUDE.md is paid on every prompt. "A 200-line CLAUDE.md costs you on every single prompt." [PB 3.2][O]
- **R-LAY-10 (SHOULD)** Keep tables and structured data as tables; they are already token-efficient. [F 1.3]
- **R-LAY-11 (MAY)** A contract MAY state a load order ("Building animation? → Follow this specific load order"). The paper names ordering inside a layer as an open question. [O][P §5.4]

---

## 5. Tier 1: Rooms (the Foundations workspace)

This is what Jake teaches first in Clief Notes. Use it for ongoing work split by kind of task, with no fixed sequence. [F]

### 5.1 The three-file first folder [F 1.2, 3.1]

"Three files. Five minutes." Name the folder after the work. Use `.md` (plain `.txt` also works).

```
my-first-workspace/
├── CLAUDE.md      who Claude is working for and how to behave
├── CONTEXT.md     what you are working on right now
└── REFERENCES.md  background material Claude should know about but does not need to act on directly
```

- `CLAUDE.md`: Identity ("You are helping [NAME] with [WHAT YOU DO]"); the folder structure (for example `/drafts`, `/final`, `/references`); rules ("Write in plain, clear language"; "Ask clarifying questions before making assumptions"; "When you are unsure, say so"; "Read this file first on every new task"; "Ask before creating files outside of /drafts").
- `CONTEXT.md`: What we are building (2 to 3 sentences); What good looks like; What to avoid.
- `REFERENCES.md`: Examples of good work; relevant links; notes.

Three ways to load it: Claude Code (`cd` into the folder, run `claude`); a Claude Project (upload the files as Project Knowledge, and re-upload them when they change); or paste them at the top of the first message. [F 1.2]

This is the seed. Once there is more than one kind of work, grow it into rooms (§5.2). [I]

### 5.2 Map / Rooms / Tools skeleton [F 3.1, 3.2, 4.5]

```
my-project/
├── CLAUDE.md                 THE MAP: identity line, rooms, routing table, naming conventions
├── _shared/                  (optional) [EXT name] references used by several rooms: voice.md, stakeholders.md
├── writing-room/
│   ├── CONTEXT.md            THE ROOM: purpose, process, files, skills, what good looks like, what to avoid
│   ├── references/           (optional) references only this room uses
│   ├── drafts/
│   └── final/
├── analysis/
│   └── CONTEXT.md
└── planning/
    └── CONTEXT.md
```

- **The Map (`CLAUDE.md`)** is read first every time. It holds what the project is, the folder structure, the naming conventions, where things go, and the **routing table**:

  > "This is the most important pattern in the whole system. Inside it, you put a simple table that tells the AI: for this task, read these files, skip those files, you might need these skills. Without this, the AI either reads everything and wastes tokens, guesses wrong about what matters, or produces work you cannot edit along the way." [F 3.1]

- **A Room (`CONTEXT.md`)** describes what the room is for, its process ("first I do this, then I do that"), what files live there and how they are organized, which skills or tools to use, what good looks like, and what to avoid. "Plain English. Short documents. A few paragraphs." It MAY point to separate reference files when there is a lot of material. "You say 'go to writing room, let's start making something' and the AI immediately reads the context file", loads voice and style, and asks what to build. [F 3.1, 3.2]

- **The Tools (skills, MCP servers)** are wired into the rooms that need them, never loaded everywhere. "You can reference 15, 20, or 100 skills in a project, but each workspace only loads the ones it needs." [F 3.1]

The `_shared/` folder does not count as a room. A reference used by one room lives in that room's `references/`. A reference used by two or more rooms lives in `_shared/`. [EXT]

### 5.3 Rules

**Boundaries**

- **R-T1-01 (MUST)** Separate kinds of work into separate rooms, so unrelated material never shares a context window ("an AI writing a blog post is also reading your video production notes"). [F 3.1]
- **R-T1-02 (SHOULD)** Start with 2 to 3 rooms. "You can always add more." [F 3.3]
- **R-T1-03 (SHOULD) The mental-mode test.** A room boundary is a change of mental mode. "If you find yourself wishing Claude would 'forget' what it was just doing and focus on something else, that is a workspace boundary." "Drafting and editing are the same mental mode at different stages. That is one workspace with a process inside it." [F 3.2, 3.3]
- **R-T1-04 (SHOULD)** "If you are not sure whether something deserves its own workspace, it does not." Make it a subfolder. [F 3.3]
- **R-T1-05 (MUST)** One folder per client, each with its own CONTEXT.md. "Never reference one client's information in another client's workspace." To onboard a client, copy the structure, write a new CONTEXT.md, and add one routing row. [F 3.2]

**Inside a room**

- **R-T1-06 (SHOULD)** More than 8 to 10 files at one level means subfolders. Group by room (what kind of work) first, then by stage or type. "The folder structure is the architecture." [F 3.3]
- **R-T1-07 (MAY)** Use stage or status subfolders: `ideas/ drafts/ final/`; `briefs/ specs/ builds/ output/`; `intake/ deliverables/ communications/`; `active/ complete/`. [F 3.2][O]
- **R-T1-08 Naming conventions replace databases (SHOULD).** Put type, status, version, and date in filenames, and document the convention in CLAUDE.md, so the agent can find files by name: `api-auth-guide_draft.md`, `topic-name_final.md`, `2026-03-launch-week.md`, `YYYY-MM-platform-topic.md`, `demo_v2.md`, `feature-name_spec.md`, `YYYY-MM-DD-decision-title.md`. "You can say 'pull my demo v2 and build a spec from it'... No SQL. No vector database." [F 3.1, 3.2] Tier 1 uses `_` as the separator between slug and status or version; this is a sanctioned exception to R-NAME-02.
- **R-T1-09 (SHOULD)** Shared templates live in their own room (`templates/`), and new work starts by copying from it: "Proposals always start from /templates and get customized in the client folder." [F 3.2]
- **R-T1-10 (SHOULD)** Name sub-parts semantically, and record in the context file where the editable parts live, so the agent can make a targeted edit without scanning. "If your layers are called 'Layer 1' and 'Group 3,' Claude has to guess. It guesses wrong." Use patterns like `[character]_[part]_[side]`. If Claude broke something while editing, "this usually means the context file doesn't point to the right locations." [PB 1.2]

**The Map**: see §7.1. In Tier 1 it MAY also hold an identity line and a few workspace-wide rules (R-L0-02).

**Room context files**

- **R-T1-11 Describe the work, not the AI (SHOULD).** "Claude responds to context about the work far more than context about itself." Spend about 80% of a context file on the project, the audience, what has been done, what good looks like, and what to avoid. Spend 20% or less on behavioral instructions. "If your context file reads like a personality quiz, rewrite it." [F 3.3]
- **R-T1-12 (SHOULD)** Specific audience facts beat role labels: "mid-market HR directors who... are skeptical of AI claims" beats "you are a senior copywriter". [F 3.3]
- **R-T1-13 (SHOULD)** Every room context file includes "What good looks like" and "What to avoid". [F 1.2]
- **R-T1-14 Keep context alive (SHOULD).** Context files are "working notes, not finished documents". Update them when the project changes; this is "the single highest-leverage habit in the whole system". Add a "Last updated" line. When Claude seems to "get worse", suspect stale context first. [F 3.2, 3.3, 4.4]
- **R-T1-15 (SHOULD)** Keep reference material (examples, links, style guides) separate from instructions: "anything Claude should have access to but does not need to act on directly". [F 1.2]

**What goes in each kind of room** [F 3.2]

| Room | Its CONTEXT.md covers |
|---|---|
| Script lab / writing | your voice, your audience, the kind of content you make, the process from idea to finished piece |
| Production | the production process, tools, visual standards |
| Distribution | platforms, posting cadence, rules for adapting content per channel |
| Client | who the client is, what the engagement is, the current phase, the deliverables, client-specific rules (tone, terminology, things to avoid) |
| Templates | what each template is for and how to use it |
| Business development | your ideal client, your services, your positioning |
| Planning (dev) | the app, the tech stack, current priorities, architectural principles |
| Source code | code structure, naming conventions, patterns you use and avoid, testing requirements, standard libraries |
| Docs | documentation standards, the audience for each kind of doc, how docs relate to the code |
| Ops | infrastructure, deploy process, runbook conventions |

A routing row MAY chain reads across rooms: `| Build a new proposal | /templates | CONTEXT.md, then client folder |`. [F 3.2]

### 5.4 A single code project's CLAUDE.md [F 4.4]

About 15 lines, written in about 10 minutes, with five parts: overview (2 to 3 sentences); tech stack (or document types); how to run things (or how to use these files); key conventions; what to avoid. "Write it for a smart person who just joined your project." "A mediocre CLAUDE.md beats no CLAUDE.md every time." Test it by moving it out and comparing the outputs. It works for non-code folders too. The template is in §20.3.

### 5.5 Building and maintaining it

The procedure is in §15.1. Maintenance:

- "The first version will not be perfect." Add what is missing after a few days, and fix what is wrong after a week. "The best folder setups in the community were all built incrementally." [F 3.3]
- The smallest experiment: two folders, each with its own CLAUDE.md. Run the same kind of task in each and watch the behavior differ. Then join them under one routing table. [F 4.5]
- When it gets messy, ask the agent: "Clean up this project folder and update CLAUDE.md to reflect the structure." [PB 1.3]

### 5.6 Graduating from Tier 1 to Tier 2

When a sequence inside a room starts repeating (for example script → spec → build → render), turn the room into a pipeline: numbered stage folders, contracts, and `output/` handoffs (§6). The Map keeps routing to it. The origin system did this: an umbrella of rooms (brand-vault, script-lab, topic-engine, animation-studio...) in which `animation-studio` held `workflows/01-scripts → 02-specs → 03-builds → 04-renders`. [O][I]

---

## 6. Tier 2: Pipeline Structure and Naming

### 6.1 Canonical pipeline skeleton

```
workspace-name/
├── CLAUDE.md                  L0: identity, folder map, routing, triggers, the one rule
├── CONTEXT.md                 L1: the pipeline in one screen
├── PROGRESS.md                session continuity (§11)
├── setup/
│   ├── questionnaire.md       configures the factory once (§10)
│   └── new-run.md             (optional) [EXT] what the "new run" trigger does
├── _shared/                   L3 factory: voice.md, rules.md, definition-of-done.md, design-system.md
│   └── CONTEXT.md             only if the folder grows past easy scanning
├── _templates/                only when units are instantiated by copying (INV-10)
├── _archive/
│   └── runs/<run-id>/         [EXT] completed runs' outputs, kept as data
├── scripts/                   [EXT location] mechanical, non-AI work called by stages
├── skills/                    bundled domain skills (optional)
│   └── skill-name/SKILL.md
└── stages/
    ├── 01_intake/
    │   ├── CONTEXT.md         L2: stage contract
    │   ├── input/             [EXT] L4: raw per-run inputs the human drops in (entry stage only)
    │   ├── references/        L3: stage-specific reference
    │   └── output/            L4: this run's artifact, handed to 02
    ├── 02_draft/
    │   ├── CONTEXT.md
    │   ├── references/
    │   └── output/
    └── 03_finalize/
        ├── CONTEXT.md
        ├── references/
        └── output/
```

[P Fig. 2][A forms][R]; folders marked [EXT] are additions (§A5).

The ICM repo workspaces use an equally valid variant: `stages/01-script/`, `shared/` for cross-stage files, and a named context folder such as `brand-vault/` or `design-system/` with its own `CONTEXT.md`. Pick one style per workspace and hold it. [R]

### 6.2 Where things go

| Material | Location | Source |
|---|---|---|
| Identity, folder map, routing table, triggers | `CLAUDE.md` | [R][A] |
| Pipeline overview, shared-resource index | root `CONTEXT.md` | [R][A] |
| Stage-specific rules, formats, templates, tool setup guides | `stages/NN_name/references/` | [R] |
| Cross-stage reference (voice, brand, design, platform specs, definition of done) | `_shared/` (or `shared/`) | [A][R] |
| Brand, voice, or design collections big enough to need routing | a dedicated folder (`brand-vault/`, `design-system/`, `_config/`) with its own `CONTEXT.md` | [R] |
| Domain skills | `skills/<skill-name>/` | [R] |
| Raw per-run inputs (exports, uploads, source documents) | the entry stage's `input/`, or the conversation for pasted text | [EXT] (Jake: "User / (uploaded files or pasted text)" [R]) |
| Workspace scripts | `scripts/` at the root, or inside the skill that owns them | [EXT] (Jake's skills keep `scripts/` and say "Copy both into the project root" [R]) |
| Blank templates for new units of work | `_templates/` | [A] |
| Generated indexes, logs | `_index/` | [A][M] |
| The workspace's own schema (graph forms) | `_meta/schema.md` | [A] |
| Build-time design artifacts (workflow map, contracts draft, dependency diagram) | `_meta/build/` | [EXT] |
| Superseded or dead files | `_archive/` (never silently delete) | [A] |
| Completed runs kept as data | `_archive/runs/<run-id>/`, or `output/archive/<slug>-vN.ext` for earlier cuts | [EXT]; earlier cuts [R] |
| Secrets | `.env` (gitignored), plus `env-template.md` listing the variables with empty values | [R] |
| Per-run metadata (name, topic, audience) | the entry stage's `output/<slug>-meta.md`, carried forward | [R] |
| Plans and progress across sessions | `PRD.md` (or `docs/prd.md`), `PROGRESS.md` at the root | [PB] |
| Final deliverables | the last stage's `output/` (or `output/final/`), with a delivery manifest | [R] |

### 6.3 Naming rules

- **R-NAME-01 (MUST)** Stage folders carry a zero-padded two-digit order prefix. The default is `NN_kebab-name` (`01_research`) [A][P]; the variant is `NN-kebab-name` (`01-script`) [R]. Use one style per workspace.
- **R-NAME-02 (SHOULD)** Folders and files use lowercase kebab-case with no spaces. [R][A] **Exceptions** [EXT, codifying observed practice]:
  - Entry, contract, and session files are uppercase: `CLAUDE.md`, `AGENTS.md`, `CONTEXT.md`, `PROGRESS.md`, `SKILL.md`, `README.md`.
  - Generated indexes may be uppercase (`FILE-MAP.md`).
  - Code files follow their language's convention (`Beat01.tsx`, `count_issues.py`).
  - Tier 1 status suffixes use `_` (R-T1-08).
  - Title Case is allowed for human-browsed node files when the schema declares it (R-NAME-07).
- **R-NAME-03 (SHOULD)** Meta and system folders take an underscore prefix so they sort to the top: `_meta/`, `_system/`, `_shared/`, `_config/`, `_templates/`, `_index/`, `_archive/`. "Underscore = 'about the workspace, not of the work.'" [A]
- **R-NAME-04 (MAY)** Ordered files inside a folder use an ordinal-only prefix (`00-tracker.md`). [A]
- **R-NAME-05 (SHOULD)** Output artifacts are named `<topic-slug>-<artifact-type>.md` (`hello-world-script.md`). [R] (Jake writes `[topic-slug]`; this document uses `<...>` for per-run variables, see §10.1.)
- **R-NAME-06 (MAY)** Typed content files prefix their type (`data-customer-list.md`). [A]
- **R-NAME-07 (MUST)** For records and nodes, pick kebab-case slugs (machine-facing) or Title Case (where a person browses daily, as in an Obsidian vault). Pick one per workspace and write it into the schema: "drift between schema and files is the most common decay." [A]
- **R-NAME-08 (SHOULD)** Templates are blank, named for what they produce, and live together (`_templates/pilot-brief.md`). [A]
- **R-NAME-09 (MUST)** Placeholders follow §10.1.
- **R-NAME-10 (MUST)** The entry file is `CLAUDE.md` for Claude Code and `AGENTS.md` for other agents. If both exist, one is generated from the other or is a one-line pointer. Never two hand-maintained copies. [A]
- **R-NAME-11 (SHOULD)** Use sortable dates (`YYYY-MM-DD-...`). For run IDs use lowercase: `2026-w39`, `2026-09-29`, or `<slug>`. [F 3.2][M]; run-ID form [EXT]
- **R-NAME-12 (MUST)** Renumbering reorders the pipeline. In the same change, edit every input path that names a renamed folder. [A]
- **R-NAME-13 (MAY)** Alternative branches a human chooses between are sibling stages, `03a_...` and `03b_...`. [P §5.2][I]
- **R-NAME-14 (SHOULD)** Every folder that should persist but starts empty gets a `.gitkeep`. [R]
- **R-NAME-15 (MAY)** Status and version may live in filenames (`[PILLAR]-[slug]-[draft|review|final].md`, `T-[id]-[slug]-v[version].mp4`). ID systems used everywhere (pillar codes, topic codes) belong in L0. [O]
- **R-NAME-16 (MAY)** A naming convention may double as an ID scheme: `ht10-second-brain` = type + counter + slug. [A]

---

## 7. File Specifications

### 7.1 Entry file: `CLAUDE.md` (L0, the Map)

**Purpose.** Answer "where am I, where does everything live, where do I go for task X", and nothing else. It is auto-loaded into every conversation, so every line costs tokens on every task. [A][R][PB 3.2]

| Section | Content | Tier | Source |
|---|---|---|---|
| Title + one sentence | What this workspace is and what leaves it | all | [A][R] |
| Identity line | "You are helping [NAME] with [WHAT]" | 1 (optional in 2) | [F 1.2] |
| When to use this workspace | One or two lines that tell it apart from sibling workspaces ("If your video has no narration, use `script-to-animation` instead") | when siblings exist | [R voice-driven] |
| Folder map | Tree or table: folder → what it holds | all | [R][A][F] |
| Routing table | Task (or "what just happened") → go to → read → skills → stop at | all | [F][R][A] |
| Naming conventions | File patterns, ID schemes | all | [F 3.1][O] |
| Triggers | `setup`, `status`, workspace-specific keywords; each points to the file that defines it | 2, 3 | [R]; pointer rule [EXT] |
| What to Load | Task → Load These → Do NOT Load | 2, recommended | [R] |
| Starting a new run | How a run begins, the default entry stage (set in setup, overridable per run), "clear the output folders from the previous run" | 2 | [R course-deck] |
| Stage handoffs note | "Each stage writes its output to its own output/ folder. The next stage reads from there. If you edit an output file, the next stage picks up your edits." | 2 | [R] |
| The one rule | "Nothing moves to the next stage until a person has read the output of the last one." | 2, 3 | [A] |

Rules:

- **R-L0-01 (MUST)** Route, never hold content: no definitions, rule sets, examples, voice guidance, or process. [A][R][F]
- **R-L0-02 (MUST)** Stay within the §3 limits. *Allowance*: an identity line and up to about five workspace-wide rules (behavior defaults such as "Ask clarifying questions before making assumptions"; isolation rules such as "Never reference one client's information in another client's workspace") are permitted. Voice, style, and process are not. [F 1.2, 3.2][I resolving A vs F]
- **R-L0-03 (MUST NOT)** Contain setup placeholders (`{{...}}`), because it must work before onboarding runs. [R]
- **R-L0-04 (SHOULD)** A repo or umbrella root `CLAUDE.md` routes into sub-workspaces. "Navigate into a workspace folder and that workspace's CLAUDE.md takes over." [R]
- **R-L0-05 (SHOULD)** Route by task, or by "what just happened" (If | Go to | Then stop at). [A][F]
- **R-L0-06 (SHOULD)** In the What to Load table, list what NOT to load for each task: other stages' references, unneeded skills, prior runs. A Do NOT load list "gives the agent permission to not look". [R]; phrase [X]
- **R-L0-07 (SHOULD)** "The map states only what rarely changes; details live in each pipeline." [A]
- **R-L0-08 (MAY)** Include a start sequence: read this file → identify the task → go to the room or stage → read its CONTEXT.md → do the work → consult other areas only through cross-references. [O]
- **R-L0-09 (SHOULD)** A trigger row names the procedure file that defines it (`setup` → `setup/questionnaire.md`; `new run` → `setup/new-run.md`). The procedure lives in that file, not in CLAUDE.md. [EXT]
- **R-L0-10 (SHOULD)** In memory and knowledge workspaces, include a numbered "How to answer a question" procedure: read this file; follow it to the index or folder; read only the leaves you need. [M]

### 7.2 Root `CONTEXT.md` (L1)

Choose one shape per workspace:

- **Shape A, "the pipeline in one screen"** [A]. Use it when there is one linear pipeline. Contents: a one-line flow; one table `Stage | Job | Input | Output | Human check`; one line naming where the factory lives and one naming where the product lives; the deliverable line [EXT]; and the status rule.
- **Shape B, task routing** [R]. Use it when there are several entry tasks or the stages are entered independently. Contents: a one-sentence description; a `Task Type | Go To | Description` table; a `Resource | Location | Contains` table of shared resources (context folders, shared files, skills).

Rules:

- **R-L1-01 (MUST)** Routing only. The purity rules of §7.3 apply.
- **R-L1-02 (MUST NOT)** Routing tables contain placeholders. A conditional *section* (`{{?BUILD_STAGE}}`) outside the tables is allowed, as in Jake's script-to-animation. [R]
- **R-L1-03 (SHOULD)** List every shared resource with its location, so stages point to it instead of copying it. [R]
- **R-L1-04 (MUST)** The Shape A table summarizes the stage contracts. It is a sanctioned catalog summary (§8.4), and the contract is canonical. If they disagree, fix the summary. [A][EXT reconciliation]
- **R-L1-05 (SHOULD)** In Tier 1 there is usually no root CONTEXT.md. The Map routes straight to each room. [F]

### 7.3 Stage `CONTEXT.md` (L2, the stage contract)

**Purpose.** The contract for one stage: what it reads, what it does, what it writes, and what a human checks. "Simple enough that a non-technical user can read it and understand what is happening. Structured enough that an agent can follow it reliably. Every stage follows this exact shape. No exceptions." [R Pattern 1]

**Section order** (unified from [R] and [A]; delete the optional sections a stage does not need):

| # | Element | Form | Status | Source |
|---|---|---|---|---|
| 1 | Title | `# NN_stage-name: the job in about five words` (repo form: `# Stage 01: Script Writing`) | required | [A][R] |
| 2 | Job line | `One job: ...` (one sentence) | required | [A][R] |
| 3 | `## Inputs` | table or list | required | [P][R][A] |
| 4 | `Do NOT load:` | a line under Inputs, not a heading | strongly recommended | [A template] |
| 5 | `## Process` | numbered steps | required | [P][R][A] |
| 6 | `## Checkpoints` | table | creative and analytic stages | [R] |
| 7 | `## Audit` | table | creative, analytic, build stages | [R] |
| 8 | `## Verify` | list (proposed) | optional | [P §6.2] |
| 9 | `## Outputs` | table or list | required | [P][R][A] |
| 10 | `## Human check` | one paragraph: the act, the reviewer, the gate type | required | [A]; reviewer and gate fields [EXT] |

**Inputs**

- **R-CTR-01 (MUST)** List every file the agent needs. Paths in a CONTEXT.md are relative to that file. Paths in CLAUDE.md are relative to the workspace root. A Do NOT load line may name folders from the root. [R][A]; path base [EXT]
- **R-CTR-02 (MUST)** Label each input **Working (this run)** (L4) or **Reference (every run)** (L3). The paper writes `Layer 4 (working)` / `Layer 3 (reference)`. [P][A]
- **R-CTR-03 Route to sections, not just files (MUST).** Name the section ("'Hard Constraints' through 'What the Voice Is NOT'"). Write "Full file" when the whole file is needed, "Header only" when only the metadata header is needed, and "Path only" for binaries passed to a script. [R Pattern 4][R] The origin system called this "the highest-leverage pattern in the whole system... same principle as database views." "A 150-line file might have only 60 lines of actionable rules for a specific stage." [O][R]
- **R-CTR-04 (MAY)** Table form `Source | File/Location | Section/Scope | Why` [R], or list form `- Working (this run): ../01_research/output/research.md` [A].
- **R-CTR-05 (MUST)** The working input names the previous folder's real name: "renumbering the pipeline means editing this path." [A]
- **R-CTR-06 (MUST)** User input is a row with Source `User` and Location `(conversation)`, `(uploaded files or pasted text)`, or `input/` [EXT]. [R]
- **R-CTR-07** Skill row: `| Skill | ../../skills/<name>/SKILL.md | Index, then load rules as needed | <what it provides> |`. A skill MAY declare a core set of rules to load every time, plus as-needed rules ("Load `rules/timing.md`... for every build. Load other rule files as needed."). [R]
- **R-CTR-08 (MAY)** When an output folder may hold several files, select with a phrase such as "Most recent script file (full)". [R]
- **R-CTR-09 (MUST NOT)** Point inputs at earlier runs' outputs *to learn patterns* (§8.7). Declared prior-run *data* inputs are allowed under §9.9. [R][EXT]

**Do NOT load**

- **R-CTR-10 (SHOULD)** Name anything an eager agent would wrongly pull in: other stages' references, prior runs, the whole `_shared` folder, skills this stage does not need. In build stages add "Do not read other output/ files to learn patterns." [A][R]

**Process**

- **R-CTR-11 (MUST)** Numbered steps. Each step is one concrete action. [R]
- **R-CTR-12 (MUST)** "Be specific enough that two different agents following these steps would produce structurally similar outputs." [R]
  - Too vague: "Write the script." Good: "Write the full script in one pass, then audit against the voice hard constraints and value brief."
  - Too vague: "Generate ideas." Good: "Propose 3-5 concept angles, each as a single sentence. Tag each with its value type and format."
- **R-CTR-13 (SHOULD)** Keep it short. "Constraints live in L3 files, not restated here." "Contracts that restate reference material (point instead)" is a named failure. [A]
- **R-CTR-14 (MAY)** Restate hard limits worth repeating (length, count, format: "Keep under 90 seconds spoken"), with the canonical file named in parentheses. [A]; pointer [EXT]
- **R-CTR-15 (SHOULD)** Mark checkpoint steps inline: `**[Checkpoint N]** -- Present X to the human for Y`. [R]
- **R-CTR-16 (SHOULD)** The second-to-last step is usually "Run the audit checks below. If any fail, revise before saving." The last step is "Save to output/". [R]
- **R-CTR-17 (SHOULD)** In the entry stage, step 1 restates the task in one sentence so the human can confirm scope (a checkpoint after step 1). Then collect the per-run metadata (name, topic, audience, scope) and write it to `output/<slug>-meta.md`. [R voice-driven 01-research, course-deck 01-extraction]
- **R-CTR-18 (SHOULD)** Frame steps as production ("read X, produce Y"), not exploration ("help me explore X"). [X][I]
- **R-CTR-19 (MUST)** Before any paid, external, or irreversible call: check the preconditions ("Confirm `.env` exists and is in `.gitignore`. If not, stop and ask the human"), do a dry run, and put a checkpoint on the dry-run result ("Approve or fix the script before spending API credits"). [R 03-voice]

**Outputs**

- **R-CTR-20 (MAY)** Table form `Artifact | Location | Format` [R], or list form `- script_draft.md → output/` [A][P].
- **R-CTR-21 (MUST (validation))** Every output is consumed by a downstream stage or is the final deliverable. [R WB 02]
- **R-CTR-22 (SHOULD)** Say that the output is the human's edit surface and the next stage reads whatever is there. [R][A]
- **R-CTR-23 (SHOULD)** Each output starts with a header (§9.4).

**Human check**

- **R-CTR-24 (MUST)** Exactly one human check per stage, stated as something a person *does*, not a vague "review". Examples: "Read the draft aloud." "Verify the numbers against X." "Confirm the argument order survived from research." Close with: "Edit in place; the next stage reads whatever is here." [A]
- **R-CTR-25** Checkpoints and the Human check are different things. Checkpoints happen *inside* the stage, before output is written; there can be several. The Human check is the single gate on the *saved* output, before the next stage reads it. Repo-style stages that have only checkpoints SHOULD gain a Human check line. [I reconciling R and A]
- **R-CTR-26 (SHOULD)** The Human check names the reviewer (`Reviewer: analyst`, `Reviewer: manager`) and the gate type (§9.6). [EXT]

**Verify (proposed in the paper; partly practiced)**

- **R-CTR-27 (SHOULD where drift is possible)** A late stage audits against outputs two or more stages back, not only its immediate input. Jake's practice: an audit file that makes "the agent trace back from the specification to the original script, re-verifying timing for each phrase" ("checking that the output of stage n is consistent with the output of stage n − 2"). It catches "frame count discrepancies, visual density mismatches, and pacing breaks at scene boundaries". Another live example: "Claims sourced: every quantitative claim traces to a citation in the brief." The paper proposes formalizing this as a `## Verify` section: which earlier outputs to check, and against what criteria. [P §6.2][R]

**Purity and size**

- **R-CTR-28 CONTEXT.md is routing, not content (MUST).** It answers three questions: what is this folder, what do I load, what is the process. "No definitions. No rules. No extended examples. No voice guidelines." [R Pattern 6]
- **R-CTR-29 (SHOULD)** "If you find yourself writing more than a one-sentence description in a CONTEXT.md, that content belongs in a separate file that the CONTEXT.md points to." [R]
- **R-CTR-30 (MUST (validation))** Allowed content only: the elements in the table above, plus a "Source of truth" or "When to loop back" table in final and validation stages (§9.10). [R WB 05 check 6][R voice-driven]
- **R-CTR-31 (MUST)** Size per §3 (under 80 lines). Warning signs: more than 80 lines; code examples; "Why it works" sections; information duplicated from another CONTEXT.md. [R][O]
- **R-CTR-32 (SHOULD)** It doubles as human documentation (literate programming). [P]

### 7.4 Room `CONTEXT.md` (Tier 1)

Required: what the room is for; its process; what lives here and how files are named; the skills and tools to use; what good looks like; what to avoid; a "Last updated" line. Same purity rule as R-CTR-28 (pointers to references, no long pasted material). Size per §3. [F 1.2, 3.1, 3.2, 3.3] The template is in §20.2.

### 7.5 Reference files (L3)

- **R-REF-01 (MUST)** Under 200 lines. Split longer files. [R]
- **R-REF-02 (MUST)** Reference files hold the rules, definitions, examples, and templates that CONTEXT.md files may not. [R]
- **R-REF-03 "Write for machines, store for humans."** Source docs explain why each rule exists, and routing extracts only the what. A file MAY carry a "Strategic Rationale" section that section routing usually skips. [O][R]
- **R-REF-04 Reference-file anatomy (SHOULD)**, observed across Jake's reference files [R]:
  1. A purpose line: who reads it and when ("Agents reference this to ensure scripts and specs fit the target format").
  2. The configured choice first, for multi-option files ("## Active Platform: This workspace is configured for {{PRIMARY_PLATFORM}}").
  3. Required sections or fields.
  4. A numbered Rules list.
  5. What it does NOT contain or cover ("What a Spec Does NOT Contain"; "What to Skip").
  6. A paired good and bad example, with the reason the good one works ("The first produces better output because the builder can choose").
  7. Pattern cards for libraries of options: Template / Example / Best for / Avoid when / Key rule (as in the hook system).
  8. A selection guide with a default ("If none fit cleanly, default to Layered Reveal").
  9. Size targets with a consolidation trigger ("Target 3-8 chunks per expected session... If you have 300, consolidate").
  10. Common Mistakes covering *both* failure directions (over-specifying and under-specifying).
  11. Optional Strategic Rationale.
- **R-REF-05 (SHOULD)** Design-system references include **Recipes** (copy-and-adapt patterns), an **Anti-Patterns** table (`Error | Why It Fails`), and a **Production Checklist** the build audit references. [R]
- **R-REF-06 (SHOULD)** Reference values by semantic role, not literal value ("Roles, not colours. `HIGHLIGHT` is the subject...Any theme then works"), so the factory can be swapped. [lecture-deck]
- **R-REF-07 (SHOULD)** A downstream reference states its own latitude: what HOW decisions the stage owns ("The builder has full creative latitude for implementation: animation approach... layout... component choices"). [R build-conventions]
- **R-REF-08 (MUST)** Tool setup guides go in the `references/` of the stage that uses the tool, or `_shared/` if several stages need it. Write them for someone who has never installed the tool: what it is (one sentence), install steps, how to verify, how the workspace uses it. Tools bundled inside skills need no separate guide. `setup` checks which tools are needed and points to the guides. [R Pattern 7]
- **R-REF-09 (MUST)** Brand and identity folders are READ-ONLY during runs: "It's the DNA." "Never let downstream stages overwrite this folder." In conflicts, the brand file wins. A human edits them "directly if your voice evolves". [O][R]
- **R-REF-10 (SHOULD)** Use the person's real assets (their brand, their voice, their examples), not sample templates. "The value only shows up when the system reflects your actual brand." [PB Claude Design]
- **R-REF-11 Closed registries (MAY).** When builds must use only approved building blocks, keep a registry: "Specs and builds should only reference components listed here. If you need a component that does not exist, add it to this registry first." For how a registry interacts with spec purity, see §A3. [R component-registry]

### 7.6 L3 folder routers

A `CONTEXT.md` inside a reference collection (`brand-vault/`, `design-system/`, `_shared/`) uses one table: `| File | Key Sections (or Section to Load) | Load When |`. It includes rows marked rarely needed ("Strategic Rationale ... (rarely needed)"), lists which stages reference the folder, and states its edit policy ("Edit them directly if your voice evolves. Never let downstream stages overwrite this folder."). [R brand-vault, design-system] Listing consumer stages is a description, not a back-reference. The router must not route *to* those stages (R-XREF-01). [I]

### 7.7 Voice file

A voice file (`voice-rules.md` or `_shared/voice.md`) has five parts [R]:

1. **Hard Constraints.** "These are errors. If the output contains any of these, rewrite." A numbered list. The repo's defaults (keep or delete them at setup [EXT]) are: no filler transitions ("Now let's talk about..."); no "clean summaries at the end of sections"; no hype language ("game changing", "revolutionary"). Jake's own content voice also bans em dashes in scripts ("Em dashes. Never."). [R questionnaire example][O]
2. **Sentence Rules.** A `Wrong | Right` table of verbatim examples, for instance "They invested significant time in infrastructure development." → "They spent six months building a custom pipeline."
3. **Pacing.** The rhythm, for instance "setup, dense, dense, breath, dense". Derive it from the user's example sentences; do not ask for it as a description (R-Q-07).
4. **What the Voice Is NOT.** Named anti-patterns with Bad and Good examples: not performative (never announce credentials); not antithetical ("not X, but Y" at most once per piece); not rhetorically questioning.
5. **Strategic Rationale.** Why these choices fit the audience. Usually not loaded.

"Examples over descriptions. Examples are pattern-matchable. Descriptions require interpretation and produce weaker constraints." [R]

### 7.8 Reference discipline: one-way references, canonical sources, recursive routing

**One-way references** [R Pattern 3][O]

- **R-XREF-01 (MUST)** "Every folder points outward to what it needs. No folder points back." If stage 03 references stage 02's component registry, stage 02 references nothing in stage 03. A brand folder that serves several stages references no stage.
- **R-XREF-02 (SHOULD)** Before adding a reference, ask: "Does the target file already reference my folder? If yes, restructure."
- **R-XREF-03 (MUST (validation))** The within-run dependency graph is a DAG. This keeps reference growth linear instead of N-squared ("O(n²) maintenance").
- **R-XREF-04 (SHOULD)** If B would need to point back at A, you probably need a third location C that both reference. [O]
- **R-XREF-05 (MAY)** A later stage reads an earlier stage's `references/` file instead of copying it ("One canonical source, no duplication"). A workspace may point at a sibling workspace's skill instead of bundling it twice. [R]

**Canonical sources** [R Pattern 5][A][F]

- **R-CANON-01 (MUST)** "Every piece of information has ONE home. Other files point there. They do not duplicate it." "The moment the same rule exists in two files, they will inevitably drift." [R][O] The sanctioned summaries are listed in §8.4.
- **R-CANON-02 (SHOULD)** Smell test: search the workspace for a specific phrase. "If it appears in more than one file and both instances are meant to be authoritative, one needs to become a pointer."
- **R-CANON-03 (MAY)** A pointer file can stand in for a copy: "This file is a pointer, not a copy. Do not duplicate content from CONVENTIONS.md here." [R]
- **R-CANON-04 (SHOULD)** When you remove a duplicate, leave a link where the copy was if anything referenced it. [A]
- **R-CANON-05 (SHOULD)** Map the information architecture before writing prompts: what exists, where each piece canonically lives, and which tasks need which pieces. [O]

**Recursive routing** [A][P][M]

- **R-ROUTE-01 (SHOULD)** Any folder that grows past easy scanning gets its own `CONTEXT.md` router (shape in §7.6).
- **R-ROUTE-02 (MUST)** "Each level has its own small catalog, and no level's catalog describes the internals of the level below — it links down and stops." [A]
- **R-ROUTE-03 (SHOULD)** A folder's `CONTEXT.md` says what does NOT belong there and points to where it lives, for example "Plans/events (like conventions) live in [[../plans/CONTEXT.md]] instead." [M]

---

## 8. Stage Design

### 8.1 Where to cut stages

- **R-STG-01 One stage, one job (MUST).** "A stage that fetches data does not also filter it. A stage that filters does not also format the final output." Split any stage that does two jobs. [P][A]
- **R-STG-02 Cut where the human naturally pauses (SHOULD).** "Their pauses become stage boundaries. Their 'I always check X before Y' become human gates. Their 'it always has to sound like / follow Z' becomes factory reference material." [A]
- **R-STG-03 Surface the judgment call before the expensive work (MUST).** "Surfacing the judgment call (an outline, a structural plan) as an editable file before the expensive downstream work is the whole trick. Correction is cheapest at the earliest gate." Put a boundary right after any decision that determines everything downstream. [A][P §4.3]
- **R-STG-04 (SHOULD)** Give each stage a focused, scoped task, not "a monolithic instruction to do everything in a single pass". [P §3.3]
- **R-STG-05 (SHOULD)** Prefer tightly scoped stages: clear instructions, limited reference material, a specific output format. "The structure of the context delivery... may matter as much as the content of the context itself." [P §5.4]
- **R-STG-06 (SHOULD)** Mechanical steps that need no AI become scripts, called from the stage (§13.2). [P]
- **R-STG-07 (SHOULD)** If two stages always run together with no review between them, merge them. [X]
- **R-STG-08 (INFO)** Stages exist for optionality: "The AI can automate all four or you can get deeply involved at any step. That is the whole point of having it broken into stages." [PB 1.1]
- **R-STG-09 (SHOULD)** Leave steps that are faster by hand to the human's tool ("a video editor task, not an AI task"). [PB 1.1]
- **R-STG-10 (SHOULD)** Start short. Prove the pipeline on a small deliverable (a 30-second animation) before scaling (10 minutes). [PB 1.1]
- **R-STG-11 (SHOULD)** Build reusable components and pattern libraries, so the agent assembles proven parts instead of inventing them each run. [PB 1.1][R slide-patterns]
- **R-STG-12 (SHOULD)** When a stage must produce variants for several targets, keep one file per variant (`<slug>-spec-vertical.md`), and author the most constrained one first ("It is more constrained"). [R platform-specs]

### 8.2 Stage classes

| Class | Examples | Checkpoints | Audit | Default gate (§9.6) |
|---|---|---|---|---|
| **Creative** | writing, design, ideation | MUST (validation): at least one | MUST (validation) | blocking |
| **Analytic** [EXT class] | clustering, prioritizing, deciding what matters, interpreting data | SHOULD: at least one, on the judgment call | MUST (validation) | blocking |
| **Build** | code, assembly, rendering from a spec | MAY | MUST (validation) | blocking, or auto-advance if the audit is fully mechanical |
| **Linear** | extract, convert, normalize, render, validate | MAY run straight through | SHOULD where checks exist | auto-advance allowed |

[R Patterns 11 and 12 ("should"), WB 05 checks 7 and 8 (enforced)]. Any stage that makes a judgment call shaping downstream work gets a checkpoint on it (R-STG-03). [I]

### 8.3 Checkpoints (inside a stage) [R Pattern 11]

- **R-CHK-01** At least one per creative stage (MUST (validation)). They are optional in linear stages.
- **R-CHK-02 (MUST)** "The agent completes a full unit of work, presents options or a draft, and the human redirects before the next unit begins. Checkpoints go between process steps, not within them."
- **R-CHK-03 (MUST)** Table form: `After Step | Agent Presents | Human Decides`. Step numbers must point at real process steps.
- **R-CHK-04 (SHOULD)** Good checkpoint patterns:
  - Restate the task in one sentence (after step 1).
  - Show 3 to 5 options (angles, concepts) to choose from.
  - Show a brief (concept, value slots, format, hook, close) before drafting.
  - Show an extraction or plan for a completeness check.
  - Show a dry-run result before a paid call.
  - Show the dependency diagram and draft contracts.
  [R]
- **R-CHK-05 (INFO)** A checkpoint is the implemented form of the paper's proposed "breakpoint in markdown": "after the agent processes this instruction, show me what it produced before continuing." [P §6.2][I]

### 8.4 Sanctioned duplication (exceptions to one home per fact) [EXT, codifying source practice]

Walk-test W5 (§17.1) applies to *authoritative* copies only. These restatements are allowed, provided the copy names its canonical file:

| Restatement | Canonical home | Source of the practice |
|---|---|---|
| Root CONTEXT.md Shape A summary row per stage | the stage contract | [A template] |
| CLAUDE.md "Then stop at" column | the stage's Human check | [A template] |
| Hard limits restated in a Process step or an Audit row | the reference file | [A R-CTR-14] |
| "The one rule" in CLAUDE.md, repeated in contracts | CLAUDE.md | [A] |
| Per-run metadata snapshot in each stage's output | the entry stage's `<slug>-meta.md` | [R course-deck] |
| `AGENTS.md` / `routing.md` twins | `CLAUDE.md` (generated, byte-identical) | [A system-map] |
| Original source files kept in `source/` during a conversion | the converted markdown, after sign-off | [EXT] |

### 8.5 Audits (before writing output) [R Pattern 12]

- **R-AUD-01** Creative, analytic, and build stages carry an Audit table `Check | Pass Condition` (MUST (validation)).
- **R-AUD-02 (MUST)** The audit runs after the process and before writing to `output/`. "If any check fails, the agent revises before saving to output/."
- **R-AUD-03 (MUST)** "Each check should be specific enough that pass/fail is unambiguous." Good: "Em-dash count: zero"; "Every chunk traces back to a specific source document or section"; "Word count within ±10% of budget"; "Beat N's start is strictly less than Beat N+1's start". Bad: "Quality is good".
- **R-AUD-04 (INFO)** Audits are each stage's quality floor; they stop problems spreading downstream.
- **R-AUD-05 (SHOULD)** Values the agent computes are derived, never guessed, and the audit checks it: "Every `T` constant was computed `absolute - beat.start`; no values guessed." "Never adjust by ear." [R 04-animate]
- **R-AUD-06 (SHOULD)** Prove an audit works by planting a known error and confirming the audit catches it. "A guard that exists is not a guard that works. Only a planted mistake proves a guard." [X 4R]

### 8.6 QA and delivery stages [R course-deck 05, voice-driven 05][lecture-deck]

- **R-QA-01 The fix loop (SHOULD).** Inspect or render → classify issues by severity (**Critical: must fix**; **Warning: should fix**; compliance) → fix at the *source* artifact in the upstream stage, not in the rendered output → regenerate → re-verify → log each issue as resolved in a QA report → "Repeat until clean". [R][lecture-deck: "Fix, re-render what changed, repeat until clean."]
- **R-QA-02 Ship-ready definition (SHOULD).** A final stage defines "ship-ready" as a checklist, for example: all pre-flight items checked; the run exited cleanly; post-run checks pass; a human reviewer has reviewed the full artifact once and approved. "If any of those fail, do not deliver. Fix and re-render. The cost of a re-render is far smaller than the cost of shipping the wrong cut." [R render-checklist]
- **R-QA-03 Rigor by tier (MAY).** Full checks for finals, light checks for drafts: "Skip none of these on a final-cut render. Skip them all freely on a draft." [R]
- **R-QA-04 (SHOULD)** Check where defects cluster ("Watch the first 5 seconds and the last 10 seconds at full attention -- those frames are where rendering tends to drift"), and check at real size. [R][lecture-deck]
- **R-QA-05 Delivery package (SHOULD).** The final stage writes the deliverable (`output/` or `output/final/`), a QA report, a delivery manifest (contents, counts, sizes), and a release note (date, runtime or size, "any caveats (open questions from research that survived)"). It names anything that is still placeholder. Earlier cuts go to `output/archive/<slug>-vN.ext`. [R][lecture-deck]
- **R-QA-06 (SHOULD)** Distribution (sending, posting, publishing) is a human act or a declared script, outside the AI stages. [EXT]

### 8.7 Docs over outputs [R Pattern 14]

- **R-QUAL-01 (MUST NOT)** Read previous `output/` files to learn patterns. Reference docs are the authority on how to build. "Early outputs are the worst outputs. If future agents learn from them, quality never improves."
- **R-QUAL-02 (MAY) Curated exemplars are allowed.** A reviewed example that the factory owner promotes into `references/` (or `REFERENCES.md`, "Examples of good work") is reference material, not output. Copying a whole workspace's *structure* to start a new one (§A2.7) is not "learning from outputs". [I reconciling R and F]
- **R-QUAL-03 (MUST)** Examples placed next to a rule agree with it, because "a model copies examples before a model follows rules." [X, crediting Jake's audit]

### 8.8 Value validation (persuasive or teaching deliverables) [R Pattern 13]

Apply this when the deliverable must persuade, teach, or hold attention (content and courses). It is optional for operational reports. [EXT scope]

- **R-VAL-01 (SHOULD)** Define the value types once, in a reference file. Examples: NOVEL, USABLE, QUESTION-GENERATING, INTERESTING; for courses, TEACHES, PRACTICES, CHALLENGES.
- **R-VAL-02 (SHOULD)** Before the main creative work, at a checkpoint, lock which value types this piece will deliver. Minimum 2. "Two strong value slots are better than four weak ones. Three is ideal when the concept supports it."
- **R-VAL-03 (SHOULD)** The audit checks that the output delivers the locked slots. This prevents "interesting but doesn't DO anything" output.

### 8.9 Specs are contracts [R Pattern 10][PB 1.1]

- **R-SPEC-01 (MUST)** Spec stages define WHAT the output must achieve and WHEN things happen, not HOW to build it.
- **R-SPEC-02 (SHOULD)** A spec, in the animation example, contains:
  - a beat map with approximate durations, narration, and mood
  - the visual philosophy (what a muted viewer should understand)
  - 2 to 3 key moments that MUST land, and why
  - audio sync points
  - the color flow
  - persistent elements ("Delete this section if nothing persists")
- **R-SPEC-03 (MUST NOT)** A spec contains implementation choices that belong to the downstream stage. In the animation example these are frame numbers, component names, pixel positions, spring configs, prop definitions, and code.
- **R-SPEC-04 (MUST)** The split is "spec = WHAT/WHEN, design system = quality floor, builder = HOW". "Creative freedom means choosing how to implement those requirements, not whether to implement them." [R]
- **R-SPEC-05 (INFO)** The spec is "the most important file in the entire workflow... a contract between the voiceover and the animation." "Putting code-level detail in the spec actually constrained Claude and made the animations worse. Giving Claude creative room within clear boundaries produces better results." [PB 1.1]
- **R-SPEC-06 (MUST)** Do not under-specify either: "Writing 'show a diagram' without describing what the diagram contains... The spec should be detailed enough that two different animators would produce similar visuals." [R animation-guide] The inverted U: "too few constraints and you get chaos, too many and you get stiff output, the right amount and creativity increases." [PB 1.1, citing F 2.6]
- History: the origin system wrote specs as "code blueprints" and called it "the biggest single improvement". v2 reversed this because prescribing HOW "removes creative freedom from the build stage and produces rigid, uncreative output". [O][R]

### 8.10 Shared constants (code workspaces) [R Pattern 15]

- **R-CONST-01 (SHOULD)** Configurable values (colors, fonts, timing, layout) live in one shared file that every build output imports (`import { COLORS, FONTS } from "../constants"`). The questionnaire fills it once. This is canonical sources applied to code. If no constants file exists yet, define the values at the top of the file "and note that they should be extracted". [R]
- **R-CONST-02 (SHOULD)** Non-code workspaces keep shared values in reference docs instead.
- **R-CONST-03 (SHOULD)** Do not hand-code what an existing package or skill already does. Check first ("Check `@remotion/paths`... before writing custom implementations"). [R build-conventions]

### 8.11 Research and analysis stages [R voice-driven 01-research]

- **R-EVID-01 (SHOULD)** Gather a bounded set of primary sources (Jake uses 3 to 7). Each claim gets a source link, and a verbatim quote if it is a number.
- **R-EVID-02 (MUST)** Surface conflicts. "If two reputable sources publish different numbers... both numbers go in the brief." "Conflict surfacing: If sources disagree, the disagreement is in the brief, not buried."
- **R-EVID-03 (MUST)** "If no reputable source has the number you need, the script does not assert that number. Hand-wave abstractions are worse than direct uncertainty."
- **R-EVID-04 (SHOULD)** Tag non-public sources `[internal]` "so the script writer can decide whether to keep, paraphrase, or omit."
- **R-EVID-05 (SHOULD)** Audience-fit audit: the output "assumes only what [the] Audience section says they already know".
- **R-EVID-06 (SHOULD)** Numbers in a report come from scripts or cited sources, never typed by hand. "Do not type a number into a .tex file." [M]

---

## 9. Run Lifecycle (operating a pipeline)

### 9.1 Starting a run

1. Read `CLAUDE.md`, then `PROGRESS.md` if it exists (§11).
2. Decide the entry stage. Use the default set during setup unless the human overrides it for this run. "You can always override per course." [R course-deck]
3. Archive the previous run's outputs to `_archive/runs/<run-id>/` [EXT], or clear the output folders ("To start a fresh run, clear the output folders from the previous course." [R]).
4. Put raw inputs in the entry stage's `input/` [EXT], or take them from the conversation.
5. The entry stage restates the task for confirmation, then collects the per-run metadata into `output/<slug>-meta.md` (R-CTR-17).

### 9.2 Per-run variables

A per-run variable is any value that changes each run (topic slug, week, client). Paths and filenames write per-run variables as `<name>`, for example `output/<topic-slug>-script.md` or `input/<week>-tickets.csv`. [EXT syntax; Jake writes `[topic-slug]`] Each variable is defined once, in the entry stage's meta file. Per-run values MUST NOT become setup placeholders (R-Q-03). [R]

### 9.3 Handoffs

- **R-RUN-01 (MUST)** Stage N writes `stages/NN_name/output/<slug>-<artifact>.md`, and stage N+1 reads it by exact path. "No state management. No orchestration layer. Just files in predictable places." [R Pattern 2]
- **R-RUN-02 (MUST (validation))** The handoff chain is unbroken: stage N's output location matches stage N+1's input reference. [R]
- **R-RUN-03 (MUST)** Each stage output is a complete, readable artifact that "captures the work done so far and provides everything the next stage needs to continue." [P §3.3]
- **R-RUN-04** The entry stage's metadata travels forward: each stage copies `<slug>-meta.md` into its own output. This is a sanctioned snapshot (§8.4). Any stage MAY be the entry point; if it is, it collects the metadata itself. [R]
- **R-RUN-05 (MAY)** A stage reads more than its immediate predecessor (a validation stage reads 03 and 04), as long as Inputs declares it. Sibling stages MAY share one predecessor (a table stage and a digest stage both reading 02); the human runs them in sequence. [R][EXT for siblings]
- **R-RUN-06 (MUST)** Every output goes to a named file in a named folder, never only into chat. ("Save the result as summary.md in this folder.") [F 4.2]
- **R-RUN-07 (SHOULD)** Carry uncertainty forward. Each handoff artifact has an **Open Questions** (or Caveats) section: "This is where uncertainty lives so the script writer can route around it." The final release note lists the caveats that survived. [R citation-format, render-checklist]
- **R-RUN-08 (MAY)** Write an artifact with two faces when a machine and a human both consume it: a clean block for the tool ("PASTE THIS into ElevenLabs") plus an annotated working copy, kept in sync. Make anchors distinctive for the next stage's parser ("The first 3-5 words... need to be distinctive enough that they appear nowhere else"). [R script-template, beat-markers]

### 9.4 Output headers and provenance

- **R-RUN-09 (SHOULD)** Each output starts with a small metadata header: title or slug, status, targets (length, format, platform), and **the upstream source filename** (`source-script: <filename from 01-script/output/>`). Later stages can read "Header only" for checks, and the `source-*` fields give lineage. [R spec-format, script-templates, script-template]
- **R-RUN-10 (SHOULD)** The header's `status` field carries approval state (§9.5).
- **R-RUN-11 (MAY)** Mark revisions inside the artifact with a "What changed from the prior cut" table: `| Prior item | Fate (Kept / Revised / Removed / Replaced) | Note |`. [R]
- **R-RUN-12 (MAY)** The paper proposes a future practice: embed lightweight provenance markers (GUIDs, section tags, comment annotations) that point back to CONTEXT.md or reference sections, like debug symbols. [P §6.2, proposed]

### 9.5 Status and approval

**Jake's rule.** The filesystem is the state machine.

- **R-STATE-01 (MUST)** The `status` trigger scans `stages/*/output/`. A stage is COMPLETE when its output folder holds an artifact other than `.gitkeep` (list the filenames); otherwise it is PENDING. It renders an ASCII pipeline, as below. [R]
- **R-STATE-02 (MUST)** "A placeholder that only keeps the empty folder in git does not count." [A]
- **R-STATE-03 (MUST)** In record and graph forms, status lives in frontmatter or a generated index log, never in a hand-kept tracker. [A]

**Approval extension [EXT].** "COMPLETE" alone cannot show that a human passed the gate. Jake's own artifacts already carry `**Status:** draft / revised / final` [R]. Extend that header so status shows one of three states:

| State | Condition |
|---|---|
| PENDING | No artifact in `output/` |
| DRAFT | An artifact exists, and its header is `status: draft` (or `revised`) |
| APPROVED | Header `status: approved`, with `approved_by:` and `approved_on:` written by the human, or by the agent at the human's explicit instruction |

```
Pipeline Status: weekly-ops-digest   (run 2026-w39)

  [01_intake]  ---->  [02_issues]  ---->  [03_digest]  ---->  [04_table]
   APPROVED            DRAFT               PENDING             PENDING
 (2026-w39-intake.md) (2026-w39-issues.md) (empty)             (empty)
```

The next stage MUST NOT start while its predecessor is DRAFT, unless the predecessor's gate type is auto-advance (§9.6). [EXT, implementing INV-06]

### 9.6 Human review and gate types

- **R-HUM-01 (MUST)** "Nothing moves to the next stage until a person has read the output of the last one." [A]
- **R-HUM-02 (MAY)** At each gate the human may: proceed; edit the output file directly, then proceed; re-run the previous stage with different input; or abandon the run. [P §5.3]
- **R-HUM-03 (SHOULD)** Editing an output is "the primary way to steer the pipeline." [R]
- **R-HUM-04 (MUST)** Branching decisions belong to the human and are made between stages. [P]
- **R-HUM-05 (SHOULD) The U-curve.** Expect heavy editing at stage 1 (direction-setting, creative judgment), light editing in the middle (held in place by the upstream output and the reference material), and heavy editing at the last stage (alignment, closer to debugging). In the paper's practitioner group, 30 of 33 reported this, at about 92%, 30%, and 78% edit frequency across three stages. "Design the first and last outputs to be especially easy to edit." [P §4.5][A]
- **R-HUM-06 (MUST)** When an output is wrong, say what is wrong and iterate. "Starting over throws away all the context." [F 4.2]

**Gate types [EXT].** These reconcile INV-06 with Jake's statements that linear stages "run straight through" and that "the AI can automate all four". [R][PB]

| Gate type | Meaning | Allowed for |
|---|---|---|
| **blocking** (default) | The next stage waits for APPROVED | every stage |
| **auto-advance** | The next stage may start once the audit passes; the human still reads the output at the next blocking gate | linear stages, and build stages with fully mechanical audits |
| **final approval** | The ship-ready gate before delivery (R-QA-02) | the last stage |

Declare the gate type in each contract's Human check (`Gate: blocking. Reviewer: manager.`). At least one blocking gate MUST come after every creative or analytic stage. [EXT]

### 9.7 Re-running and propagation

- **R-RUN-13 (SHOULD)** Re-run only the stage that needs it. "If the research output is fine but the script needs rework, the practitioner re-runs stage 2 without touching stage 1." [P §6.1]
- **R-RUN-14 (MUST)** A stage's Inputs table declares its dependencies. When any of those files change, the stage's output may be stale: re-run it and everything downstream. "Changed script? Regenerate spec. Changed spec? Rebuild composition." [P][O]
- **R-RUN-15 (MUST)** Flow is one-way: "Don't reverse-engineer earlier stages from later ones." [O]
- **R-RUN-16 Fix upstream, do not work around it downstream (MUST).** "If two beats start with similar openers, change one. Edit the script; do not work around it in Stage 03." [R beat-markers] This is the edit-source principle applied inside a single run.
- **R-RUN-17 (INFO)** Error recovery is a manual re-run of the failed stage. [P]

### 9.8 Source of truth and loop-back tables (final and validation stages)

- **R-RUN-18 (SHOULD)** When the source of truth shifts along the pipeline, state it in a "Source of truth at each stage" table, and re-derive everything downstream when a source changes. Jake's voice-driven pipeline runs: verified cited sources → script → audio ("if the audio differs from the script, the audio wins") → beat timings → composition. "The brief is a plan, not a citation." [R pipeline-overview]
- **R-RUN-19 (SHOULD)** Final and validation stages carry a "When to Loop Back" table, mapping each symptom to the stage to re-run and the forward chain after it. [R voice-driven 05-render]

| Symptom | Loop back to |
|---|---|
| Beat lands off-cue | Stage 04 (re-derive timing from the transcript) |
| Audio sounds wrong | Stage 03 (regenerate the voice-over) |
| Script reads wrong | Stage 02 (rewrite, then 03, then 04) |
| Claim is unsupported | Stage 01 (cite or remove) |

### 9.9 Prior-run data vs pattern learning [EXT, resolving R-QUAL-01 vs recurring-trend needs]

- **R-RUN-20** A stage MAY read a previous run's output **as data** (for example, last week's issue counts for a "what changed" section). The conditions:
  - it is declared in Inputs as `Prior run (data only)`, with the exact archived path and the section;
  - it is read-only;
  - it is never used to learn style or structure (R-QUAL-01 still applies).
- **R-RUN-21 (MUST)** Edges to earlier runs (run N-1 to run N) do not count against the one-way DAG rule, which governs folders within a run. Prior runs are read from `_archive/runs/<run-id>/`, never from a live stage's `output/`.

### 9.10 The edit-source principle (improving the system over time) [P §6.3]

- **R-EDIT-01 (INFO)** "Editing the output fixes this run. Editing the source fixes every future run." Editing output is "patching the binary"; it does not improve the compiler.
- **R-EDIT-02 (SHOULD)** One-off creative edits that cannot be reduced to a rule are legitimate output edits. "Sometimes the output needs a human touch that cannot be reduced to a source-level rule."
- **R-EDIT-03 (SHOULD)** Recurring edits are debugging information. Move a recurring correction into the source:
  - a contract amendment ("keep the opening under three sentences");
  - a stronger reference example (for example, when "the tone drifts formal every time");
  - a new constraint.

  The paper proposes that the *system* surface this when the same kind of edit happens in the same stage "three runs in a row". The threshold is a proposal; the principle is stated. [P §6.3]
- **R-EDIT-04 (SHOULD)** When output is wrong, check the three possible sources: (a) the reference material is underspecified; (b) the stage contract stresses the wrong quality; (c) the previous stage's output framed things wrongly. [P §6.3]
- **R-EDIT-05 (SHOULD)** "Every constraint you give is a mistake Claude will not make." Turn each recurring annoyance into a written constraint. [F 1.3]
- **R-EDIT-06 (INFO)** The trajectory: "If workspaces improve their own source files over time... they become systems that get better with use." [P §6.3]

### 9.11 Version control and portability

- **R-GIT-01 (INFO)** A workspace is a folder. Copy it, git it, zip it, sync it. No server, no deployment step. [P §3.4]
- **R-GIT-02 (SHOULD)** Template repos gitignore stage outputs (`**/stages/*/output/*` except `.gitkeep`). A live deployment MAY commit outputs after each run to build "a version history of the entire production pipeline's behavior over time". [R][P]
- **R-GIT-03 (INFO)** Handing off a workspace means copying the folder. The recipient edits prompts without a developer. [P]
- **R-GIT-04 (MAY)** Several agent sessions may work in one folder, coordinated by the shared CLAUDE.md. [PB 3.2]
- **R-GIT-05 (SHOULD)** Confirm the workspace is tracked or backed up before any reorganization. For a non-git store (a shared drive), copy the whole tree first. [A reference-integrity]; non-git rule [EXT]

---

## 10. Setup: Questionnaire, Placeholders, Conditionals

### 10.1 Fill-in syntax [R for `{{ }}`; EXT for the rest]

| Syntax | Meaning | Filled by / when | Allowed in | Check |
|---|---|---|---|---|
| `{{SCREAMING_SNAKE}}` | Setup placeholder | the `setup` trigger, once | brand and voice files, reference files, shared files, stage contract Inputs values, Human check lines | V3: none left after setup |
| `{{?NAME}}` ... `{{/NAME}}` | Conditional section | `setup`, removed when not needed | around whole sections only; may appear in root CONTEXT.md outside tables | V4 |
| `<kebab-name>` | Per-run variable | the agent, each run, from the meta file | Inputs and Outputs paths, filenames | V3b: every `<x>` is defined in the entry stage |
| `[Description]` | Author fill-in in this document's templates | the builder, while authoring | templates only | V3b: none left at ship |

- **R-PH-01 (MUST)** Setup placeholders are literal strings replaced by string substitution. Names are descriptive (`{{BRAND_NAME}}`, not `{{BN}}`). Related ones share a prefix (`{{PRIMARY_COLOR}}`, `{{SECONDARY_COLOR}}`). Each placeholder is spelled out in full; ranges such as `_1..3` are not allowed. [R][EXT]
- **R-PH-02 (MUST NOT)** Setup placeholders do not appear in any `CLAUDE.md`, in top-level CONTEXT.md routing tables, or in `questionnaire.md` itself ("the questions are the source, not the target"). [R]
- **R-PH-03 What becomes a placeholder (MUST).** "If it varies from one user to another, it is a placeholder. If it is part of the framework's structure, it is hardcoded." Always hardcoded: the file structure, process steps, section headings, the contract pattern, audit checks, checkpoint tables, recipes. [R script-to-animation-summary]
- **R-PH-04 (MUST NOT)** Per-run template files (for example `shared/course-meta.md`) do not contain placeholders: "this is per-course data, not system config." [R]
- **R-PH-05 (MUST)** A conditional block wraps an entire section: "a heading and all content below it, up to the next heading of the same or higher level." Never inline content or list items, because "removing inline content leaves orphaned list markers, broken sentences, or malformed markdown." There are two uses: removing a whole optional stage, and removing an optional section (`{{?PILLAR_4}}`). Name the block after what it wraps (`{{?BUILD_STAGE}}`). [R]
- **R-PH-06 (SHOULD)** Template-instantiation tokens (fields filled per record when a `_templates/` folder is copied) use `[Description]` or frontmatter fields, not `{{ }}`, so V3 does not flag them. [EXT]

### 10.2 Questionnaire design [R Pattern 8 + template rule 7][R WB 04]

- **R-Q-01 Flat structure (MUST).** No category groupings, just a numbered list.
- **R-Q-02 All at once (MUST).** Every question appears in one pass. "The user should be able to answer everything in a single message."
- **R-Q-03 System-level only (MUST).** Configure what stays the same across runs: identity, brand, design, tool preferences, default workflow, default entry stage. Per-run details (project name, topic, audience, scope) are "collected conversationally at the start of each pipeline run by the entry stage."
- **R-Q-04 Derive, do not ask (MUST).** "If a field can be inferred from another answer, the agent fills it in. List derived fields under the question they depend on. Do not add a separate question."
- **R-Q-05 Sensible defaults (MUST (validation)).** "Every question should have a default or example so the user can skip what they do not care about."
- **R-Q-06 Ask once, never again (MUST).** "After setup, the user should never see these questions again. The answers are baked into the workspace files permanently." [R]; "no run should ever re-ask them". [A]
- **R-Q-07 Examples over descriptions (MUST).** For voice and style, ask for concrete examples: "sentences that sound right, sentences that sound wrong, specific error patterns". "'Give me 2-3 sentences that sound like your brand' extracts pattern-matchable rules. 'Describe your voice' extracts an abstraction the agent must interpret." [R] [A]'s form of this asks for "two examples of past work that sound right, and one that sounds wrong".
- **R-Q-08 (MUST)** A non-technical person can understand every question. [R WB 04]
- **R-Q-09 (SHOULD)** Optional stages and tools are yes/no questions: "If NO: Remove `stages/0N-name/` entirely", or remove a `{{?SECTION}}` block. Ask whether optional tools are needed, so the conditional stages can be removed. [R]
- **R-Q-10 Coverage (MUST (validation)).** Every system-level placeholder has a question, and every question maps to at least one file containing its placeholder. No orphans in either direction.
- **R-Q-11 Two-pass review for derived voice rules (SHOULD).** "After the agent populates rules from answers, it presents them to the user for review before finalizing. This catches misinterpretations."
- **R-Q-12 (SHOULD) Question entry format.**

```markdown
### Q1: [Question text a non-technical person understands]
- Placeholder: `{{PLACEHOLDER_NAME}}`
- Files: `path/to/file1.md`, `path/to/file2.md`
- Type: free text | selection | yes/no | structured
- Default: [value]        (or Example: ... / Options: A, B, C)
- Derived: `{{OTHER_FIELD}}` (filled from this answer; optional)
- Note: [optional; follow-up for vague answers]
- If NO: Remove `stages/0N-name/` entirely   (yes/no questions only)
```

- **R-Q-13 (SHOULD)** [A]'s minimal five-question factory, whose answers are written into `_shared/` files:
  1. Who it is for, and what a finished deliverable looks like → `definition-of-done.md`.
  2. Two examples of past work that sound right and one that sounds wrong → `voice.md`.
  3. Hard constraints that never bend (length, format, brand rules, compliance) → `rules.md`.
  4. What the human always checks before anything ships → each stage's Human check line.
  5. What already exists that runs should reuse (templates, examples, data sources) → linked from `_shared/`, one home per fact.

### 10.3 The `setup` procedure [R CONV Triggers][R placeholder-syntax]

1. Read `setup/questionnaire.md`.
2. Ask ALL the questions conversationally, in a single pass.
3. Collect the answers.
4. For each question, replace every instance of its placeholders in the files it lists.
5. Fill the derived fields.
6. Apply the yes/no conditionals: remove stage folders or `{{?SECTION}}` blocks.
7. If voice rules were derived, show the Hard Constraints, Sentence Rules, and Pacing for edits (pass 2) before finalizing.
8. Check which tools the answers require, and point the user to the setup guides.
9. Scan the entire workspace for remaining `{{`. If any remain, flag them and ask for the missing information.
10. "Onboarding is complete only when zero placeholders remain."
11. Tell the user what was configured and where to start. Record it in `PROGRESS.md`.

Some setups feed discovery instead of filling placeholders. The workspace-builder's four questions (domain; workflow in one sentence; users and their AI skill level; rough stage count and skippable stages) inform its stage 01. [R]

---

## 11. Sessions, Memory, and Planning

### 11.1 The workspace is the memory [PB Stack 2.4, 1.3]

> "Claude is stateless. Your workspace is stateful. The workspace is the memory."

| Layer | What it holds | When to persist |
|---|---|---|
| Project definition ("what are we building") | the PRD or spec, CLAUDE.md, the folder structure | always |
| Progress markers ("where are we") | `PROGRESS.md` or `STATUS.md`: done, in progress, blocked | after meaningful milestones |
| Session notes ("why did we do that") | key decisions and their reasons | "log what you'd be frustrated to forget" |

- **R-SESS-01 (SHOULD)** Keep a `PROGRESS.md` at the project root with these sections: Current Status; Last Session (date: completed, in progress, blocked, next); Decisions Made (each with its reason); Open Questions. [PB Stack 2.4] The template is in §20.9.
- **R-SESS-02 (SHOULD)** Start a session with "Read PROGRESS.md. What's the status? What should we work on next?" End it with "Update PROGRESS.md with what we accomplished and what's next." "This takes 30 seconds and saves you 10 minutes of re-orienting next time." [PB Stack 2.4]
- **R-SESS-03 Reconnect = orient, verify, continue (SHOULD).** "Read CLAUDE.md and PROGRESS.md. Summarize where we are." Then: "Look at the actual code/files. Does the progress file match reality?" Then continue. After an unexpected end: "Don't assume the last task completed. Check." [PB Stack 2.4]
- **R-SESS-04 (SHOULD)** Update progress before walking away, after any significant decision, and before hitting token limits ("Before you lose coherence, have Claude summarize progress"). At a token limit: note where you stopped → start a new session → have it read the PRD → have it look at what has been built → continue. [PB Stack 2.4, 1.3]
- **R-SESS-05 (SHOULD)** Record decisions with their reasons. The reason "is what stops the argument happening twice". [X RyMac; consistent with PB]
- **R-SESS-06 (INFO)** Built-in agent memory and workspace files are different layers. "The folder structure and CLAUDE.md handle routing. The built-in memory handles continuity." "You do not need to build a separate memory system." Remote and live sessions are short-term memory; workspace files are long-term memory: "You need both." [PB 3.1][PB Stack 2.4]

### 11.2 Plan before you build [PB 3.3][PB Stack 1.1 to 1.3][F 4.3]

> "Spend your thinking before you spend your tokens." "15 minutes of thinking saves 90 minutes of building the wrong thing."

- **R-PLAN-01 Decide, then build (SHOULD).** "Desktop for decisions. Code for execution. If you try to decide and build at the same time, both suffer." [F 4.3]
- **R-PLAN-02 (SHOULD)** In planning chats, start with what you are trying to accomplish, not the thing to produce. Prompt for thinking ("What am I not seeing?"), and push back on the first answer. Do not use the chat "like a vending machine". [F 4.3]
- **R-PLAN-03 (SHOULD) The pre-build sequence** [PB 3.3]:
  1. Analyze what already exists, in chat. Skip this for builds from scratch.
  2. Have the chat write a markdown briefing "for Claude to read, not for me". It carries the context from the chat into the build tool.
  3. The first build prompt sets the boundaries:
     - the folder structure (including CLAUDE.md);
     - the deployment target;
     - the scope ("what you are not building yet");
     - the tech preference (or "let us decide together");
     - and the closing line "ask me three questions to understand more", "the most important line".
  4. Answer the questions. "If you do not have an answer, say so and let Claude make a reasonable choice."
  5. "Create a PRD file... Do not start building yet." Review and edit it. "This is your last free checkpoint."
- **R-PLAN-04 (SHOULD)** A project takes under 10 prompts: about 4 to 5 for planning and 2 to 3 for building. If you used more than 12, "review where you could have combined or front-loaded information." Every "I should have done this earlier" is a token cost; move those items into the first prompt or the PRD. [PB 3.3]
- **R-PLAN-05 (SHOULD)** The PRD is "stateful prompting": persistent context the agent re-reads. It covers:
  - what is being built;
  - the repos or sources being drawn from, and what to cut from them;
  - layout and design tokens;
  - phases and steps;
  - a delivery checklist.

  Another session MAY audit it ("What's overcomplicated?"). "When Claude drifts, I point back to the document." "Let it be smarter than your instructions when it makes sense." [PB Stack 1.1 to 1.3][PB 3.1]
- **R-PLAN-06 (SHOULD) The build process** [PB Stack 1.1]: define the need → research what exists ("Don't reinvent the wheel... Make the wheel yours") → map the existing structure → write the PRD → **build inside your workspace**, not in a separate folder, so the context is already there → work in sessions.
- **R-PLAN-07 (SHOULD)** Client work: plan steps 1 and 2 during the discovery call. [PB 3.3]
- **R-PLAN-08 (SHOULD)** Visual feedback: "take screenshots of what you do not like, describe what you want instead." When an error appears, share the screenshot "before spending tokens". [PB 3.3]

---

## 12. Prompting Inside the System [F 1.3, 4.1 to 4.3][PB]

### 12.1 The five-part prompt

"A prompt is an instruction set." It has five parts: **Identity, Task, Context, Constraints, Output Format**. "You will not use all five every time. But knowing them means you always know which one is missing when the output is not right."

| Part | What it carries | Rule |
|---|---|---|
| **Identity** | Who Claude is right now | "The part most people skip... The output is always more generic without it." CLAUDE.md supplies it at project level; add it in the prompt for one-offs or role changes. |
| **Task** | A clear action, a defined scope, enough detail | The stranger test: "If you read your task out loud and a stranger could not start working on it without asking you five follow-up questions, the task is too vague." |
| **Context** | Audience, prior decisions, data | "If the output feels generic or off-target, the fix is almost always more context, not a better prompt." |
| **Constraints** | What to avoid, limits | "Every constraint you give is a mistake Claude will not make. Think about the last three times an AI output annoyed you. Those annoyances are constraints you did not set." |
| **Output Format** | The shape of the answer | "The difference between getting something you can use immediately and getting something you have to reformat for 20 minutes." |

| Task type | Parts to use |
|---|---|
| Simple | Task only |
| Creative | Identity + Task + Constraints + Output Format |
| Complex | All five |
| Ongoing (inside a workspace) | Identity and Context live in the folder files; Task and Constraints go in each prompt |

"The folder is memory. The prompt is direction."

### 12.2 Prompting rules

- **R-PROMPT-01 One clear ask per prompt (SHOULD).** Break big projects into steps, with review between them. "If something goes wrong at step 3, you only redo step 3. This is the same principle behind the folder architecture." [F 1.3]
- **R-PROMPT-02 Feed large inputs in order (SHOULD).** Structure or table of contents first, then the sections in order with a confirmation after each, then the synthesis. [F 1.3]
- **R-PROMPT-03 Be specific and name the output location (MUST).** "'Edit the eyes' is vague. 'Slow down the blink speed on the hero character' is precise." [F 4.2][PB 1.3]
- **R-PROMPT-04 Correct in place (MUST).** Say what is wrong. Do not start over. [F 4.2]
- **R-PROMPT-05 (INFO)** Claude Code's loop is **Read → Think → Write → Check → Adjust**. It is best for tasks that read and write files. Process many files in one prompt instead of many copy-pastes: 15 meeting notes at about 2k tokens each is about 30k tokens, well inside the window. [F 4.2]
- **R-PROMPT-06 (SHOULD)** When teaching a repeated task by demonstration, narrate the intent, not only the clicks: "The narration matters because it tells Claude your intent, not just the coordinates of your clicks." Keep recordings short, split big tasks, and test right after saving. "The shortcut handles the navigation. Your follow-up prompt handles the thinking." [PB 2.3]
- **R-PROMPT-07 (SHOULD)** One model, three interfaces: Desktop or claude.ai (conversation; cannot see your files), VS Code + Claude Code (editor; "what I use for almost everything"), and the terminal (command line). "If you have ever felt like Claude kind of gets it but not quite, it is probably because you are working from a pasted excerpt instead of your actual project." "The folder becomes the app. Claude Code is the thing that runs it." [F 4.1]
- **R-PROMPT-08 (SHOULD)** Install tools and skills by pointing at their docs ("Help me install Remotion. Here is the documentation: ..."). [PB 1.1]

---

## 13. Skills, Scripts, Tools, Sub-agents, and Data Safety

### 13.1 Skills inside a workspace [R Pattern 9][F 3.1]

- **R-SKILL-01 (MUST)** Wire each skill into the rooms or stages that need it. Never load every skill everywhere. [F 3.1][R]
- **R-SKILL-02 (MAY)** Bundle skills into `skills/<name>/` (`SKILL.md`, optional `rules/`, `scripts/`) so the workspace is self-contained without global installs. [R]
- **R-SKILL-03 (SHOULD)** Discover skills during workspace design: scan `~/.claude/skills/` and `~/.agents/skills/`, search public repos for the domain, present the candidates, and let the user choose. [R]
- **R-SKILL-04 (SHOULD)** Bundle a skill by copying it (local) or cloning it (remote) into `skills/` during scaffolding. [R]
- **R-SKILL-05 (SHOULD)** Load skills as "Index, then load rules as needed". "Claude does not read all of them at once. It reads the parts relevant to the current task." [R][PB 1.1]
- **R-SKILL-06 (SHOULD)** When a skill covers the same ground as a custom reference doc, the skill replaces it. Delete the duplicate and point to the skill. [R]
- **R-SKILL-07 (SHOULD)** Keep workspace-specific files (design system, brand, build conventions) next to skills, not inside them. [R]
- **R-SKILL-08 (MUST NOT)** Do not bundle skills about the agent tool itself (skill-creator, mcp-builder). Bundle only runtime domain knowledge. [R]
- **R-SKILL-09 (SHOULD)** For workspace-specific knowledge, use reference files rather than skills; they are cheaper on tokens ("prefer CONTEXT.md files first to save tokens"). [O]
- **R-SKILL-10 (SHOULD)** A named folder with its own context is already "the agent" for that job. Many "I want an agent for X" requests are really "I want the AI to keep X in mind", which is a reference file. [V][X]
- **R-SKILL-11 (MAY)** A workspace may point to a sibling workspace's skill instead of bundling a second copy. [R]

### 13.2 Scripts for mechanical work

- **R-SCRIPT-01 (SHOULD)** "Local scripts handle the mechanical work that does not need AI at all": fetching data, moving files, formatting output, sending email, rendering, transcription, rebuilding indexes, counting. [P][M]
- **R-SCRIPT-02 (MUST)** Run a dry run before any expensive or external call (`--dry-run` before generating audio), and put a checkpoint on its result (R-CTR-19). [R]
- **R-SCRIPT-03 (MUST)** Generated files (indexes, tables, numbers) come only from scripts. "Anything hand-copied will eventually contradict the data." [M]
- **R-SCRIPT-04 (SHOULD)** Scripts live in `scripts/` or inside the skill that owns them, and each one is documented in the stage that calls it (input, output, how to run). [EXT]
- **R-SCRIPT-05 (SHOULD)** Script defaults state their reason: "We default to `medium.en` on CPU because `large-v3` on GPU has been observed to segfault." [R whisper-beat-finder]

### 13.3 Tools and MCP

- **R-TOOL-01 (SHOULD)** Scope tool definitions to individual stages or rooms. Loading every tool definition up front slows agents and raises cost. [P §2.2][F]
- **R-TOOL-02 (SHOULD)** External services come in through local scripts or MCP connections called from a stage. [P]

### 13.4 Sub-agents and models

- **R-SUB-01** One orchestrating agent runs the pipeline. It MAY hand sub-tasks within a stage to faster sub-agents. The folder structure drives the delegation: the orchestrator reads the stage's CONTEXT.md and L3 files to decide what to delegate and what context each sub-agent receives. "There is no separate orchestration framework." In the paper's setup, Opus orchestrated and Sonnet ran the sub-agents in Claude Code. [P §4.1, §4.2]
- **R-SUB-02 (SHOULD)** Sub-agents and plan mode are tool features. The architecture stays the folder. [PB Stack 1.3][I]
- **R-SUB-03 (INFO)** The method is model-agnostic: it specifies folder structure, file formats, and naming. In one test, a memory built by one vendor's model was read by another vendor's model at the same accuracy (n = 5, directional). [P][M]
- **R-SUB-04 (MAY)** Use a small or local model for bulk mechanical building (ingestion, filing) and a frontier model for judgment and reading. Build is about 95% of a memory's spend at break-even, and local models make possible "histories that cannot leave the premises". An exported folder runs on "any coding agent that can read files and navigate a folder structure". [M][PB Claude Design]

### 13.5 Data safety

- **R-SEC-01 (MUST)** Secrets live in `.env` only, never in committed files. Confirm `.env` is listed in `.gitignore`, and provide `env-template.md` with empty values. Per-run creative content never goes in `.env` (".env is for credentials only"). Generate a separate key for each project. [R]
- **R-SEC-02 (SHOULD)** Also gitignore `node_modules`, build output, and any private markdown (voice docs, client files). The test is "would I be comfortable if a stranger read this file?" [PB 3.2]
- **R-SEC-03 (SHOULD)** Mark data with access limits. Examples: an `access_tier` frontmatter field (abstracted patterns may leave the machine, raw private quotes may not); `[internal]` source tags; `governance: internal | sensitive | external` on context-map nodes. [A][R]
- **R-SEC-04 (MUST)** Keep each client's information in its own folder (R-T1-05). [F 3.2]
- **R-SEC-05 (SHOULD)** Review agent-filed files for personal data. In one case the memory agent "lifted a real person's phone number and email out of a cover letter... filed them tidily under a heading", and it was found only because someone opened the folder. "A structure whose contents you can see is a structure whose mistakes you can also see." [M]
- **R-SEC-06 (SHOULD)** When inputs contain personal data (support tickets, customer records), the intake stage strips or masks fields that downstream stages do not need. Inputs and outputs holding personal data are gitignored, and each later stage's audit includes a "no personal data" row. [EXT]

---

## 14. Writing Skills in Jake's Style

This section is derived from Jake's own skills: icm-architect, lecture-deck, whisper-beat-finder, elevenlabs-narration, and remotion-scene-anatomy. [A][R][I]

### 14.1 Skill anatomy

```
skill-name/
├── SKILL.md            the method on one to a few screens: what, when, procedure, rules, file index
├── references/         depth, one concern per file, read only when SKILL.md says so
├── rules/              (alternative to references/) one rule topic per file
├── assets/templates/   copyable starters the skill instantiates
└── scripts/            mechanical work (render, transcribe, check, build)
```

### 14.2 SKILL.md rules

- **R-SKW-01 Frontmatter (MUST).** `name` is kebab-case. `description` acts as a router: it says what the skill does, lists concrete trigger situations and literal trigger phrases ("make this an ICM", "ICM this", "structure this for agents"), and says what the skill is NOT for ("Not for pitch decks that must be PowerPoint"). [A][lecture-deck]
- **R-SKW-02 (SHOULD)** Open with the method in one paragraph, plus one governing metaphor if it helps (the library). [A][lecture-deck]
- **R-SKW-03 (SHOULD)** State the invariants, or "the rules that make it good", as a short list with bold titles. [A][lecture-deck]
- **R-SKW-04 (SHOULD)** Give a numbered procedure ("When you get a request: 1... 7..."), with modes when the skill has more than one job (Build or Restructure). Put checkpoints at the judgment calls ("For anything over ten screens, critique the storyboard before building"). [A][lecture-deck]
- **R-SKW-05 (MUST)** Include a validation step before delivery: a walk test, render-and-look, or a register check. "Repeat until clean." [A][lecture-deck]
- **R-SKW-06 (SHOULD)** Name the guardrails, and say honestly where the method loses. [A]
- **R-SKW-07 (SHOULD)** End with a file index that says when to read each reference ("Read when writing contracts or when a structural call is contested"). This is selective routing applied to the skill itself. [A]
- **R-SKW-08 (SHOULD)** Push depth down. SKILL.md stays one to a few screens. References hold the detail, templates hold the shapes, scripts hold the mechanics. [A][R]
- **R-SKW-09 (SHOULD)** A tool-wrapping skill follows this shape: `## When to Use` (which stage, what it outputs, who reads the output) → `## What You Need` → defaults with reasons → `## How It Works` (numbered) → `## Scripts` → `## Output Format` (the exact table the next stage reads). [R whisper-beat-finder]
- **R-SKW-10 (MAY)** A skill may carry setup placeholders that the workspace's `setup` fills (`{{WHISPER_MODEL}}`). [R]
- **R-SKW-11 (SHOULD)** Commands are listed literally, with their flags, in a `## Commands` block. [lecture-deck]

The template is in §20.12, the build procedure in §15.4, and the checks in §17.6.

---

## 15. Procedures

### 15.1 Build a Tier 1 rooms workspace (about 15 minutes) [F 3.2, 3.3]

1. Ask what kinds of work this person does in the project. Apply the mental-mode test (R-T1-03) to get 2 to 3 rooms.
2. Create the root folder, named after the work, and one folder per room. Add `_shared/` only if a reference is already used by two or more rooms.
3. Write each room's `CONTEXT.md` from §20.2, under a page, about 80% about the work. Point to reference files; do not paste long material in.
4. Write `CLAUDE.md` from §20.1: an identity line, the rooms, the routing table (Task | Go to | Read | Skills), the naming conventions, and at most about five workspace-wide rules.
5. Add subfolders only where a room already holds more than 8 to 10 files or has clear stages (drafts/final).
6. Add `PROGRESS.md` if the work spans sessions.
7. Validate with the Tier 1 checks (§17.3), then start working. Revisit after a few days. Update context files whenever the project changes.

### 15.2 Build a Tier 2 or Tier 3 workspace (Build mode) [A][R workspace-builder][P §4.4]

**Step 1. Extract the structure from dialogue.** "The structure is already in how the person describes the work — don't impose a shape, surface theirs." Ask a few at a time, not all at once: [A]

1. What is the repeating unit of work (an episode, a client, a report, a person, a team)?
2. Walk me through one run, start to finish. Where do you stop and check something before continuing?
3. What stays the same every run (voice, rules, brand, schema), and what is new every run?
4. What does "done" look like? What artifact leaves the workspace?
5. Who else touches this, and what do they need to find without asking you?

Map the answers:
- Pauses become stage boundaries.
- "I always check X before Y" becomes a human gate, with its reviewer.
- "It always has to sound like / follow Z" becomes factory reference material.

Capture the intake on the workflow intake template (§20.13: trigger, starting point, steps, end state, variations, worth-automating check). [PB 2.3]

For each stage, ask: what goes in, what comes out, and what does the agent need to know? Then identify:
- context shared across stages;
- user-specific values (these become placeholders);
- per-run values (these become `<variables>`);
- optional stages (these become conditionals);
- tools needing installation (these become setup guides);
- relevant skills (bundle them);
- sensitive data (§13.5).

Classify each stage (§8.2). Save the workflow map to `_meta/build/workflow-map.md` [EXT] and present it for confirmation (checkpoint). [R 01-discovery]

**Form-specific interview add-ons** [I from A forms]:

| Form | Also ask |
|---|---|
| Record library | What fields does every record have? What is the lifecycle (statuses)? What is the ID scheme? |
| Knowledge bundle | What must always load? What loads by task? What is evidence? What may never leave the machine? |
| Context map | What are the teams? Which processes have high value and high pain? Which data assets does each consume and produce? What may not be automated? |
| System map | Which nouns and movements actually exist? What do product names call them, compared with the code? What points into the tree from outside? |
| Umbrella | Which pipelines share which factory layers? |

**Step 2. Pick the form** (§16). Tie-break when several fit: choose by what the *reader* most often looks up. Use the author's production unit as an internal pipeline (§16.8). [EXT]

**Step 3. Map contracts and dependencies** [R 02-mapping]:
1. Write each stage's Inputs, Process, and Outputs.
2. Map the cross-references, and choose the canonical source for each fact.
3. Draw the dependency graph and confirm it is a DAG.
4. Confirm every output is consumed downstream or is the final deliverable.
5. Present the diagram and the contracts (checkpoint). Save them to `_meta/build/`.

**Step 4. Scaffold the smallest structure that carries the work** [A][R 03-scaffolding]. Create:
- root `CLAUDE.md` and root `CONTEXT.md`;
- `setup/questionnaire.md`, if the factory needs configuring;
- the factory folder: `_shared/`, or a brand or design folder with its own CONTEXT.md if it is large;
- `stages/NN_name/{CONTEXT.md, references/, output/}`, plus `input/` for the entry stage;
- `scripts/` and `skills/`, if needed;
- `_templates/`, if units are created by copying;
- `.gitkeep` in every empty folder;
- `.gitignore`.

Then:
- Add a value framework if the deliverable must persuade or teach, and a constants file for code workspaces.
- Structure voice rules as Hard Constraints, Sentence Rules, and Pacing, never as a single description placeholder.
- Delete any Checkpoints or Audit sections that do not apply to their stage class.
- Do not create folders for stages that do not exist yet.
- If the job fits in one saved prompt, stop and say so.

**Step 5. Design the questionnaire** (§10.2). Scan for every `{{`. Split system-level values from per-run values. Then check coverage both ways.

**Step 6. Validate** with the matrix in §17.3. Fix the structure, then re-run the failed checks.

**Step 7. Run it once end to end (MUST).** [R] If real data is not available, a synthetic run is acceptable. Record it in PROGRESS.md, and run it in a copy (the instance) so the template stays clean. [EXT]

**Step 8.** Write `PROGRESS.md`. Tell the user how to start a run and how to run `setup`.

### 15.3 Restructure an existing folder (Restructure mode) [A]

1. **Inventory before touching.** List the tree. For each area, note what it is, when it was last touched, and what refers to it. Never delete or move anything in this pass. [A]
2. **Find the hidden form.** Ask the owner, or infer and confirm: what is the repeating unit here? Where does work enter and leave? "The mess usually contains a real pipeline, library, or map that grew without a skeleton — extract it, don't replace it. Interview the folder the way you'd interview the person." [A]
3. **Classify every file** into one role [A]:
   - **Catalog**: identity or routing. It becomes or feeds `CLAUDE.md` and the index files.
   - **Contract**: describes how a step works. It becomes a `CONTEXT.md`.
   - **Factory**: stable reference. It goes to `_shared/`, `_system/`, or `references/`.
   - **Product**: run-specific artifacts. They go to a stage `output/` or a record folder.
   - **Dead**: stale, duplicated, or superseded. Propose `_archive/`; never delete silently. A file is Dead only after step 4 shows nothing depends on it. "Apparent disuse is not proof."
4. **Check reference integrity before proposing anything** [A]. List what points at each file you plan to move:
   - references inside the workspace;
   - sibling-path `../` references, which break when folders are regrouped;
   - symlinks;
   - external consumers: other repos, deploy scripts, cron jobs, issue trackers, agent configs.

   External consumers are a question for the human, not an endless grep. A file with a live referrer is held, or moved only if every referrer is updated in the same change.
5. **Propose before moving.** Show the target tree and a migration map (§20.14: `old path → new path → role → referrers found`), and get approval. "This is a human gate in a method built on human gates — honor it." The reviewer approves against the reference report, not a hunch. [A]
6. **Migrate: copy, verify, then remove** [A]:
   - Confirm the root is tracked or backed up (R-GIT-05).
   - Before any copy or rename, check whether the destination already exists **case-folded**. On Windows and macOS, `CLAUDE.md` → `CONTEXT.md` can silently overwrite an existing `context.md`. Raise any collision at the approval gate.
   - Copy, verify parity (file count and content hash; for zipped office formats compare the unzipped content), and only then remove the original. Leave a pointer if anything referred to it.
   - Write the entry file and contracts. De-duplicate toward one home per fact.
   - Keep the method (the blank template) apart from this instance.
7. **Conversion sub-step, for non-markdown sources such as .docx or .pdf** [EXT]:
   - Convert to markdown with frontmatter `converted_from: <original path>`.
   - Verify *text* parity (the headings and numbered steps are all present). Byte hashes cannot match across formats.
   - Keep the originals in `source/` until the owner signs off, then archive them.
   - Flag scanned or image-only files for human transcription; do not guess their content.
8. **Finish like a build.** Where a factory exists, run §15.2 steps 5 to 7: the questionnaire, the validation matrix, and one end-to-end run.
9. **Validate with the walk test** (§17.1), including W6: does every reference that existed before the move still resolve?

### 15.4 Build a skill [I from §14 and Jake's skills; EXT procedure]

1. Run decision D2 (§1.2). The task repeats and fits one prompt plus references and scripts, with no human review between steps. If it needs reviewed stages, build a workspace instead.
2. Write the trigger list (phrases a user would actually say), the not-for list, and the modes.
3. Draft SKILL.md from §20.12. Keep the procedure numbered and the rules short. Push depth into `references/`, shapes into `assets/templates/`, and mechanics into `scripts/`.
4. Write the file index, saying when each reference is read.
5. Add the validation step the skill runs before delivering.
6. Test on a small fixture. If it produces an artifact (for example, a workspace), run that artifact's own validation.
7. Run the skill checks in §17.6.

### 15.5 Run setup for an existing workspace

Follow §10.3.

---

## 16. The Six Forms [A forms]

Choose by asking: **what is the repeating unit of work?**

| The unit is... | Form | Optimizes for |
|---|---|---|
| a run (same stages, new deliverable each time) | **Pipeline** (= Tier 2) | Repeatable production with review gates |
| several kinds of runs sharing one identity | **Umbrella** | Shared brand and voice across distinct pipelines |
| a record that accumulates (person, client, session, SOP) | **Record library** | Uniform shape and fast retrieval |
| the knowledge itself (claims, notes, evidence) | **Knowledge bundle** | Navigable knowledge with layered loading |
| an organization (teams, processes, data, handoffs) | **Context map** | The org as a graph; automation candidates |
| a folder later agents must edit (code, markdown, mixed) | **System map** | Change impact without reading the whole tree |

Every form obeys the invariants. "Each level has its own small catalog, and no level's catalog describes the internals of the level below — it links down and stops." [A]

### 16.1 Pipeline: the production line

The skeleton is in §6.1. Defining moves:
- The handoff is `output/` → the next stage's input. A human edits in between; the next stage reads whatever is there.
- Each contract carries "load this / do NOT load that".
- `status` scans `stages/*/output/`.
- Boundaries sit where the human pauses. "Surfacing the judgment call... as an editable file before the expensive downstream work is the whole trick."
- Expect the U-curve.

Watch for: stages that do two jobs; contracts that restate reference material; pipelines built before the process has repeated.

### 16.2 Umbrella: a portfolio of pipelines

```
workspace/
├─ CLAUDE.md               the map: what lives where, which pipeline for which job
├─ 01-pillars/             shared factory: positioning, pillars
├─ 02-brand-voice/         shared factory: voice, style
├─ 03-video-production/    a full Pipeline workspace (own CLAUDE.md)
├─ 04-scene-generation/    a full Pipeline workspace (own CLAUDE.md)
└─ 05-animation-studio/    a full Pipeline workspace (own CLAUDE.md)
```

- Each sub-pipeline is self-contained with its own entry file, and "they don't share state" except through the root reference layers.
- The root routes by task ("making a talking-head video → 03; animating a diagram → 05") and holds nothing else.
- A pipeline MAY host sibling patterns: two variants of the same line, such as record-then-cut vs animation-first.
- Each sub-workspace's CLAUDE.md SHOULD say when to use it rather than a sibling (§7.1). [R]
- In this form, numbered top-level folders are allowed for factory layers. [A]

Watch for: a stale root map (it should state only what rarely changes); shared reference duplicated into sub-pipelines (link up instead).

### 16.3 Record library: the unit is a record

```
workspace/
├─ CLAUDE.md               one line: "Read 00_START-HERE.md first." [EXT: Claude Code auto-loads only CLAUDE.md]
├─ 00_START-HERE.md        the map (identity + routing in one file)
├─ _index/                 catalog: log.md, one line per record, id + status
├─ _templates/
│  └─ record-template/     every record starts as a copy of this
├─ 01_reference/           factory: the method, rules, shared knowledge
└─ records/
   ├─ acme-corp/           each record has the same internal shape
   └─ jane-doe/
```

- A new record is a copy, not a blank page: "the template is the schema".
- The index log is the declared source of truth for what exists: one line per record, with a small lifecycle such as `briefed → active → archived`.
- The naming convention doubles as an ID scheme (`ht10-second-brain`).
- Records may recurse: a record can hold its own mini pipeline or knowledge bundle.
- Records inherit their purpose from the template, so they need no per-record CONTEXT.md. [EXT, per §2.1]
- `00_START-HERE.md` and `01_reference/` are Jake's names here. Numbering marks reading order, not pipeline order. [A]

Watch for: records drifting from the template shape (re-stamp them); the index log absorbing content; half-created records (finish the stamp or archive them).

### 16.4 Knowledge bundle: the product is the knowledge

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

- Every note carries typed YAML frontmatter (`type:`, `layer:`, `access_tier:`, `strength:`).
- Notes cross-link by relative path or wikilink. Navigation is link-following, not folder-crawling. "A link that doesn't resolve yet marks something worth writing, not an error."
- The reading protocol: always-load layer first, task-relevant nodes second, evidence only when needed. Never read the whole bundle.
- `access_tier` gates what may leave the machine.
- Regenerating the bundle is a factory run, and every change appends to a log.

Watch for: reading the bundle as a search index instead of a model (it answers "how does this think", not "find me the file"); frontmatter fields nobody queries (cut them); extraction runs that edit the product by hand (fix the factory instead).

### 16.5 Context map: the organization as a graph

```
workspace/
├─ CLAUDE.md / AGENTS.md   entry (one generated from the other)
├─ FILE-MAP.md             GENERATED index; agents jump here, never crawl
├─ _meta/                  the rules: schema.md, maturity-levels.md, ritual docs
├─ teams/
│  └─ marketing/
│     ├─ Marketing.md      node card: In / Movement / Out / Edges
│     ├─ governance.md     what may not be automated, and why
│     ├─ jobs/             outcome nodes
│     ├─ processes/        workflow nodes (the workhorses)
│     └─ data/             data-<thing>.md asset nodes: source of truth, shape, sensitivity
├─ patterns/               cross-team patterns, written bottom-up only
└─ dashboards/             00-tracker.md ... live queries over frontmatter
```

- A closed set of node types (team, job, process, data-asset, governance, pattern) is defined once in `_meta/schema.md`. Every node declares its `type:`.
- Process nodes carry scoring frontmatter (template §20.10): owner; `ai-level` (L0 manual · L1 copy-paste · L2 structured · L3 integrated); frequency; value 1 to 5; pain 1 to 5; `consumes:` and `produces:` as wikilinks to data assets. The links draw the org graph on their own. value + pain ≥ 8 flags a pilot candidate.
- "The workshop is the data event." Map live with the team, and end every session in node files, not slides. "You don't point an agent at a legacy mess — you clean the shelf first."
- The librarian ritual per team: inventory → single source of truth → give it shape → catalogue → shelve by sensitivity → connect the agent. The human stays the approval gate; the agent drafts and proposes.
- A pattern needs three independent occurrences: "one team complaining is a gripe".
- When practice and the schema disagree, "reconcile the same day".

Watch for: a schema that mandates names the files stopped using; duplicate entry files; instance data tangled into the method (extract the blank starter kit early); node types multiplying past what anyone queries.

### 16.6 System map: a body of work as an edit graph [A system-map]

Use it when someone will change a tree they do not hold in their head ("map this repo", "what would a change hit"). Do not use it for a production line, an org chart, or a model of how someone thinks. "If the tree is small enough that one `CONTEXT.md` plus an index answers 'what is X' and 'what else moves,' stop there."

```
map/                         next to existing orientation (docs/, developer-docs/, vault root), never inside src/
├─ CLAUDE.md                 L0 catalog; AGENTS.md + routing.md generated as byte-identical twins
├─ CONTEXT.md                how to walk; the universes; name collisions ("Chat = `Incubator`")
├─ _meta/schema.md           closed node types
├─ _templates/               object.md, process.md
├─ objects/
│  ├─ CONTEXT.md
│  ├─ _index.md              one line per noun (stub | verified | stale)
│  └─ <cluster>/             cards, clustered by how an editor asks, not by folder layout
├─ processes/                only after nouns exist; only real movements
└─ effects/CONTEXT.md        "if you are changing X, open these cards"
```

- **Universes.** *live* (in force; cite and implement against these), *leftover* (still present, no longer the main path), *ghost* (named or filed but not wired: stubs, dead types, docs of functions that do not exist; never implement against these).
- **The subject tree stays the source of truth.** Cards cite `path:line` for code, or the owning file for markdown. "If a comment and the code disagree, the code wins and the card says so." The map "never becomes a second spec".
- **Gated slices.** Stop after each slice for a human or a cold walk:
  - 0 Inventory: classify, infer nouns and verbs, mark universes, propose a tree, get approval. No cards yet.
  - 1 Catalog: write the entry files, schema, templates, and `_index.md` with stub lines. Wire one routing row from the subject's entry file.
  - 2 Nouns: one card per type.
  - 3 Verbs: only movements that actually run. "Do not invent a sixth."
  - 4 Change-impact index: then walk it backwards and ask the owner what points INTO the tree from outside.
  - 5 Re-verify the load-bearing claims: "Wrong waterfalls are more expensive than missing cards."
- **Status.** `verified` requires a date, a commit or revision, and citations. `stale` is allowed. "A confident wrong date is not."
- **The seven object-card sections.**
  1. One sentence (the product name and the code name, if they differ).
  2. Why this shape.
  3. Shape (keys, constraints, or owning files, with citations).
  4. Connected to (owns / owned-by / joins / looks-like-but-is-not).
  5. If you change this (**Hits / Does not hit**, first-order only; "does not hit" names the obvious next noun that is the wrong one).
  6. Surfaces (who reads or writes).
  7. See (the source file, plus at most one as-built page).
- **Process cards.** Input → Movement → Output; numbered steps with citations; `consumes` / `produces` links; Hits / Does not hit.
- **Walk test for this form.**
  1. Is the map one hop from the subject's entry file?
  2. Can `map/CLAUDE.md` explain the colliding names without opening a card?
  3. Does one card cite its source, state the why, and give a first-order waterfall?
  4. Can `effects/CONTEXT.md` name what a given change hits and what it does not?
  5. Does a `See` link land on source, not on another essay?
  6. Do entry + hub + one card fit in 2k to 8k tokens?

Watch for: mapping aspirations as live (ghost them); copying as-built behavior into cards (point at the owning file); empty `processes/` or `effects/` folders; two hand-edited entry files; `verified` with no citations; slurping all of `objects/` in a later session; an `effects/` index that only walks outward.

### 16.7 Memory variant: ICM as long-term agent memory [M]

A knowledge bundle or record library that the agent builds one conversation at a time.

**Builder invariants**:
- one folder, one job, each with its own CONTEXT.md;
- a root CLAUDE.md under 60 lines that only routes;
- the catalog holds no books;
- one home per fact;
- generated indexes rebuilt by command;
- markdown + YAML frontmatter + wikilinks;
- answering means reading the entry file, one index, and one or two leaves.

**Builder rules**:
- Reorganize as the picture develops: "a shape that suited ten conversations may not suit fifty".
- Do not copy sources verbatim; record what matters.
- When you add a leaf, update the indexes above it (the folder CONTEXT.md and CLAUDE.md).
- When the right place already exists, filing is "a matter of finding it instead of designing it".
- Reading cost grows "with the size of the catalog, not with the size of everything stored underneath it". Note that "filing into an existing structure is not cheaper than building one".
- Index conventions in the study: `_index/timeline.md` (`| Date | Session | Topic |`), generated with a do-not-edit header; session files named `YYYY-MM-DD_HHMM_<id>.md` with `session_id`, `date`, `turns` frontmatter.
- Review filed leaves for personal data (R-SEC-05).

**Reader rules**:
- Read the entry file first and follow it. Open only what you need. Grep "when catalog topics are too coarse".
- Ground every claim in something you actually read.
- Use frontmatter dates for timing. The most recent fact wins a conflict.
- If the archive does not contain the answer, say so plainly. Do not accept a false premise.
- Before saying "not found", make an explicit search-exhaustiveness pass, because "a reader that has seen only what it opened cannot distinguish absent information from unfound information."
- Answer "directly and specifically — a short factual answer, not a summary of your search."

A relational or columnar store MAY sit underneath for data it is genuinely good at, with the files above it holding what a person needs to read.

### 16.8 Form chooser for common corpora [EXT, applying §16 and §15.2 step 2]

| Corpus | Reader mostly looks up | Suggested form | Notes |
|---|---|---|---|
| SOPs / runbooks | one procedure at a time | Record library (one SOP per record, from an SOP template) | Add a Pipeline for "write or revise an SOP" if that recurs. SOP authoring rule: "Anything you have explained out loud more than twice" becomes an SOP; "If a step can fail, put the check for it right under that step." [X RyMac] |
| Policies / FAQs | answers to questions | Knowledge bundle | Layer A: always-load principles; B: by topic; C: source documents (evidence). |
| Ticket or case histories | patterns over time, single cases | Record library (cases) + Pipeline (periodic digest) | Prior runs are data (§9.9). |
| A team's processes and handoffs | who does what, with which data | Context map | |
| A codebase or docs vault to be changed | what X is, what a change hits | System map | |
| Client engagements | one client at a time | Record library, or Tier 1 rooms per client | Strict isolation (R-SEC-04). |

### 16.9 Composing forms

The forms nest:
- a record library whose records are knowledge bundles;
- a pipeline that emits into a record library;
- an umbrella over pipelines that share one knowledge bundle as their factory;
- a context map whose team folders each grow a small pilot pipeline;
- a repo that hosts a system map beside a setup pipeline.

One rule stays absolute: each level's catalog links down and stops.

---

## 17. Validation

### 17.1 The walk test [A]

Walk the workspace cold, as an agent with no memory.

| # | Check | Pass condition |
|---|---|---|
| W1 | Open the root. Can you answer "where am I" and "where do I go for the current task"? | Within the entry file plus at most two more reads |
| W2 | Pick any stage or node. Does its contract name exact input paths, the job, the output, and the human check? | All four present |
| W3 | Can you state pipeline status purely by scanning `output/` folders (or node frontmatter)? | Yes |
| W3b | Can you tell, from files alone, which gate was last passed (APPROVED vs DRAFT)? [EXT] | Yes |
| W4 | Is any routing file carrying content payload? | No (move it to a shelf, leave a pointer) |
| W5 | Is any fact stored authoritatively in two places? (The §8.4 sanctioned summaries are exempt.) | No |
| W6 | After a restructure, does every reference that existed before still resolve? | Yes |
| W7 | Token check: entry file + one contract + its inputs | About 2k to 8k tokens (under is fine) |
| W8 | System map only: can a cold agent answer "what is X" and "what else moves if I change X" from `map/CLAUDE.md` plus one card? | Yes |
| W9 | Is every folder reachable from the entry file's routing (no unrouted folders, no dead routes)? [X 4R] | Yes |

"If a step fails, fix the structure — not by explaining more, but by moving or splitting files until the walk works." [A]

### 17.2 Structural checks [R 05-validation, generalized]

| # | Check | Pass condition |
|---|---|---|
| V1 | Cross-reference integrity | Every path in every Inputs table resolves (resolving `<variables>` against the current run, using R-CTR-01 path bases) |
| V2 | No circular dependencies | The within-run reference graph is a DAG |
| V3 | Placeholder coverage | Every `{{X}}` has a question; every question maps to a file containing its placeholder; after setup, none remain |
| V3b | Fill-in hygiene [EXT] | No `[Description]` author fill-ins remain; every `<variable>` is defined in the entry stage's meta |
| V4 | Conditional validity | Every `{{?X}}...{{/X}}` wraps a complete section |
| V5 | Handoff chain | Stage N's output location equals stage N+1's input reference |
| V6 | CONTEXT.md purity | Only the allowed elements (R-CTR-30) |
| V7 | Checkpoints | Creative stages have at least one; analytic stages SHOULD; step numbers are valid |
| V8 | Audits | Creative, analytic, and build stages have unambiguous checks that run before output is written |
| V9 | Contract purity in spec stages | The spec has no implementation choices owned downstream (in animation: no component names, frame numbers, props, or spring configs) and is not under-specified |
| V10 | Line counts | Within §3 (CONTEXT.md under 80 lines; reference files under 200; CLAUDE.md about 60) |
| V11 | Naming | One stage-prefix style (`NN_` or `NN-`), zero-padded; kebab-case apart from the R-NAME-02 exceptions; `.gitkeep` in empty folders |
| V12 | Tool prerequisites | Every system-level tool has a setup guide with install and verify steps; the questionnaire asks about optional tools |
| V13 | Quality scan | No unexplained jargon; clean markdown; no em dashes if the house style bans them |
| V14 | Safety [EXT] | `.env` is gitignored; no keys in files; personal-data inputs and outputs are gitignored; client isolation holds |
| V15 | Gates [EXT] | Every contract declares a gate type and a reviewer; a blocking gate follows every creative or analytic stage |

### 17.3 Which checks apply (by tier and form) [EXT]

| Check | Tier 1 Rooms | Pipeline | Umbrella | Record lib. | Knowledge b. | Context map | System map |
|---|---|---|---|---|---|---|---|
| W1, W4, W5, W7, W9 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| W2 | room form (§7.4) | ✓ | per sub-pipeline | template | extraction pipeline | node cards | cards |
| W3, W3b | — | ✓ | per sub-pipeline | index log | corpus manifest | frontmatter | `_index.md` statuses |
| W6 | after restructure | after restructure | ✓ | ✓ | ✓ | ✓ | ✓ |
| W8 | — | — | — | — | — | — | ✓ |
| V1, V2, V5 | V1 only | ✓ | ✓ | V1 | ✓ | V1 | V1 |
| V3, V3b, V4 | — | if setup exists | if setup exists | V3b | if setup exists | V3b | V3b |
| V6 to V9 | — | ✓ | ✓ | — | extraction | — | — |
| V10, V11, V13, V14 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V12, V15 | — | ✓ | ✓ | if stages | extraction | — | slices |

**Tier 1 checklist**:
- [ ] One routing row per room.
- [ ] Each room's CONTEXT.md has its purpose, process, files, skills, "What good looks like", "What to avoid", and a "Last updated" line.
- [ ] No room CONTEXT.md is longer than a page.
- [ ] CLAUDE.md is about one screen, with no payload.
- [ ] No more than 8 to 10 files sit loose at any level.
- [ ] Client folders are isolated.

### 17.4 Ongoing health checks

- **Cold-chat test.** Open a brand-new session and ask a status question. If it takes more than about two moves to find the answer, "that is a hole in your files". [X RyMac, consistent with W1]
- **Stale-context check.** If output quality "got worse", read the context files before blaming the model. [F 3.3]
- **CLAUDE.md test.** Move CLAUDE.md out, run the same task, and compare. [F 4.4]
- **Guard test.** Plant a known error and confirm the audit catches it (R-AUD-06). [X 4R]
- **Rule-only-in-a-sentence check.** "A rule held only by a sentence is a finding, even when everyone obeys the rule." Back each MUST with a structure, a script, or an audit row. [X 4R, crediting Jake's audit]
- **Audit discipline.** When auditing someone's workspace, never change the target during the audit, cite `file:line` for each finding, and propose the smallest safe fix, then wait for approval. [X]

### 17.5 Ship checklist (workspace) [R README]

- [ ] Built through the builder procedure, not assembled ad hoc
- [ ] `setup` runs cleanly and every placeholder resolves
- [ ] At least one end-to-end run completed (synthetic is allowed, in an instance copy)
- [ ] No stage outputs committed (template repos)
- [ ] All CONTEXT.md under 80 lines; all reference files under 200
- [ ] Creative stages have at least one checkpoint and an audit
- [ ] No circular dependencies
- [ ] The walk test passes (§17.1)

### 17.6 Skill checks [EXT, from R-SKW rules]

- [ ] Frontmatter has `name` and a `description` with trigger situations, literal trigger phrases, and a NOT-for line
- [ ] Method paragraph, rules list, and numbered procedure (with modes if the skill has more than one)
- [ ] A validation step runs before delivery
- [ ] Guardrails and "where it loses" are stated
- [ ] The file index resolves, and every reference says when to read it
- [ ] SKILL.md is one to a few screens; depth lives in references and templates
- [ ] A dry run on a fixture succeeded, and its artifacts passed their own validation

### 17.7 Style guardrails [R]

- Plain English, no jargon: "If a term needs explaining, it is too specialized."
- Every markdown file should be readable by someone who knows markdown and git basics but has no deep engineering background.
- No em dashes in workspace files is the repo's house style (use `--`). icm-architect itself uses em dashes, so this is a choice. It is an error in Jake's own script voice.

---

## 18. Anti-patterns and Failure Modes

| # | Anti-pattern | Why it fails | Fix | Source |
|---|---|---|---|---|
| AP-01 | Multi-agent framework for a sequential, reviewed workflow | Overhead the problem does not need; opacity; developer dependency | One agent + folders | [P] |
| AP-02 | Context-stuffing ("photocopying the library into a backpack") | 30k to 50k token prompts; diluted attention | Layered loading; Inputs; Do NOT load | [P][A] |
| AP-03 | CLAUDE.md as a brain dump, project brief, or style guide | Paid on every prompt; "context files hiding inside it" | Move content into room or reference files | [F 3.3][A] |
| AP-04 | No routing table, or routing that works "sometimes" | Inconsistent loading and output | One row per kind of work | [F 3.3] |
| AP-05 | Too many rooms | Upkeep outgrows the work | 2 to 3 rooms; mental-mode test | [F 3.3] |
| AP-06 | Context about the AI instead of the work | The model responds to the work, not to personality | 80% work, 20% behavior | [F 3.3] |
| AP-07 | Never updating context | Claude seems to "get worse" | Update as you go; "Last updated" line | [F 3.3] |
| AP-08 | Everything in one flat folder | Wrong file picks | Subfolders past 8 to 10 files | [F 3.3] |
| AP-09 | Building the whole system before using it | "Built the factory without ever making a product" | 15-minute first version; grow from use | [F 3.3] |
| AP-10 | Routing files that carry payload; CONTEXT.md over 80 lines, with code or "why it works" sections | Bloat, staleness, duplication | Move payload to a shelf, leave a pointer | [A][R][O] |
| AP-11 | The same rule in two authoritative places | They drift | One home per fact; pointers elsewhere | [R][A] |
| AP-12 | `CLAUDE.md` and `AGENTS.md` both hand-edited | Drift | Generate one from the other, or a one-line pointer | [A] |
| AP-13 | Hand-edited generated indexes | They drift from the files | Rebuild by script | [A][M] |
| AP-14 | A schema naming things the files stopped using | Rot | Reconcile the same day | [A] |
| AP-15 | Circular references between folders | N-squared growth | One-way references; a third shared location | [R][O] |
| AP-16 | Stages that do two jobs | Muddy handoffs, weaker output | Split | [A] |
| AP-17 | Contracts restating reference material | Duplication, drift | Point instead | [A] |
| AP-18 | Vague process steps ("write the script") | Output you cannot reproduce | Concrete, one-action steps | [R] |
| AP-19 | Vague human check ("review") | Nobody knows what to verify | One concrete act, with a named reviewer | [A] |
| AP-20 | Over-specified specs (frame numbers, props, code) | Stiff, uncreative builds | Specs give WHAT and WHEN | [R][PB] |
| AP-21 | Under-specified specs ("show a diagram") | Each builder invents something different | Detailed enough that two builders produce similar results | [R] |
| AP-22 | Agents learning from old outputs | They copy the earliest, worst work | Docs over outputs; curated exemplars only | [R] |
| AP-23 | Examples beside a rule that contradict it | Models copy examples before following rules | Make the examples obey the rule | [X] |
| AP-24 | Setup questions asked every run; per-run details in setup | Friction; wrong layer | Setup once; the entry stage collects per-run details | [R] |
| AP-25 | Asking for voice descriptions instead of examples | Weak, interpreted constraints | Ask for right and wrong examples | [R] |
| AP-26 | Inline conditional placeholders | Broken markdown after removal | Wrap whole sections only | [R] |
| AP-27 | Speculative stages, "misc" buckets, a workspace for a task done twice | Scaffolding, not architecture | The smallest structure that carries the work | [A] |
| AP-28 | Automated mid-pipeline branching | Turns ICM back into a framework | A human decides between stages | [P] |
| AP-29 | Moving files without checking referrers; silent deletes | Broken references | Reference-integrity gate; `_archive/` | [A] |
| AP-30 | Workshops ending in slides | Nothing the structure can shelve | Every session ends in files | [A] |
| AP-31 | Patterns declared top-down | False structure | Three independent occurrences | [A] |
| AP-32 | Only ever fixing outputs | The same correction every run | Edit-source principle | [P] |
| AP-33 | Working around an upstream flaw downstream | Hidden drift between stages | Fix upstream, re-run forward | [R] |
| AP-34 | Starting over when output is wrong | Throws away the context | Correct in place | [F 4.2] |
| AP-35 | Deciding and building at the same time | Both suffer | Plan in chat, build in Code | [F 4.3] |
| AP-36 | Losing progress between sessions | Re-explaining, missed details | PRD + PROGRESS.md; verify on reconnect | [PB] |
| AP-37 | Secrets, personal data, or private files committed | Leaks | `.env`, `.gitignore`, intake masking, the stranger test | [R][PB][M] |
| AP-38 | One client's information inside another client's room | Leakage, confusion | One isolated folder per client | [F 3.2] |
| AP-39 | Building a new tool in a folder apart from its context | The context is not there | Build inside the workspace | [PB Stack] |
| AP-40 | Guessed values (timings, counts, numbers) | Silent errors | Derive by script and audit "no values guessed" | [R][M] |
| AP-41 | Uncertainty buried in prose | Downstream asserts what is not known | An Open Questions section in every handoff | [R] |
| AP-42 | Paid or irreversible calls with no dry run or precondition check | Wasted credits; leaked keys | Precondition check → dry run → checkpoint | [R] |

---

## 19. Quick-Reference Card (for an agent mid-task)

1. **Classify the request** (§1.1): build, restructure, skill, run, or setup.
2. **Does it need a workspace?** One-off → chat. Fits one prompt → a skill. Not yet repeating → wait. Repeating with several parts → a workspace.
3. **Which tier or form?** Ongoing kinds of work → Rooms. A reviewed sequence that repeats → Pipeline. A record, knowledge, an organization, or a codebase → the matching form.
4. **Root CLAUDE.md**: about 30 to 60 lines, routes only. The routing table is Task | Go to | Read | Skills.
5. **Rooms**: start with 2 to 3, split by mental mode. CONTEXT.md under a page, 80% about the work, kept up to date.
6. **Stages**: cut where the human pauses. Surface judgment calls as editable files before the expensive work. Classify each stage as creative, analytic, build, or linear.
7. **Each stage**: `CONTEXT.md` containing:
   - Inputs, with exact paths and sections
   - Do NOT load
   - Process, as numbered concrete steps
   - Checkpoints, if creative or analytic
   - Audit
   - Outputs, each with a header
   - Human check: one act, the reviewer, and the gate type

   Plus `references/` and `output/`, and `input/` for the entry stage.
8. **Factory** (`_shared/`, `references/`, `skills/`) sits apart from **product** (`input/`, `output/`).
9. **Budget**: 2k to 8k tokens per stage. Over budget → split the stage, tighten the inputs, or push detail down into references.
10. **One home per fact.** References point one way. Indexes and numbers are generated by script.
11. **Limits** live in §3.
12. **Setup**: flat list, all questions at once, system-level only, defaults, examples rather than descriptions, no `{{` left afterwards.
13. **Run**: archive the old run, drop inputs, restate the task, collect the metadata, run stage by stage, PENDING → DRAFT → APPROVED, and nothing moves on until a human has read the last output.
14. **Problems**: fix upstream and re-run forward; use the loop-back table; turn recurring edits into source changes.
15. **Sessions**: read CLAUDE.md and PROGRESS.md, verify against the files, work, update PROGRESS.md.
16. **Prompts**: Identity, Task, Context, Constraints, Output Format. One ask per prompt. Correct in place.
17. **Validate**: walk test, matrix checks, one end-to-end run.

---

## 20. Templates (copy-ready)

Conventions: `[Description]` is filled by the builder while authoring. `{{NAME}}` is filled by `setup`. `<name>` is a per-run variable (§10.1).

### 20.1 Tier 1 `CLAUDE.md` (the Map) [F 3.1, 3.2]

```markdown
# [Project Name]

You are helping [NAME] with [WHAT THEY DO], for [AUDIENCE].

## Rooms
- /[room-1]: [what happens here]
- /[room-2]: [what happens here]
- /_shared: references used by more than one room

## Routing
| Task | Go to | Read | Skills |
|------|-------|------|--------|
| [task type 1] | /[room-1] | CONTEXT.md | [skill or none] |
| [task type 2] | /[room-2] | CONTEXT.md, then /_shared/[file].md | [skill or none] |

## Naming conventions
- Drafts: topic-name_draft.md
- Final: topic-name_final.md
- Dated: YYYY-MM-DD-topic.md

## Rules
- Read this file first on every new task. Then read PROGRESS.md if it exists.
- Ask clarifying questions before making assumptions. When unsure, say so.
- Save work to files in the right room, not only in chat.
- [one workspace-wide rule, e.g. never mix client information across folders]
```

### 20.2 Tier 1 room `CONTEXT.md` [F 1.2, 3.1 to 3.3]

```markdown
# [Room Name]

Last updated: [YYYY-MM-DD]

## What this room is for
[One or two sentences about the work done here and who it is for.]

## Process
First [step], then [step], then [step].

## What lives here
- drafts/  final/   (naming: topic-name_draft.md, topic-name_final.md)
- references/[file].md: [what it holds; load when ...]
- ../_shared/[file].md: [what it holds; load when ...]

## Skills and tools
- [skill name]: [when to use it]

## What good looks like
[Specific description, or a pointer to a curated example in references/.]

## What to avoid
[The mistakes and annoyances that keep happening.]
```

### 20.3 Single-project `CLAUDE.md` [F 4.4]

```markdown
# [Project Name]

[One or two sentences: what this is.]
[Tech stack or document types]

## Commands (or: How to use these files)
[command] | [command] | [command]

## Conventions
[Where things go. Patterns used.]

## Avoid
[Things not to do, and what to use instead.]
```

### 20.4 Tier 2 `CLAUDE.md` (merged template) [A][R]

```markdown
# [Workspace name]

[One sentence: what this workspace is and what leaves it.]
[Optional: Use this when [...]. Not for [...]; use [sibling] instead.]

Built on ICM: folders carry sequencing, hierarchy carries context, files carry state. If something needs explaining, the explanation goes in that folder's CONTEXT.md.

## Where things live
| Folder | What it holds |
|---|---|
| `stages/` | the pipeline, in execution order (overview: CONTEXT.md) |
| `_shared/` | factory: rules and reference that never change per run |
| `scripts/` | mechanical, non-AI steps called by stages |
| `setup/` | one-time configuration and run procedures |
| `_archive/runs/` | completed runs, kept as data |

## Route by what just happened
| If | Go to | Then stop at |
|---|---|---|
| starting a new run | `setup/new-run.md`, then `stages/01_[name]/CONTEXT.md` | the human approves 01's output |
| [NN] output approved | the next numbered stage | that stage's Human check |
| asked for `status` | scan `stages/*/output/` headers | report PENDING / DRAFT / APPROVED |
| asked for `setup` | `setup/questionnaire.md` | zero `{{` remain |

## Naming
Outputs: `<run-id>-<artifact>.md`. Run IDs: [format, e.g. 2026-w39].

## The one rule
Nothing moves to the next stage until a person has read the output of the last one.
```

### 20.5 Root `CONTEXT.md`, Shape A (the pipeline in one screen) [A]

```markdown
# [Workspace name]: the pipeline

The flow in one line: [plan it, make it, check it, ship it, in this workspace's words].

| Stage | Job | Input | Output | Human check (canonical: stage contract) |
|---|---|---|---|---|
| `01_[name]` | [about five words] | `input/` | `output/<run-id>-[artifact].md` | [reviewer]: [act] |
| `02_[name]` | [about five words] | 01's output | `output/<run-id>-[artifact].md` | [reviewer]: [act] |
| `03_[name]` | [about five words] | 02's output | `output/<run-id>-[artifact].md` | [reviewer]: [act] |

Factory (stable, every run): `_shared/` (voice.md, rules.md, definition-of-done.md)
Product (new each run): each stage's `output/`
Deliverable: [file] from stage [NN], delivered by [human act or script].

Status is whatever exists: PENDING (no artifact), DRAFT, APPROVED (from the output header). A placeholder that only keeps the empty folder in git does not count.
```

### 20.6 Stage `CONTEXT.md` (unified) [A][R]

```markdown
# [NN]_[stage-name]: [the job in about five words]

One job: [the single thing this stage does].

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Working (this run) | `../[NN-1]_[prev]/output/<run-id>-[artifact].md` | Full file | The artifact to transform |
| Reference (every run) | `../../_shared/voice.md` | "Hard Constraints" through "What the Voice Is NOT" | Tone rules |
| Reference (every run) | `references/[stage-guide].md` | Full file | Structure for this stage |

Do NOT load: [other stages' references, prior runs, the whole _shared folder, unneeded skills]. Do not read other output/ files to learn patterns.

## Process

1. Read the inputs. [Entry stage only: restate the task in one sentence for confirmation; write `output/<run-id>-meta.md`.]
2. [One concrete action.]
3. **[Checkpoint 1]** -- Present [options or draft] to the human for [decision].
4. [One concrete action, following the reference constraints.]
5. [Hard limit worth restating (canonical: references/[file].md).]
6. Run the audit checks below. If any fail, revise before saving.
7. Save to output/ with the header (status: draft).

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | [what to show] | [what to choose] |

## Audit

| Check | Pass Condition |
|-------|---------------|
| [Check name] | [Unambiguous pass/fail condition] |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| [Name] | `output/<run-id>-[artifact].md` | Header (status, source, targets) + body + Open Questions |

## Human check

Reviewer: [role]. Gate: [blocking | auto-advance | final approval].
[One concrete act: read it aloud / verify the numbers against X / confirm the order survived.] Edit the output in place, then set `status: approved`; the next stage reads whatever is here.
```

### 20.7 Setup questionnaire (pairs with §20.8; passes V3) [R][A]

```markdown
# Onboarding Questionnaire

<!-- Agent: read this when the user types "setup". Ask ALL questions in one pass.
     Replace placeholders in the listed files. Run pass 2 for derived voice rules.
     Then scan the workspace for "{{". Rules: flat list, all at once, system-level
     only, derive don't ask, sensible defaults, ask once never again, examples over
     descriptions. -->

### Q1: What is the brand or team name, and who is the audience?
- Placeholder: `{{BRAND_NAME}}`, `{{TARGET_AUDIENCE}}`
- Files: `_shared/voice.md`, `_shared/definition-of-done.md`
- Type: free text
- Example: "Acme Ops; regional operations leadership"

### Q2: What does a finished deliverable look like?
- Placeholder: `{{DEFINITION_OF_DONE}}`
- Files: `_shared/definition-of-done.md`
- Type: free text
- Example: "One page, five sections, ready to forward without edits."

### Q3: Paste two short examples of past work that sound right, and one that sounds wrong.
- Placeholder: `{{VOICE_RIGHT_EXAMPLE_1}}`, `{{VOICE_RIGHT_EXAMPLE_2}}`, `{{VOICE_WRONG_EXAMPLE_1}}`
- Files: `_shared/voice.md`
- Type: structured
- Derived: `{{VOICE_HARD_CONSTRAINT_1}}`, `{{VOICE_HARD_CONSTRAINT_2}}`, `{{VOICE_PACING}}` (show these back for review in pass 2)

### Q4: What hard constraints never bend (length, format, brand rules, compliance)?
- Placeholder: `{{HARD_RULES}}`
- Files: `_shared/rules.md`
- Type: free text
- Default: "None beyond the definition of done."

### Q5: What do you always check before anything ships?
- Placeholder: `{{FINAL_HUMAN_CHECK}}`
- Files: `stages/03_[name]/CONTEXT.md` (Human check line)
- Type: free text
- Example: "Verify every number against the source export."

### Q6: What already exists that runs should reuse (templates, examples, data sources)?
- Placeholder: `{{REUSABLE_ASSETS}}`
- Files: `_shared/assets.md`
- Type: free text
- Default: "None yet."

### Q7: Do you need the optional [name] stage?
- Type: yes/no
- If NO: Remove `stages/[NN]_[name]/` entirely, and its rows in CLAUDE.md and CONTEXT.md.

---

## After Onboarding

Tell the user what was configured and where to start. Scan the whole workspace for remaining `{{`. If any remain, ask for the missing information. Onboarding is complete only when none remain. Record the setup in PROGRESS.md.
```

### 20.8 Voice file (pairs with §20.7) [R]

```markdown
# Voice Rules: {{BRAND_NAME}}

How {{BRAND_NAME}} writes. Load the sections named in each stage's Inputs.

## Hard Constraints
These are errors. If the output contains any of these, rewrite.
1. {{VOICE_HARD_CONSTRAINT_1}}
2. {{VOICE_HARD_CONSTRAINT_2}}
3. Filler transitions ("Now let's talk about..."). Just start the next thought.   <!-- default; keep or delete -->
4. Recap summaries at the end of sections.                                         <!-- default; keep or delete -->
5. Hype language ("game changing", "revolutionary").                               <!-- default; keep or delete -->

## Sentence Rules
| Wrong | Right |
|-------|-------|
| {{VOICE_WRONG_EXAMPLE_1}} | {{VOICE_RIGHT_EXAMPLE_1}} |
| "They invested significant time in infrastructure development." | "They spent six months building a custom pipeline." |

Target sentences: {{VOICE_RIGHT_EXAMPLE_2}}

## Pacing
{{VOICE_PACING}}

## What the Voice Is NOT
**Not performative.** Bad: "As someone who works extensively in this field..." Good: "A company I worked with spent six months on this exact problem."
**Not antithetical.** "Not X, but Y" at most once per piece.
**Not rhetorically questioning.** Cut questions that exist only for effect.

## Strategic Rationale
Why these choices work for {{TARGET_AUDIENCE}}. (Usually not loaded.)
```

### 20.9 `PROGRESS.md` [PB Stack 2.4]

```markdown
# Progress

## Current Status
[One or two lines: what is being built or run now, and what is next.]

## Last Session ([YYYY-MM-DD])
- Completed:
- In Progress:
- Blocked:
- Next:

## Decisions Made
- [Decision] ([reason])

## Open Questions
- [Question]
```

### 20.10 Context-map process node [A]

```markdown
---
type: process
team: [team-slug]
owner: [name]
ai-level: L0   # L0 manual · L1 copy-paste · L2 structured · L3 integrated
frequency: [daily|weekly|monthly|ad-hoc]
value: 3       # 1-5, to the business
pain: 3        # 1-5, to the people doing it
consumes: ["[[data-input-asset]]"]
produces: ["[[data-output-asset]]"]
governance: internal   # internal · sensitive · external
---

# [Process name]

## Input → Movement → Output
## Now
## What is working / not working
## If we structure this
## What the human keeps checking
```

### 20.11 Memory entry-file seed [M]

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

### 20.12 `SKILL.md` [I from A, lecture-deck, R skills]

```markdown
---
name: [skill-name]
description: [What it does in one sentence]. Use when [situation 1], [situation 2], or the user says "[trigger phrase]", "[trigger phrase]". Not for [near-miss task]; use [alternative] instead.
---

# [Skill Name]

[One paragraph: the method. One governing metaphor if it helps.]

## The rules that make it good
- **[Rule title].** [One or two sentences.]
- **[Rule title].** [One or two sentences.]

## When you get a request
1. [Ask for or infer the inputs that matter.]
2. [Write the plan artifact first, e.g. a brief or storyboard. Checkpoint it with the human.]
3. [Build.]
4. [Validate: render, walk, or check. Fix and repeat until clean.]
5. [Deliver, and name anything still placeholder.]

## Guardrails
- [Where this loses; what not to use it for.]

## Commands
    python scripts/[tool].py [args]

## Files
- `references/[topic].md`: read when [condition].
- `assets/templates/[file].md`: copy when [condition].
- `scripts/[tool].py`: [what it does].
```

### 20.13 Workflow intake (discovery) [PB 2.3][R 01-discovery]

```markdown
# Workflow intake: [name]

TRIGGER: [what starts it; how often]
STARTING POINT: [what exists at the start]
STEPS (as done today):
1.
2.
STOPS AND CHECKS: [where the person pauses; what they verify; who]
STAYS THE SAME EVERY RUN: [voice, rules, schema]  -> factory
NEW EVERY RUN: [inputs, topic]                     -> product / per-run variables
END STATE: [the artifact that leaves; who receives it]
VARIATIONS: [optional stages; branches a human decides]
TOOLS / SKILLS: [installs needed; skills to bundle]
SENSITIVE DATA: [personal or confidential fields]

WORTH AUTOMATING? (check all that apply)
[ ] Done weekly or more often
[ ] 3-15 steps
[ ] Steps are the same each time
[ ] Decisions do not change step to step (or the variable decision can be a human checkpoint)
[ ] Inputs arrive in a stable format
4-5: build it. 2-3: try a saved prompt first. 0-1: probably not worth it.
```

(The original browser-shortcut checklist used "No CAPTCHAs or complex logins" and "The site layout is stable" as its last two boxes. They are generalized here. [EXT])

### 20.14 Migration map (restructure) [A]

```markdown
# Migration map: [workspace]

Approved by: [name] on [YYYY-MM-DD]   (leave blank until approved)

| Old path | New path | Role (catalog/contract/factory/product/dead) | Referrers found | Action |
|---|---|---|---|---|
| [path] | [path] | [role] | [in-vault / ../ / symlink / external, or none] | copy-verify-remove / hold / archive |

Case-folded collisions: [none, or list]
External consumers named by the owner: [list]
Parity method: [count + hash | text parity for conversions]
```

---

# PART II: REFERENCE APPENDIX

## A1. Rationale and Mental Models

### A1.1 The central observation

> "If the prompts and context for each stage of a workflow already exist as files in a well-organized folder hierarchy, you do not need a coordination framework to manage multiple specialized agents. You need one orchestrating agent that reads the right files at the right moment. The folder structure tells it what to do at each step, and if the agent delegates sub-tasks, the same folder structure determines what context those sub-agents receive. Local Python scripts handle the parts that do not need AI." [P §1]

> "This is going backward before going forward. The principles that made Unix pipelines effective in the 1970s and multi-pass compilers tractable in the 1980s apply directly to AI agent orchestration in the 2020s." [P §1]

The problem, as Jake states it to beginners: "Most people open Claude or ChatGPT, type something, get a response, and start over... You are burning tokens on stuff that does not matter. You cannot edit what the AI produces at each step. And every conversation starts from zero. The folder structure fixes all of that." [F 3.1]

### A1.2 Framework vs ICM control surfaces [P Table 1]

| Operation | Framework approach | ICM approach |
|---|---|---|
| Change stage order | Edit orchestration code, redeploy | Rename or reorder folders |
| Modify a prompt | Edit agent configuration in code | Edit a markdown file |
| Add or remove a stage | Write a new agent class, update the orchestrator | Add or delete a folder |
| Inspect intermediate state | Add logging, build a dashboard | Open the folder, read the files |
| Hand off to another person | Document environment, dependencies, setup | Copy the folder |
| Who can make changes | A developer | Anyone with a text editor |
| Error recovery mid-pipeline | Built-in retry, fallback, exception handling | Manual re-run of the failed stage |
| Conditional branching | Programmatic routing on agent output | Human decides between stages |
| Concurrent execution | Native parallel agents | Sequential by design |
| External services | Programmatic API calls, auth | Local scripts or MCP connections |

ICM wins the first six rows; frameworks win the last four. [P]

### A1.3 The five design principles [P §3.1][R][A core]

| # | Principle | Borrowed from | Practice |
|---|---|---|---|
| 1 | **One stage, one job** | McIlroy (Unix), Parnas (information hiding) | "A stage that fetches data does not also filter it." |
| 2 | **Plain text as the interface** | Kernighan & Pike | Markdown and JSON. No binaries, no databases in the loop, no proprietary serialization. |
| 3 | **Layered context loading** | Context engineering; "lost in the middle" (Liu et al.) | "Prevention rather than compression." Reference and working context are kept structurally apart. |
| 4 | **Every output is an edit surface** | Horvitz (mixed initiative), Shneiderman (direct manipulation) | "The system picks up whatever the human left there." |
| 5 | **Configure the factory, not the product** | Continuous delivery | Set up once; each run emits a new deliverable. |

### A1.4 Mental models

| Model | Statement | Design implication | Source |
|---|---|---|---|
| **Map / Rooms / Tools** | A floor plan on the wall; rooms with their own context; tools wired into the rooms that need them | The root only orients; detail lives in the rooms | [F 3.1, 4.5] |
| **The library** | "The routing files are the catalog: small, stable, they point at everything and store almost nothing... One librarian — one model — walks the building... Nobody photocopies the library into a backpack; that is what context-stuffing is." | Pointers, never payload | [A] |
| **Factory vs product** | L3 is the factory, L4 is the product: the recipe and the ingredients. And the warning: "They built the factory without ever making a product." | Separate the stable from the per-run; do not over-build | [P][R][A][F 3.3] |
| **Folder = memory, prompt = direction** | Identity and context live in files; the task and constraints go in prompts | | [F 1.2, 1.3] |
| **Stateless model, stateful workspace** | "The workspace is the memory." | Persist plans, progress, decisions | [PB Stack 2.4] |
| **The new hire** | CLAUDE.md is "an onboarding document for a new hire. Except the new hire reads the entire thing in two seconds and follows every word." | Write for a smart outsider | [F 4.4] |
| **Mad Libs (1953)** | The model fills blanks without seeing the story, so it sees only its context window | Control the story it can see | [V][F 2.3 via 4.2] |
| **Unix pipeline** | "Programs that do one thing. Output of one becomes input of another. Plain text as universal interface. Human-readable intermediate state." | One stage, one job; text handoffs | [P §1, §7] |
| **Multi-pass compiler** | Each stage is a pass producing an intermediate representation; re-run only the stale passes | Complete, readable outputs; selective re-runs | [P §4.2, §6.1] |
| **Literate programming** | Instructions and documentation are one artifact | CONTEXT.md is readable by humans and followable by agents | [P §3.3] |
| **Glass box** | "It was never opaque in the first place." | Observability comes for free | [P §5.3][R] |
| **Index lookup vs table scan** | Reading everything is a scan; a catalog plus 2 or 3 files is a lookup | Resolve via entry → index → leaves | [M] |
| **Make** | Files are both the work and the coordination | No orchestration layer; generated indexes | [P §2.1][M] |
| **Codd normalization** | "A fact should live in one place and be pointed at from everywhere else, because copies of a fact drift apart." | One home per fact | [M] |
| **Origin layer metaphors** | L0 "the DNS of the system", L1 "a load balancer", L2 "the app servers" | Routing layers route; they do not work | [O] |
| **Worse is Better** | "ICM trades the flexibility of a programmatic orchestrator for the portability, inspectability, and editability of plain files. That tradeoff is the point." | Simplest structure that works | [P §3.2] |
| **Orchestration vs intelligence** | A 100K-star "agent" product has no AI of its own; it is orchestration | Most agent value is organization | [V][F 4.5] |
| **"The machine is smart"** | "Being smart is not the hard part." "Productionize your opinion, not just your process." "If your value lives in a clever prompt, you are racing the labs, and you will lose." Engelbart: intelligence depends on organization. | Encode judgment and arrangement | [SS] |
| **The abstraction ladder** | "One line of Python triggers 12,000 lines of code"; every layer of computing started unreliable | Build structure around probabilistic AI; work at the right layer ("build your business layer as markdown files on top of what skills and tools your AI partners already provide") | [SS][V] |
| **The folder is the app** | "The folder becomes your app. This is your UI. What simpler UI than a folder?" | No custom UI unless it is proven necessary | [F 3.1] |
| **Inverted U** | "Too few constraints and you get chaos, too many and you get stiff output, the right amount and creativity increases." | Creative room within clear boundaries | [PB 1.1, citing F 2.6] |
| **Car to check the mailbox** | Chat-only use leaves most capability unused | Give the model your files | [F 4.1] |
| **Vending machine vs thinking partner** | Use chat to challenge your thinking, not just to dispense content | Plan before building | [F 4.3] |
| **Every document on one desk** | A flat folder causes wrong picks | Subfolders | [F 3.3] |

### A1.5 Who does what

| Actor | Does | Does not |
|---|---|---|
| One orchestrating agent | Reads routing, runs one stage or task at a time, writes files, runs audits, presents checkpoints | Load everything; branch on its own; learn from old outputs |
| Sub-agents (optional) | Delegated sub-tasks inside a stage, prompted from the same files | Coordinate through code |
| Local scripts | Mechanical work: fetching, moving, formatting, rendering, transcribing, counting, indexing | Make judgment calls |
| Human | Reviews outputs; edits files; branches between stages; approves restructures; fixes sources | Re-answer setup each run |

> "The folder hierarchy is both the human's control surface and the model's orchestration logic." [P §4.1]

### A1.6 Full glossary

| Term | Definition |
|---|---|
| Workspace | A self-contained folder holding one ICM system. In Tier 1, Jake also calls each room a "workspace". [P][F] |
| Room | A Tier 1 area for one kind of work, with its own `CONTEXT.md`. [F] |
| Entry file (L0, the Map) | Root `CLAUDE.md` or `AGENTS.md`: routing only. [A][F] |
| Root CONTEXT.md (L1) | Workspace routing: "the pipeline in one screen" or a task-routing table. [A][R] |
| Stage | A numbered folder that does one job in sequence. [P] |
| Stage contract (L2) | A stage's `CONTEXT.md`. "The control point of the entire system." [P] |
| Inputs table | Names exactly which files and sections to load; makes selection "explicit, editable, and auditable". [P] |
| Routing table | Task → go to → read → skills. "The most important pattern in the whole system." [F 3.1] |
| Reference material (L3, factory) | Stable rules; internalized as constraints. [P] |
| Working artifacts (L4, product) | Per-run content; processed as input. [P] |
| Handoff | One stage's `output/` read as the next stage's input. [R] |
| Edit surface | An intermediate output a human may edit. [P] |
| Checkpoint | An in-stage pause between process steps. [R] |
| Human check / gate | The single act a person performs on a stage's saved output. [A] |
| Gate type | blocking, auto-advance, or final approval. [EXT] |
| Audit | Pass/fail checks run before saving. [R] |
| Verify | A proposed section for checking against earlier outputs. [P §6.2] |
| Trigger | A keyword (`setup`, `status`) that points to a procedure. [R] |
| Questionnaire | One-time onboarding that configures the factory. [R][A] |
| Placeholder | A `{{SCREAMING_SNAKE}}` token filled by `setup`. [R] |
| Conditional section | `{{?NAME}}...{{/NAME}}` around a whole section. [R] |
| Per-run variable | A `<name>` token resolved each run. [EXT] |
| Skill | A folder of `SKILL.md` + rules or references + scripts. [R][A] |
| Form | Pipeline, Umbrella, Record library, Knowledge bundle, Context map, System map. [A] |
| Walk test | A cold-agent validation. [A] |
| Catalog / Contract / Factory / Product / Dead | The five restructure roles. [A] |
| Canonical source | The one authoritative home of a fact. [R] |
| PRD | A product requirements document; "stateful prompting". [PB] |
| PROGRESS.md | Session continuity file. [PB] |
| Edit-source principle | "Editing the output fixes this run. Editing the source fixes every future run." [P §6.3] |
| Universe (system map) | live, leftover, or ghost. [A] |

---

## A2. Worked Examples

### A2.1 Tier 1 trees [F 3.2]

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

Its CLAUDE.md rules:
- "Never reference one client's information in another client's workspace"
- "Proposals always start from /templates and get customized in the client folder"
- "Deliverables go in /client-[name]/deliverables, drafts stay in working folders."

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

**Website project** [PB 3.2]:
- Root `CLAUDE.md` (master routing, 30 to 50 lines)
- `docs/brand-voice.md`, `docs/design-tokens.md`, `docs/prd.md`
- `src/components/README.md`, `src/pages/README.md`, `src/layouts/README.md` for folder-level detail
- `.gitignore` covering `.env`, `node_modules`, build output

### A2.2 script-to-animation (Pipeline, 3 stages) [R][P §4.2]

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
    └── 03-build/    references: build-conventions, remotion-setup   (optional; removed if setup says no)
```

- **01-script.** Topic → pick the pillar → propose 3 to 5 angles, tagged with value slots and format → **Checkpoint 1** → value brief (concept, 2+ value slots, format, hook, close) → **Checkpoint 2** → write the full script in one pass → audit → metadata header → `output/[topic-slug]-script.md`. The audit checks:
  - the voice hard constraints;
  - delivery on the locked value slots;
  - the tension lands within 2 to 3 seconds;
  - the close is something you could say to a friend;
  - no gap over 5 seconds without a retention beat;
  - the share test.
- **02-spec.** Script → core visual metaphor → beats → beat map → visual philosophy → 2 to 3 key moments → audio sync → color flow → audit (mute test, one concept per beat, contract purity, key moments, 3+ sync points) → `output/[topic-slug]-spec.md`.
- **03-build.** Inputs: the spec, build conventions, the Remotion skill (index, then rules), and `../02-spec/references/design-system.md` (a one-way cross-stage reference). Output: `output/[topic-slug]/{index.tsx, beats/*.tsx, constants.ts, assets/}`. The audit checks spec coverage, shared constants, platform specs, no hard cuts, mobile readability, and safe zones.
- Its What to Load table excludes, per task, the other stages' references and any unneeded skills.

### A2.3 course-deck-production (Pipeline, 5 stages) [R][P §4.3]

1. **01-extraction.** The entry stage collects course metadata into `output/[course-slug]-meta.md`. Chunks are tagged by topic, complexity, and source. It has a checkpoint and an audit (coverage, tag accuracy, citations, one concept per chunk).
2. **02-curriculum.** Modules and sessions, with 2 to 3 objectives each.
3. **03-outline.** 15 to 25 slides per session, drawn from a slide-pattern library.
4. **04-generation.** HTML per slide, then html2pptx to `.pptx`. Linear, with no checkpoint.
5. **05-qa-delivery.** Thumbnail grids; a must-fix / should-fix loop back into 04's HTML; `output/final/`; a QA report; a delivery manifest.

Setup includes a default start stage, and the metadata travels forward. The design reason: "By surfacing the structural plan as an editable markdown file before any slides are drafted, ICM lets the human course-correct at the point where correction is cheapest."

### A2.4 voice-driven-animation (Pipeline, 5 stages, 3 custom skills) [R]

1. **01-research.** Restate the topic for confirmation; gather 3 to 7 primary sources, with verbatim quotes for numbers and conflicts surfaced. Produces a brief with Summary, Claims, Angle, and Open Questions.
2. **02-script.** A word budget at about 150 to 170 wpm. Produces a paste block for the text-to-speech tool plus a beat-annotated copy with `<!-- BEAT N -- desc (~Ns) -->` markers. The audit allows at most one antithesis, zero em dashes, a word count within ±10%, and claims sourced to the brief, and runs a dry-run extract.
3. **03-voice.** Precondition `.env` check → dry run → checkpoint before spending credits → audio → transcript JSON → beat timings by phrase match. All steps are scripts.
4. **04-animate.** A timing file and per-beat scenes. Values are derived, never guessed.
5. **05-render.** Pre-flight, render, a runtime within 5%, a release note, and a "When to Loop Back" table.

Its source-of-truth chain runs: cited sources → script → audio → beat timings → composition. Its CLAUDE.md has a "When to Use This Workspace" section that tells it apart from script-to-animation.

### A2.5 workspace-builder (meta-pipeline, 5 stages) [R][P §4.4]

| Stage | Output |
|---|---|
| 01-discovery | `workflow-map.md` |
| 02-mapping | `stage-contracts.md` plus an ASCII dependency diagram |
| 03-scaffolding | the whole new workspace, in `output/` |
| 04-questionnaire-design | `questionnaire.md` |
| 05-validation | `validation-report.md` (13 checks) |

Its own setup asks four questions, and the answers feed discovery. "The builder enforces the same structural rules it was built with."

### A2.6 The origin system (Content-Agent-Routing-Promptbase) [O]

An umbrella of rooms under one CLAUDE.md:
- `brand-vault/`: READ-ONLY "DNA".
- `script-lab/`: 6 hook types, script templates; scripts sorted by format and by pillars P1 to P5.
- `topic-engine/`: topics T-01 to T-50.
- `products-and-offers/`, `platform-playbook/`, `production-rhythm/`.
- `animation-studio/`: a component registry and design system, plus `workflows/01-scripts → 02-specs → 03-builds/[active|complete] → 04-renders`.

Measured budgets:

| Task | With routing | Without |
|---|---|---|
| Write a script | ~4,000 tokens | 15,000+ |
| Generate a spec | ~5,000 | 12,000+ |
| Research topics | ~2,500 | 15,000+ |
| Plan the week | ~1,500 | 15,000+ |
| Render | ~500 | 15,000+ |

History: a monolith that "worked for about two weeks", then a "distributed monolith" (duplication and drift), then the routing architecture. Jake traces the instinct to maintaining crypto systems in the Marines: "the system that works is the one where every component has one job, and the interfaces between components are explicit and documented."

### A2.7 Duplicate and adapt [P §4.5]

People with a working workspace for one format (short explainers) duplicate the folder and edit the stage prompts for another format (long-form essays) instead of rebuilding. "This mirrors how Unix users build new shell scripts by modifying existing ones."

### A2.8 Practitioner variants [X]

These are shown for contrast only. They are not Jake's.
- **RyMac.** An 11-line "map" CLAUDE.md that only says to read `Context.md`, work inside the folder it points to, and update it before stopping. The `Context.md` "desk" has four headings: What we are working on (one thing) / Already decided (with the reason) / Where the material lives (one path) / Next (one line).
- **LVLY bot workspaces.** One workspace per invocation; "What NOT to Load" tables.
- **KTN.** `IDENTITY.md` as L0; "Conversations happen during review gates, not during execution."

---

## A3. Conflicts Between Sources and How This Document Resolves Them

| Topic | Variant A | Variant B | Resolution |
|---|---|---|---|
| Stage separator | `01_research` [P][A] | `01-script` [R] | Default `NN_`; either allowed; one per workspace |
| Shared folder | `_shared/` [A] | `shared/`, `brand-vault/`, `design-system/`; `_config/` in diagrams [R][P] | Default `_shared/`; named context folders allowed when they need a router |
| Entry-file size | under ~60 lines [A][M]; one screen, 30 to 50 lines [F][PB] | ~800 tokens; Jake's workspace CLAUDE.md files run 67 to 81 lines (repo root 42) [R][P] | Target 30 to 50; the limit is ~60. (The 80-line rule in [R] applies to CONTEXT.md, not CLAUDE.md.) |
| Number of layers | three (Map / Rooms / Tools) [F] | five (L0 to L4) [P][R][A] | One architecture at two resolutions (§4.1) |
| Stage contract shape | Inputs table + optional Checkpoints and Audit [R] | Working/Reference list + Do NOT load + one Human check [A] | Unified superset (§7.3); Checkpoints ≠ Human check (R-CTR-25) |
| Specs | Code blueprints [O] | Contracts: WHAT and WHEN [R v2][PB] | Contracts, and not under-specified |
| Component registry vs spec purity | "Specs and builds should only reference components listed here" [R registry] | Specs contain zero component names [R spec-format, V9] | The registry constrains builds; specs describe visual concepts. (The registry's "specs" wording is a leftover of the blueprint era.) [I] |
| Learning from outputs | Read one existing build [O] | Never [R v2] | Never; curated exemplars in `references/` are allowed |
| Committing outputs | Gitignore outputs [R] | Commit after each run for history [P] | Templates: no. Deployments: may |
| Em dashes | Banned in the repo [R] | Used freely [A] | House style; banned in Jake-voice scripts [O] ("does not necessarily apply to technical doc[s]") |
| Name | Model Workspace Protocol (MWP) [P v1][R early] | Interpretable Context Methodology (ICM) | ICM |
| Questionnaire | Grouped categories, one voice description [early MWP] | Flat, all at once, examples [R v2] | Flat, all at once, examples |
| Skills vs context files | "Prefer CONTEXT.md files first to save tokens" [O] | Bundle skills; skills replace reference docs [R] | Reference files for workspace-specific knowledge; skills for reusable domain knowledge, wired in per room or stage |
| Human gate vs straight-through | "Nothing moves until a person has read..." [A] | Linear stages "run straight through"; "AI can automate all four" [R][PB] | Gate types (§9.6) [EXT] |
| Placeholders in root CONTEXT.md | Forbidden in routing tables [R] | script-to-animation's CONTEXT.md holds a `{{?BUILD_STAGE}}` block [R] | Conditional sections are allowed outside tables (R-L1-02) |
| 60/30/10 split | 60% traditional/database, 30% rule-based logic, 10% AI [SS snippet] | ~60% data processing, ~30% orchestration, ~10% AI calls [X wiki on Ethics Engine] | Cite the [SS] version; both say AI is the smallest slice |
| Do NOT load | In [A]'s stage template and Pipeline form | Not in [A] core.md's contract format, and not checked by the walk test | Strongly recommended (§7.3) |
| Record-library entry | `00_START-HERE.md` [A] | Claude Code auto-loads only `CLAUDE.md` | Add a one-line `CLAUDE.md` pointer [EXT] |

---

## A4. Evidence and Claims (for calibration)

- **Token budgets.** In the paper's figure, the ICM stages ran about 4.9k, 5.5k, and 5.6k tokens, against about 42k for one monolithic prompt. [P Fig. 3]
- **Practitioners.** These come from a 52-member invite-only community. All are self-reported, not instrumented. [P §4.5, §4.6]
  - 30 of 33 reported a U-shaped editing pattern (about 92%, 30%, 78%).
  - Non-technical users edited CONTEXT.md successfully.
  - Three people with no coding experience built and ran workspaces that produced ten-minute animated videos.
  - People duplicate and adapt workspaces rather than starting fresh.
- **External adopters.** University of Edinburgh Neuropolitics Lab, ICR Research, and the Academy of International Affairs (Bonn). Details are under NDA. [P §4.4]
- **Model setup.** Claude Code, with Opus 4.6 orchestrating and Sonnet 4.6 as sub-agents. [P §4.1]
- **Memory study, on LongMemEval.** Folder memory was compared against the whole history in context. [M]
  - Accuracy did not differ significantly: 0.744 vs 0.872, p = 0.227.
  - The folder read 97% fewer tokens and cost 95% less per query. It broke even after about 7 questions (range 5.7 to 8.7).
  - The same agent *without* ICM conventions was significantly worse than long context (p = 0.021). ICM vs the unguided agent was 6 to 1 on discordant pairs (p = 0.125, not significant).
  - A memory built by one vendor's model and read by another's scored the same accuracy at 96% lower cost (n = 5, directional).
  - Accuracy rankings reversed twice as the sample grew. Cost figures moved under 4%. "The two halves of this paper do not deserve equal confidence."
- **Community scale.** Clief Notes had about 49,400 members in a 2026 search snapshot. The old community drew 7,000 members in its first twelve days. Jake has cited "30,000 people" building without frameworks. [SS]
- **Honest limits.** No controlled comparison of staged vs monolithic quality exists yet. Testing used a single model family, and the community is self-selected. The benchmark cannot measure what ICM exists for: auditability, correction, collaboration. [P][M]
- **Open questions the authors name.**
  - Does the hierarchy generalize across model families?
  - Do larger context windows reduce the need for scoping? (The human-interaction arguments remain either way.)
  - How sensitive is output to the order and formatting of context within a layer? [P §5.4]
  - "The advantage of structured, human-readable memory grows with the number of parties who touch it." This is a hypothesis, with proposed metrics: convention drift, collision rate, repair cost. [M]

---

## A5. Extensions Register (`[EXT]`: ours, not Jake's)

These close gaps that turned up when an agent built real workspaces from the sourced rules alone. Review them before adopting.

| ID | Extension | Where | Why it was needed |
|---|---|---|---|
| EXT-01 | Approval states PENDING / DRAFT / APPROVED, set by a `status:` field in the output header | §9.5 | "COMPLETE" alone cannot show that the human gate was passed |
| EXT-02 | Gate types (blocking, auto-advance, final approval), each with a named reviewer | §9.6, R-CTR-26 | Reconciles "nothing moves until read" with straight-through linear stages; handles multiple reviewers |
| EXT-03 | `input/` folder in the entry stage | §6.1 | No home existed for raw per-run inputs |
| EXT-04 | `scripts/` folder at the root | §6.1, R-SCRIPT-04 | Scripts were required but had no location |
| EXT-05 | Run archive `_archive/runs/<run-id>/`; prior-run data allowed as declared, read-only input | §9.9 | Trend and "what changed" needs collided with docs-over-outputs and the DAG rule |
| EXT-06 | Fill-in syntax: `[Description]`, `{{X}}`, `<var>` | §10.1 | The templates mixed three syntaxes, and per-run variables had none |
| EXT-07 | The "analytic" stage class | §8.2 | Judgment-heavy stages fit no existing class |
| EXT-08 | Sanctioned duplication list, with W5 scoped to authoritative copies | §8.4 | Jake's own templates restate facts |
| EXT-09 | Invariant applicability by tier | §2.1 | Tier 1 cannot satisfy all ten invariants |
| EXT-10 | Naming exceptions (uppercase entry files, code conventions, Tier 1 `_` suffix) | R-NAME-02 | The kebab-case rule conflicted with required filenames |
| EXT-11 | Path-base rule for CONTEXT.md vs CLAUDE.md | R-CTR-01 | Validators produced false hits without it |
| EXT-12 | Trigger rows point to procedure files (`setup/new-run.md`) | R-L0-09 | Procedures cannot live in CLAUDE.md |
| EXT-13 | `_meta/build/` for design artifacts | §6.2 | Build-time artifacts had no home |
| EXT-14 | Conversion sub-step for .docx and .pdf in restructures | §15.3 step 7 | Hash parity cannot hold across formats |
| EXT-15 | Personal-data intake masking and audit row | R-SEC-06 | Ticket and customer pipelines |
| EXT-16 | Skill-build procedure, SKILL.md template, skill checks | §15.4, §20.12, §17.6 | The guidance had rules only |
| EXT-17 | Checks-by-tier-and-form matrix; Tier 1 checklist | §17.3 | Validation did not say which checks apply where |
| EXT-18 | Form chooser for common corpora; reader-lookup tie-break | §16.8 | SOP-type corpora fit several forms |
| EXT-19 | Synthetic end-to-end run in an instance copy | §15.2 step 7 | No data available at build time |
| EXT-20 | "Fits one prompt" threshold in D2 | §1.2 | No threshold was given |
| EXT-21 | One-line `CLAUDE.md` pointer for record libraries | §16.3 | Claude Code auto-loads only CLAUDE.md |
| EXT-22 | Deliverable line in root CONTEXT.md; distribution happens outside the AI stages | §20.5, R-QA-06 | Final delivery was undefined |

---

## A6. Rule Index

<!-- GENERATED from the bold rule IDs in Part I by scratchpad/build_rule_index.py. Do not edit by hand; regenerate. -->

| ID | Keyword | Section | Title / gist | Sources |
|---|---|---|---|---|
| R-SCOPE-01 | MUST NOT | §1.3 | If the whole job fits in one saved prompt, say so. MUST NOT  | [A] |
| R-SCOPE-02 | MUST NOT | §1.3 | MUST NOT build a pipeline before the process has actually re | [A] |
| R-SCOPE-03 | MUST NOT | §1.3 | "Three real stages beat seven imagined ones." MUST NOT creat | [A] |
| R-SCOPE-04 | SHOULD | §1.3 | A Tier 1 first version SHOULD take about 15 minutes. "If it  | [F 3.3] |
| R-SCOPE-05 | INFO | §1.3 | "The moment it starts feeling heavy or complicated, somethin | [F 3.3] |
| R-SCOPE-06 | SHOULD | §1.3 | Use the simplest tool that solves the problem. Tool ladder:  | [PB 3.3] [PB Stack 1.1] |
| R-SCOPE-07 | SHOULD | §1.3 | "You can't write requirements for emergent behavior." For cl | [SS] |
| R-SCOPE-08 | SHOULD | §1.3 | Much "AI isn't good enough" frustration "is actually a conte | [O] |
| R-SCOPE-09 | SHOULD | §1.3 | Decide where AI fits at all. Jake's 60/30/10 framing: about  | [SS snippet; a different [X] |
| R-SCOPE-10 | SHOULD | §1.3 | If the person "make different decisions based on what  see", | [PB 2.3] |
| INV-01 | MUST | §2 | One folder, one job |  |
| INV-02 | MUST | §2 | A small, stable entry file |  |
| INV-03 | MUST | §2 | Numbering encodes order |  |
| INV-04 | MUST | §2 | Every folder-level contract is explicit |  |
| INV-05 | MUST | §2 | Factory vs product |  |
| INV-06 | MUST | §2 | Every output is an edit surface |  |
| INV-07 | MUST | §2 | Load only what the step needs |  |
| INV-08 | MUST | §2 | Plain text, linkable, queryable |  |
| INV-09 | MUST | §2 | The filesystem is the state machine |  |
| INV-10 | MUST | §2 | Instantiate by copying |  |
| R-LIB-01 | MUST | §2.2 | The catalog holds no books |  |
| R-LIB-02 | MUST | §2.2 | One home per fact | [A] [F 4.5] |
| R-LIB-03 | MUST | §2.2 | Generated indexes are never hand-edited | [A] [M] |
| R-LIB-04 | SHOULD | §2.2 | The structure is the documentation | [A] [P §3.3] |
| R-LIB-05 | SHOULD | §2.2 | Method and instance live apart | [A] |
| R-LIB-06 | SHOULD | §2.2 | Working sessions end in artifacts | [A] [F 4.3] |
| R-LIB-07 | INFO | §2.2 | New sessions start clean | [F 4.5] |
| R-LIB-08 | INFO | §2.2 | Same quality for everyone | [F 4.5] |
| R-LIB-09 | INFO | §2.2 | Change the labels, keep the architecture | [F 3.1, 3.2] |
| R-LAY-01 | MUST | §4.4 | No agent reads everything. Each task reads only as deep as i | [P] [R] |
| R-LAY-02 | MUST | §4.4 | L0 to L2 are the catalog: small, stable, no content payload. | [A] |
| R-LAY-03 | MUST | §4.4 | L2's Inputs section makes context selection explicit, editab | [A] [P] |
| R-LAY-04 | SHOULD | §4.4 | An L3 collection that grows past easy scanning gets its own  | [A] [P fn4 "can include"] [R] |
| R-LAY-05 | INFO | §4.4 | "Every token of irrelevant context is a token of diluted att | [O] [R] |
| R-LAY-06 | INFO | §4.4 | "The context window is working memory, not storage."  "200K  | [F 4.5] [O] [R] |
| R-LAY-07 | SHOULD | §4.4 | Token discipline | [A] [R] |
| R-LAY-08 | SHOULD | §4.4 | Each stage condenses and structures its output, so the next  | [I] [P] |
| R-LAY-09 | INFO | §4.4 | Every token in CLAUDE.md is paid on every prompt. "A 200-lin | [O] [PB 3.2] |
| R-LAY-10 | SHOULD | §4.4 | Keep tables and structured data as tables; they are already  | [F 1.3] |
| R-LAY-11 | MAY | §4.4 | A contract MAY state a load order ("Building animation? → Fo | [O] [P §5.4] |
| R-T1-01 | MUST | §5.3 | Separate kinds of work into separate rooms, so unrelated mat | [F 3.1] |
| R-T1-02 | SHOULD | §5.3 | Start with 2 to 3 rooms. "You can always add more." | [F 3.3] |
| R-T1-03 | SHOULD | §5.3 | The mental-mode test | [F 3.2, 3.3] |
| R-T1-04 | SHOULD | §5.3 | "If you are not sure whether something deserves its own work | [F 3.3] |
| R-T1-05 | MUST | §5.3 | One folder per client, each with its own CONTEXT.md. "Never  | [F 3.2] |
| R-T1-06 | SHOULD | §5.3 | More than 8 to 10 files at one level means subfolders. Group | [F 3.3] |
| R-T1-07 | MAY | §5.3 | Use stage or status subfolders: `ideas/ drafts/ final/`; `br | [F 3.2] [O] |
| R-T1-08 | SHOULD | §5.3 | Naming conventions replace databases | [F 3.1, 3.2] |
| R-T1-09 | SHOULD | §5.3 | Shared templates live in their own room (`templates/`), and  | [F 3.2] |
| R-T1-10 | SHOULD | §5.3 | Name sub-parts semantically, and record in the context file  | [PB 1.2] |
| R-T1-11 | SHOULD | §5.3 | Describe the work, not the AI | [F 3.3] |
| R-T1-12 | SHOULD | §5.3 | Specific audience facts beat role labels: "mid-market HR dir | [F 3.3] |
| R-T1-13 | SHOULD | §5.3 | Every room context file includes "What good looks like" and  | [F 1.2] |
| R-T1-14 | SHOULD | §5.3 | Keep context alive | [F 3.2, 3.3, 4.4] |
| R-T1-15 | SHOULD | §5.3 | Keep reference material (examples, links, style guides) sepa | [F 1.2] |
| R-NAME-01 | MUST | §6.3 | Stage folders carry a zero-padded two-digit order prefix. Th | [A] [P] [R] |
| R-NAME-02 | SHOULD | §6.3 | Folders and files use lowercase kebab-case with no spaces.   | [A] [EXT, codifying observed practice] [R] |
| R-NAME-03 | SHOULD | §6.3 | Meta and system folders take an underscore prefix so they so | [A] |
| R-NAME-04 | MAY | §6.3 | Ordered files inside a folder use an ordinal-only prefix (`0 | [A] |
| R-NAME-05 | SHOULD | §6.3 | Output artifacts are named `<topic-slug>-<artifact-type>.md` | [R] |
| R-NAME-06 | MAY | §6.3 | Typed content files prefix their type (`data-customer-list.m | [A] |
| R-NAME-07 | MUST | §6.3 | For records and nodes, pick kebab-case slugs (machine-facing | [A] |
| R-NAME-08 | SHOULD | §6.3 | Templates are blank, named for what they produce, and live t | [A] |
| R-NAME-09 | MUST | §6.3 | Placeholders follow §10.1. |  |
| R-NAME-10 | MUST | §6.3 | The entry file is `CLAUDE.md` for Claude Code and `AGENTS.md | [A] |
| R-NAME-11 | SHOULD | §6.3 | Use sortable dates (`YYYY-MM-DD-...`). For run IDs use lower | [EXT] [F 3.2] [M] |
| R-NAME-12 | MUST | §6.3 | Renumbering reorders the pipeline. In the same change, edit  | [A] |
| R-NAME-13 | MAY | §6.3 | Alternative branches a human chooses between are sibling sta | [I] [P §5.2] |
| R-NAME-14 | SHOULD | §6.3 | Every folder that should persist but starts empty gets a `.g | [R] |
| R-NAME-15 | MAY | §6.3 | Status and version may live in filenames (`--.md`, `T---v.mp | [O] |
| R-NAME-16 | MAY | §6.3 | A naming convention may double as an ID scheme: `ht10-second | [A] |
| R-L0-01 | MUST | §7.1 | Route, never hold content: no definitions, rule sets, exampl | [A] [F] [R] |
| R-L0-02 | MUST | §7.1 | Stay within the §3 limits. *Allowance*: an identity line and | [F 1.2, 3.2] [I resolving A vs F] |
| R-L0-03 | MUST NOT | §7.1 | Contain setup placeholders (`{{...}}`), because it must work | [R] |
| R-L0-04 | SHOULD | §7.1 | A repo or umbrella root `CLAUDE.md` routes into sub-workspac | [R] |
| R-L0-05 | SHOULD | §7.1 | Route by task, or by "what just happened" (If / Go to / Then | [A] [F] |
| R-L0-06 | SHOULD | §7.1 | In the What to Load table, list what NOT to load for each ta | [R] [X] |
| R-L0-07 | SHOULD | §7.1 | "The map states only what rarely changes; details live in ea | [A] |
| R-L0-08 | MAY | §7.1 | Include a start sequence: read this file → identify the task | [O] |
| R-L0-09 | SHOULD | §7.1 | A trigger row names the procedure file that defines it (`set | [EXT] |
| R-L0-10 | SHOULD | §7.1 | In memory and knowledge workspaces, include a numbered "How  | [M] |
| R-L1-01 | MUST | §7.2 | Routing only. The purity rules of §7.3 apply. |  |
| R-L1-02 | MUST NOT | §7.2 | Routing tables contain placeholders. A conditional *section* | [R] |
| R-L1-03 | SHOULD | §7.2 | List every shared resource with its location, so stages poin | [R] |
| R-L1-04 | MUST | §7.2 | The Shape A table summarizes the stage contracts. It is a sa | [A] [EXT reconciliation] |
| R-L1-05 | SHOULD | §7.2 | In Tier 1 there is usually no root CONTEXT.md. The Map route | [F] |
| R-CTR-01 | MUST | §7.3 | List every file the agent needs. Paths in a CONTEXT.md are r | [A] [EXT] [R] |
| R-CTR-02 | MUST | §7.3 | Label each input (L4) or (L3). The paper writes `Layer 4 (wo | [A] [P] |
| R-CTR-03 | MUST | §7.3 | Route to sections, not just files | [O] [R Pattern 4] [R] |
| R-CTR-04 | MAY | §7.3 | Table form `Source / File/Location / Section/Scope / Why` ,  | [A] [R] |
| R-CTR-05 | MUST | §7.3 | The working input names the previous folder's real name: "re | [A] |
| R-CTR-06 | MUST | §7.3 | User input is a row with Source `User` and Location `(conver | [EXT] [R] |
| R-CTR-07 | MAY | §7.3 | Skill row: `/ Skill / ../../skills/<name>/SKILL.md / Index,  | [R] |
| R-CTR-08 | MAY | §7.3 | When an output folder may hold several files, select with a  | [R] |
| R-CTR-09 | MUST NOT | §7.3 | Point inputs at earlier runs' outputs *to learn patterns* (§ | [EXT] [R] |
| R-CTR-10 | SHOULD | §7.3 | Name anything an eager agent would wrongly pull in: other st | [A] [R] |
| R-CTR-11 | MUST | §7.3 | Numbered steps. Each step is one concrete action. | [R] |
| R-CTR-12 | MUST | §7.3 | "Be specific enough that two different agents following thes | [R] |
| R-CTR-13 | SHOULD | §7.3 | Keep it short. "Constraints live in L3 files, not restated h | [A] |
| R-CTR-14 | MAY | §7.3 | Restate hard limits worth repeating (length, count, format:  | [A] [EXT] |
| R-CTR-15 | SHOULD | §7.3 | Mark checkpoint steps inline: ` -- Present X to the human fo | [R] |
| R-CTR-16 | SHOULD | §7.3 | The second-to-last step is usually "Run the audit checks bel | [R] |
| R-CTR-17 | SHOULD | §7.3 | In the entry stage, step 1 restates the task in one sentence | [R voice-driven 01-research, course-deck 01-extraction] |
| R-CTR-18 | SHOULD | §7.3 | Frame steps as production ("read X, produce Y"), not explora | [I] [X] |
| R-CTR-19 | MUST | §7.3 | Before any paid, external, or irreversible call: check the p | [R 03-voice] |
| R-CTR-20 | MAY | §7.3 | Table form `Artifact / Location / Format` , or list form `-  | [A] [P] [R] |
| R-CTR-21 | MUST (validation) | §7.3 | Every output is consumed by a downstream stage or is the fin | [R WB 02] |
| R-CTR-22 | SHOULD | §7.3 | Say that the output is the human's edit surface and the next | [A] [R] |
| R-CTR-23 | SHOULD | §7.3 | Each output starts with a header (§9.4). |  |
| R-CTR-24 | MUST | §7.3 | Exactly one human check per stage, stated as something a per | [A] |
| R-CTR-25 | SHOULD | §7.3 | Checkpoints and the Human check are different things. Checkp | [I reconciling R and A] |
| R-CTR-26 | SHOULD | §7.3 | The Human check names the reviewer (`Reviewer: analyst`, `Re | [EXT] |
| R-CTR-27 | SHOULD | §7.3 | where drift is possible | [P §6.2] [R] |
| R-CTR-28 | MUST | §7.3 | CONTEXT.md is routing, not content | [R Pattern 6] |
| R-CTR-29 | SHOULD | §7.3 | "If you find yourself writing more than a one-sentence descr | [R] |
| R-CTR-30 | MUST (validation) | §7.3 | Allowed content only: the elements in the table above, plus  | [R WB 05 check 6] [R voice-driven] |
| R-CTR-31 | MUST | §7.3 | Size per §3 (under 80 lines). Warning signs: more than 80 li | [O] [R] |
| R-CTR-32 | SHOULD | §7.3 | It doubles as human documentation (literate programming). | [P] |
| R-REF-01 | MUST | §7.5 | Under 200 lines. Split longer files. | [R] |
| R-REF-02 | MUST | §7.5 | Reference files hold the rules, definitions, examples, and t | [R] |
| R-REF-03 | MAY | §7.5 | "Write for machines, store for humans." | [O] [R] |
| R-REF-04 | SHOULD | §7.5 | Reference-file anatomy | [R] |
| R-REF-05 | SHOULD | §7.5 | Design-system references include (copy-and-adapt patterns),  | [R] |
| R-REF-06 | SHOULD | §7.5 | Reference values by semantic role, not literal value ("Roles |  |
| R-REF-07 | SHOULD | §7.5 | A downstream reference states its own latitude: what HOW dec | [R build-conventions] |
| R-REF-08 | MUST | §7.5 | Tool setup guides go in the `references/` of the stage that  | [R Pattern 7] |
| R-REF-09 | MUST | §7.5 | Brand and identity folders are READ-ONLY during runs: "It's  | [O] [R] |
| R-REF-10 | SHOULD | §7.5 | Use the person's real assets (their brand, their voice, thei | [PB Claude Design] |
| R-REF-11 | MAY | §7.5 | Closed registries | [R component-registry] |
| R-XREF-01 | MUST | §7.8 | "Every folder points outward to what it needs. No folder poi |  |
| R-XREF-02 | SHOULD | §7.8 | Before adding a reference, ask: "Does the target file alread |  |
| R-XREF-03 | MUST (validation) | §7.8 | The within-run dependency graph is a DAG. This keeps referen |  |
| R-XREF-04 | SHOULD | §7.8 | If B would need to point back at A, you probably need a thir | [O] |
| R-XREF-05 | MAY | §7.8 | A later stage reads an earlier stage's `references/` file in | [R] |
| R-CANON-01 | MUST | §7.8 | "Every piece of information has ONE home. Other files point  | [O] [R] |
| R-CANON-02 | SHOULD | §7.8 | Smell test: search the workspace for a specific phrase. "If  |  |
| R-CANON-03 | MAY | §7.8 | A pointer file can stand in for a copy: "This file is a poin | [R] |
| R-CANON-04 | SHOULD | §7.8 | When you remove a duplicate, leave a link where the copy was | [A] |
| R-CANON-05 | SHOULD | §7.8 | Map the information architecture before writing prompts: wha | [O] |
| R-ROUTE-01 | SHOULD | §7.8 | Any folder that grows past easy scanning gets its own `CONTE |  |
| R-ROUTE-02 | MUST | §7.8 | "Each level has its own small catalog, and no level's catalo | [A] |
| R-ROUTE-03 | SHOULD | §7.8 | A folder's `CONTEXT.md` says what does NOT belong there and  | [M] |
| R-STG-01 | MUST | §8.1 | One stage, one job | [A] [P] |
| R-STG-02 | SHOULD | §8.1 | Cut where the human naturally pauses | [A] |
| R-STG-03 | MUST | §8.1 | Surface the judgment call before the expensive work | [A] [P §4.3] |
| R-STG-04 | SHOULD | §8.1 | Give each stage a focused, scoped task, not "a monolithic in | [P §3.3] |
| R-STG-05 | SHOULD | §8.1 | Prefer tightly scoped stages: clear instructions, limited re | [P §5.4] |
| R-STG-06 | SHOULD | §8.1 | Mechanical steps that need no AI become scripts, called from | [P] |
| R-STG-07 | SHOULD | §8.1 | If two stages always run together with no review between the | [X] |
| R-STG-08 | INFO | §8.1 | Stages exist for optionality: "The AI can automate all four  | [PB 1.1] |
| R-STG-09 | SHOULD | §8.1 | Leave steps that are faster by hand to the human's tool ("a  | [PB 1.1] |
| R-STG-10 | SHOULD | §8.1 | Start short. Prove the pipeline on a small deliverable (a 30 | [PB 1.1] |
| R-STG-11 | SHOULD | §8.1 | Build reusable components and pattern libraries, so the agen | [PB 1.1] [R slide-patterns] |
| R-STG-12 | SHOULD | §8.1 | When a stage must produce variants for several targets, keep | [R platform-specs] |
| R-CHK-01 | MUST (validation) | §8.3 | At least one per creative stage (MUST (validation)). They ar |  |
| R-CHK-02 | MUST | §8.3 | "The agent completes a full unit of work, presents options o |  |
| R-CHK-03 | MUST | §8.3 | Table form: `After Step / Agent Presents / Human Decides`. S |  |
| R-CHK-04 | SHOULD | §8.3 | Good checkpoint patterns: |  |
| R-CHK-05 | INFO | §8.3 | A checkpoint is the implemented form of the paper's proposed | [I] [P §6.2] |
| R-AUD-01 | MUST (validation) | §8.5 | Creative, analytic, and build stages carry an Audit table `C |  |
| R-AUD-02 | MUST | §8.5 | The audit runs after the process and before writing to `outp |  |
| R-AUD-03 | MUST | §8.5 | "Each check should be specific enough that pass/fail is unam |  |
| R-AUD-04 | INFO | §8.5 | Audits are each stage's quality floor; they stop problems sp |  |
| R-AUD-05 | SHOULD | §8.5 | Values the agent computes are derived, never guessed, and th | [R 04-animate] |
| R-AUD-06 | SHOULD | §8.5 | Prove an audit works by planting a known error and confirmin | [X 4R] |
| R-QA-01 | SHOULD | §8.6 | The fix loop | [R] |
| R-QA-02 | SHOULD | §8.6 | Ship-ready definition | [R render-checklist] |
| R-QA-03 | MAY | §8.6 | Rigor by tier | [R] |
| R-QA-04 | SHOULD | §8.6 | Check where defects cluster ("Watch the first 5 seconds and  | [R] |
| R-QA-05 | SHOULD | §8.6 | Delivery package | [R] |
| R-QA-06 | SHOULD | §8.6 | Distribution (sending, posting, publishing) is a human act o | [EXT] |
| R-QUAL-01 | MUST NOT | §8.7 | Read previous `output/` files to learn patterns. Reference d |  |
| R-QUAL-02 | MAY | §8.7 | Curated exemplars are allowed | [I reconciling R and F] |
| R-QUAL-03 | MUST | §8.7 | Examples placed next to a rule agree with it, because "a mod | [X, crediting Jake's audit] |
| R-VAL-01 | SHOULD | §8.8 | Define the value types once, in a reference file. Examples:  |  |
| R-VAL-02 | SHOULD | §8.8 | Before the main creative work, at a checkpoint, lock which v |  |
| R-VAL-03 | SHOULD | §8.8 | The audit checks that the output delivers the locked slots.  |  |
| R-SPEC-01 | MUST | §8.9 | Spec stages define WHAT the output must achieve and WHEN thi |  |
| R-SPEC-02 | SHOULD | §8.9 | A spec, in the animation example, contains: |  |
| R-SPEC-03 | MUST NOT | §8.9 | A spec contains implementation choices that belong to the do |  |
| R-SPEC-04 | MUST | §8.9 | The split is "spec = WHAT/WHEN, design system = quality floo | [R] |
| R-SPEC-05 | INFO | §8.9 | The spec is "the most important file in the entire workflow. | [PB 1.1] |
| R-SPEC-06 | MUST | §8.9 | Do not under-specify either: "Writing 'show a diagram' witho | [PB 1.1, citing F 2.6] [R animation-guide] |
| R-CONST-01 | SHOULD | §8.10 | Configurable values (colors, fonts, timing, layout) live in  | [R] |
| R-CONST-02 | SHOULD | §8.10 | Non-code workspaces keep shared values in reference docs ins |  |
| R-CONST-03 | SHOULD | §8.10 | Do not hand-code what an existing package or skill already d | [R build-conventions] |
| R-EVID-01 | SHOULD | §8.11 | Gather a bounded set of primary sources (Jake uses 3 to 7).  |  |
| R-EVID-02 | MUST | §8.11 | Surface conflicts. "If two reputable sources publish differe |  |
| R-EVID-03 | MUST | §8.11 | "If no reputable source has the number you need, the script  |  |
| R-EVID-04 | SHOULD | §8.11 | Tag non-public sources `` "so the script writer can decide w |  |
| R-EVID-05 | SHOULD | §8.11 | Audience-fit audit: the output "assumes only what  Audience  |  |
| R-EVID-06 | SHOULD | §8.11 | Numbers in a report come from scripts or cited sources, neve | [M] |
| R-RUN-01 | MUST | §9.3 | Stage N writes `stages/NN_name/output/<slug>-<artifact>.md`, | [R Pattern 2] |
| R-RUN-02 | MUST (validation) | §9.3 | The handoff chain is unbroken: stage N's output location mat | [R] |
| R-RUN-03 | MUST | §9.3 | Each stage output is a complete, readable artifact that "cap | [P §3.3] |
| R-RUN-04 | MAY | §9.3 | The entry stage's metadata travels forward: each stage copie | [R] |
| R-RUN-05 | MAY | §9.3 | A stage reads more than its immediate predecessor (a validat | [EXT for siblings] [R] |
| R-RUN-06 | MUST | §9.3 | Every output goes to a named file in a named folder, never o | [F 4.2] |
| R-RUN-07 | SHOULD | §9.3 | Carry uncertainty forward. Each handoff artifact has an (or  | [R citation-format, render-checklist] |
| R-RUN-08 | MAY | §9.3 | Write an artifact with two faces when a machine and a human  | [R script-template, beat-markers] |
| R-RUN-09 | SHOULD | §9.4 | Each output starts with a small metadata header: title or sl | [R spec-format, script-templates, script-template] |
| R-RUN-10 | SHOULD | §9.4 | The header's `status` field carries approval state (§9.5). |  |
| R-RUN-11 | MAY | §9.4 | Mark revisions inside the artifact with a "What changed from | [R] |
| R-RUN-12 | MAY | §9.4 | The paper proposes a future practice: embed lightweight prov | [P §6.2, proposed] |
| R-STATE-01 | MUST | §9.5 | The `status` trigger scans `stages/*/output/`. A stage is CO | [R] |
| R-STATE-02 | MUST | §9.5 | "A placeholder that only keeps the empty folder in git does  | [A] |
| R-STATE-03 | MUST | §9.5 | In record and graph forms, status lives in frontmatter or a  | [A] |
| R-HUM-01 | MUST | §9.6 | "Nothing moves to the next stage until a person has read the | [A] |
| R-HUM-02 | MAY | §9.6 | At each gate the human may: proceed; edit the output file di | [P §5.3] |
| R-HUM-03 | SHOULD | §9.6 | Editing an output is "the primary way to steer the pipeline. | [R] |
| R-HUM-04 | MUST | §9.6 | Branching decisions belong to the human and are made between | [P] |
| R-HUM-05 | SHOULD | §9.6 | The U-curve | [A] [P §4.5] |
| R-HUM-06 | MUST | §9.6 | When an output is wrong, say what is wrong and iterate. "Sta | [F 4.2] |
| R-RUN-13 | SHOULD | §9.7 | Re-run only the stage that needs it. "If the research output | [P §6.1] |
| R-RUN-14 | MUST | §9.7 | A stage's Inputs table declares its dependencies. When any o | [O] [P] |
| R-RUN-15 | MUST | §9.7 | Flow is one-way: "Don't reverse-engineer earlier stages from | [O] |
| R-RUN-16 | MUST | §9.7 | Fix upstream, do not work around it downstream | [R beat-markers] |
| R-RUN-17 | INFO | §9.7 | Error recovery is a manual re-run of the failed stage. | [P] |
| R-RUN-18 | SHOULD | §9.8 | When the source of truth shifts along the pipeline, state it | [R pipeline-overview] |
| R-RUN-19 | SHOULD | §9.8 | Final and validation stages carry a "When to Loop Back" tabl | [R voice-driven 05-render] |
| R-RUN-20 | MAY | §9.9 | A stage MAY read a previous run's output (for example, last  |  |
| R-RUN-21 | MUST | §9.9 | Edges to earlier runs (run N-1 to run N) do not count agains |  |
| R-EDIT-01 | INFO | §9.10 | "Editing the output fixes this run. Editing the source fixes |  |
| R-EDIT-02 | SHOULD | §9.10 | One-off creative edits that cannot be reduced to a rule are  |  |
| R-EDIT-03 | SHOULD | §9.10 | Recurring edits are debugging information. Move a recurring  |  |
| R-EDIT-04 | SHOULD | §9.10 | When output is wrong, check the three possible sources: (a)  | [P §6.3] |
| R-EDIT-05 | SHOULD | §9.10 | "Every constraint you give is a mistake Claude will not make | [F 1.3] |
| R-EDIT-06 | INFO | §9.10 | The trajectory: "If workspaces improve their own source file | [P §6.3] |
| R-GIT-01 | INFO | §9.11 | A workspace is a folder. Copy it, git it, zip it, sync it. N | [P §3.4] |
| R-GIT-02 | SHOULD | §9.11 | Template repos gitignore stage outputs (`**/stages/*/output/ | [P] [R] |
| R-GIT-03 | INFO | §9.11 | Handing off a workspace means copying the folder. The recipi | [P] |
| R-GIT-04 | MAY | §9.11 | Several agent sessions may work in one folder, coordinated b | [PB 3.2] |
| R-GIT-05 | SHOULD | §9.11 | Confirm the workspace is tracked or backed up before any reo | [A reference-integrity] [EXT] |
| R-PH-01 | MUST | §10.1 | Setup placeholders are literal strings replaced by string su | [EXT] [R] |
| R-PH-02 | MUST NOT | §10.1 | Setup placeholders do not appear in any `CLAUDE.md`, in top- | [R] |
| R-PH-03 | MUST | §10.1 | What becomes a placeholder | [R script-to-animation-summary] |
| R-PH-04 | MUST NOT | §10.1 | Per-run template files (for example `shared/course-meta.md`) | [R] |
| R-PH-05 | MUST | §10.1 | A conditional block wraps an entire section: "a heading and  | [R] |
| R-PH-06 | SHOULD | §10.1 | Template-instantiation tokens (fields filled per record when | [EXT] |
| R-Q-01 | MUST | §10.2 | Flat structure |  |
| R-Q-02 | MUST | §10.2 | All at once |  |
| R-Q-03 | MUST | §10.2 | System-level only |  |
| R-Q-04 | MUST | §10.2 | Derive, do not ask |  |
| R-Q-05 | MUST (validation) | §10.2 | Sensible defaults |  |
| R-Q-06 | MUST | §10.2 | Ask once, never again | [A] [R] |
| R-Q-07 | MUST | §10.2 | Examples over descriptions | [A] [R] |
| R-Q-08 | MUST | §10.2 | A non-technical person can understand every question. | [R WB 04] |
| R-Q-09 | SHOULD | §10.2 | Optional stages and tools are yes/no questions: "If NO: Remo | [R] |
| R-Q-10 | MUST (validation) | §10.2 | Coverage |  |
| R-Q-11 | SHOULD | §10.2 | Two-pass review for derived voice rules |  |
| R-Q-12 | SHOULD | §10.2 | Question entry format |  |
| R-Q-13 | SHOULD | §10.2 | 's minimal five-question factory, whose answers are written  | [A] |
| R-SESS-01 | SHOULD | §11.1 | Keep a `PROGRESS.md` at the project root with these sections | [PB Stack 2.4] |
| R-SESS-02 | SHOULD | §11.1 | Start a session with "Read PROGRESS.md. What's the status? W | [PB Stack 2.4] |
| R-SESS-03 | SHOULD | §11.1 | Reconnect = orient, verify, continue | [PB Stack 2.4] |
| R-SESS-04 | SHOULD | §11.1 | Update progress before walking away, after any significant d | [PB Stack 2.4, 1.3] |
| R-SESS-05 | SHOULD | §11.1 | Record decisions with their reasons. The reason "is what sto | [X RyMac; consistent with PB] |
| R-SESS-06 | INFO | §11.1 | Built-in agent memory and workspace files are different laye | [PB 3.1] [PB Stack 2.4] |
| R-PLAN-01 | SHOULD | §11.2 | Decide, then build | [F 4.3] |
| R-PLAN-02 | SHOULD | §11.2 | In planning chats, start with what you are trying to accompl | [F 4.3] |
| R-PLAN-03 | SHOULD | §11.2 | The pre-build sequence | [PB 3.3] |
| R-PLAN-04 | SHOULD | §11.2 | A project takes under 10 prompts: about 4 to 5 for planning  | [PB 3.3] |
| R-PLAN-05 | SHOULD | §11.2 | The PRD is "stateful prompting": persistent context the agen |  |
| R-PLAN-06 | SHOULD | §11.2 | The build process | [PB Stack 1.1] |
| R-PLAN-07 | SHOULD | §11.2 | Client work: plan steps 1 and 2 during the discovery call. | [PB 3.3] |
| R-PLAN-08 | SHOULD | §11.2 | Visual feedback: "take screenshots of what you do not like,  | [PB 3.3] |
| R-PROMPT-01 | SHOULD | §12.2 | One clear ask per prompt | [F 1.3] |
| R-PROMPT-02 | SHOULD | §12.2 | Feed large inputs in order | [F 1.3] |
| R-PROMPT-03 | MUST | §12.2 | Be specific and name the output location | [F 4.2] [PB 1.3] |
| R-PROMPT-04 | MUST | §12.2 | Correct in place | [F 4.2] |
| R-PROMPT-05 | INFO | §12.2 | Claude Code's loop is . It is best for tasks that read and w | [F 4.2] |
| R-PROMPT-06 | SHOULD | §12.2 | When teaching a repeated task by demonstration, narrate the  | [PB 2.3] |
| R-PROMPT-07 | SHOULD | §12.2 | One model, three interfaces: Desktop or claude.ai (conversat | [F 4.1] |
| R-PROMPT-08 | SHOULD | §12.2 | Install tools and skills by pointing at their docs ("Help me | [PB 1.1] |
| R-SKILL-01 | MUST | §13.1 | Wire each skill into the rooms or stages that need it. Never | [F 3.1] [R] |
| R-SKILL-02 | MAY | §13.1 | Bundle skills into `skills/<name>/` (`SKILL.md`, optional `r | [R] |
| R-SKILL-03 | SHOULD | §13.1 | Discover skills during workspace design: scan `~/.claude/ski | [R] |
| R-SKILL-04 | SHOULD | §13.1 | Bundle a skill by copying it (local) or cloning it (remote)  | [R] |
| R-SKILL-05 | SHOULD | §13.1 | Load skills as "Index, then load rules as needed". "Claude d | [PB 1.1] [R] |
| R-SKILL-06 | SHOULD | §13.1 | When a skill covers the same ground as a custom reference do | [R] |
| R-SKILL-07 | SHOULD | §13.1 | Keep workspace-specific files (design system, brand, build c | [R] |
| R-SKILL-08 | MUST NOT | §13.1 | Do not bundle skills about the agent tool itself (skill-crea | [R] |
| R-SKILL-09 | SHOULD | §13.1 | For workspace-specific knowledge, use reference files rather | [O] |
| R-SKILL-10 | SHOULD | §13.1 | A named folder with its own context is already "the agent" f | [V] [X] |
| R-SKILL-11 | MAY | §13.1 | A workspace may point to a sibling workspace's skill instead | [R] |
| R-SCRIPT-01 | SHOULD | §13.2 | "Local scripts handle the mechanical work that does not need | [M] [P] |
| R-SCRIPT-02 | MUST | §13.2 | Run a dry run before any expensive or external call (`--dry- | [R] |
| R-SCRIPT-03 | MUST | §13.2 | Generated files (indexes, tables, numbers) come only from sc | [M] |
| R-SCRIPT-04 | SHOULD | §13.2 | Scripts live in `scripts/` or inside the skill that owns the | [EXT] |
| R-SCRIPT-05 | SHOULD | §13.2 | Script defaults state their reason: "We default to `medium.e | [R whisper-beat-finder] |
| R-TOOL-01 | SHOULD | §13.3 | Scope tool definitions to individual stages or rooms. Loadin | [F] [P §2.2] |
| R-TOOL-02 | SHOULD | §13.3 | External services come in through local scripts or MCP conne | [P] |
| R-SUB-01 | MAY | §13.4 | One orchestrating agent runs the pipeline. It MAY hand sub-t | [P §4.1, §4.2] |
| R-SUB-02 | SHOULD | §13.4 | Sub-agents and plan mode are tool features. The architecture | [I] [PB Stack 1.3] |
| R-SUB-03 | INFO | §13.4 | The method is model-agnostic: it specifies folder structure, | [M] [P] |
| R-SUB-04 | MAY | §13.4 | Use a small or local model for bulk mechanical building (ing | [M] [PB Claude Design] |
| R-SEC-01 | MUST | §13.5 | Secrets live in `.env` only, never in committed files. Confi | [R] |
| R-SEC-02 | SHOULD | §13.5 | Also gitignore `node_modules`, build output, and any private | [PB 3.2] |
| R-SEC-03 | SHOULD | §13.5 | Mark data with access limits. Examples: an `access_tier` fro | [A] [R] |
| R-SEC-04 | MUST | §13.5 | Keep each client's information in its own folder (R-T1-05). | [F 3.2] |
| R-SEC-05 | SHOULD | §13.5 | Review agent-filed files for personal data. In one case the  | [M] |
| R-SEC-06 | SHOULD | §13.5 | When inputs contain personal data (support tickets, customer | [EXT] |
| R-SKW-01 | MUST | §14.2 | Frontmatter | [A] |
| R-SKW-02 | SHOULD | §14.2 | Open with the method in one paragraph, plus one governing me | [A] |
| R-SKW-03 | SHOULD | §14.2 | State the invariants, or "the rules that make it good", as a | [A] |
| R-SKW-04 | SHOULD | §14.2 | Give a numbered procedure ("When you get a request: 1... 7.. | [A] |
| R-SKW-05 | MUST | §14.2 | Include a validation step before delivery: a walk test, rend | [A] |
| R-SKW-06 | SHOULD | §14.2 | Name the guardrails, and say honestly where the method loses | [A] |
| R-SKW-07 | SHOULD | §14.2 | End with a file index that says when to read each reference  | [A] |
| R-SKW-08 | SHOULD | §14.2 | Push depth down. SKILL.md stays one to a few screens. Refere | [A] [R] |
| R-SKW-09 | SHOULD | §14.2 | A tool-wrapping skill follows this shape: `## When to Use` ( | [R whisper-beat-finder] |
| R-SKW-10 | MAY | §14.2 | A skill may carry setup placeholders that the workspace's `s | [R] |
| R-SKW-11 | SHOULD | §14.2 | Commands are listed literally, with their flags, in a `## Co |  |

Total rules indexed: 313.

---

## A7. Sources and Coverage Notes

### A7.1 Primary sources

- Van Clief, J. & McDermott, D. (2026). *Interpretable Context Methodology: Folder Structure as Agent Architecture*. arXiv:2603.16021. https://arxiv.org/abs/2603.16021
- Van Clief, J., McDermott, D. & Kumar (2026). *The Cost of Remembering: Filesystem Memory Against Long Context on LongMemEval*. https://github.com/RinDig/cost-of-remembering
- https://github.com/RinDig/icm-architect
- https://github.com/RinDig/Interpretable-Context-Methodology
- https://github.com/RinDig/Content-Agent-Routing-Promptbase
- https://github.com/RinDig/lecture-deck-skill (skill-writing style)
- Clief Notes (Skool): https://www.skool.com/cliefnotes. Lesson text was read through community transcriptions and clippings: `donroy26/Clief-Notes-Foundations-Tutor` and `Naxxy/workspace-builder-skill/_design/skool-references/`.
- YouTube: https://www.youtube.com/@JEVanClief. Videos: "Stop Building AI Agents. Use This Folder System Instead."; "You're Automating The Wrong Layer"; "Stop Buying Agent Tools. Your Folders Already Do This."; "How a 1953 Word Game Explains AI Memory"; "How One Line of Python Triggers 12,000 Lines of Code"; "Clawdbot (Moltbot) Has 100K Stars. It Has Zero AI."
- Substack: https://jakevanclief.substack.com. Posts: "The Machine Is Smart."; "Augmenting Human Intellect"; "How One Line of Python Triggers 12,000 Lines of Code".

### A7.2 Coverage gaps (fill these later if access allows)

- No YouTube transcripts could be retrieved. Video content comes from Jake's written lesson companions (which say they cover the same ground) and from search snippets.
- Substack and Skool posts were seen only as search snippets.
- The "Abstraction Series" lessons (2.1 to 2.7: the Ladder, Video as Code, 60/30/10, Book / Movie / Video Game) and lesson 1.1 were recovered only as titles and headline ideas.
- Premium material (The Vault, including the "Building Your First Workflow End to End" course) and VIP material (The Drawing Room) was not accessible.
- The full text of the Ethics Engine paper (arXiv:2510.11742) was not retrieved; it is tangential to the method.
- Jake's own ICM audit, which a practitioner credits, was not located.
