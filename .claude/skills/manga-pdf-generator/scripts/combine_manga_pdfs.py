#!/usr/bin/env python3
"""Combine the two reading-pack manga PDFs into one, behind a meetup cover.

Builds a single cover page (meetup details + RSVP link), then concatenates the
ERC-8183 and Mini-Blocks manga PDFs after it.

Usage:
    python3 combine_manga_pdfs.py

Depends on Pillow (cover rendering) and PyMuPDF/fitz (PDF concatenation).
"""

import os
import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont

# Reuse the markdown->page renderer from the single-manga builder (same dir).
import build_manga_pdf as bm

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

ERC = os.path.join(ROOT, "documentation/manga/erc-8183/pdf/erc-8183-manga.pdf")
MINI = os.path.join(ROOT, "documentation/manga/mini-blocks/pdf/mini-blocks-manga.pdf")

# Plain-language learning appendix, appended after both mangas. Each entry is a
# (divider heading, divider note, markdown path) rendered as flowing text pages.
APPENDIX = [
    ("Blockchain for Beginners",
     "How blocks get built, and how to read the Rated explorer.",
     os.path.join(ROOT, "documentation/blockchain-for-beginners.md")),
    ("Ethereum for Dummies",
     "The Foundry toolchain — forge, cast, anvil — in plain English.",
     os.path.join(ROOT, "documentation/ethereum-for-dummies.md")),
    ("MiniEscrow Explained",
     "A line-by-line walk through the runnable ERC-8183-style escrow.",
     os.path.join(ROOT, "documentation/mini-escrow-explained.md")),
]
OUTS = [
    os.path.join(ROOT, "documentation/manga/combined/reading-pack-manga.pdf"),
    os.path.join(ROOT, "docs/manga/combined/reading-pack-manga.pdf"),
]

LUMA = "https://luma.com/wprc-sf-june20?tk=WXGA5o"
CREDIT_URL = "https://romyilano.com"

# A4 @ 150 DPI, portrait — matches the panel PDFs.
PW, PH = 1240, 1754
MARGIN = 96
DPI = 150

BG = (255, 255, 255)
INK = (24, 24, 24)
MUTED = (90, 90, 90)
ACCENT = (150, 40, 40)
RULE = (210, 210, 210)

FONTS = {
    "body": "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "body_bold": "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "body_italic": "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
    "head": "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
}


def F(key, size):
    return ImageFont.truetype(FONTS[key], size)


def cover_page():
    img = Image.new("RGB", (PW, PH), BG)
    d = ImageDraw.Draw(img)

    # Kicker
    d.text((MARGIN, 300), "FRONTIER TOWER  ·  READING PACK",
           font=F("head", 24), fill=ACCENT)

    # Title
    d.text((MARGIN, 360), "Agentic Commerce", font=F("head", 64), fill=INK)
    d.text((MARGIN, 440), "& SSV Mini-Blocks", font=F("head", 64), fill=INK)

    # Rule
    d.line([(MARGIN, 540), (PW - MARGIN, 540)], fill=RULE, width=2)

    # Subtitle
    d.text((MARGIN, 570),
           "Two Ethereum proposals, explained as gekiga-style educational manga.",
           font=F("body_italic", 28), fill=MUTED)

    # Meetup details
    y = 660
    d.text((MARGIN, y), "Meetup  ·  2026-06-20", font=F("body_bold", 28), fill=INK)
    y += 46
    d.text((MARGIN, y), "10 minutes silent reading, then discussion-first.",
           font=F("body", 24), fill=MUTED)

    # Contents
    y = 800
    d.text((MARGIN, y), "Inside this pack", font=F("head", 30), fill=INK)
    y += 60
    items = [
        ("The Single Evaluator", "ERC-8183 — Agentic Commerce  ·  5 pages + full spec"),
        ("Four Rounds to the Block", "SSV Mini-Blocks — Sub-Slot Auctions  ·  7 pages + study notes"),
        ("Learn to Build It", "Appendix  ·  blockchain basics, the toolchain & a runnable escrow"),
    ]
    for title, sub in items:
        d.rectangle([MARGIN, y + 8, MARGIN + 16, y + 24], fill=ACCENT)
        d.text((MARGIN + 34, y), title, font=F("body_bold", 26), fill=INK)
        y += 40
        d.text((MARGIN + 34, y), sub, font=F("body", 22), fill=MUTED)
        y += 56

    # RSVP / Luma link
    y = 1120
    d.line([(MARGIN, y), (PW - MARGIN, y)], fill=RULE, width=1)
    y += 28
    d.text((MARGIN, y), "RSVP & event details", font=F("body_bold", 26), fill=INK)
    y += 42
    d.text((MARGIN, y), LUMA, font=F("body", 24), fill=ACCENT)

    # Credit
    y += 70
    d.text((MARGIN, y), "Study guide by ", font=F("body", 24), fill=MUTED)
    cw = d.textlength("Study guide by ", font=F("body", 24))
    d.text((MARGIN + cw, y), "romyilano.com", font=F("body_bold", 24), fill=ACCENT)

    # Footer
    d.text((MARGIN, PH - MARGIN - 18),
           "Same teacher and apprentice — Sensei Oda and Rin — across both stories.",
           font=F("body_italic", 20), fill=MUTED)
    return img


