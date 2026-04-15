"""
split_dune.py
-------------
Dedicated splitter for "Dune" by Frank Herbert.
The main split_books.py can't handle Dune because it has no "Chapter N"
headings — each chapter opens with an italicized epigraph ending in an
em-dash attribution, e.g.:

        A beginning is the time for taking the most delicate care...

        —FROM "MANUAL OF MUAD'DIB"
        BY THE PRINCESS IRULAN

Structure:
  Book One (Dune)     — 22 chapters
  Book Two (Muad'Dib) — 15 chapters
  Book Three (The Prophet) — 11 chapters
  Appendixes I-IV
  Terminology
  Afterword

Total: 48 chapters + 6 backmatter sections

Usage:
    python scripts/splitters/split_dune.py --dry-run
    python scripts/splitters/split_dune.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "US" / "Dune.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "US" / "Dune"

# Skip reviews / front matter (first 125 lines)
BODY_START = 125

# Backmatter starts at APPENDIXES
BACKMATTER_MARKER = "APPENDIXES"

# Book boundary markers (ALL CAPS)
BOOK_MARKERS = {
    "BOOK ONE":   "Book ONE - Dune",
    "BOOK TWO":   "Book TWO - Muad'Dib",
    "BOOK THREE": "Book THREE - The Prophet",
}

# Backmatter sections (line markers)
BACKMATTER_SECTIONS = [
    ("APPENDIX I:",     "Appendix I - The Ecology of Dune"),
    ("APPENDIX II:",    "Appendix II - The Religion of Dune"),
    ("APPENDIX III:",   "Appendix III - Report on Bene Gesserit Motives and Purposes"),
    ("APPENDIX IV:",    "Appendix IV - The Almanak en-Ashraf"),
    ("TERMINOLOGY OF",  "Terminology of the Imperium"),
    ("AFTERWORD",       "Afterword"),
]

# Em-dash patterns (handle — – - variants)
EM_DASH_PATTERN = re.compile(r"^[—–-](?:[A-Z]|FROM|\s+[A-Z])")


def find_em_dash_lines(lines: list[str], start: int, end: int) -> list[int]:
    """Find all em-dash attribution lines in the body text."""
    results = []
    for i in range(start, min(end, len(lines))):
        s = lines[i].strip()
        if EM_DASH_PATTERN.match(s):
            results.append(i)
    return results


def find_chapter_start(lines: list[str], em_dash_line: int, prev_boundary: int) -> int:
    """
    Walk backward from the em-dash line to find where the chapter starts.
    The chapter boundary is at the first non-blank line after a gap of
    5+ blank lines (which separates chapters).
    """
    # Start from em_dash_line and walk back looking for blank-line gap
    i = em_dash_line - 1
    while i > prev_boundary:
        # Count consecutive blank lines going backward from position i
        blank_count = 0
        j = i
        while j > prev_boundary and not lines[j].strip():
            blank_count += 1
            j -= 1
        if blank_count >= 5:
            # Found a gap — chapter starts at i (first blank after gap edge)
            # The gap is from j+1 to i. Chapter starts at j+blank_count+...
            # Actually: the gap runs j+1..i (inclusive), and the chapter starts
            # at the first non-blank line AFTER i, which is i+1... but we want
            # the blank line before the first text (to preserve the space).
            # Return the first line of content (j+blank_count+1 = i+1)
            return i + 1
        if blank_count > 0:
            # Skip past these blanks
            i = j
        else:
            i -= 1
    return prev_boundary + 1


def find_line_starting_with(lines: list[str], prefix: str, start: int = 0) -> int:
    """Find the first line whose stripped content starts with prefix."""
    for i in range(start, len(lines)):
        if lines[i].strip().startswith(prefix):
            return i
    return -1


def split_book(dry_run: bool = False) -> None:
    if not BOOK_PATH.exists():
        print(f"ERROR: {BOOK_PATH} not found", file=sys.stderr)
        sys.exit(1)

    text = BOOK_PATH.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Find backmatter start
    backmatter_start = find_line_starting_with(lines, BACKMATTER_MARKER, BODY_START)
    if backmatter_start < 0:
        backmatter_start = len(lines)

    # Find Book markers
    book_lines = {}
    for marker, label in BOOK_MARKERS.items():
        idx = find_line_starting_with(lines, marker, BODY_START)
        if idx >= 0:
            book_lines[idx] = label

    # Find all em-dash attribution lines in the body
    em_dash_lines = find_em_dash_lines(lines, BODY_START, backmatter_start)

    # Build chapter boundaries — each chapter starts just before its epigraph
    # Walk backward from each em-dash line to find the start-of-chapter boundary
    chapter_boundaries = []
    prev = BODY_START - 1
    for em_dash in em_dash_lines:
        start = find_chapter_start(lines, em_dash, prev)
        chapter_boundaries.append(start)
        prev = em_dash

    # Assemble sections in order:
    # Book marker (if present at this position) merges into next chapter label
    sections = []  # list of (start_line, label)
    chapter_num = 0
    for i, boundary in enumerate(chapter_boundaries):
        # Check if any book marker falls before this boundary and after previous one
        prev_boundary = chapter_boundaries[i - 1] if i > 0 else BODY_START
        book_label = None
        book_line = None
        for book_idx in sorted(book_lines.keys()):
            if prev_boundary <= book_idx < boundary:
                book_label = book_lines[book_idx]
                book_line = book_idx
                break
        chapter_num += 1
        if book_label:
            # Start this chapter at the Book marker line, label with Book + Chapter
            label = f"{book_label} - Chapter {chapter_num:02d}"
            sections.append((book_line, label))
        else:
            label = f"Chapter {chapter_num:02d}"
            sections.append((boundary, label))

    # Add backmatter sections
    for marker, label in BACKMATTER_SECTIONS:
        idx = find_line_starting_with(lines, marker, backmatter_start)
        if idx >= 0:
            sections.append((idx, label))

    # Sort by line number to ensure ordering
    sections.sort(key=lambda x: x[0])

    # Build section content
    chunks = []
    for idx, (start_line, label) in enumerate(sections):
        if idx + 1 < len(sections):
            end_line = sections[idx + 1][0]
        else:
            end_line = len(lines)
        content = "\n".join(lines[start_line:end_line]).strip()
        chunks.append((label, content))

    # Front matter (before body)
    front_matter = "\n".join(lines[:sections[0][0]]).strip() if sections else ""

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  Dune — {len(chunks)} sections")
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
    parser = argparse.ArgumentParser(description="Split Dune")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
