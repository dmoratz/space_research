"""
split_wandering_earth.py
-------------------------
Dedicated splitter for "The Wandering Earth" by Cixin Liu.
The main split_books.py cannot handle this book because chapter headings
are split across two lines:
    CHAPTER
    1 The Reining Age

Usage:
    python scripts/split_wandering_earth.py --dry-run
    python scripts/split_wandering_earth.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "China" / "The Wandering Earth.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "China" / "The Wandering Earth"

# Chapters: search for "CHAPTER" line followed by "N Title" line
CHAPTERS = [
    ("1 The Reining Age",    "Chapter 1 - The Reining Age"),
    ("2 The Exodial Age",    "Chapter 2 - The Exodial Age"),
    ("3 Rebellion",          "Chapter 3 - Rebellion"),
    ("4 The Wandering Age",  "Chapter 4 - The Wandering Age"),
]

# Skip TOC (first ~50 lines)
MIN_BODY_LINE = 50


def find_chapter_starts(lines: list[str]) -> list[tuple[int, str]]:
    """Find each CHAPTER heading (the line with 'CHAPTER' on it)."""
    results = []
    used_lines: set[int] = set()

    for search_suffix, label in CHAPTERS:
        found = False
        for i in range(MIN_BODY_LINE, len(lines)):
            if i in used_lines:
                continue
            stripped = lines[i].strip().rstrip('\r')
            if stripped == "CHAPTER":
                # Look at next non-blank line for the number + title
                for j in range(i + 1, min(i + 5, len(lines))):
                    next_stripped = lines[j].strip().rstrip('\r')
                    if next_stripped == search_suffix:
                        results.append((i, label))
                        used_lines.add(i)
                        found = True
                        break
                if found:
                    break
        if not found:
            print(f"  WARNING: could not find '{search_suffix}' for '{label}'",
                  file=sys.stderr)

    results.sort(key=lambda x: x[0])
    return results


def split_book(dry_run: bool = False) -> None:
    if not BOOK_PATH.exists():
        print(f"ERROR: {BOOK_PATH} not found", file=sys.stderr)
        sys.exit(1)

    text = BOOK_PATH.read_text(encoding="utf-8")
    lines = text.split("\n")

    chapter_starts = find_chapter_starts(lines)

    if not chapter_starts:
        print("ERROR: no chapters found!", file=sys.stderr)
        sys.exit(1)

    # Build chapter content
    chunks = []
    for idx, (start_line, label) in enumerate(chapter_starts):
        if idx + 1 < len(chapter_starts):
            end_line = chapter_starts[idx + 1][0]
        else:
            end_line = len(lines)
        content = "\n".join(lines[start_line:end_line]).strip()
        chunks.append((label, content))

    # Front matter
    front_matter = "\n".join(lines[:chapter_starts[0][0]]).strip()

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  The Wandering Earth — {len(chunks)} chapters")
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

    print(f"\n  Done: {len(chunks)} chapters written to {OUTPUT_DIR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split The Wandering Earth")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
