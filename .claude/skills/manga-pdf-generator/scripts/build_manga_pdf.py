#!/usr/bin/env python3
"""Build a print-ready PDF from an educational-manga project folder.

One panel image per page, optionally followed by a source document (e.g. the
paper/spec the manga explains) rendered as text pages.

Usage:
    python3 build_manga_pdf.py <manga_dir> [options]

    <manga_dir>   Path to a manga project folder containing a panels/ subdir
                  (e.g. documentation/manga/erc-8183).

Options:
    --title TEXT      Big title on the cover page. Default: derived from the
                      manga dir name (e.g. "erc-8183" -> "ERC-8183").
    --subtitle TEXT   Italic subtitle under the title rule.
    --tagline TEXT    Small line under the subtitle.
    --source TEXT     Footer line on the cover (e.g. a URL).
    --paper PATH      Markdown file to append as "Source Specification" text
                      pages. Default: auto-detect <dir>/*-paper.md if present.
    --out PATH        Output PDF path. Default: <dir>/pdf/<dirname>-manga.pdf.

Depends only on Pillow (PIL), which ships broadly and needs no PDF toolchain.
Fonts are macOS system fonts; override FONTS below for other platforms.
"""

import argparse
import os
import sys
from PIL import Image, ImageDraw, ImageFont

# A4 @ 150 DPI, portrait
PW, PH = 1240, 1754
MARGIN = 96
DPI = 150

BG = (255, 255, 255)
INK = (24, 24, 24)
MUTED = (90, 90, 90)
CODE_BG = (244, 244, 246)
RULE = (210, 210, 210)

# macOS system fonts. On Linux, point these at DejaVu/Liberation equivalents.
FONTS = {
    "body": "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "body_bold": "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "body_italic": "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
    "head": "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "mono": "/System/Library/Fonts/Menlo.ttc",
}

_FONT_FALLBACKS = {
    "body": ["/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"],
    "body_bold": ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"],
    "body_italic": ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"],
    "head": ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "mono": ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"],
}


def _font_path(key):
    if os.path.exists(FONTS[key]):
        return FONTS[key]
    for fb in _FONT_FALLBACKS.get(key, []):
        if os.path.exists(fb):
            return fb
    raise SystemExit(f"Font for '{key}' not found. Edit FONTS in {__file__}.")


def F(key, size):
    return ImageFont.truetype(_font_path(key), size)


def new_page():
    return Image.new("RGB", (PW, PH), BG)


def wrap(draw, text, font, max_w):
    words = text.split()
    if not words:
        return [""]
    lines, cur = [], words[0]
    for w in words[1:]:
        if draw.textlength(cur + " " + w, font=font) <= max_w:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


class Renderer:
    """Flows blocks onto pages, auto-paginating."""

    def __init__(self):
        self.pages = []
        self._start_page()

    def _start_page(self):
        self.img = new_page()
        self.draw = ImageDraw.Draw(self.img)
        self.y = MARGIN
        self.pages.append(self.img)

    def space(self, h):
        self.y += h

    def _ensure(self, h):
        if self.y + h > PH - MARGIN:
            self._start_page()

    def line(self, s, font, color=INK, lh=1.4, indent=0, max_w=None):
        max_w = max_w or (PW - 2 * MARGIN - indent)
        for ln in wrap(self.draw, s, font, max_w):
            asc, desc = font.getmetrics()
            h = int((asc + desc) * lh)
            self._ensure(h)
            self.draw.text((MARGIN + indent, self.y), ln, font=font, fill=color)
            self.y += h

    def rich(self, s, font, bold_font, color=INK, lh=1.4, indent=0):
        """Draw a line honoring inline **bold** markers, with word wrap."""
        max_w = PW - 2 * MARGIN - indent
        tokens = []
        for i, chunk in enumerate(s.split("**")):
            if not chunk:
                continue
            fnt = bold_font if i % 2 == 1 else font
            for w in chunk.split(" "):
                if w:
                    tokens.append((w, fnt))
        asc, desc = font.getmetrics()
        h = int((asc + desc) * lh)
        x = MARGIN + indent
        space = self.draw.textlength(" ", font=font)
        self._ensure(h)
        line_start = True
        for word, fnt in tokens:
            ww = self.draw.textlength(word, font=fnt)
            if not line_start and x + ww > MARGIN + indent + max_w:
                self.y += h
                self._ensure(h)
                x = MARGIN + indent
                line_start = True
            self.draw.text((x, self.y), word, font=fnt, fill=color)
            x += ww + space
            line_start = False
        self.y += h

    def rule(self):
        self._ensure(24)
        self.y += 8
        self.draw.line([(MARGIN, self.y), (PW - MARGIN, self.y)], fill=RULE, width=1)
        self.y += 16

    def code_block(self, lines):
        font = F("mono", 17)
        asc, desc = font.getmetrics()
        h = int((asc + desc) * 1.35)
        pad = 14
        i = 0
        while i < len(lines):
            self._ensure(h * 2)
            block_top = self.y
            seg = []
            while i < len(lines) and self.y + h <= PH - MARGIN:
                seg.append(lines[i])
                self.y += h
                i += 1
            self.draw.rectangle(
                [MARGIN, block_top - pad, PW - MARGIN, self.y + pad], fill=CODE_BG
            )
            yy = block_top
            for ln in seg:
                s = ln
                limit = PW - 2 * MARGIN - 2 * pad
                while self.draw.textlength(s, font=font) > limit and len(s) > 4:
                    s = s[:-2]
                if s != ln:
                    s = s[:-1] + "…"
                self.draw.text((MARGIN + pad, yy), s, font=font, fill=(40, 40, 40))
                yy += h
            self.y += pad + 6
            if i < len(lines):
                self._start_page()


