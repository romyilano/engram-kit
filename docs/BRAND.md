# Brand Identity — *ENGRAM // KIT*

A stark, typographic, lab-grade identity for the ENGRAM memory challenge and its
two whitepaper mangas. It borrows the Cargo.site discipline of the v1 reading-pack
identity but trades the warm editorial look for a **terminal / archive** aesthetic:
monochrome, Helvetica, and a single rationed **recall-green**.

> **Living guidelines:** this file is the written spec. The visual,
> self-demonstrating styleguide — which renders the real tokens, type scale, and
> components — lives at [`brand-guidelines.html`](brand-guidelines.html). When the
> system changes, update `assets/css/cargo.css`, the guidelines page, and this
> file together.

## Positioning

> **The memory that answers without hindsight.**

ENGRAM is staged like a lab notebook: dated states arrive in order, memory is
written, questions are answered without peeking ahead. The manga is the headline
act — it pushes to the very top of the page as the hero; the challenge spec is the
catalogue underneath.

## Voice

- Declarative, short, confident. Lowercase nav, uppercase structural labels.
- Curatorial captions ("The Forgetful Robot", "The Causality Graph").
- No emoji in body copy; arrows (→ ↓ ▶) and the `//` mark used as quiet wayfinding.
- Mechanics are stated exactly: `update`, `answer`, `STATE_DIR`, `MEMORY_DIR`.

## Logotype

`ENGRAM//KIT` set in **Helvetica Neue**, heavy weight, tight tracking (`-0.02em`),
all caps. The double slash `//` is the brand mark — it reads as a path separator
(state // memory) and as the gap between *what happened* and *what is remembered*.
It is always recall-green. Use `//` standalone at favicon / avatar scale.

## Typography

- **Display + UI:** Helvetica Neue / Helvetica / Arial. One family, many weights.
  No serif. Big, tight, confident.
- **Display scale:** `clamp(2.6rem, 11vw, 10.5rem)` for hero; outlined oversized
  numerals for section indices (`01 / 02`).
- **Body:** Helvetica at 1.05–1.15rem, line-height 1.55.
- **Labels:** uppercase, `letter-spacing: 0.22em`, 0.7rem.
- **Code / mechanics:** monospace (`--mono`) for commands and file surfaces.

## Colour

| Token          | Hex       | Use                                            |
|----------------|-----------|------------------------------------------------|
| `--ink`        | `#0b0b0d` | Backgrounds, type on light                     |
| `--paper`      | `#f3f1ec` | Light backgrounds, type on dark                |
| `--paper-2`    | `#e7e4dc` | Section banding, recessed panels               |
| `--signal`     | `#00e0a4` | Recall-green accent — memory, recall, `answer` |
| `--signal-deep`| `#06a079` | Signal-coloured **text** on light (keeps AA)   |
| `--stale`      | `#d98a3d` | Muted amber — ONLY for stale / superseded info |
| `--smoke`      | `#8a8a86` | Muted text, captions                           |
| `--hairline`   | `rgba(0,0,0,.14)` | Rules, borders                         |

Monochrome by default. **Recall-green is the only loud colour and is rationed** —
the `//` mark, links on hover, the live marquee, one or two structural accents.
Because green is light, set it as a *fill* (with ink text) or use `--signal-deep`
for green text on a light field. Amber `--stale` appears **only** where the
challenge's stale/superseded states are described.

## Motion

Cargo-grade, restrained, physical.

- **Parallax** on manga panels (foreground drifts faster than the page).
- **Scroll-reveal**: blocks rise + fade in via IntersectionObserver.
- **Marquee ticker** under the hero — the challenge vocabulary on an infinite loop.
- **Scroll-progress** hairline pinned to the top of the viewport.
- **Hover**: images lift and regain tone; links wipe in the signal colour.
- All motion is gated behind `prefers-reduced-motion: reduce`.

## Layout principles

1. **Manga first.** Full-bleed hero owned by the manga.
2. **Asymmetric grids.** Off-centre columns, large negative space.
3. **Hairline rules**, not boxes. No drop-shadow "sticker" cards.
4. **Edge-to-edge imagery.** Panels bleed to the gutters.
5. **State the contract exactly.** Commands and file surfaces are set in monospace,
   never paraphrased.

## Imagery — the manga

The soft-color educational manga is the brand's signature imagery and leads every
key surface. The two books share a cast — **Engy** (the librarian-robot whose
chest-notebook is `MEMORY_DIR`) and **Sensei** (the narrator-teacher). Treatment:
near-grayscale at rest, returning to full soft tone on hover/focus; panels bleed
edge-to-edge, never framed in shadow boxes. Always pair panels with a path to read
(flipbook or PDF) — never decorative-only.
