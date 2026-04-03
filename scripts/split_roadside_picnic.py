"""
split_roadside_picnic.py
-------------------------
Dedicated splitter for "Roadside Picnic" by Arkady and Boris Strugatsky.
The main split_books.py cannot handle this book because chapter headings
are character name/age lines with OCR spacing artifacts:
    "1.  REDRICK  SCHUHART,  AGE  23,"

Structure:
  Introduction (by Theodore Sturgeon)
  Chapter 1 - Redrick Schuhart Age 23
  Chapter 2 - Redrick Schuhart Age 28
  Chapter 3 - Richard H Noonan Age 51
  Chapter 4 - Redrick Schuhart Age 31

Usage:
    python scripts/split_roadside_picnic.py --dry-run
    python scripts/split_roadside_picnic.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "Russia" / "Roadside Picnic.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "Russia" / "Roadside Picnic"

# Sections: (regex_pattern, display_label)
SECTIONS = [
    (r"^INTRODUCTION$",
     "Introduction"),
    (r"^1\.\s+REDRICK\s+SCHUHART",
     "Chapter 1 - Redrick Schuhart Age 23"),
    (r"^2\.\s+REDRICK\s+SCHUHART",
     "Chapter 2 - Redrick Schuhart Age 28"),
    (r"^3\.\s+RICHARD\s+H\.?\s+NOONAN",
     "Chapter 3 - Richard H Noonan Age 51"),
    (r"^4\.\s+REDRICK\s+SCHUHART",
     "Chapter 4 - Redrick Schuhart Age 31"),
]

MIN_BODY_LINE = 0  # Introduction is near the top


def find_section_starts(lines: list[str]) -> list[tuple[int, str]]:
    """Find each section heading using regex patterns."""
    results = []

    for pattern, label in SECTIONS:
        regex = re.compile(pattern)
        found = False
        # Start after last found section
        search_start = results[-1][0] + 1 if results else MIN_BODY_LINE
        for i in range(search_start, len(lines)):
            stripped = lines[i].strip().rstrip('\r')
            # Normalize multiple spaces to single
            normalized = re.sub(r'\s+', ' ', stripped)
            if regex.match(normalized):
                results.append((i, label))
                found = True
                break
        if not found:
            print(f"  WARNING: could not find pattern '{pattern}' for '{label}'",
                  file=sys.stderr)

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
        print(f"  Roadside Picnic — {len(chunks)} sections")
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
    parser = argparse.ArgumentParser(description="Split Roadside Picnic")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
