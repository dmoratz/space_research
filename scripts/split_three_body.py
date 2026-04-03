"""
split_three_body.py
-------------------
Dedicated splitter for "The Three Body Problem" (cleaned) by Cixin Liu.
The main split_books.py cannot handle this book because:
  1. The TOC extends past line 300, so TOC entries leak through
  2. Chapters use bare numbers on one line with titles on the next line
  3. The file contains a Dark Forest preview that should be excluded

Structure:
  Part I (chapters 1-3)
  Part II (chapters 4-20)
  Part III (chapters 21-35)
  Each chapter: bare number line, then title line a few lines later

Usage:
    python scripts/split_three_body.py --dry-run
    python scripts/split_three_body.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "China" / "The Three Body Problem_cleaned.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "China" / "The Three Body Problem_cleaned"

# Chapter titles (from the TOC)
CHAPTER_TITLES = {
    1: "The Madness Years",
    2: "Silent Spring",
    3: "Red Coast I",
    4: "The Frontiers of Science",
    5: "A Game of Pool",
    6: "The Shooter and the Farmer",
    7: "Three Body - King Wen of Zhou and the Long Night",
    8: "Ye Wenjie",
    9: "The Universe Flickers",
    10: "Da Shi",
    11: "Three Body - Mozi and Fiery Flames",
    12: "Red Coast II",
    13: "Red Coast III",
    14: "Red Coast IV",
    15: "Three Body - Copernicus Universal Football and Tri-Solar Day",
    16: "The Three-Body Problem",
    17: "Three Body - Newton Von Neumann the First Emperor and Tri-Solar Syzygy",
    18: "Meet-up",
    19: "Three Body - Einstein the Pendulum Monument and the Great Rip",
    20: "Three Body - Expedition",
    21: "Rebels of Earth",
    22: "Red Coast V",
    23: "Red Coast VI",
    24: "Rebellion",
    25: "The Deaths of Lei Zhicheng and Yang Weining",
    26: "No One Repents",
    27: "Evans",
    28: "The Second Red Coast Base",
    29: "The Earth-Trisolaris Movement",
    30: "Two Protons",
    31: "Operation Guzheng",
    32: "Trisolaris - The Listener",
    33: "Trisolaris - Sophon",
    34: "Bugs",
    35: "The Ruins",
}

# Parts and their start search patterns
PARTS = [
    (r"^Part I$", "Part I"),
    (r"^Part II$", "Part II"),
    (r"^Part III$", "Part III"),
]

# Body starts after line 690 (skip TOC and front matter)
MIN_BODY_LINE = 690

# End marker: stop before backmatter
END_MARKERS = ["We hope you enjoyed this book", "Author\u2019s Postscript"]


def find_sections(lines: list[str]) -> list[tuple[int, str]]:
    """Find all Parts and Chapters in the body text."""
    results = []

    # Find Parts
    for pattern, label in PARTS:
        regex = re.compile(pattern)
        for i in range(MIN_BODY_LINE, len(lines)):
            stripped = lines[i].strip().rstrip('\r')
            if regex.match(stripped):
                results.append((i, label))
                break

    # Find Chapters (bare number lines)
    for ch_num in range(1, 36):
        ch_str = str(ch_num)
        for i in range(MIN_BODY_LINE, len(lines)):
            stripped = lines[i].strip().rstrip('\r')
            if stripped == ch_str:
                # Verify: next non-blank line should be the chapter title
                title = CHAPTER_TITLES.get(ch_num, "")
                label = f"Chapter {ch_num} - {title}" if title else f"Chapter {ch_num}"
                results.append((i, label))
                break

    results.sort(key=lambda x: x[0])
    return results


def find_end_line(lines: list[str]) -> int:
    """Find where the story content ends (before backmatter/preview)."""
    # Look for the "~" marker or "We hope you enjoyed" text
    for i in range(len(lines) - 1, MIN_BODY_LINE, -1):
        stripped = lines[i].strip()
        if stripped == "~":
            return i + 1
        for marker in END_MARKERS:
            if stripped.startswith(marker):
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

    sections = find_sections(lines)
    end_line = find_end_line(lines)

    if not sections:
        print("ERROR: no sections found!", file=sys.stderr)
        sys.exit(1)

    # Build section content
    chunks = []
    for idx, (start_line, label) in enumerate(sections):
        if idx + 1 < len(sections):
            section_end = sections[idx + 1][0]
        else:
            section_end = end_line
        content = "\n".join(lines[start_line:section_end]).strip()
        chunks.append((label, content))

    # Front matter
    front_matter = "\n".join(lines[:sections[0][0]]).strip()

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  The Three Body Problem — {len(chunks)} sections")
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
    parser = argparse.ArgumentParser(description="Split The Three Body Problem")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
