"""
split_aelita.py
---------------
Dedicated splitter for "Aelita" by Alexei Tolstoi.
The main split_books.py cannot handle this book because it uses
ALL-CAPS titled chapters without numbers (e.g., "THE WORKSHOP",
"BLACK SKY", "THE DESCENT").

This script finds ALL-CAPS short lines (chapter headings) in the body
text and splits accordingly.

Usage:
    python scripts/split_aelita.py --dry-run
    python scripts/split_aelita.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "Russia" / "Aelita.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "Russia" / "Aelita"

# Expected chapter titles (ALL CAPS) in order of appearance.
# These are matched against stripped lines in the body text.
CHAPTERS = [
    "A STRANGE NOTICE",
    "THE WORKSHOP",
    "A FELLOW-TRAVELLER",
    "A SLEEPLESS NIGHT",
    "THE SAME NIGHT",
    "THE TAKE-OFF",
    "BLACK SKY",
    "THE DESCENT",
    "MARS",
    "THE DESERTED HOUSE",
    "THE SUNSET",
    "LOS LOOKS AT THE EARTH",
    "THE MARTIANS",
    "BEYOND THE MOUNTAINS",
    "SOATSERA",
    "IN THE AZURE COPSE",
    "REST",
    "THE BALL OF MIST",
    "ON THE STAIRS",
    "AELITA'S FIRST STORY",
    "A CHANCE DISCOVERY",
    "AELITA'S MORNING",
    "AELITA'S SECOND STORY",
    "GUSEV OBSERVES THE CITY",
    "TUSCOOB",
    "LOS IS ALONE",
    "THE SPELL",
    "THE SONG OF LONG AGO",
    "LOS FLIES TO GUSEV'S AID",
    "GUSEV'S ACTIVITIES",
    "EVENTS TAKE A NEW TURN",
    "THE COUNTER-ATTACK",
    "QUEEN MAGR'S LABYRINTH",
    "KHAO",
    "ESCAPE",
    "OBLIVION",
    "THE EARTH",
    "THE VOICE OF LOVE",
]

# Minimum line number to start searching (skip the TOC / front matter)
MIN_BODY_LINE = 220


def find_chapter_starts(lines: list[str]) -> list[tuple[int, str]]:
    """
    Find each chapter heading in the body text.
    Returns sorted list of (line_number, title_case_label).
    """
    results = []
    used_lines: set[int] = set()

    for chapter_title in CHAPTERS:
        found = False
        for i in range(MIN_BODY_LINE, len(lines)):
            if i in used_lines:
                continue
            stripped = lines[i].strip().rstrip('\r')
            if stripped == chapter_title:
                # Convert to Title Case for the label
                label = chapter_title.title()
                # Fix possessives: "Aelita'S" → "Aelita's"
                label = re.sub(r"'S\b", "'s", label)
                results.append((i, label))
                used_lines.add(i)
                found = True
                break
        if not found:
            print(f"  WARNING: could not find '{chapter_title}'",
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

    # Front matter: everything before the first chapter
    front_matter = "\n".join(lines[:chapter_starts[0][0]]).strip()

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  Aelita — {len(chunks)} chapters")
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
    parser = argparse.ArgumentParser(description="Split Aelita")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
