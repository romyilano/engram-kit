# Pitfalls Research

**Domain:** AI-generated (ChatGPT) soft-color manga explainer comic — educational content, human-in-the-loop rendering
**Researched:** 2026-06-18
**Confidence:** MEDIUM-HIGH (image-model behavior = HIGH/stable & widely reproduced; ENGRAM facts = HIGH/from repo; exact prompt phrasings = MEDIUM/best-practice judgment)

> This is a **content project**, not a software build. The standard PITFALLS template's
> security / performance / integration / scale sections do not apply and have been
> replaced with the categories that actually bite an AI-image manga explainer:
> **visual consistency, text-in-image, panel layout, pedagogy/accuracy, factual history,
> and workflow**. Each pitfall maps to a *page-prompt phase*, not a software phase.

---

## Critical Pitfalls

### Pitfall 1: Mascot / character drift across separate generations

**What goes wrong:**
"Engy" (the librarian-robot) and the narrator-sensei look different on every page — chest
notebook changes shape, robot becomes humanoid then mechanical, sensei's age/outfit/hair
shifts, proportions wander. Each ChatGPT image generation is an independent roll; the model
does not "remember" what Engy looked like two prompts ago even within one chat, and reliably
forgets entirely in a fresh session.

**Why it happens:**
ChatGPT image generation re-synthesizes from text each time. A short character reference
("a robot librarian") underspecifies thousands of degrees of freedom, so the model fills them
differently every run. Authors assume the chat "remembers" the character — it does not, in a
stable, reproducible way.

**How to avoid:**
- Write a **frozen Character Bible block** once (Engy + sensei) with concrete, countable
  attributes: body type, exact colors with names, head/eye shape, the chest-notebook's look,
  height ratio between the two, default expression. Paste this *verbatim* into **every** page
  prompt. Treat it as a constant, never paraphrase it.
- Lock specifics that models otherwise randomize: number of fingers/segments, eye style
  (e.g. "two round cyan LED eyes, no mouth"), notebook = "a spiral-bound notebook embedded
  flush in the chest panel labeled in the caption, not in-image."
