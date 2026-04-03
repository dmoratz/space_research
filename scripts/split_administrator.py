"""
split_administrator.py
----------------------
Dedicated splitter for "Administrator" by Taku Mayumura.
This is a collection of 4 short stories, not a novel with chapter headings.

Usage:
    python scripts/split_administrator.py --dry-run
    python scripts/split_administrator.py
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOK_PATH = PROJECT_ROOT / "data" / "books" / "Japan" / "Administrator by Taku Mayumura.txt"
OUTPUT_DIR = PROJECT_ROOT / "data" / "books" / "Japan" / "Administrator by Taku Mayumura"

# Story titles as they appear in the body text (with indentation stripped)
STORIES = [
    ("The Flame and the Blossom", "The Flame and the Blossom"),
    ("A Distant Noon",            "A Distant Noon"),
    ("The Wind in the Ruins",     "The Wind in the Ruins"),
    ("Bound Janus",               "Bound Janus"),
]

# Marker for the end of story content (Contributors / copyright section)
END_MARKER = "Contributors"

# Skip TOC (first ~50 lines)
MIN_BODY_LINE = 50


def find_story_starts(lines: list[str]) -> list[tuple[int, str]]:
    """Find each story title in the body text (after the TOC)."""
    results = []
    used_lines: set[int] = set()

    for search_title, label in STORIES:
        found = False
        for i in range(MIN_BODY_LINE, len(lines)):
            if i in used_lines:
                continue
            stripped = lines[i].strip().rstrip('\r')
            if stripped == search_title:
                results.append((i, label))
                used_lines.add(i)
                found = True
                break
        if not found:
            print(f"  WARNING: could not find '{search_title}'",
                  file=sys.stderr)

    results.sort(key=lambda x: x[0])
    return results


def find_end_line(lines: list[str], after_line: int) -> int:
    """Find where the Contributors/copyright section starts."""
    for i in range(after_line, len(lines)):
        if lines[i].strip().rstrip('\r') == END_MARKER:
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

    story_starts = find_story_starts(lines)

    if not story_starts:
        print("ERROR: no stories found!", file=sys.stderr)
        sys.exit(1)

    # Find end of last story (before Contributors section)
    end_of_content = find_end_line(lines, story_starts[-1][0])

    # Build story content
    chunks = []
    for idx, (start_line, label) in enumerate(story_starts):
        if idx + 1 < len(story_starts):
            end_line = story_starts[idx + 1][0]
        else:
            end_line = end_of_content
        content = "\n".join(lines[start_line:end_line]).strip()
        chunks.append((label, content))

    # Front matter
    front_matter = "\n".join(lines[:story_starts[0][0]]).strip()

    if dry_run:
        print(f"\n{'=' * 60}")
        print(f"  Administrator — {len(chunks)} stories")
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

    print(f"\n  Done: {len(chunks)} stories written to {OUTPUT_DIR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split Administrator")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be split without writing files")
    args = parser.parse_args()
    split_book(dry_run=args.dry_run)
