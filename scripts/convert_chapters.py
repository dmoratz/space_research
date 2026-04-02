"""
convert_chapters.py
-------------------
Converts .docx chapter files to .txt files in-place (alongside originals).

Walks the book data directory and converts any .docx file that doesn't
already have a corresponding .txt.  Skips files that have already been
converted so it's safe to re-run.

Usage:
    # Convert all books under a specific country:
    python scripts/convert_chapters.py --country US

    # Convert everything:
    python scripts/convert_chapters.py --all

    # Dry run — show what would be converted without writing:
    python scripts/convert_chapters.py --country US --dry-run

Expects the directory layout:
    data/books/<Country>/<Book Title>/Chapter N_ Book Title.docx
"""

import argparse
import sys
from pathlib import Path

try:
    import docx
except ImportError:
    print(
        "ERROR: python-docx is required for .docx conversion.\n"
        "       Install it with:  pip install python-docx"
    )
    sys.exit(1)

# Project root is one level up from scripts/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOKS_DIR = PROJECT_ROOT / "data" / "books"


def docx_to_text(docx_path: Path) -> str:
    """Extract all paragraph text from a .docx file."""
    doc = docx.Document(str(docx_path))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


def convert_country(country_dir: Path, dry_run: bool = False) -> int:
    """
    Convert all .docx files under a country directory to .txt.
    Returns the number of files converted.
    """
    docx_files = sorted(country_dir.rglob("*.docx"))
    if not docx_files:
        print(f"  No .docx files found under {country_dir}")
        return 0

    converted = 0
    for docx_path in docx_files:
        txt_path = docx_path.with_suffix(".txt")

        if txt_path.exists():
            continue  # already converted

        if dry_run:
            print(f"  [dry-run] would convert: {docx_path.relative_to(BOOKS_DIR)}")
            converted += 1
            continue

        try:
            text = docx_to_text(docx_path)
            txt_path.write_text(text, encoding="utf-8")
            print(f"  ✓ {docx_path.relative_to(BOOKS_DIR)} → .txt ({len(text):,} chars)")
            converted += 1
        except Exception as e:
            print(f"  ✗ {docx_path.relative_to(BOOKS_DIR)}: {e}")

    return converted


def list_countries() -> list[str]:
    """Return sorted list of country folder names under data/books/."""
    if not BOOKS_DIR.exists():
        return []
    return sorted(
        d.name for d in BOOKS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )


def main():
    p = argparse.ArgumentParser(
        description="Convert .docx chapter files to .txt for Gemini analysis."
    )
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--country",
        help="Country folder name to convert (e.g. 'US', 'UK').",
    )
    group.add_argument(
        "--all", action="store_true",
        help="Convert all countries.",
    )
    p.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be converted without writing files.",
    )
    args = p.parse_args()

    if not BOOKS_DIR.exists():
        print(f"ERROR: books directory not found at {BOOKS_DIR}")
        sys.exit(1)

    countries = list_countries()
    if not countries:
        print(f"ERROR: no country folders found under {BOOKS_DIR}")
        sys.exit(1)

    if args.all:
        targets = countries
    else:
        country_dir = BOOKS_DIR / args.country
        if not country_dir.exists():
            print(f"ERROR: country folder '{args.country}' not found.")
            print(f"Available: {', '.join(countries)}")
            sys.exit(1)
        targets = [args.country]

    total = 0
    for country_name in targets:
        country_dir = BOOKS_DIR / country_name
        print(f"\n{'='*50}")
        print(f"Country: {country_name}")
        print(f"{'='*50}")
        n = convert_country(country_dir, dry_run=args.dry_run)
        total += n

    action = "would convert" if args.dry_run else "converted"
    print(f"\nDone — {action} {total} file(s)")


if __name__ == "__main__":
    main()
