"""
split_vagabonds.py
------------------
Dedicated splitter for "Vagabonds" by Hao Jingfang.
The main split_books.py cannot handle this book because chapter headings
are generic ALL-CAPS words (THE SHIP, HOME, BOOK, etc.) that would be
too aggressive for a generic pattern, and some titles repeat across
parts (PROLOGUE x3, LUOYING x3, REINI x2).

Structure:
  Part One: Star Dance    (18 chapters including Prologue)
  Part Two: Cloud Light   (14 chapters including Prologue)
  Part Three: Gale Wings  (14 chapters including Prologue)

Usage:
    python scripts/split_vagabonds.py --dry-run
    python scripts/split_vagabonds.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "China" / "Vagabonds.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "China" / "Vagabonds"

# Sections in order of appearance.
# (search_key, display_label)
# search_key must match the stripped body line exactly (ALL CAPS).
# For repeated titles, they are matched in order of appearance.
SECTIONS = [
    # Part One: Star Dance
    ("PART ONE",                        "Part 1"),
    ("PROLOGUE",                        "Part 1 - Prologue"),
    ("THE SHIP",                        "Part 1 - The Ship"),
    ("THE HOTEL",                       "Part 1 - The Hotel"),
    ("HOME",                            "Part 1 - Home"),
    ("THE FILM ARCHIVE",                "Part 1 - The Film Archive"),
    ("THE STUDY",                       "Part 1 - The Study"),
    ("THE FAIR",                        "Part 1 - The Fair"),
    ("THE REGISTRY OF FILES",           "Part 1 - The Registry of Files"),
    ("THE COFFEE LOUNGE",               "Part 1 - The Coffee Lounge"),
    ("THE GRAND THEATER",               "Part 1 - The Grand Theater"),
    ("THE ATELIER",                     "Part 1 - The Atelier"),
    ("THE GALLERY",                     "Part 1 - The Gallery"),
    ("THE TOWER",                       "Part 1 - The Tower"),
    ("YINGHUO",                         "Part 1 - Yinghuo"),
    ("THE HOSPITAL",                    "Part 1 - The Hospital"),
    ("THE SKYDECK",                     "Part 1 - The Skydeck"),
    ("THE HOTEL ROOM AT NIGHT",         "Part 1 - The Hotel Room at Night"),
    ("AN ENDING SERVING AS A BEGINNING","Part 1 - An Ending Serving as a Beginning"),

    # Part Two: Cloud Light
    ("PART TWO",                        "Part 2"),
    ("PROLOGUE",                        "Part 2 - Prologue"),
    ("BOOK",                            "Part 2 - Book"),
    ("CRYSTAL",                         "Part 2 - Crystal"),
    ("MESSAGES",                        "Part 2 - Messages"),
    ("MEMBRANE",                        "Part 2 - Membrane"),
    ("MEDAL",                           "Part 2 - Medal"),
    ("ROCK",                            "Part 2 - Rock"),
    ("WINGS",                           "Part 2 - Wings"),
    ("SHIP",                            "Part 2 - Ship"),
    ("WIND",                            "Part 2 - Wind"),
    ("SAND",                            "Part 2 - Sand"),
    ("STARS",                           "Part 2 - Stars"),
    ("MORNING",                         "Part 2 - Morning"),
    ("A BEGINNING SERVING AS AN END",   "Part 2 - A Beginning Serving as an End"),

    # Part Three: Gale Wings
    ("PART THREE",                      "Part 3"),
    ("PROLOGUE",                        "Part 3 - Prologue"),
    ("RUDY",                            "Part 3 - Rudy"),
    ("CHANIA",                          "Part 3 - Chania"),
    ("REINI",                           "Part 3 - Reini (1)"),
    ("LUOYING",                         "Part 3 - Luoying (1)"),
    ("GIELLE",                          "Part 3 - Gielle"),
    ("PIERRE",                          "Part 3 - Pierre"),
    ("SORIN",                           "Part 3 - Sorin"),
    ("LUOYING",                         "Part 3 - Luoying (2)"),
    ("REINI",                           "Part 3 - Reini (2)"),
    ("ANKA",                            "Part 3 - Anka"),
    ("HANS",                            "Part 3 - Hans"),
    ("LUOYING",                         "Part 3 - Luoying (3)"),
    ("AN ENDING BUT ALSO A BEGINNING",  "Part 3 - An Ending but also a Beginning"),
]

# Skip TOC (first ~265 lines)
MIN_BODY_LINE = 265


def find_section_starts(lines: list[str]) -> list[tuple[int, str]]:
    """Find each section heading in the body text, in order."""
    results = []
    used_lines: set[int] = set()

    for search_key, label in SECTIONS:
        found = False
        # Start searching after the last found line to handle repeated titles
        search_start = max(MIN_BODY_LINE, results[-1][0] + 1) if results else MIN_BODY_LINE
        for i in range(search_start, len(lines)):
            if i in used_lines:
                continue
            stripped = lines[i].strip().rstrip('\r')
            if stripped == search_key:
                results.append((i, label))
                used_lines.add(i)
                found = True
                break
        if not found:
            print(f"  WARNING: could not find '{search_key}' for '{label}'",
                  file=sys.stderr)

    return results  # Already in order since we search forward


def split_book(dry_run: bool = False) -> None:
    if not BOOK_PATH.exists():
        print(f"ERROR: {BOOK_PATH} not found", file=sys.stderr)
        sys.exit(1)

    text = BOOK_PATH.read_text(encoding="utf-8")
    lines = text.split("\n")

    section_starts = find_section_starts(lines)

    if not section_starts:
        print("ERROR: no sections found!", file=sys.stderr)
        sys.exit(1)

    # Merge PART markers into their first chapter:
    # "Part 1" label is just a marker; its content goes up to the Prologue.
    # We keep Part markers as separate tiny files for structure.

    # Build section content
    chunks = []
    for idx, (start_line, label) in enumerate(section_starts):
        if idx + 1 < len(section_starts):
            end_line = section_starts[idx + 1][0]
        else:
            end_line = len(lines)
        content = "\n".join(lines[start_line:end_line]).strip()
        chunks.append((label, content))

    # Front matter
    front_matter = "\n".join(lines[:section_starts[0][0]]).strip()

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  Vagabonds — {len(chunks)} sections")
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
    parser = argparse.ArgumentParser(description="Split Vagabonds")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
