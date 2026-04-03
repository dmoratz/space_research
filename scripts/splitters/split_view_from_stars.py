"""
split_view_from_stars.py
------------------------
Dedicated splitter for "A View from the Stars" by Cixin Liu.
This is a collection of 19 essays/stories, each preceded by an
ALL-CAPS title line and a "TRANSLATED BY" credit line.

The main split_books.py cannot handle this book because the ALL-CAPS
titles are short and could match inline text, and there are no chapter
numbers.

Usage:
    python scripts/split_view_from_stars.py --dry-run
    python scripts/split_view_from_stars.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "China" / "A View from the Stars.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "China" / "A View from the Stars"

# Sections in order of appearance.
# (search_key, display_title)
# search_key: the ALL-CAPS title as it appears on a single line in the body text.
SECTIONS = [
    ("TIME ENOUGH FOR LOVE",
     "Time Enough for Love"),
    ("WHALE SONG",
     "Whale Song"),
    ("A JOURNEY IN SEARCH OF HOME",
     "A Journey in Search of Home"),
    ("THE MESSENGER",
     "The Messenger"),
    ("THIRTY YEARS OF MAKING MAGIC OUT OF ORDINARINESS",
     "Thirty Years of Making Magic Out of Ordinariness"),
    ("BUTTERFLY",
     "Butterfly"),
    ("ONE AND ONE HUNDRED THOUSAND EARTHS",
     "One and One Hundred Thousand Earths"),
    ("ON FINISHING DEATH\u2019S END, THE LAST BOOK IN THE REMEMBRANCE OF EARTH\u2019S PAST TRILOGY",
     "On Finishing Deaths End"),
    ("THE BATTLE BETWEEN SCI-FI AND FANTASY",
     "The Battle Between Sci-Fi and Fantasy"),
    ("THE \u201CCHURCH\u201D OF SCI-FI",
     "The Church of Sci-Fi"),
    ("END OF THE MICROCOSMOS",
     "End of the Microcosmos"),
    ("POETIC SCIENCE FICTION",
     "Poetic Science Fiction"),
    ("CIVILIZATION\u2019S EXPANSION IN REVERSE",
     "Civilizations Expansion in Reverse"),
    ("DESTINY",
     "Destiny"),
    ("THE DARK FOREST THEORY",
     "The Dark Forest Theory"),
    ("THE WORLD IN FIFTY YEARS",
     "The World in Fifty Years"),
    ("HEARD IT IN THE MORNING",
     "Heard It in the Morning"),
    ("ON BALL LIGHTNING",
     "On Ball Lightning"),
    ("WE\u2019RE SCI-FI FANS",
     "Were Sci-Fi Fans"),
]

# End-of-content marker (backmatter starts here)
END_MARKER = "ALSO BY CIXIN LIU"

# Skip TOC / front matter (first ~70 lines)
MIN_BODY_LINE = 70


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
            # Handle both smart quotes and straight quotes
            normalized = stripped.replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
            search_normalized = search_key.replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
            if normalized == search_normalized or stripped == search_key:
                results.append((i, label))
                used_lines.add(i)
                found = True
                break
        if not found:
            print(f"  WARNING: could not find '{search_key}' for '{label}'",
                  file=sys.stderr)

    results.sort(key=lambda x: x[0])
    return results


def find_end_line(lines: list[str], after_line: int) -> int:
    """Find where the backmatter starts (ALSO BY CIXIN LIU)."""
    for i in range(after_line, len(lines)):
        stripped = lines[i].strip().rstrip('\r')
        if stripped == END_MARKER:
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

    section_starts = find_section_starts(lines)

    if not section_starts:
        print("ERROR: no sections found!", file=sys.stderr)
        sys.exit(1)

    # Find end of last section (before backmatter)
    end_of_content = find_end_line(lines, section_starts[-1][0])

    # Build section content
    chunks = []
    for idx, (start_line, label) in enumerate(section_starts):
        if idx + 1 < len(section_starts):
            end_line = section_starts[idx + 1][0]
        else:
            end_line = end_of_content
        content = "\n".join(lines[start_line:end_line]).strip()
        chunks.append((label, content))

    # Front matter
    front_matter = "\n".join(lines[:section_starts[0][0]]).strip()

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  A View from the Stars — {len(chunks)} sections")
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
    parser = argparse.ArgumentParser(description="Split A View from the Stars")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
