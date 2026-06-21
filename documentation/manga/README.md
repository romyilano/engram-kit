# ENGRAM // KIT — Educational Manga

Two frontier papers on **agentic memory**, retold as soft-color educational manga.
Both books share a cast — **Engy** (a librarian-robot whose chest-notebook *is* its
memory) and **Sensei** (the narrator-teacher) — and both land on the **ENGRAM**
challenge: build memory that ingests dated states over time and answers *without
hindsight*.

| Book | Paper | Pages | Source | Folder |
|------|-------|-------|--------|--------|
| *The Notebook That Redesigns Itself* | **ALMA** — meta-learning agentic memory designs | 8 | [arXiv 2602.07755](https://arxiv.org/abs/2602.07755) | [`alma/`](alma/) |
| *The Long Road Test* | **AMA-Bench** — evaluating long-horizon agent memory | 7 | [arXiv 2602.22769](https://arxiv.org/abs/2602.22769) | [`ama-bench/`](ama-bench/) |

Together they bracket the ENGRAM problem from both sides: **ALMA** is the *design*
side (how is a good memory design found?), **AMA-Bench** is the *evaluation* side (how
do you measure whether agent memory is any good?).

## Each project folder contains

- `manifest.md` — the plan: concepts, page table, locked style block, status.
- `README.md` — human-facing overview with the page list.
- `character-sheet.md` — the recurring cast (kept consistent across pages).
- `page-01.md … page-NN.md` — one self-contained image-generation prompt per page.
- `notes.md` — omissions, sequel ideas, alternative metaphors, references.
- `<topic>-paper.md` — the source abstract + plain-English summary (appended to PDFs).
- `panels/` — the rendered pages (**currently labeled placeholders**).
- `pdf/` — a print-ready PDF (placeholder build until panels are rendered).

## Style (both books)

Soft-color / watercolor educational manga — warm cream paper, soft ink linework, muted
pastel washes, and a single rationed **recall-green (#00e0a4)** for memory, recall, and
"it worked" moments. The locked style block is restated verbatim in every page prompt.

## Pipeline (human-in-the-loop)

1. Open a `page-XX.md` prompt and paste it into an image model (ChatGPT, etc.).
2. Save the result to `panels/<topic>_pageNN.png` (zero-padded), replacing the placeholder.
3. Optionally run the `manga-pdf-generator` skill to rebuild `pdf/<topic>-manga.pdf`
   (it can append the `<topic>-paper.md` source).
4. The GitHub Pages site in [`../../docs/`](../../docs/) reads the same panels for its
   hero, feature cards, panel strip, and flipbook — they sharpen automatically as real
   panels land.

## The combined reading pack

[`combined/reading-pack-manga.pdf`](combined/reading-pack-manga.pdf) bundles a cover and
both stories into one print-ready PDF (placeholder build for now).
