"""
split_ten_billion.py
--------------------
Dedicated splitter for "Ten Billion Days and One Hundred Billion Nights"
by Ryu Mitsuse.

The main split_books.py cannot handle this book because chapter headings
(CHAPTER ONE, etc.) only appear in the TOC, not in the body text.
Chapters in the body are separated by 10+ consecutive blank lines
followed by an epigraph, then 8+ blank lines before the chapter text.

Structure:
  Prologue (body text before first chapter break)
  Chapter 1 - Shadowplay Upon the Sea
  Chapter 2 - Orichalcum
  Chapter 3 - Maitreya
  Chapter 4 - Jerusalem
  Chapter 5 - The Lost City
  Chapter 6 - The New Galactic Age
  Chapter 7 - The Last Humans
  Chapter 8 - The Long Road
  Afterword

Usage:
    python scripts/split_ten_billion.py --dry-run
    python scripts/split_ten_billion.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "Japan" / "ten billion days and one hundred billion nights.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "Japan" / "ten billion days and one hundred billion nights"

# Chapter names (from the TOC).
# There are 8 chapter breaks (10+ blank lines) in the body,
# plus 3 more in the backmatter (afterword, commentary, publisher info).
# We keep 10 sections: Prologue + 8 Chapters + Afterword + Commentary.
CHAPTER_NAMES = [
    "Prologue",
    "Chapter 1 - Shadowplay Upon the Sea",
    "Chapter 2 - Orichalcum",
    "Chapter 3 - Maitreya",
    "Chapter 4 - Jerusalem",
    "Chapter 5 - The Lost City",
    "Chapter 6 - The New Galactic Age",
    "Chapter 7 - The Last Humans",
    "Chapter 8 - The Long Road",
    "Afterword",
    None,  # skip blank separator
    "Commentary - The Passion of Loss by Mamoru Oshii",
]

# Max sections to output (stop before publisher info / trailing TOC)
MAX_SECTIONS = 12

# Body starts after the initial TOC (around line 280)
BODY_START = 280

# End of body (before the trailing TOC)
END_MARKER = "Table of Contents"
END_SEARCH_START = 9000


def find_chapter_breaks(lines: list[str]) -> list[int]:
    """
    Find chapter break points by detecting 10+ consecutive blank lines
    in the body text. Returns list of line indices where the blank
    stretch starts (these are the boundaries between chapters).
    """
    breaks = []
    blank_count = 0
    blank_start = 0

    for i in range(BODY_START, len(lines)):
        stripped = lines[i].strip()
        if not stripped:
            if blank_count == 0:
                blank_start = i
            blank_count += 1
        else:
            if blank_count >= 10:
                breaks.append(blank_start)
            blank_count = 0

    return breaks


def find_body_end(lines: list[str]) -> int:
    """Find the end of body text (before trailing TOC / backmatter)."""
    for i in range(END_SEARCH_START, len(lines)):
        if lines[i].strip().rstrip('\r') == END_MARKER:
            # Back up past blank lines
            end = i
            while end > 0 and not lines[end - 1].strip():
                end -= 1
            return end
    return len(lines)


def split_book(dry_run: bool = False) -> None:
    if not BOOK_PATH.exists():
        print(f"ERROR: {BOOK_PATH} not found", file=sys.stderr)
        sys.exit(1)

    text = BOOK_PATH.read_text(encoding="utf-8")
    lines = text.split("\n")

    breaks = find_chapter_breaks(lines)
    body_end = find_body_end(lines)

    # We expect 9 breaks: 8 chapter breaks + 1 afterword break
    if len(breaks) < 9:
        print(f"WARNING: expected 9 chapter breaks, found {len(breaks)}",
              file=sys.stderr)

    # Build sections:
    # - Prologue: BODY_START to first break
    # - Chapters 1-8: between consecutive breaks
    # - Afterword: last break to body_end
    section_starts = [BODY_START] + breaks
    section_ends = breaks + [body_end]

    chunks = []
    for idx, (start, end) in enumerate(zip(section_starts, section_ends)):
        if idx >= MAX_SECTIONS:
            break
        if idx < len(CHAPTER_NAMES):
            label = CHAPTER_NAMES[idx]
        else:
            label = f"Section {idx}"
        if label is None:
            continue  # skip blank separators
        content = "\n".join(lines[start:end]).strip()
        if content:
            chunks.append((label, content))

    # Front matter (before body)
    front_matter = "\n".join(lines[:BODY_START]).strip()

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  Ten Billion Days — {len(chunks)} sections")
        print(f"{'=' * 60}")
        for label, content in chunks:
            print(f"  {label}  ({len(content):,} chars)")
        if front_matter:
            print(f"  [front matter: {len(front_matter):,} chars]")
        print()
        return

    # Write output files
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if front_matter:
        (OUTPUT_DIR / "front_matter.txt").write_text(front_matter, encoding="utf-8")
        print(f"  wrote front_matter.txt  ({len(front_matter):,} chars)")

    for label, content in chunks:
        safe_name = re.sub(r'[<>:"/\\|?*]', '', label)
        out_path = OUTPUT_DIR / f"{safe_name}.txt"
        out_path.write_text(content, encoding="utf-8")
        print(f"  wrote {safe_name}.txt  ({len(content):,} chars)")

    print(f"\n  Done: {len(chunks)} sections written to {OUTPUT_DIR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split Ten Billion Days and One Hundred Billion Nights")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
