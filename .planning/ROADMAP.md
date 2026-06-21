# ROADMAP — ENGRAM Kit

Phases are sequential. Status: ✅ complete · 🚧 in progress · ⬜ not started.

---

## Milestone v2 — Whitepaper Mangas & ENGRAM // KIT Brand Identity

**Goal:** Explain the two agentic-memory whitepapers in [`documents/`](../documents/)
as soft-color educational mangas, and give the project a stark, Cargo-grade **ENGRAM
// KIT** brand identity with a manga-first GitHub Pages site — modeled on the
`frontier_tower/20260620_ecommerce` reading-pack project. Ship the markdown prompts +
labeled placeholders first; the author drops real ChatGPT panels in later.

**Source papers:**
- **ALMA** — *Learning to Continually Learn via Meta-learning Agentic Memory Designs* (arXiv 2602.07755)
- **AMA-Bench** — *Evaluating Long-Horizon Memory for Agentic Applications* (arXiv 2602.22769)

**Success criteria for the milestone:**
1. Both whitepaper mangas exist as complete per-page prompt projects (manifest, README, character sheet, pages, notes, source paper) in the layout the `manga-pdf-generator` skill expects. ✅
2. A consistent series — shared Engy + Sensei cast, one locked soft-color style block. ✅
3. A written brand spec + a self-demonstrating styleguide that renders the live tokens. ✅
4. A manga-first GitHub Pages site (landing + flipbook for both books) that works today on placeholders and sharpens when real panels land. ✅
5. The manga skills are vendored so the repo is self-contained. ✅
6. v2 is recorded in the GSD framework (PROJECT.md + this roadmap). ✅

---

### Phase 1 — Vendor the manga skills ✅
**Goal:** Make the repo self-contained for manga production.
- Copy `educational-manga-generator`, `manga-pdf-generator`, `socratic-reading` from the ecommerce project into `.claude/skills/`.
- **Done:** all three skills present under `.claude/skills/`.

### Phase 2 — ALMA whitepaper manga (markdown) ✅
**Goal:** An 8-page soft-color explainer of ALMA as per-page image prompts.
- `documentation/manga/alma/`: `manifest.md`, `README.md`, `character-sheet.md`, `page-01.md … page-08.md`, `notes.md`, `alma-paper.md`.
- Cast: Engy, Sensei, the Meta Agent, the Archive. Centerpiece: the open-ended Meta-Agent loop (page 4).
- **Done.** Panels are labeled placeholders pending generation.

### Phase 3 — AMA-Bench whitepaper manga (markdown) ✅
**Goal:** A 7-page soft-color explainer of AMA-Bench as per-page image prompts.
- `documentation/manga/ama-bench/`: `manifest.md`, `README.md`, `character-sheet.md`, `page-01.md … page-07.md`, `notes.md`, `ama-bench-paper.md`.
- Cast: Engy, Sensei, the Examiner, the Long Road/Trajectory. Four QA categories (page 4); causality graph (page 6).
- **Done.** Panels are labeled placeholders pending generation.

### Phase 4 — ENGRAM // KIT brand identity ✅
**Goal:** A new identity distinct from `AGENTIC//COMMERCE`, same caliber.
- `docs/BRAND.md` (written spec) + `docs/brand-guidelines.html` (renders live tokens).
- Tokens in `docs/assets/css/cargo.css`: monochrome + rationed recall-green `#00e0a4` (+ deep green for text on light), stale-amber `#d98a3d` for stale/superseded, Helvetica, the `//` mark.
- **Done.**

### Phase 5 — GitHub Pages site ✅
**Goal:** Manga-first reading-pack site, modeled on the ecommerce `docs/`.
- `index.html` (hero, ticker, manga showcase, panel strip, two papers, the challenge contract, compete), `flipbook.html` + `flipbook.js` (multi-book: `?book=alma` / `?book=ama-bench`), `style.css`, `site.js`, `README.md`, `.nojekyll`.
- Placeholder panels + per-manga and combined placeholder PDFs so every link resolves.
- **Done.**

### Phase 6 — GSD wiring ✅
**Goal:** Record v2 in the framework.
- `PROJECT.md` updated (milestones table, What This Is, v2 Active requirements, Key Decisions, footer).
- This `ROADMAP.md` created.
- **Done.**

---

### Outstanding (human-in-the-loop, outside this milestone's automation)
- ⬜ **Generate real panels** in ChatGPT from each `page-XX.md` prompt → save over `panels/<topic>_pageNN.png`.
- ⬜ **Rebuild PDFs** with the `manga-pdf-generator` skill once real panels exist (it can append the `*-paper.md` sources).
- ⬜ **Enable GitHub Pages** (Settings → Pages → `main` / `/docs`).

---

## Requirement coverage (v2 Active → phase)

| Requirement (PROJECT.md, v2) | Phase |
|------------------------------|-------|
| ALMA whitepaper manga | Phase 2 ✅ |
| AMA-Bench whitepaper manga | Phase 3 ✅ |
| Shared Engy + Sensei cast / locked style | Phases 2–3 ✅ |
| ENGRAM // KIT brand identity | Phase 4 ✅ |
| GitHub Pages site | Phase 5 ✅ |
| Manga skills vendored | Phase 1 ✅ |
| Placeholder panels + PDFs | Phases 2–5 ✅ |
