# ENGRAM // KIT — site

A static, GitHub Pages–ready site for the **ENGRAM** memory challenge and its two
whitepaper mangas, built on the **ENGRAM // KIT** brand identity (v2).

- `index.html` — the landing page: manga-first hero, the two papers (ALMA &
  AMA-Bench), the two-command challenge contract, and how to compete.
- `brand-guidelines.html` — the self-demonstrating styleguide. Renders the live
  tokens from `assets/css/cargo.css`. Written spec lives in [`BRAND.md`](BRAND.md).
- `flipbook.html` — a multi-book flipbook reader for the educational mangas. Pick a
  book with `?book=alma` or `?book=ama-bench`.
- `assets/` — `cargo.css` (landing + guidelines), `style.css` (flipbook),
  `site.js` (scroll/parallax), `flipbook.js` (the book data + reader).
- `manga/<topic>/panels/` — the rendered manga pages. **Currently placeholders**;
  drop the generated panels in over the same filenames (`alma_pageNN.png`,
  `amabench_pageNN.png`).
- `.nojekyll` — disables Jekyll so all asset paths are served verbatim.

## Placeholders

Panel art is generated separately (ChatGPT / image model) from the per-page prompts
in [`../documentation/manga/`](../documentation/manga/). Until then, labeled
placeholder PNGs stand in at the exact filenames the site and flipbook expect, so
the layout, flipbook, and PDFs all work today and simply sharpen when real panels
replace them.

## Publish on GitHub Pages

1. Push this branch (or merge to `main`).
2. Repo **Settings → Pages**.
3. **Source:** Deploy from a branch. **Branch:** `main`, **Folder:** `/docs`.
4. Save. The site appears at `https://<user>.github.io/<repo>/`.

## Preview locally

```bash
cd docs && python3 -m http.server 8000
# open http://localhost:8000
```
