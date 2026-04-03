"""
split_broken_stars.py
---------------------
Dedicated splitter for "Broken Stars" — a Chinese SF anthology.
The main split_books.py cannot handle this book because it's a short
story collection, not a novel with chapter headings.

This script splits the anthology into individual stories and essays
using known section markers (author names + story title lines).

Usage:
    python scripts/split_broken_stars.py --dry-run
    python scripts/split_broken_stars.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "China" / "Broken Stars.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "China" / "Broken Stars"

# ---------------------------------------------------------------------------
# Story / essay definitions  (in order of appearance in the text)
# ---------------------------------------------------------------------------
# Each entry: (search_key, display_title)
#   search_key: first ALL-CAPS word(s) of the story title as they appear in
#               the body text (after the TOC).  Multi-line titles use just
#               the first line.
#   display_title: clean filename-safe title for output.

SECTIONS = [
    # Editor's introduction
    ("INTRODUCTION",           "Introduction"),

    # Stories
    ("GOODNIGHT,",             "Goodnight Melancholy - Xia Jia"),
    ("MOONLIGHT",              "Moonlight - Liu Cixin"),
    ("BROKEN STARS",           "Broken Stars - Tang Fei"),
    ("SUBMARINES",             "Submarines - Han Song"),
    ("SALINGER AND",           "Salinger and the Koreans - Han Song"),
    ("UNDER A",                "Under a Dangling Sky - Cheng Jingbo"),
    ("WHAT HAS PASSED",        "What Has Passed Shall in Kinder Light Appear - Baoshu"),
    ("THE NEW YEAR TRAIN",     "The New Year Train - Hao Jingfang"),
    ("THE ROBOT WHO LIKED",    "The Robot Who Liked to Tell Tall Tales - Fei Dao"),
    ("THE SNOW OF",            "The Snow of Jinyang - Zhang Ran"),
    ("THE RESTAURANT",         "The Restaurant at the End of the Universe Laba Porridge - Anna Wu"),
    ("THE FIRST",              "The First Emperors Games - Ma Boyong"),
    ("REFLECTION",             "Reflection - Gu Shi"),
    ("THE BRAIN BOX",          "The Brain Box - Regina Kanyu Wang"),
    ("COMING OF THE LIGHT",    "Coming of the Light - Chen Qiufan"),
    ("A HISTORY OF",           "A History of Future Illnesses - Chen Qiufan"),

    # Essays
    ("A BRIEF INTRODUCTION",   "Essay - A Brief Introduction to Chinese SF and Fandom - Regina Kanyu Wang"),
    ("A NEW CONTINENT",        "Essay - A New Continent for China Scholars - Mingwei Song"),
    ("SCIENCE FICTION: EMBARRASSING", "Essay - Science Fiction Embarrassing No More - Fei Dao"),
]

# Author bio sections that precede stories.  We use these to find where
# the author bio + editor note block starts (so we can include it with
# the story, or skip it — configurable).
AUTHOR_MARKERS = [
    "XIA JIA", "LIU CIXIN", "TANG FEI", "HAN SONG", "CHENG JINGBO",
    "BAOSHU", "HAO JINGFANG", "FEI DAO", "ZHANG RAN", "ANNA WU",
    "MA BOYONG", "GU SHI", "REGINA KANYU WANG", "CHEN QIUFAN",
]

# Minimum line number to start searching (skip the TOC)
MIN_BODY_LINE = 250


def find_section_starts(lines: list[str]) -> list[tuple[int, str]]:
    """
    For each section in SECTIONS, find the line number where it starts.
    Returns a sorted list of (line_number, display_title).
    """
    results = []
    used_lines: set[int] = set()

    for search_key, title in SECTIONS:
        found = False
        for i in range(MIN_BODY_LINE, len(lines)):
            if i in used_lines:
                continue
            stripped = lines[i].strip()
            if stripped.startswith(search_key):
                results.append((i, title))
                used_lines.add(i)
                found = True
                break
        if not found:
            print(f"  WARNING: could not find '{search_key}' for '{title}'",
                  file=sys.stderr)

    results.sort(key=lambda x: x[0])
    return results


def find_author_bio_starts(lines: list[str]) -> dict[int, str]:
    """
    Find all author bio section starts after the TOC.
    Returns {line_number: author_name}.
    """
    bios = {}
    for i in range(MIN_BODY_LINE, len(lines)):
        stripped = lines[i].strip().rstrip('\r')
        if stripped in AUTHOR_MARKERS:
            bios[i] = stripped
    return bios


def split_anthology(dry_run: bool = False) -> None:
    if not BOOK_PATH.exists():
        print(f"ERROR: {BOOK_PATH} not found", file=sys.stderr)
        sys.exit(1)

    text = BOOK_PATH.read_text(encoding="utf-8")
    lines = text.split("\n")

    section_starts = find_section_starts(lines)
    author_bios = find_author_bio_starts(lines)

    if not section_starts:
        print("ERROR: no sections found!", file=sys.stderr)
        sys.exit(1)

    # For each section, determine its boundaries.
    # The section runs from its start line to just before the NEXT author bio
    # or section start (whichever comes first), or to the start of the
    # copyright notices at the end.

    # Find the copyright/acknowledgments section (starts with story credits)
    copyright_line = len(lines)
    for i in range(len(lines) - 1, 0, -1):
        stripped = lines[i].strip()
        if stripped.startswith("Essays:"):
            # This is in the credits section
            # Look backwards for the first credit line
            break
    # Find the first line that looks like a credit: "story title" (Chinese) by Author
    for i in range(len(lines)):
        if i > section_starts[-1][0] and re.match(
            r'^".*".*by\s', lines[i].strip()
        ):
            # Go back to find the blank lines before this block
            copyright_line = i
            while copyright_line > 0 and not lines[copyright_line - 1].strip():
                copyright_line -= 1
            break

    # Build the ordered list of all boundary points
    all_boundaries = set()
    for line_no, _ in section_starts:
        all_boundaries.add(line_no)
    for line_no in author_bios:
        all_boundaries.add(line_no)
    all_boundaries = sorted(all_boundaries)

    # For each story section, we include the author bio that precedes it.
    # Find the author bio line that comes before each section start.
    def find_preceding_author_bio(section_line: int) -> int | None:
        best = None
        for bio_line in sorted(author_bios.keys()):
            if bio_line < section_line:
                best = bio_line
            else:
                break
        return best

    # Compute output chunks
    chunks = []
    for idx, (start_line, title) in enumerate(section_starts):
        # Include author bio if it comes between this section and the previous one
        bio_line = find_preceding_author_bio(start_line)
        effective_start = start_line

        if bio_line is not None:
            # Only include bio if it's not already claimed by a previous section
            prev_section_line = section_starts[idx - 1][0] if idx > 0 else 0
            if bio_line > prev_section_line:
                effective_start = bio_line

        # End line: next section's effective start (or next author bio, or copyright)
        if idx + 1 < len(section_starts):
            next_start = section_starts[idx + 1][0]
            # Check if there's an author bio before the next section
            next_bio = find_preceding_author_bio(next_start)
            if next_bio and next_bio > start_line:
                end_line = next_bio
            else:
                end_line = next_start
        else:
            end_line = copyright_line

        content = "\n".join(lines[effective_start:end_line]).strip()
        chunks.append((title, content))

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  Broken Stars — {len(chunks)} sections")
        print(f"{'=' * 60}")
        for title, content in chunks:
            print(f"  {title}  ({len(content):,} chars)")
        print()
        return

    # Write output files
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for title, content in chunks:
        safe_name = re.sub(r'[<>:"/\\|?*]', '', title)
        out_path = OUTPUT_DIR / f"{safe_name}.txt"
        out_path.write_text(content, encoding="utf-8")
        print(f"  wrote {out_path.name}  ({len(content):,} chars)")

    # Write front matter (everything before first author bio)
    first_boundary = min(
        section_starts[0][0],
        min(author_bios.keys()) if author_bios else section_starts[0][0],
    )
    front_matter = "\n".join(lines[:first_boundary]).strip()
    if front_matter:
        fm_path = OUTPUT_DIR / "front_matter.txt"
        fm_path.write_text(front_matter, encoding="utf-8")
        print(f"  wrote front_matter.txt  ({len(front_matter):,} chars)")

    print(f"\n  Done: {len(chunks)} sections written to {OUTPUT_DIR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split Broken Stars anthology")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_anthology(dry_run=args.dry_run)
