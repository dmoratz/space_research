"""
split_orbital_cloud.py
----------------------
Dedicated splitter for "Orbital Cloud" by Taiyo Fujii.
The main split_books.py cannot handle this book because its chapters
use bare "N Title" format (no period, single space) which is too
aggressive for a generic pattern.

Structure:
  Prologue  (date + location header)
  Part One / Part Two / Part Three  (section markers only)
  15 numbered chapters: "1 Erratic Debris", "2 A Proclamation", etc.
  Epilogue  (date + location header)

Usage:
    python scripts/split_orbital_cloud.py --dry-run
    python scripts/split_orbital_cloud.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "Japan" / "Orbital Cloud.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "Japan" / "Orbital Cloud"

# Sections in order of appearance (search_key, display_label)
# search_key: the first words of the line as it appears in the body text
SECTIONS = [
    ("August 15, 2015",    "Prologue"),
    ("1 Erratic Debris",   "Chapter 1 - Erratic Debris"),
    ("2 A Proclamation",   "Chapter 2 - A Proclamation"),
    ("3 The Launch",       "Chapter 3 - The Launch"),
    ("4 Standby",          "Chapter 4 - Standby"),
    ("5 Evasion",          "Chapter 5 - Evasion"),
    ("6 Discovery/Pursuit","Chapter 6 - Discovery Pursuit"),
    ("7 War",              "Chapter 7 - War"),
    ("8 The Team",         "Chapter 8 - The Team"),
    ("9 Great Leap",       "Chapter 9 - Great Leap"),
    ("10 Riot",            "Chapter 10 - Riot"),
    ("11 Unity",           "Chapter 11 - Unity"),
    ("12 Seed Pod",        "Chapter 12 - Seed Pod"),
    ("13 Pier 37",         "Chapter 13 - Pier 37"),
    ("14 Team Seattle",    "Chapter 14 - Team Seattle"),
    ("15 Meteors",         "Chapter 15 - Meteors"),
    ("December 25, 2022",  "Epilogue"),
]

# Skip the TOC (first ~260 lines)
MIN_BODY_LINE = 260


def find_section_starts(lines: list[str]) -> list[tuple[int, str]]:
    """Find each section heading in the body text."""
    results = []
    used_lines: set[int] = set()

    for search_key, label in SECTIONS:
        found = False
        for i in range(MIN_BODY_LINE, len(lines)):
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

    results.sort(key=lambda x: x[0])
    return results


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
        print(f"  Orbital Cloud — {len(chunks)} sections")
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
    parser = argparse.ArgumentParser(description="Split Orbital Cloud")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
