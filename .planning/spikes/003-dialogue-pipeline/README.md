---
spike: 003
name: dialogue-pipeline
type: standard
validates: "Given the existing documentation/manga/*/page-NN.md lettering blocks, when parsed, then a structured VN script (scene → speaker + text + panel background) is auto-extractable, so VN authoring isn't from scratch."
verdict: VALIDATED
related: [001, 002]
tags: [pipeline, parsing, content, authoring]
---

# Spike 003: Dialogue Pipeline

## What This Validates

**Given** the 15 existing `documentation/manga/{alma,ama-bench}/page-NN.md` files — each with a
`Lettering:` block of `- Panel N — Speaker: "line"` entries — **when** parsed, **then** a
structured VN script (per page: background panel + ordered speaker/text lines) is auto-extractable.
This answers the authoring-cost question: the dialogue for the VN is *already written* as a
byproduct of the manga, so the real build adapts content instead of authoring it from scratch.

## Research

No external libraries — pure Node string parsing. The only "research" was characterizing the
source format by inspection:

- Dialogue lines are **bulleted** (`- Panel N — …`); non-bulleted `Panel N — LABEL:` lines are
  *panel descriptions* inside the image prompt and must be excluded.
- Two speaker forms: named (`Sensei: "…"`, colon-delimited) and captions (`(caption) "…"`, no
  colon). The first `: ` is the speaker/text split for named lines; captions are matched separately
  because their text can contain internal colons.
- Markdown emphasis `*word*` maps to the engine's `<em>` green-emphasis convention.
- The em dash is `—` (U+2014); the regex also tolerates `–`/`-`.

## How to Run

```bash
cd .planning/spikes/003-dialogue-pipeline
node extract.js          # parses all 15 pages -> script.json + script.js
open play.html           # plays the auto-extracted ALMA book (no server needed)
```

`extract.js` reads from the repo's real manga markdown, writes `script.json` (both books, the proof
artifact) and `script.js` (`window.VN_SCRIPT` for ALMA — a `window` global so `play.html` opens via
`file://` with no fetch/CORS). `play.html` runs the Spike 001 engine over the generated script.

## What to Expect

Extractor output:

```
book        page  lines  speakers
alma        01    6      sensei,engy,narrator
...
ama-bench   07    6      sensei,engy,narrator
TOTAL       15    87     across 2 books
```

`play.html`: the full 8-page ALMA story plays as a VN — Engy, Sensei, Meta Agent, and narrator
captions, each over its page's panel, typed out in the brand style — entirely from content that
already existed in the repo. The HUD shows `auto-extracted · page NN`.

## Investigation Trail

1. **Exclusion first.** A naive `Panel N —` match swept up panel *descriptions* (`Panel 1 — SAMPLE:`,
   `Panel 4 — IMPLEMENT:`) which are art directions, not dialogue. Restricting to **bulleted** lines
   (`^- Panel`) cleanly separated lettering from prompt scaffolding.
2. **Captions broke the colon split.** `(caption) "Four very different worlds: real and synthetic."`
   has an internal colon, so "split on first `: `" mis-parsed it. Added a dedicated `(caption)`
   branch (speaker → `narrator`, no colon expected) ahead of the named-speaker split.
3. **Yield.** 87 dialogue lines across all 15 pages, 2 books, with correct speaker attribution
   (Engy 22+, Sensei 24+, Examiner 8, Meta Agent 9, captions as narrator). All 8 ALMA backgrounds
   resolve to real panel PNGs — verified headlessly.
4. **One genuine edge case (1/87).** `ama-bench/page-05` Panel 4 packs *two* speakers and a stage
   direction into one lettering line:
   `Engy: "Um... it was always open?" (wrong) — Examiner: "Incorrect."`
   The parser keeps the first speaker and over-captures the rest. **This is a content shape, not a
   parser bug** — and notably that line is *already a comprehension checkpoint written in prose*,
   which is exactly the Spike 002 pattern. Signal: a handful of "dual-utterance" lines want a tiny
   authoring convention (one utterance per bullet) or a manual touch-up pass.

## Results

**Verdict: VALIDATED.** Existing manga lettering is a usable VN script source.

- **87 lines / 15 pages / 2 books parsed automatically**, ~99% clean (1 line needs touch-up).
  The VN does **not** start from a blank page — the dialogue is a byproduct of the manga already
  shipped.
- The generated `script.js`/`script.json` shape (`{bg, page, speaker, label, text}`) is exactly the
  flat array the Spike 001/002 engine consumes — the three spikes compose into one pipeline:
  **markdown lettering → `extract.js` → `script.js` → VN runner (+ 002 checkpoints).**
- Backgrounds map deterministically: page `NN` → `<book>_pageNN.png`, all resolve.
- **Carries into the real build:** (a) adopt a "one utterance per `- Panel` bullet" lettering
  convention so extraction stays lossless; (b) the per-page panel granularity is coarse (one image
  per page, not per panel) — fine for a VN, but a future enhancement could slice panels for
  per-beat backgrounds; (c) checkpoints (002) are authored *on top of* the extracted script, not
  parsed from it.
