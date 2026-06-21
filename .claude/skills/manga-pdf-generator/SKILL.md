---
name: manga-pdf-generator
description: Build a print-ready PDF from an educational-manga project folder — one panel image per page, optionally with the source paper/spec appended as text pages at the end. Use when the user wants to export the manga panels under documentation/manga/<topic>/ as a single PDF, or "make a PDF of the manga".
---

# Manga PDF Generator

Turn an educational-manga project folder (the kind produced by the
`educational-manga-generator` skill) into a single, print-ready PDF:

- **One panel image per PDF page**, scaled and centered on A4 portrait.
- A simple **cover page** (title / subtitle / source).
- Optionally, the **source paper/spec the manga explains, appended as text
  pages** at the end (rendered from a Markdown file).

It depends only on **Pillow (PIL)** — no `convert`, `img2pdf`, or ghostscript
needed, which matters on machines without a PDF toolchain.

## When to use
- The user asks to "make a PDF of the manga", "export the panels to PDF", or
  "one image per page" for a `documentation/manga/<topic>/` folder.
- The user wants the explained paper/spec bundled at the end of the manga PDF.

## Expected input layout

```
documentation/manga/<topic>/
├── panels/
│   ├── <topic>_page01.png
│   ├── <topic>_page02.png
│   └── ...
├── <topic>-paper.md      # OPTIONAL — source doc appended at the end
└── pdf/                  # created by the script if missing
    └── <topic>-manga.pdf # output
```

Panels are sorted by filename, so zero-pad page numbers (`page01`, not `page1`).
Supported image types: png, jpg, jpeg, webp.

## How to run

```bash
python3 .claude/skills/manga-pdf-generator/scripts/build_manga_pdf.py \
  documentation/manga/<topic> \
  --title "ERC-8183: Agentic Commerce" \
  --subtitle "The Single Evaluator" \
  --tagline "an educational manga in gekiga form" \
  --source "Source: eips.ethereum.org/EIPS/eip-8183"
```

The only required argument is the manga directory. Everything else has
defaults:
- `--title` defaults to the folder name upper-cased (`erc-8183` → `ERC-8183`).
- `--paper` auto-detects a `*-paper.md` file in the manga dir; pass a path to
  override, or omit the file to skip the appended paper.
- `--out` defaults to `<dir>/pdf/<dirname>-manga.pdf`.

Run with `-h` for the full option list.

## Appending the source paper

If the user wants the paper/spec at the end:

1. Save the source text as Markdown at `documentation/manga/<topic>/<topic>-paper.md`.
   Prefer the **canonical/verbatim source** (e.g. fetch the official EIP/RFC/paper
   with WebFetch) rather than a paraphrase, so the appended document is accurate.
2. The script auto-detects `*-paper.md` and renders it as text pages after a
   "Source Specification" divider.

The Markdown renderer handles: `#`–`####` headings, `**bold**` (including
inline), `-` bullets, fenced ```code blocks``` (monospace on a gray panel), and
GitHub-style `|` tables (rendered as monospace rows). It is intentionally
lightweight — keep paper Markdown simple.

## After building
- Verify visually. The system may lack a PDF rasterizer (`pdftoppm`, ghostscript).
  If so, render representative pages straight from PIL by importing the script's
  functions, save them as PNG, and Read them — the PDF is just those page
  canvases, so checking the canvases is equivalent. Always check the cover, one
  panel page, and (if appended) the first paper page and a code-block page.
- Offer to `open` the PDF (macOS) once built.

## Platform notes
Font paths in the script point at macOS system fonts (Georgia, Arial Bold,
Menlo). Linux fallbacks to DejaVu are built in; for other setups, edit the
`FONTS` dict at the top of `scripts/build_manga_pdf.py`.