def render_markdown(r, md):
    body = F("body", 21)
    bold = F("body_bold", 21)
    h1 = F("head", 34)
    h2 = F("head", 27)
    h3 = F("head", 22)

    lines = md.split("\n")
    i = 0
    in_code = False
    code_buf = []
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()

        if stripped.startswith("```"):
            if in_code:
                r.code_block(code_buf)
                code_buf = []
                in_code = False
                r.space(8)
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(ln.rstrip("\n"))
            i += 1
            continue

        if not stripped:
            r.space(12)
        elif stripped.startswith("#### "):
            r.space(12)
            r.line(stripped[5:], h3, color=MUTED)
            r.space(4)
        elif stripped.startswith("### "):
            r.space(14)
            r.line(stripped[4:], h3, color=INK)
            r.space(6)
        elif stripped.startswith("## "):
            r.space(20)
            r.line(stripped[3:], h2, color=INK)
            r.rule()
        elif stripped.startswith("# "):
            r.space(10)
            r.line(stripped[2:], h1, color=INK)
            r.space(10)
        elif stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                i += 1
                continue
            r.code_block(["  ".join(cells)])
        elif stripped.startswith("- "):
            r.rich("**•** " + stripped[2:], body, bold, indent=24)
            r.space(2)
        else:
            r.rich(stripped, body, bold)
            r.space(2)
        i += 1
    if in_code and code_buf:
        r.code_block(code_buf)


def panel_pages(panels_dir):
    pages = []
    files = sorted(
        f for f in os.listdir(panels_dir)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    )
    if not files:
        raise SystemExit(f"No panel images found in {panels_dir}")
    for f in files:
        im = Image.open(os.path.join(panels_dir, f)).convert("RGB")
        page = new_page()
        avail_w, avail_h = PW - 2 * 40, PH - 2 * 40
        scale = min(avail_w / im.width, avail_h / im.height)
        nw, nh = int(im.width * scale), int(im.height * scale)
        im = im.resize((nw, nh), Image.LANCZOS)
        page.paste(im, ((PW - nw) // 2, (PH - nh) // 2))
        pages.append(page)
    return pages, files


def cover_page(title, subtitle, tagline, source):
    img = new_page()
    d = ImageDraw.Draw(img)
    small = F("body", 20)
    parts = title.split(":", 1)
    d.text((MARGIN, 560), parts[0].strip(), font=F("head", 52), fill=INK)
    if len(parts) > 1:
        d.text((MARGIN, 630), parts[1].strip(), font=F("head", 40), fill=INK)
        ry = 700
    else:
        ry = 640
    d.line([(MARGIN, ry), (PW - MARGIN, ry)], fill=RULE, width=2)
    yy = ry + 30
    if subtitle:
        d.text((MARGIN, yy), subtitle, font=F("body_italic", 26), fill=MUTED)
        yy += 40
    if tagline:
        d.text((MARGIN, yy), tagline, font=small, fill=MUTED)
    if source:
        d.text((MARGIN, PH - MARGIN - 18), source, font=small, fill=MUTED)
    return img


def divider_page(heading, note):
    img = new_page()
    d = ImageDraw.Draw(img)
    d.text((MARGIN, 740), heading, font=F("head", 40), fill=INK)
    d.line([(MARGIN, 810), (PW - MARGIN, 810)], fill=RULE, width=2)
    if note:
        d.text((MARGIN, 840), note, font=F("body_italic", 24), fill=MUTED)
    return img


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manga_dir")
    ap.add_argument("--title")
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--tagline", default="an educational manga in gekiga form")
    ap.add_argument("--source", default="")
    ap.add_argument("--paper")
    ap.add_argument("--out")
    args = ap.parse_args()

    mdir = os.path.abspath(args.manga_dir)
    if not os.path.isdir(mdir):
        raise SystemExit(f"Not a directory: {mdir}")
    panels_dir = os.path.join(mdir, "panels")
    if not os.path.isdir(panels_dir):
        raise SystemExit(f"No panels/ subdir in {mdir}")

    name = os.path.basename(mdir.rstrip("/"))
    title = args.title or name.upper().replace("_", "-")

    paper = args.paper
    if paper is None:
        candidates = sorted(
            f for f in os.listdir(mdir) if f.endswith("-paper.md")
        )
        if candidates:
            paper = os.path.join(mdir, candidates[0])

    out = args.out or os.path.join(mdir, "pdf", f"{name}-manga.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)

    pages = [cover_page(title, args.subtitle, args.tagline, args.source)]
    panels, files = panel_pages(panels_dir)
    pages += panels

    if paper and os.path.exists(paper):
        pages.append(divider_page(
            "Source Specification",
            "The full text of the source this manga explains.",
        ))
        with open(paper, encoding="utf-8") as fh:
            r = Renderer()
            render_markdown(r, fh.read())
            pages += r.pages

    first, rest = pages[0], pages[1:]
    first.save(out, "PDF", resolution=DPI, save_all=True, append_images=rest)
    print(f"Wrote {out}")
    print(f"  {len(files)} panels + {'paper appended' if paper else 'no paper'}"
          f" = {len(pages)} pages")


if __name__ == "__main__":
    main()
