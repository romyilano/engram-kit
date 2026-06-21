# Stack Research — Tooling & Prompt Craft

**Domain:** Multi-page soft-color manga "explainer" comic, rendered by hand in ChatGPT image generation (no API)
**Researched:** 2026-06-18
**Confidence:** MEDIUM-HIGH (based on Jan-2026 knowledge of ChatGPT's GPT-4o native image model; live web verification tools were unavailable this session — see Sources / Confidence notes)

> **Tooling note:** This is a content project, not a software build. There is nothing to `npm install`. The "stack" here is the **image-generation engine + the prompt-craft technique set** the author uses to render consistent pages by hand. Headings below are adapted accordingly.

---

## Recommended Stack

### Core Technologies (the rendering engine + the technique that pins consistency)

| Technology / Technique | "Version" | Purpose | Why Recommended |
|------------------------|-----------|---------|-----------------|
| **ChatGPT native image generation (GPT-4o image model, a.k.a. `gpt-image-1`)** | The default image generator in ChatGPT since the March-2025 rollout that replaced DALL-E 3 | Renders each manga page from a text prompt + optional uploaded reference image | It is the tool the author has chosen and has by far the **best in-image text rendering** and **best reference-image conditioning** of the ChatGPT-accessible models. DALL-E 3 (the old engine) could not reliably ingest a reference image for character consistency; the GPT-4o model can. **HIGH confidence this is the right and only sensible engine inside ChatGPT.** |
| **Reference-image conditioning (upload "Engy" + a sample page, ask to match)** | n/a | Keeps the mascot and palette consistent across separate generations | The single most reliable consistency lever. Once you have ONE good Engy + ONE good page you like, **re-upload them as references on every subsequent page** and instruct "match this character and this art style exactly." Beats text description alone. **HIGH confidence.** |
| **Restated "Style + Character Block" prepended to every page prompt** | n/a | Makes each page prompt self-contained so a *fresh* ChatGPT session reproduces the look | The author's workflow re-pastes into new sessions; conversation memory cannot be relied on. A verbatim block (palette hex-ish description, line weight, mascot spec) restated every time is what prevents drift. **HIGH confidence — this is the project's core constraint.** |
| **Character reference sheet (a "model sheet" page generated first)** | n/a | A canonical Engy turnaround (front/side, expressions) used as the master reference | Standard comic/animation practice. Generate it as **Page 0**, lock it, and reference it forever. **HIGH confidence.** |

### Supporting Techniques (use as needed, page by page)

| Technique | Purpose | When to Use |
|-----------|---------|-------------|
| **Single reference image per generation, not many** | Avoids the model "averaging" several conflicting references | Always prefer 1 (mascot sheet) — or at most 2 (mascot + a style-exemplar page). More than ~2 references degrades fidelity. |
| **Minimal baked-in text + "leave space for captions"** | Sidesteps the model's text-rendering weakness | Whenever a page would need more than a few short words. Ask for **empty narration boxes / blank speech bubbles**, then the author adds text later (or accepts short labels only). |
| **Explicit panel grid description ("2x2 grid, read left-to-right, top-to-bottom")** | Controls multi-panel layout + reading order | Every multi-panel page. State panel count, arrangement, gutter color, and reading direction in words. |
| **"Western reading order, left-to-right" instruction** | Prevents right-to-left manga paneling confusion | Always (this is an explainer for a Western dev audience even though the *style* is manga). |
| **Regenerate-and-pick, then edit in place** | Iterates toward a keeper without losing consistency | After a good base page, use ChatGPT's "edit this image / change only X" follow-ups rather than re-rolling from scratch. |
| **Aspect-ratio request (e.g. "portrait page, 2:3 / tall comic page")** | Consistent page dimensions across the set | Every page — state the same ratio each time so the saved set is uniform. |
| **Fixed seed value** | Would pin randomness | **NOT available in the ChatGPT UI.** Listed here only to say: do not rely on it; the API exposes seeds, ChatGPT does not. Consistency must come from references + restated blocks. |

### Author Tools (the human-in-the-loop side)

| Tool | Purpose | Notes |
|------|---------|-------|
| ChatGPT (web or desktop app) | Generate + iteratively edit each page | Desktop/web makes uploading the reference image and downloading the result easiest. |
| Local image folder beside each spike | Save the rendered PNG next to its prompt | Matches the project's "store prompt as GSD spike, drop graphic alongside" constraint. |
| (Optional) Any basic image editor / Canva / Figma | Add real caption + bubble text *after* rendering | Recommended given text-rendering limits — see "What NOT to rely on." Out of first-pass scope per PROJECT.md, but the cleanest path to legible text. |

---

## The Copy-Paste Prompt Skeleton

This is the load-bearing deliverable. Prepend the **Style + Character Block** to every page; fill the **Page Block** per page. Designed to drop into a fresh ChatGPT session with the Engy model-sheet image attached.

```
[Attach: engy-model-sheet.png  +  (optional) a previously-approved page you like]

STYLE + CHARACTER BLOCK — keep IDENTICAL on every page:

Art style: soft-color manga / light-anime "explainer panel" illustration.
Gentle watercolor-style shading, soft cel coloring, clean thin black ink
outlines, rounded friendly shapes. Pastel palette: soft sky-blue, warm
cream paper background, muted teal, soft coral accents. Bright, calm,
approachable, educational — NOT dark, NOT gritty, NOT photorealistic.
Match the attached reference image's colors, line weight, and rendering exactly.

Recurring mascot "Engy": a small friendly librarian-robot. Rounded white-and-
soft-blue body, large kind circular eyes, a little antenna. On Engy's CHEST
is an open notebook/ledger that represents MEMORY_DIR (visibly labeled space
for dated entries). Engy looks the same on every page — same proportions,
same colors, same face. Use the attached model sheet as the source of truth.

Secondary character "Sensei": a calm narrator-teacher figure who explains
mechanics, gesturing toward diagrams. Same soft-manga style.

Page format: tall portrait comic page, 2:3 aspect ratio, cream paper
background, thin dark panel borders with soft white gutters. Western reading
order: left-to-right, top-to-bottom. Keep any text SHORT and leave clean
empty space inside narration boxes and speech bubbles for captions to be
added later. Do not crowd the page with small text.

----------------------------------------------------------------
PAGE BLOCK — fill in per page:

Page title (concept being taught): <<e.g. "The Two Commands">>
Panel layout: <<e.g. 2x2 grid, four equal panels>>
Panel 1: <<what Engy/Sensei do, what diagram/object appears>>
Panel 2: <<...>>
Panel 3: <<...>>
Panel 4: <<...>>
Narration boxes (keep words minimal, large legible space): <<short labels only>>
Mood: warm, clear, "this just clicked" feeling.

Generate this as ONE single manga page image matching the Style + Character
Block and the attached reference exactly.
```

**Usage rules (give these to whoever writes the page spikes):**
1. **Always attach the locked Engy model sheet.** Text-only restatement drifts; the image anchor is what holds the character.
2. **Restate the whole Style + Character Block verbatim every page** — never "same as before," because a fresh session has no memory.
3. **Keep baked-in text to a few short words.** Treat the model as a *layout + art* engine, not a typesetter.
4. **Generate Page 0 first** (the Engy model sheet) and freeze it before any story page.

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| ChatGPT GPT-4o image model (in-UI) | Midjourney + `--cref` (character reference) | If the author moved off ChatGPT. Midjourney's character-reference and style-reference flags give stronger consistency, but it is a different tool and violates the project's "ChatGPT, manual" constraint. Don't switch for the first pass. |
| Reference image + restated block | Pure text-description-only consistency | Only if no reference can be attached (e.g. quick thumbnail). Expect noticeable drift. |
| Minimal in-image text, add captions after | Fully baked-in lettering by the model | Acceptable only for very short labels (1–3 words). For sentences, render blank and letter afterward. |
| Multi-panel single image (one page = one generation) | One panel per generation, composite later | Use per-panel generation if a specific page keeps failing as a grid, or if you need pixel-clean text per panel. Costs more manual compositing; out of first-pass scope. |

---

## What NOT to Use / NOT to Rely On

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| **Seeds for reproducibility in ChatGPT** | The ChatGPT UI does not expose a seed control (only the API does). | Reference image + verbatim restated style block. |
| **Relying on conversation memory for consistency** | The author re-pastes into fresh sessions; prior context is gone. | Self-contained prompt with the block restated + reference attached every time. |
| **Long paragraphs of text baked into the image** | Even the much-improved GPT-4o model still garbles longer text, mangles small fonts, and misspells under density. | Short labels only; add real caption/bubble text in an editor afterward. |
| **Many reference images at once (4+)** | The model averages/blends them, weakening both character and style fidelity. | One mascot sheet, optionally plus one style-exemplar page. |
| **Right-to-left "authentic manga" paneling** | Confuses a Western dev audience reading an explainer. | Explicitly request left-to-right, top-to-bottom reading order. |
| **DALL-E-3-era assumptions** ("it can't do text / can't take a reference") | Outdated since the March-2025 GPT-4o image rollout; text + reference are now usable. | Treat the current model as reference-capable and short-text-capable, but still not a typesetter. |
| **Dense, tiny-panel pages (6+ panels)** | Each extra panel shrinks detail and multiplies text/character drift. | 2–4 panels per page; split concepts across more pages instead. |

---

## Technique Patterns by Variant

**If a page is concept-heavy with lots of narration:**
- Use 2–3 large panels, generate with **blank narration boxes**, and letter the text afterward in an editor.
- Because: legibility of the explanation matters more than baked-in text, and the explainer's whole point is comprehension.

**If a page is a simple "hero moment" (e.g. the core-idea reveal):**
- Single large panel or splash, Engy front-and-center, one short caption.
- Because: the two must-land pages (core idea + two commands) deserve maximum visual clarity and minimal clutter.

**If Engy starts drifting after several pages:**
- Re-anchor: open a fresh session, attach the locked model sheet AND your best recent page, and say "match both exactly."
- Because: drift compounds when you keep referencing slightly-off outputs; always reference the *locked originals*, not the latest result.

**If a multi-panel grid keeps failing (wrong panel count, merged panels):**
- Fall back to one-panel-per-generation and composite manually.
- Because: the model's grid control is good but not perfectly deterministic; per-panel is the reliable escape hatch.

---

## "Version Compatibility" (capability assumptions to verify before writing pages)

| Assumption | Status | Notes |
|-----------|--------|-------|
| ChatGPT uses the GPT-4o native image model (reference-capable, decent text) | HIGH confidence as of Jan 2026 | Verify the author's account is on the current image generator, not a legacy DALL-E path. |
| Reference-image upload conditions the output | HIGH | Core to the whole consistency plan; confirm on Page 0 + Page 1 before committing to 15 pages. |
| No seed control in the UI | HIGH | Plan does not depend on seeds. |
| Short in-image text renders acceptably | MEDIUM | Spell-check every rendered label; expect to fix some by hand. |
| Multi-panel single-image pages work | MEDIUM | Validate the grid approach on an early page; per-panel fallback exists. |

---

## Sources

- **Author's `.planning/PROJECT.md`** — project constraints (ChatGPT-manual, mascot "Engy", soft-color manga, one prompt per page, restate-the-block requirement). HIGH confidence (primary source).
- **Model knowledge of ChatGPT's GPT-4o native image generation rollout (March 2025, replacing DALL-E 3)** — capabilities re: reference images, in-image text, no UI seed. MEDIUM-HIGH confidence; **live web verification was unavailable this session** (WebSearch/WebFetch disabled), so confirm current UI behavior on the first 1–2 rendered pages before scaling to 15.
- **Standard comic/animation production practice** (model sheets, locked references, left-to-right reading order) — HIGH confidence, stable domain knowledge.

> **Recommended verification step before the full 15-page run:** generate Page 0 (Engy model sheet) and one real page, confirm (a) reference upload holds the character, (b) the restated block reproduces in a fresh session, and (c) short labels render legibly. These three checks de-risk the entire roadmap. If any fails, escalate to the "add text afterward" / "per-panel composite" fallbacks already specified above.

---
*Stack research for: ChatGPT-rendered soft-color manga explainer (prompt-craft, no API)*
*Researched: 2026-06-18*
