# Spike Conventions

Patterns and stack choices established across spike sessions. New spikes follow these unless the
question requires otherwise.

## Stack

- **Vanilla HTML/CSS/JS, zero dependencies, no build step.** Every spike is a single `.html` file
  (plus optional Node `.js` tooling) that opens via `file://`. This matches the project's `docs/`
  static site and its GitHub Pages deployment — no npm, no bundler, no framework.
- **Node** (v24) for content tooling only (parsing/codegen), never as a runtime dependency of the
  playable artifact.
- Rationale: the real target is a GitHub Pages add-on next to the existing flipbook. Anything that
  needs a build contradicts that. Locked in Spike 001 (build-vs-buy survey rejected Monogatari /
  Twine / Ren'Py for this reason).

## Structure

- One directory per spike: `.planning/spikes/NNN-name/`.
- Playable demo is always `index.html` (or `play.html` when a generator feeds it).
- VN backgrounds reference the real shipped panels by relative path:
  `../../../docs/manga/<book>/panels/<book-prefix>_pageNN.png` (three levels up from the spike dir).
  ALMA prefix `alma_`, AMA-Bench prefix `amabench_`.
- Generated content is emitted as a `window` global in a `script.js` (`window.VN_SCRIPT = […]`) so
  the player loads it with `<script src>` — avoids `file://` fetch/CORS entirely. JSON twins
  (`script.json`) are written alongside as the human-readable proof artifact.

## Patterns

- **VN script = flat array of nodes.** `{bg, speaker, text}` for lines; `{choice}` / `{tag}` /
  `{goto}` for branching; `{quiz}` for comprehension checkpoints; `{end}`. The engine walks the
  array; branching jumps by tag. ~250 lines of JS total for the full runner.
- **Typewriter that preserves markup:** tokenize on `/(<[^>]+>)/`, emit whole tags in one step and
  text char-by-char, so `<em>` (green emphasis) survives the reveal.
- **Brand-native learning cue:** backgrounds sit desaturated/dim at rest and warm to full color on
  "it-worked / recall" beats (the `lit` flag) — reusing the brand's "near-grayscale → full tone on
  hover" rule as an emotional/learning signal.
- **Diegetic checkpoints:** quizzes are administered by an in-world character (the **Examiner**),
  with per-distractor corrective feedback and retry — never a generic modal popup. Wrong answers
  block advance but teach; first-try-correct vs. total-attempts is the mastery signal.
- **Speaker name plates by role:** green skewed plate for characters, amber (`--stale`) for the
  Examiner, paper-white for the Meta Agent, quiet uppercase label for narration/captions.
- **Forensic log layer in every interactive spike:** `LOG[]` with seconds-since-load timestamps,
  category tags, an on-screen toggle, and an **export** button that downloads JSON with a summary
  (event counts, duration, and — for learning spikes — a `{checkpoints, passed, firstTryCorrect,
  totalAttempts}` block).

## Tools & Libraries

- **None.** No runtime packages. Brand tokens are copied inline from `docs/BRAND.md`
  (`--ink #0b0b0d`, `--paper #f3f1ec`, `--signal #00e0a4`, `--stale #d98a3d`, Helvetica, mono for
  labels/commands). Keep the palette and the `//` mark consistent with the site.
- Content source of truth for dialogue: `documentation/manga/<book>/page-NN.md` `Lettering:` blocks.
  Authoring convention to preserve lossless extraction: **one utterance per `- Panel N — Speaker:`
  bullet** (avoid packing two speakers into one line).
