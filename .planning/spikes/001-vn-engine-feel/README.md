---
spike: 001
name: vn-engine-feel
type: standard
validates: "Given the existing manga panels + ENGRAM//KIT brand, when a player clicks through a VN scene (panel background, name plate, typewriter dialogue, click-to-advance, branching choice), then it feels like a real visual novel and runs on the static site with zero build."
verdict: VALIDATED
related: [002, 003]
tags: [vn, ui, brand, static-site]
---

# Spike 001: VN Engine Feel

## What This Validates

Given the existing ALMA manga panels and the ENGRAM // KIT brand, **when** a player clicks
through a VN scene — panel background, character name plate, typewriter dialogue, click/space to
advance, and a branching choice that changes what happens next — **then** it feels like a real
visual novel and runs on the `docs/` static site with **zero dependencies and no build step**.

## Research

### Build vs. buy — VN engines surveyed

| Approach | Tool | Pros | Cons | Status |
|----------|------|------|------|--------|
| Hand-roll | vanilla HTML/JS | Zero deps, opens via `file://`, full ENGRAM//KIT brand control, reuses panels + flipbook CSS, ~250 lines total | We write the scene runner (typewriter, branching, choices) | **Chosen** |
| Web VN engine | [Monogatari](https://monogatari.io/) | Save/load, scene DSL, menus, character system built-in | npm/build + bundle, restyle to brand, heavy vs a flipbook-adjacent page | Rejected — overweight for a static `docs/` add-on |
| Hypertext | [Twine/Harlowe](https://twinery.org/) | Great for branching prose, no-code authoring | Not panel/portrait-first, awkward to brand, exports its own runtime | Rejected — wrong shape (prose, not panel-VN) |
| Native VN | [Ren'Py](https://www.renpy.org/) (web export) | Industry-standard VN features | Python→web export is a heavy artifact, not a `docs/` page; overkill | Rejected — not web-native |

**Chosen approach:** hand-rolled vanilla JS. The deciding constraints are the existing
zero-build static site, the need for exact brand control (recall-green, Helvetica, mono labels),
and that the hard assets (panels, dialogue) already exist in-repo. A VN runner is a small amount
of code; an engine is a large amount of integration. Locked as a Requirement in MANIFEST.md.

## How to Run

Open the file directly in a browser — no server needed:

```bash
open .planning/spikes/001-vn-engine-feel/index.html
```

Click or press **space/enter** to advance. First click finishes the typewriter; second advances.
At the branch, pick **A** or **B** — the next two lines differ, then both paths converge.
Top-right: **log** shows the forensic event stream; **export** downloads `spike001-log.json`.

## What to Expect

- A 16:9 letterboxed stage with an ALMA panel as the (desaturated) background.
- A recall-green skewed name plate (ENGY / SENSEI) or a quiet uppercase NARRATION label.
- Dialogue typed out character-by-character with a blinking green caret; `<em>` words render green.
- A branch ("How should we give Engy memory?") with two styled choices that change Sensei's reply.
- "Recall" beats warm the background to full color (the `lit` flag) on the it-worked lines.
- An end card with Replay.

## Observability

Forensic log layer: every `boot / bg / line / choice-shown / choice / replay / end / export`
event is timestamped (seconds since load). The **export** button downloads a JSON with a summary
(event count, duration, per-category counts) + the full event list — so a playthrough is
reconstructable without watching over the user's shoulder.

## Investigation Trail

1. **First cut** — scenes as a flat array of `{bg, speaker, text}`; typewriter via `setTimeout`
   per character. Felt right immediately; the panels carry the production value.
2. **Typewriter vs. markup** — naive per-character typing split `<em>` tags mid-tag and broke
   the green emphasis. Fixed by tokenizing on `/(<[^>]+>)/` and emitting whole tags in one step
   so markup stays intact while text reveals char-by-char.
3. **Branching** — added `{choice}`, `{tag}`, `{goto}` nodes. **Bug caught by simulation before
   any browser test:** `findTag` originally required a node to have `bg||s||end`, so the bare
   `{tag:'converge'}` merge marker returned `-1` and the handcraft branch's `{goto:'converge'}`
   would crash on `SCRIPT[-1]`. Relaxed `findTag` to match the tag alone; the bare marker is then
   skipped by the existing marker-advance guard in `render()`.
4. **Headless branch check** — re-implemented the navigation in Node over the same script shape
   and played both choices with a 100-step infinite-loop guard. Both terminate and converge:
   - `HANDCRAFT → panel 3 → merge → panel 6 → panel 7 → END`
   - `META → panel 4 → merge → panel 6 → panel 7 → END`

## Results

**Verdict: VALIDATED** (logic, paths, and branching verified headlessly; final "feel" is a
human playtest — open the file).

- A complete, branded, branching VN scene is **~250 lines of one HTML file, zero dependencies**,
  and opens with `file://`. This comfortably fits alongside the existing `docs/` flipbook.
- The existing panel PNGs do the heavy visual lifting; the engine only needs dialogue chrome.
- Branching + convergence works and is cheap to author (tag/goto markers in a flat array).
- **Surprise / signal:** the desaturate-at-rest, warm-on-recall treatment (reused straight from
  the brand's "near-grayscale → full tone on hover" rule) maps perfectly onto VN emotional beats —
  the background literally lights up when Engy remembers. That's a brand-native learning cue, free.
- **Carries into 002:** the `{choice}` node is already the seam where a *comprehension checkpoint*
  (not just a flavor branch) plugs in. **Carries into 003:** the flat `{bg, s, t}` script shape is
  exactly what a parser would emit from the `page-NN.md` lettering blocks.