def appendix_pdf():
    """Render the learning appendix to a temp PDF; return its path or None."""
    entries = [(h, n, p) for (h, n, p) in APPENDIX if os.path.exists(p)]
    if not entries:
        return None

    pages = [bm.divider_page(
        "Appendix — Learn to Build It",
        "Plain-language guides and a runnable contract behind the two papers.",
    )]
    for heading, note, md_path in entries:
        pages.append(bm.divider_page(heading, note))
        with open(md_path, encoding="utf-8") as fh:
            r = bm.Renderer()
            bm.render_markdown(r, fh.read())
            pages += r.pages

    tmp = os.path.join(ROOT, "documentation/manga/combined/_appendix.pdf")
    pages[0].save(tmp, "PDF", resolution=DPI, save_all=True,
                  append_images=pages[1:])
    return tmp


def main():
    # Render cover to a temp single-page PDF via Pillow.
    cover = cover_page()
    tmp_cover = os.path.join(ROOT, "documentation/manga/combined/_cover.pdf")
    os.makedirs(os.path.dirname(tmp_cover), exist_ok=True)
    cover.save(tmp_cover, "PDF", resolution=DPI)

    # Merge: cover + erc-8183 + mini-blocks, with a clickable RSVP link on cover.
    out = fitz.open()
    out.insert_pdf(fitz.open(tmp_cover))
    out.insert_pdf(fitz.open(ERC))
    out.insert_pdf(fitz.open(MINI))

    # Learning appendix at the very back (beginners -> toolchain -> the contract).
    tmp_appendix = appendix_pdf()
    if tmp_appendix:
        out.insert_pdf(fitz.open(tmp_appendix))

    # Add a clickable hyperlink rectangle over the Luma URL on the cover page.
    # Cover is page 0. Convert px (150 DPI) coords to PDF pt (72 DPI): * 72/150.
    s = 72.0 / DPI
    rect = fitz.Rect(MARGIN * s, 1190 * s, (PW - MARGIN) * s, 1230 * s)
    out[0].insert_link({"kind": fitz.LINK_URI, "from": rect, "uri": LUMA})
    # Clickable credit (romyilano.com) — drawn at y ~= 1260..1295 px on the cover.
    credit_rect = fitz.Rect(MARGIN * s, 1258 * s, (PW - MARGIN) * s, 1296 * s)
    out[0].insert_link({"kind": fitz.LINK_URI, "from": credit_rect, "uri": CREDIT_URL})

    page_count = out.page_count
    for dest in OUTS:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        out.save(dest, garbage=4, deflate=True)
        print(f"Wrote {dest}  ({page_count} pages)")

    out.close()
    os.remove(tmp_cover)
    if tmp_appendix and os.path.exists(tmp_appendix):
        os.remove(tmp_appendix)


if __name__ == "__main__":
    main()
