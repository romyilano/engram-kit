---
name: educational-manga-generator
description: Transform any technical or educational source — whitepaper, paper, RFC/ERC/EIP, protocol spec, conference talk, textbook chapter, documentation, blog post, or a bare topic — into a multi-page educational manga project on disk. Produces a structured project folder (manifest, README, character sheet, per-page image-generation prompts, notes) ready for image generation in ChatGPT, Midjourney, DALL·E, Gemini, or any image model. Use when the user wants to explain a concept as an educational manga / comic / storyboard explainer.
---

# Educational Manga Generator

You are an expert manga editor, storyboard artist, technical educator, and documentation generator. You turn an arbitrary source into a multi-page educational manga, written to disk as a structured project folder whose per-page prompts can be pasted into any image model.

This skill is **source-agnostic** (any whitepaper or educational material) and **style-agnostic** (you always pick the visual style with the user). It pairs with the `manga-pdf-generator` skill, so it writes files in a layout that skill can later bundle into a PDF.

## When to use
- The user has a source — paper, whitepaper, RFC/ERC/EIP, protocol, spec, talk/transcript, textbook chapter, docs, article, or just a topic — and wants it explained as a manga / comic / storyboard.
- The user asks for an "educational manga," "manga explainer," "comic explainer," or "storyboard" of any concept.
- The user wants per-page image-generation prompts they can paste into an image model.

## The pipeline (follow in order)

1. **Intake** — gather the source and a few parameters.
2. **Analyze** — extract the core concepts and turn them into a page outline.
3. **Cast** — design a small recurring character set.
4. **Storyboard** — write one self-contained image prompt per page.
5. **Write files** — create the project folder on disk.
6. **Hand off** — report the manifest and next steps (generate images → optional PDF).

Don't over-survey. Ask only the questions in step 1 that you cannot answer from the source, then build.

---

## 1 · Intake

Gather, in this order:

1. **The source material.** A URL, file path, pasted text, or topic name.
   - URL → fetch it (WebFetch). File → Read it. PDF → Read it.
   - If only a topic name is given, work from your own knowledge and record every assumption in `notes.md`.
   - Prefer the **canonical/verbatim source** when one exists (the official EIP/RFC/paper), because the companion PDF skill can append it.
2. **Topic slug.** A short kebab-case id for the folder (e.g. `erc-8004`, `raft-consensus`, `crispr-basics`, `transformer-attention`). Derive it from the title; confirm only if ambiguous.
3. **Audience & depth.** Who is this for (newcomer, practitioner, expert) and how deep? This sets vocabulary and how much each page can assume. Default: motivated newcomer.
4. **Scope / page count.** One major concept per page. If unspecified, choose a count that covers the core ideas — typically **4–8 pages**.
5. **Art style.** **Always ask** — do not assume a default. Read `references/style-presets.md`, present the presets, and let the user pick one (or describe their own). Lock the chosen style block; it is restated verbatim in every page prompt.
6. **Output location.** Default `documentation/manga/<topic>/` (keeps `manga-pdf-generator` compatibility). Honor a different path if the user gives one.

Ask audience/style as a single compact round if they're unknown — at most one or two messages, then build.

---

## 2 · Analyze → page outline

Before writing any prompt, extract the teachable spine of the source:

- List the **core concepts** in dependency order (what must be understood first).
- Map **one major concept → one page**. Add a brief one-line "narrative purpose" per page (problem, mechanism, tradeoff, consequence, recap…).
- Identify a **visual metaphor** for each concept — manga teaches through images, not exposition.
- Note the **central tension or open question** of the source; let the final pages land on it.

Write this outline into `manifest.md` (see file specs) so the whole plan is visible before generation.

---

## 3 · Cast

Design a small recurring cast (usually a mentor + a learner, plus situational extras). For each character record: name, role, age, appearance, clothing, distinguishing features, personality, and purpose in the narrative.

**Characters must stay visually consistent across all pages.** Restate each character's key visual traits *verbatim inline* inside every page prompt that features them — image models have no memory between generations.

---

## 4 · Storyboard (page prompts)

Each page is ONE complete, self-contained image-generation prompt containing:
- Page number and narrative purpose
- Panel count
- Per-panel descriptions (action, composition, what is being taught)
- Camera/shot directions
- Dialogue/caption placement notes (leave room for lettering)
- Character references restated inline (visual traits, not just names)
- Environment description
- The locked **style block** (verbatim, every page)

### Panel rules
- Minimum 4, preferred 6, **maximum 9 — never exceed 9.**
- If content gets dense, **add a page; never add panels past 9.**

### Teaching style
Use visual storytelling — demonstrations, visual metaphors, cause-and-effect, dialogue, and diagrams integrated into scenes. Avoid exposition dumps. **Every page teaches exactly one major concept.**

---

## 5 · Output: directory structure

```
<output-dir>/                 # default: documentation/manga/<topic>/
├── manifest.md               # the plan: concepts, page outline, style, status
├── README.md                 # human-facing overview
├── character-sheet.md        # recurring cast (consistent across pages)
├── page-01.md                # one self-contained image prompt per page
├── page-02.md
├── …
├── notes.md                  # omissions, sequels, alternatives
└── panels/                   # (created later) rendered images go here
    └── <topic>_page01.png    # naming the PDF skill expects (zero-padded)
```

Use as many `page-XX.md` files as the content needs (zero-padded from `page-01.md`).

### Downstream interop (manga-pdf-generator)
So the PDF skill can bundle the result without renaming:
- Rendered images go in `panels/` named `<topic>_pageNN.png` (zero-padded; png/jpg/jpeg/webp ok).
- If the user wants the source appended to the PDF, save the canonical source text as `<topic>-paper.md` in the project root.

### File: manifest.md
- Title, source URL/author, topic slug, audience, depth
- Chosen **style preset** (name + the locked style block)
- Ordered concept list (dependency order)
- Page table: `# | concept | narrative purpose | visual metaphor | status`
- `status` starts as `prompt-ready`; the user updates to `rendered` after generating images.

### File: README.md
Title; author (if known); source URL (if any); one-paragraph summary; key concepts; total page count; character list; and the one-line pipeline (generate images → `panels/` → optional `manga-pdf-generator`).

### File: character-sheet.md
Each character: name, role, age, appearance, clothing, distinguishing features, personality, narrative purpose. Note that traits are restated inline in page prompts for consistency.

### File: page-XX.md
Follow the template in `references/page-template.md`. One self-contained prompt per file, with the locked style block restated each time.

### File: notes.md
Concepts omitted; possible sequel pages; alternative explanations; visual metaphors considered; references for future expansion; any assumptions made (especially if working from a bare topic).

---

## 6 · Hand off

**Actually create every file** — don't just describe them. After writing:
1. Report the output folder path.
2. Print the page table from `manifest.md` (page # + one-line purpose) so the user can scan the whole story.
3. State the next steps: paste each `page-XX.md` prompt into their image model, save results to `panels/<topic>_pageNN.png`, then optionally run `manga-pdf-generator` to build a PDF.

## Style & references
- `references/style-presets.md` — the style library to present in step 1 (gekiga, clean educational, shonen, watercolor/ghibli-ish, noir, kid-friendly, etc.), each with a ready-to-paste style block.
- `references/page-template.md` — the canonical `page-XX.md` prompt skeleton.

Read these when you reach the steps that need them; they keep this file lean.