- Generate **one canonical reference page first**, save it, and in later sessions attach/paste
  that image as a visual anchor where ChatGPT supports image input ("match this character
  exactly"). Image-conditioning holds character far better than text alone.
- Keep the cast **small** (2 recurring characters). Every additional recurring character
  multiplies drift surface.

**Warning signs:**
Side-by-side pages where Engy's silhouette differs; the notebook migrating around the body;
sensei aging or changing gender/outfit; color names in the prompt not matching what rendered.

**Phase to address:** Character/Style Bible phase (before any content page) + every page-prompt phase re-states it.

---

### Pitfall 2: Style & color-palette drift (the soft-color look wanders)

**What goes wrong:**
Page 1 is soft watercolor pastel; page 7 comes back high-saturation cel-shaded; page 12 looks
like 3D render or photoreal. Line weight, screentone, and background treatment vary, so the set
doesn't read as one comic.

**Why it happens:**
Same root cause as character drift, plus: vague style words ("manga style," "anime") map to a
huge range. Different sessions/days and even small wording changes nudge the model into a
different visual basin. Adding rich *content* description can crowd out the style tokens.

**How to avoid:**
- Pin a **Style Block** alongside the Character Bible: medium ("soft watercolor manga,
  light cel shading"), palette (3–5 named hues + "muted, low saturation, lots of white space"),
  line ("thin clean black ink lines"), and mood. Repeat verbatim every page.
- Name the palette in plain color words, not hex (image chat ignores hex reliably); e.g.
  "pale sky blue, warm cream, soft coral, light sage, charcoal lines."
- Keep the Style Block phrasing **identical** across pages — don't rephrase it per page even
  if it feels repetitive. Stable tokens = stable output.
- Specify aspect ratio and "single illustration, flat 2D, no photographic rendering" to keep
  pages from drifting into 3D/photoreal.

**Warning signs:**
Saturation jump between saved pages; backgrounds going from flat wash to detailed rendering;
the set not feeling cohesive when thumbnails are laid out in a grid.

**Phase to address:** Character/Style Bible phase; verified at a mid-project "lay out all saved pages" review.

---

### Pitfall 3: Garbled / misspelled text rendered inside the image

**What goes wrong:**
ChatGPT renders `update STATE_DIR MEMORY_DIR` as `updaet STATE_DRI MEMROY`, speech bubbles
contain dream-language gibberish, and key terms (`MEMORY_DIR`, `answer`, `no hindsight`) come
out misspelled — fatal for an *explainer* whose whole job is teaching exact commands and terms.

**Why it happens:**
Image models generate text as visual texture, not as typed characters. Accuracy collapses with
longer strings, code, underscores, and anything technical. Even when one word is right, a second
generation re-garbles it. This is the single highest-risk failure for a *technical* explainer.

**How to avoid:**
- **Minimize in-image text by design.** The prompt should ask for *near-textless* panels:
  visual metaphors, arrows, icons, empty speech bubbles or blank caption bars.
- **Leave deliberate space for hand-added captions/labels.** Instruct: "leave a clean empty
  caption band along the bottom" and "empty speech balloons" — the author types real text later
  (image editor, slide, or layout tool). This makes correctness *guaranteed* instead of hoped-for.
- For the few words that **must** appear in-image, keep them to 1–3 short plain-English words,
  and still verify every render character-by-character; regenerate or plan to overlay if wrong.
- **Never** ask the model to render the literal commands / file paths / JSON as image text.
  Render them as a stylized "terminal card" *shape* with a blank screen, and overlay the real
  monospace text afterward.

**Warning signs:**
Any visible misspelling; underscores/slashes mangled; bubbles full of fake glyphs; the author
tempted to "just let the AI write the label."

**Phase to address:** Style/layout-convention phase (establish "blank bubbles + caption band" rule) — applies to every page, most critically the two-commands and rules pages.

---

### Pitfall 4: Oversimplifying ENGRAM until the explanation is wrong

**What goes wrong:**
To make it friendly, a page says something subtly false: "ENGRAM remembers everything,"
"the AI predicts the future," "memory = a database you query," or it blurs `STATE_DIR` and
`MEMORY_DIR` into one "memory." The reader ends up confidently misunderstanding the system.

**Why it happens:**
Simplification pressure + a cute mascot makes "close enough" feel fine. The core ENGRAM ideas
are precise and easy to round off: **no hindsight** (no future states, no answer keys),
**two distinct surfaces** (STATE_DIR = current bounded workspace = read-only-ish input;
MEMORY_DIR = your persistent writable memory), and **cite evidence / distinguish
current vs stale vs superseded vs uncertain**.

**How to avoid:**
- Anchor each content page to a **single load-bearing true fact** from `CONTRACT.md` /
  `README.md`, and write that fact in plain language *before* writing the prompt. The mascot
  dramatizes the fact; it must not contradict it.
- Keep the **two surfaces visually distinct and never merged**: STATE_DIR as the world/desk
  Engy reads; MEMORY_DIR as Engy's own notebook she writes. One image, two clearly different
  objects.
- Preserve the non-negotiables even when simplifying: *no future states*, *no answer keys/
  rubrics*, *answer from current state + memory*, *cite evidence paths*, *4 info states
  (current / stale / superseded / uncertain)*. These can be drawn simply but must stay true.
- Sanity-check each page caption against the repo wording; if the mascot metaphor forces a
  false statement, change the metaphor, not the fact.

**Warning signs:**
A caption you couldn't defend against `CONTRACT.md`; "future"/"predict" language; STATE_DIR and
MEMORY_DIR depicted as the same object; "answer key" implied to be available.

**Phase to address:** Core-idea + two-commands + rules content phases (the must-land pages).

---

### Pitfall 5: Cramming too much per page / too many panels

**What goes wrong:**
A page tries to teach update *and* answer *and* the four info-states *and* submission, with 6–9
tiny panels. The image model merges panels, drops some, garbles the now-tiny text, and the
reader is overwhelmed — the idea fails to "click," which is the project's whole purpose.

**Why it happens:**
"One page per concept" feels efficient, and explainer scope creep is natural. But image models
degrade fast with panel count: more panels = smaller elements = worse text, worse character
fidelity, merged/blurred gutters, unreliable count (ask for 4, get 3 or 5).

**How to avoid:**
- **One concept per page.** If a page needs "and," split it into two pages.
- Cap panels at **2–4 per page**, large and clearly gutter-separated. Explicitly state the
  count and layout ("3 panels in a vertical strip, clear white gutters between them").
- Push detail into the *sequence of pages* (15+ pages is the plan) rather than into one dense
  page. Pages are cheap; clarity is the product.

**Warning signs:**
A prompt with a long "panel 1… panel 6…" list; panels rendering merged or miscounted; you
can't state the page's one takeaway in a single sentence.

**Phase to address:** Page-sequencing / outline phase (allocate one idea per page) + every page-prompt phase.

---

### Pitfall 6: Wrong reading order / merged panels in multi-panel pages

**What goes wrong:**
Panels render but flow ambiguously — Western left-to-right vs manga right-to-left confusion,
no clear gutters so two panels blur into one, or numbered steps appear out of sequence, so the
update→answer→cite logic reads scrambled.

**Why it happens:**
Image models have weak control over precise panel grids and reading order; "manga" can trigger
right-to-left flow inconsistently. Without explicit layout direction the model improvises.

**How to avoid:**
- Specify layout and direction explicitly: "**3 stacked horizontal panels, read top to bottom**,
  thick white gutters." Vertical strips are far more reliable than 2×2 grids for ordering.
- Prefer **top-to-bottom vertical** sequencing (unambiguous in any reading culture) over
  left-right rows; pick one direction and use it on every multi-panel page for consistency.
- Reinforce order with **non-text cues** the author can't misread later: directional arrows,
  big numbered circles (1,2,3 — short enough to often render, but plan to overlay if garbled).
- When ordering is critical (the two-command contract), consider **one concept = one single-panel
  page** instead of a multi-panel page.

**Warning signs:**
Missing gutters; ambiguous flow; arrows pointing the wrong way; you have to explain the order to
a test reader.

**Phase to address:** Layout-convention phase + the two-commands and how-to-compete pages.

---

### Pitfall 7: Prompts that aren't self-contained (break in a fresh ChatGPT session)

**What goes wrong:**
A page prompt says "same character and style as before" or "continue the comic" — meaningless in
a new chat or on another day. The render comes back off-model, and the page set fractures.

**Why it happens:**
The workflow is explicitly "paste each prompt into ChatGPT, one page at a time," possibly across
many sessions/days. Authors lean on conversational context that doesn't persist. ChatGPT sessions
don't carry reliable visual memory across resets.

**How to avoid:**
- Make **every spike prompt fully standalone**: it must contain the entire Character Bible +
  Style Block + layout rules + this page's content, with **zero references** to "previous,"
  "above," or "as before."
- Adopt a fixed prompt skeleton per page: `[Style Block]` → `[Character Bible]` →
  `[Layout rules]` → `[This page's scene + blank bubbles/caption band]`. The first three are
  copy-paste constants.
- Treat redundancy as a *feature*: yes, the style/character text repeats on all 15+ pages — that
  repetition is what buys cross-session consistency.

**Warning signs:**
The word "previous/above/before/continue" in a prompt; a prompt that renders fine right after
another page but wrong from a cold session.

**Phase to address:** Prompt-template / spike-format phase (define the standalone skeleton) — enforced on every page.

---

### Pitfall 8: Losing track of which page maps to which saved image

**What goes wrong:**
After 15+ manual generations, saved files are `image (4).png`, `download-7.png`; the author can't
tell which prompt produced which graphic, can't re-render a fixed page, and assembly order is lost.

**Why it happens:**
Manual save = browser default filenames + no link back to the spike. Order lives only in the
author's head and degrades over a multi-session project.

**How to avoid:**
- **Zero-padded, ordered naming** tied to the spike: `page-01-core-idea.png` saved *next to*
  its prompt spike (`.planning/spikes/page-01-core-idea/`). The spike folder holds both prompt
  and image, as PROJECT.md already intends.
- Keep a single **manifest** (page number → title → spike path → saved-image filename →
  status: drafted/rendered/text-overlaid/approved). One source of truth for sequence and progress.
- Embed the page number/title in the spike front matter so a saved image is always traceable to
  its prompt even if the filename slips.

**Warning signs:**
Default download filenames; uncertainty about page order; inability to find the prompt that made
a given image; "which version is final?" questions.

**Phase to address:** Spike-format / project-scaffolding phase + an ongoing manifest updated each render.

---

## Moderate Pitfalls

### Pitfall 9: Jargon creep for a non-expert audience

**What goes wrong:** Pages use `STATE_DIR`, `MEMORY_DIR`, "ingest," "ticks," "no-hindsight,"
"superseded" without ever grounding them visually, so the first-time reader bounces.
**Why it happens:** The source repo is dense with terms; it's easy to inherit its vocabulary.
**How to avoid:** Introduce **one term per page**, always paired with a concrete visual
(MEMORY_DIR = Engy's notebook; STATE_DIR = the desk/world she reads). Use plain words in captions
("what's true now" vs "what used to be true") and treat the literal identifier as a *label on the
drawn object*, not as prose. Defer "superseded/stale/uncertain" until a dedicated info-states page.
**Phase to address:** Outline phase (term-introduction order) + each content page.

### Pitfall 10: Misleading metaphors

**What goes wrong:** The mascot metaphor implies something false — e.g. Engy "memorizes
everything" (ENGRAM is bounded, cites evidence, distinguishes stale), or the notebook = a search
engine that fetches the future.
**Why it happens:** Cute metaphors over-promise; the librarian framing can imply omniscient recall.
**How to avoid:** Pick metaphors that *encode the constraints*: a librarian who can only file
what's been released so far (no future shelves), who writes dated notes, and who marks entries
"outdated/replaced/unsure." The metaphor should make the *rules* obvious, not hide them.
**Phase to address:** Character/metaphor-design phase + rules page.

### Pitfall 11: Inconsistent panel aspect ratio / page size across the set

**What goes wrong:** Some pages render square, some portrait, some landscape — the saved set won't
assemble into a clean comic.
**How to avoid:** Pin one **page aspect ratio** (e.g. portrait) in the Style Block on every prompt
and verify each save matches before moving on.
**Phase to address:** Style block phase.

---

## Factual Pitfalls — the 2020→present AI-memory history pages

These pages are the **highest hallucination risk** in the project, because the mascot can't save
you from a wrong date or invented product. Confidence on the *risk* is HIGH; the *facts
themselves must be verified at write-time* (web research was unavailable in this pass — flag for
the history-page phase).

| Easy-to-get-wrong claim | The pitfall | How to keep it safe |
|---|---|---|
| Exact release **years/months** of papers, models, frameworks (RAG, vector DBs, long-context models, MemGPT/Letta, etc.) | Image+chat will confidently state wrong dates | Verify every date against a primary source at write-time; prefer "around 2023" / "mid-2020s" over false precision when unsure |
| "**X invented** memory / RAG / vector search" | Origin/attribution claims are often wrong or contested | Avoid superlatives ("first/invented/pioneered"); say "popularized" or "an early widely-used approach" |
| Naming **specific products/companies** | Names misremembered or conflated; some may be defunct | Name a *category* (vector database, agent-memory framework) and give at most one well-verified example per category |
| "**Solved**" / "memory is now solved" framing | Overstates the state of the art; ENGRAM exists *because* it isn't solved | Frame history as *progression of approaches*, ending at "open problem → that's why ENGRAM" |
| Drawing **logos / real product UIs** in-image | Brand inaccuracy + text-garbling + trademark awkwardness | Use generic icons (a vector cube, a scroll for long context, a notebook for agent memory), never real logos |
| Implying a clean **linear timeline** | History was parallel/overlapping, not a single line | Show overlapping approaches; "these coexist," not "A replaced B" |

**Prevention rule for the history section:** write the **caption text first as verified prose**,
cite the source in the spike, *then* build the (near-textless) image prompt around it. The image
illustrates a vetted sentence; it never sources the fact.

**Phase to address:** Dedicated AI-memory-history research+content phase (research before drawing).

---

## "Looks Done But Isn't" Checklist

Per-page verification before marking a page approved:

- [ ] **Character:** Engy + sensei match the Bible (silhouette, colors, chest-notebook) — compare to canonical reference, not from memory.
- [ ] **Style:** palette/line/medium match the set; aspect ratio correct; not drifted to 3D/photoreal.
- [ ] **In-image text:** every visible word spell-checked character-by-character; commands/paths/JSON are **not** rendered as image text (blank terminal card + overlay instead).
- [ ] **Caption space:** the empty caption band / blank bubbles are actually present for hand-added text.
- [ ] **Panel order:** reading direction unambiguous; gutters clear; panels not merged; count correct.
- [ ] **Accuracy:** the page's one fact is defensible against `CONTRACT.md`/`README.md`; STATE_DIR ≠ MEMORY_DIR; no "future"/"answer key"/"solved" language.
- [ ] **History pages:** every date/name/claim traced to a verified source in the spike.
- [ ] **Standalone:** prompt has no "previous/above/before"; renders correctly from a cold session.
- [ ] **Traceability:** saved as `page-NN-slug.png` beside its spike; manifest updated.

---

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
|---|---|---|
| Garbled in-image command/term | LOW | Don't fight the model — switch that page to blank bubble/terminal card + overlay real text in an editor. |
| Character/style drift on one page | LOW–MEDIUM | Re-render with the verbatim Bible/Style block; attach the canonical reference image; if still off, regenerate (cheap). |
| Whole set drifted (palette/character) over many pages | HIGH | Re-pin the Bible/Style block, pick a canonical reference, re-render the off-model pages in a batch session for consistency. |
| Wrong/merged panels | LOW | Re-render as a vertical strip with explicit count + gutters, or split into single-panel pages. |
| Oversimplified-to-wrong content | MEDIUM | Rewrite the verified caption first, change the metaphor (not the fact), re-render. |
| Wrong history fact already drawn | MEDIUM | Fix the verified prose, regenerate the near-textless image, re-overlay caption. |
| Lost prompt↔image mapping | MEDIUM | Rebuild the manifest from spike folders; rename saved files to `page-NN-slug.png`. |

---

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
|---|---|---|
| Mascot/character drift | Character/Style Bible (foundation) | Lay saved pages in a grid; silhouettes match |
| Style/palette drift | Character/Style Bible | Grid review; consistent palette & aspect ratio |
| Garbled in-image text | Layout-convention (blank-bubble rule) | No misspellings; commands overlaid, not rendered |
| Oversimplified-to-wrong | Core-idea / two-commands / rules content | Each caption defensible vs CONTRACT.md |
| Too much per page / panel count | Outline / page-sequencing | One stateable takeaway per page; ≤4 panels |
| Reading order / merged panels | Layout-convention + key contract pages | Unambiguous top-to-bottom flow, clear gutters |
| Non-standalone prompts | Prompt-template / spike-format | Cold-session render test; no "previous/above" |
| Lost page↔image mapping | Scaffolding + manifest (ongoing) | Manifest complete; `page-NN-slug` naming |
| Jargon creep | Outline (term order) + each page | One term per page, each visually grounded |
| Misleading metaphor | Metaphor-design + rules page | Metaphor encodes constraints, not omniscience |
| History factual errors | AI-memory-history research+content | Every date/name/claim cited in spike |

---

## Sources

- Repo source of truth (HIGH): `CONTRACT.md`, `README.md`, `PROJECT.md` — ENGRAM mechanics, the
  two surfaces, boundary rules, four info-states, no-hindsight.
- Image-model behavior (HIGH, stable/widely reproduced characteristics of current diffusion &
  GPT-image generation): independent per-generation synthesis (drift), unreliable in-image text
  rendering (especially code/underscores/long strings), weak panel-grid/reading-order control,
  inconsistent requested panel counts, no reliable cross-session visual memory.
- Prompt phrasings & process rules (MEDIUM, best-practice judgment for this workflow): verbatim
  Bible/Style blocks, blank-bubble + caption-band strategy, vertical-strip ordering, standalone
  prompt skeleton, manifest + zero-padded naming.
- **Gap flagged:** live web verification was unavailable this pass. The 2020→present AI-memory
  history facts (dates, names, attributions) **must be verified against primary sources during
  the history-page phase** — do not draw from memory.

---
*Pitfalls research for: AI-generated manga explainer (ChatGPT, human-in-the-loop) for the ENGRAM memory challenge*
*Researched: 2026-06-18*
