"""
split_quantum_thief.py
-----------------------
Dedicated splitter for "The Quantum Thief" by Hannu Rajaniemi.
The main split_books.py cannot handle this because:
  - Chapter titles in the body are bare ALL-CAPS without numbers
    ("THE THIEF AND THE PRISONER'S DILEMMA")
  - The TOC uses "1: THE THIEF AND..." format which could conflict
  - Interludes are just "Interlude" with no distinguishing text

Structure:
  21 numbered chapters + 7 interludes = 28 sections

Usage:
    python scripts/split_quantum_thief.py --dry-run
    python scripts/split_quantum_thief.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "Finland" / "Quantum Thief.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "Finland" / "Quantum Thief"

# Sections in body order.  (search_key, display_label)
# For chapters: search_key is the ALL-CAPS title as it appears on its own line.
# For interludes: "Interlude" appears as a bare line; they are numbered for output.
SECTIONS = [
    ("THE THIEF AND THE PRISONER'S DILEMMA",  "Chapter 01 - The Thief and the Prisoners Dilemma"),
    ("THE THIEF AND THE ARCHONS",             "Chapter 02 - The Thief and the Archons"),
    ("THE DETECTIVE AND THE CHOCOLATE DRESS",  "Chapter 03 - The Detective and the Chocolate Dress"),
    ("Interlude",                              "Interlude 1"),
    ("THE THIEF AND THE BEGGAR",              "Chapter 04 - The Thief and the Beggar"),
    ("THE DETECTIVE AND THE ZOKU",            "Chapter 05 - The Detective and the Zoku"),
    ("Interlude",                              "Interlude 2"),
    ("THE THIEF AND PAUL SERNINE",            "Chapter 06 - The Thief and Paul Sernine"),
    ("THE DETECTIVE AND HIS FATHER",          "Chapter 07 - The Detective and His Father"),
    ("Interlude",                              "Interlude 3"),
    ("THE THIEF AND THE PIRATES",             "Chapter 08 - The Thief and the Pirates"),
    ("THE DETECTIVE AND THE LETTER",          "Chapter 09 - The Detective and the Letter"),
    ("THE THIEF AND THE SECOND FIRST DATE",   "Chapter 10 - The Thief and the Second First Date"),
    ("Interlude",                              "Interlude 4"),
    ("THE THIEF AND THE TZADDIKIM",           "Chapter 11 - The Thief and the Tzaddikim"),
    ("THE DETECTIVE AND CARPE DIEM",          "Chapter 12 - The Detective and Carpe Diem"),
    ("Interlude",                              "Interlude 5"),
    ("THE THIEF IN THE UNDERWORLD",           "Chapter 13 - The Thief in the Underworld"),
    ("THE DETECTIVE AND THE ARCHITECT",       "Chapter 14 - The Detective and the Architect"),
    ("THE THIEF AND THE GODDESS",             "Chapter 15 - The Thief and the Goddess"),
    ("THE THIEF AND MEMORY",                  "Chapter 16 - The Thief and Memory"),
    ("Interlude",                              "Interlude 6"),
    ("THE DETECTIVE AND THE GORDIAN KNOT",    "Chapter 17 - The Detective and the Gordian Knot"),
    ("THE THIEF AND THE KING",               "Chapter 18 - The Thief and the King"),
    ("THE DETECTIVE AND THE RING",            "Chapter 19 - The Detective and the Ring"),
    ("TWO THIEVES AND A DETECTIVE",           "Chapter 20 - Two Thieves and a Detective"),
    ("THE THIEF AND THE STOLEN GOODBYE",      "Chapter 21 - The Thief and the Stolen Goodbye"),
    ("Interlude",                              "Interlude 7"),
]

# Skip TOC (first ~170 lines)
MIN_BODY_LINE = 170


def find_section_starts(lines: list[str]) -> list[tuple[int, str]]:
    """Find each section heading in the body text, searching forward."""
    results = []
    used_lines: set[int] = set()

    for search_key, label in SECTIONS:
        found = False
        # Start searching after the last found section
        search_start = max(MIN_BODY_LINE, results[-1][0] + 1) if results else MIN_BODY_LINE
        for i in range(search_start, len(lines)):
            if i in used_lines:
                continue
            stripped = lines[i].strip().rstrip('\r')
            # Normalize smart quotes for comparison
            normalized = stripped.replace('\u2019', "'").replace('\u2018', "'")
            search_normalized = search_key.replace('\u2019', "'").replace('\u2018', "'")
            if normalized == search_normalized or stripped == search_key:
                results.append((i, label))
                used_lines.add(i)
                found = True
                break
        if not found:
            print(f"  WARNING: could not find '{search_key}' for '{label}'",
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
        print(f"  The Quantum Thief — {len(chunks)} sections")
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
    parser = argparse.ArgumentParser(description="Split The Quantum Thief")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
