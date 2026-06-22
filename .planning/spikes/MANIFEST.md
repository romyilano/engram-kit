# Spike Manifest

## Idea

Explore building a **visual-novel game around the ENGRAM papers (ALMA & AMA-Bench) for learning**.
The repo already ships those papers as soft-color manga panels (15 pages), an ENGRAM // KIT brand,
and a passive flipbook. A *learning* visual novel must earn its place over the flipbook with
interactivity — typewriter dialogue over panel backgrounds, branching choices, and comprehension
checkpoints where Engy/Sensei give in-character corrective feedback. Target stack matches the
existing `docs/` static site: zero-dependency vanilla HTML/CSS/JS, runnable by opening a file,
deployable to GitHub Pages.

## Requirements

Design decisions locked in during spiking. Non-negotiable for the real build.

- Hand-rolled, **zero-dependency vanilla JS** VN runner (no Monogatari/Twine/Ren'Py) — matches the
  `docs/` static site, no build step, full ENGRAM // KIT brand control.
- Reuse existing assets: manga panel PNGs as scene backgrounds, the brand palette
  (recall-green `#00e0a4`, ink, Helvetica, mono labels), and the existing cast (Engy, Sensei, Examiner).
- The VN must add **interactive learning** (choices + comprehension checkpoints), not just replay the
  flipbook.

## Spikes

| # | Name | Type | Validates | Verdict | Tags |
|---|------|------|-----------|---------|------|
| 001 | vn-engine-feel | standard | Vanilla-JS VN scene (panel bg, typewriter dialogue, click-advance, branching choice) feels like a real VN and fits the static site, zero build | ✓ VALIDATED | vn, ui, brand, static-site |
| 002 | learning-loop | standard | Comprehension checkpoints with in-character corrective feedback reinforce the paper concept better than passive reading | PENDING | vn, pedagogy, quiz, learning |
| 003 | dialogue-pipeline | standard | Existing `page-NN.md` "Panel N — Speaker: line" blocks auto-parse into a structured VN script, so authoring isn't from scratch | PENDING | pipeline, parsing, content, authoring |
