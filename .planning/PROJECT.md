# ENGRAM Manga Explainer

## What This Is

A soft-color **manga comic that explains the ENGRAM memory-system challenge** in a way that is easy to understand. It turns the abstract concepts in this repo (the `update`/`answer` contract, `STATE_DIR`/`MEMORY_DIR`, no-hindsight rules) plus a short history of memory in AI/agentic systems (2020→present) into a sequence of narrated explainer-panel pages. The deliverable is a set of **ChatGPT image prompts — one prompt per page** — stored as GSD spikes; the author pastes each prompt into ChatGPT, generates the page, and saves the graphic manually.

This is an **educational / content project**, not a software build. The existing ENGRAM Kit is the *source material* being explained, not the thing being modified.

## Core Value

After reading the finished manga, a non-expert understands **what ENGRAM is and how a memory system answers questions without hindsight** — the idea finally "clicks" visually. If everything else is cut, the core-idea + two-commands pages must land.

## Requirements

### Validated

(None yet — generate prompts, render in ChatGPT, save graphics to validate that they actually make ENGRAM click)

### Active

- [ ] A recurring **mascot + visual language** is defined once and reused in every page prompt for consistency (mascot = "Engy", a librarian-robot whose notebook chest is MEMORY_DIR; a narrator-sensei explains the mechanics)
- [ ] Page prompts explain **the core idea** — ENGRAM is a memory system that ingests dated workspace states over time and answers without hindsight
- [ ] Page prompts explain **the two-command contract** — `update STATE_DIR MEMORY_DIR` and `answer STATE_DIR MEMORY_DIR QUESTION_JSON ANSWER_JSON`, and what each surface means
- [ ] Page prompts explain **the challenge rules** — no future states, no answer keys, cite evidence paths, distinguish current/stale/superseded/uncertain info
- [ ] Page prompts explain **how to compete** — what a participant builds, the submission folder + `run.sh`, and how `check_submission.py` validates it
- [ ] Page prompts cover a **history of memory in AI/agentic systems, 2020→present** (researched for factual accuracy — RAG, vector DBs, long context, agent memory, etc.)
- [ ] All prompts produce a consistent **soft-color manga** look (light watercolor/anime palette) suitable for saving page by page
- [ ] Each page's prompt is **stored as a GSD spike** under `.planning/spikes/`, with room to drop the saved graphic alongside it
- [ ] Full first pass is **15+ pages**, sequenced as a coherent explainer

### Out of Scope

- **Modifying the ENGRAM Kit code** (`check_submission.py`, the contract, sample states) — this project explains the kit, it does not change it
- **Auto-generating the images programmatically** (API image generation) — the author generates in ChatGPT and saves graphics manually by choice
- **A character-driven plot/story** — chosen format is narrated explainer panels, not a narrative arc
- **Print layout / typesetting / lettering tooling** — out of scope for the first pass; prompts target single page images
- **Building an actual ENGRAM submission** (a real memory system) — separate effort; this is the explainer only

## Context

- **Source material lives in this repo** and is already mapped in `.planning/codebase/`. Key inputs for accurate manga content:
  - `CONTRACT.md` — the two-command interface (authoritative)
  - `STATE_FORMAT.md`, `QUESTION_FORMAT.md`, `SUBMISSION_FORMAT.md` — the data surfaces and JSON shapes
  - `README.md` — the framing of ENGRAM as a time-sequence memory challenge
  - `examples/simple_memory/` and `check_submission.py` — what a submission and validation look like
- **Author's goal is comprehension.** The author finds the kit and its context hard to understand; the manga is a tool to make it click. Clarity beats cleverness on every page.
- **Workflow is human-in-the-loop:** GSD produces the prompt (spike) → author pastes into ChatGPT → author saves the rendered page manually. The project never calls an image API.
- **History section needs research** to be accurate across 2020→present (RAG, vector stores, long-context models, agent memory frameworks like MemGPT/Letta, etc.).

## Constraints

- **Tooling**: Image generation is **ChatGPT, manual** — prompts must be self-contained, copy-paste ready, and reproducible page to page (re-state the mascot/style block in each prompt so a fresh ChatGPT session stays consistent).
- **Consistency**: Soft-color manga style + the "Engy" mascot must be **pinned once and repeated** in every prompt; drift between pages is the main quality risk.
- **Accuracy**: ENGRAM mechanics must match the kit exactly (commands, file surfaces, rules). The history timeline must be factually grounded, not hallucinated.
- **Storage**: Prompts are **GSD spikes** under `.planning/spikes/`, one per page, leaving space to save the graphic next to its prompt.
- **Audience**: Non-expert / first-time reader — minimize jargon; define terms visually.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Output is ChatGPT image prompts, not rendered images | Author renders + saves manually; GSD's job is high-quality, consistent prompts | — Pending |
| One prompt per page (multi-panel page) | Author's chosen packaging; easier to save page by page | — Pending |
| Format = narrated explainer panels (not story) | Clearer for technical flow; author chose this over character-driven plot | — Pending |
| Soft-color manga style, pinned in every prompt | Friendly + approachable; re-stating style block prevents page-to-page drift | — Pending |
| Recurring mascot "Engy" (notebook = MEMORY_DIR) + narrator-sensei | Makes abstract memory concepts physical and visual; author asked me to design it | — Pending |
| Store each page prompt as a GSD spike | Fits the GSD workflow already in use; keeps prompt + saved graphic together | — Pending |
| Research the 2020→present AI-memory history before writing those pages | Timeline must be factually accurate, not invented | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-06-18 after initialization*
