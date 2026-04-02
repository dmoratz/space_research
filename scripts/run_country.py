"""
run_country.py
--------------
Master script that orchestrates the full analysis pipeline for one country:

  1. Lists available country folders under data/books/
  2. Prompts you to pick one (or accepts --country on the CLI)
  3. Converts any .docx chapters → .txt  (calls convert_chapters logic)
  4. For each book folder, runs analyze_book against all .txt chapters
  5. All results land in a single project-wide CSV (data/results.csv)

Usage:
    # Interactive — shows a menu of available countries:
    python scripts/run_country.py

    # Direct — skip the prompt:
    python scripts/run_country.py --country US

    # Resume after a crash:
    python scripts/run_country.py --country US --resume

Environment:
    GEMINI_API_KEY   – required
    GEMINI_MODEL     – optional (default: gemini-2.0-flash)
"""

import argparse
import re
import sys
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOKS_DIR = PROJECT_ROOT / "data" / "books"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "nlp_analysis_results.csv"

# Import sibling modules
sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert_chapters import convert_country, list_countries
from analyze_book import (
    create_gemini_client,
    load_questions,
    build_csv_columns,
    load_completed_chapters,
    read_chapter_file,
    check_chapter_size,
    estimate_tokens,
    analyze_chapter,
    chapter_rows_to_wide,
    write_wide_csv,
    QUESTIONS_FILE,
    DEFAULT_MODEL,
)


# ---------------------------------------------------------------------------
# Chapter label extraction
# ---------------------------------------------------------------------------

# Matches filenames like "Chapter 1_ The Martian.txt" or "CHAPTER 3_ The Martian.txt"
CHAPTER_RE = re.compile(
    r"^(?P<label>chapter\s+\d+)",
    re.IGNORECASE,
)


def extract_chapter_label(filename: str) -> str:
    """
    Pull a clean chapter label from a filename.
      "Chapter 1_ The Martian.txt"  →  "Chapter 1"
      "CHAPTER 3_ The Martian.txt"  →  "Chapter 3"
      "ch05.txt"                    →  "ch05"
    """
    m = CHAPTER_RE.match(filename)
    if m:
        # Normalize to "Chapter N"
        raw = m.group("label")
        parts = raw.split()
        return f"Chapter {parts[1]}"
    # Fallback: use the stem
    return Path(filename).stem


def natural_sort_key(path: Path):
    """Sort key that handles 'Chapter 1', 'Chapter 2', ..., 'Chapter 10' correctly."""
    parts = re.split(r"(\d+)", path.name)
    return [int(p) if p.isdigit() else p.lower() for p in parts]


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_books(country_dir: Path) -> list[dict]:
    """
    Find all book folders under a country directory.
    Returns list of dicts with 'title' and 'path'.
    """
    books = []
    for d in sorted(country_dir.iterdir()):
        if d.is_dir() and not d.name.startswith("."):
            books.append({"title": d.name, "path": d})
    return books


def discover_chapters(book_dir: Path) -> list[Path]:
    """
    Find all .txt chapter files in a book folder.
    Returns paths sorted in natural chapter order.
    """
    txt_files = list(book_dir.glob("*.txt"))
    return sorted(txt_files, key=natural_sort_key)


# ---------------------------------------------------------------------------
# Interactive country selection
# ---------------------------------------------------------------------------

def prompt_for_country() -> str:
    """Show available countries and let the user pick."""
    countries = list_countries()
    if not countries:
        print(f"ERROR: no country folders found under {BOOKS_DIR}")
        sys.exit(1)

    print("\nAvailable countries:")
    for i, c in enumerate(countries, 1):
        # Count books in each
        book_count = len([
            d for d in (BOOKS_DIR / c).iterdir()
            if d.is_dir() and not d.name.startswith(".")
        ])
        print(f"  {i}. {c}  ({book_count} book{'s' if book_count != 1 else ''})")

    while True:
        choice = input("\nEnter country name or number: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(countries):
                return countries[idx]
        elif choice in countries:
            return choice
        print("Invalid choice, try again.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="Run the full analysis pipeline for one country's books."
    )
    p.add_argument(
        "--country",
        help="Country folder name (e.g. 'US'). If omitted, shows an interactive menu.",
    )
    p.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT,
        help=f"Output CSV path (default: {DEFAULT_OUTPUT.relative_to(PROJECT_ROOT)}).",
    )
    p.add_argument(
        "--resume", action="store_true",
        help="Skip books/chapters already in the output CSV.",
    )
    p.add_argument(
        "--one-by-one", action="store_true",
        help="Send each question as a separate API call (debug mode).",
    )
    p.add_argument(
        "--model", default=None,
        help="Gemini model name override.",
    )
    p.add_argument(
        "--api-key", default=None,
        help="Gemini API key (or set GEMINI_API_KEY env var).",
    )
    return p.parse_args()


def main():
    args = parse_args()

    # ---------- Pick country ----------
    if args.country:
        country_name = args.country
        country_dir = BOOKS_DIR / country_name
        if not country_dir.exists():
            print(f"ERROR: country folder '{country_name}' not found at {country_dir}")
            available = list_countries()
            if available:
                print(f"Available: {', '.join(available)}")
            sys.exit(1)
    else:
        country_name = prompt_for_country()
        country_dir = BOOKS_DIR / country_name

    print(f"\n{'='*60}")
    print(f"  Country: {country_name}")
    print(f"{'='*60}")

    # ---------- Step 1: Convert .docx → .txt ----------
    print("\n--- Step 1: Converting .docx → .txt ---")
    n_converted = convert_country(country_dir)
    if n_converted > 0:
        print(f"  Converted {n_converted} file(s)")
    else:
        print("  All chapters already converted (or no .docx files)")

    # ---------- Step 2: Discover books & chapters ----------
    books = discover_books(country_dir)
    if not books:
        print(f"\nERROR: no book folders found under {country_dir}")
        sys.exit(1)

    print(f"\nFound {len(books)} book(s):")
    for b in books:
        chapters = discover_chapters(b["path"])
        print(f"  • {b['title']}  ({len(chapters)} chapter(s))")

    # ---------- Step 3: Set up Gemini + questions ----------
    model_name = args.model or DEFAULT_MODEL
    client = create_gemini_client(args.api_key)
    questions = load_questions()
    csv_columns = build_csv_columns(questions)
    print(f"\nLoaded {len(questions)} questions")

    # Resume support
    completed = set()
    if args.resume:
        completed = load_completed_chapters(args.output)
        if completed:
            print(f"Resume mode: {len(completed)} chapter(s) already in output")

    # ---------- Step 4: Analyze ----------
    print(f"\n--- Step 2: Analyzing with Gemini ({model_name}) ---")
    total_chapters = 0
    total_errors = 0
    total_unmatched = 0

    for book_idx, book in enumerate(books, 1):
        book_title = book["title"]
        chapters = discover_chapters(book["path"])

        if not chapters:
            print(f"\n[Book {book_idx}/{len(books)}] {book_title} — no .txt chapters, skipping")
            continue

        print(f"\n{'─'*60}")
        print(f"[Book {book_idx}/{len(books)}] {book_title}  ({len(chapters)} chapters)")
        print(f"{'─'*60}")

        for chap_idx, chap_path in enumerate(chapters, 1):
            chapter_label = extract_chapter_label(chap_path.name)

            # Resume check
            if (country_name, book_title, chapter_label) in completed:
                print(f"  [{chap_idx}/{len(chapters)}] {chapter_label} — already done")
                continue

            print(f"  [{chap_idx}/{len(chapters)}] {chapter_label}")

            # Read
            try:
                content = read_chapter_file(chap_path)
            except ValueError as e:
                print(f"    ERROR reading: {e}")
                continue

            if content.text is not None and not content.text.strip():
                print(f"    WARNING: empty file, skipping")
                continue

            # Size check
            check_chapter_size(content, chapter_label)
            tokens_est = estimate_tokens(content)
            if content.is_pdf:
                size_kb = len(content.pdf_bytes) / 1024
                print(f"    PDF {size_kb:,.0f} KB (~{tokens_est:,} tokens)")
            else:
                words = len(content.text.split())
                print(f"    {words:,} words (~{tokens_est:,} tokens)")

            # Analyze
            chapter_results = analyze_chapter(
                client, content, chapter_label, book_title, questions,
                model_name=model_name, one_by_one=args.one_by_one,
            )

            # Write immediately (checkpoint)
            wide_row = chapter_rows_to_wide(
                chapter_results, country_name, book_title, chapter_label, questions,
            )
            write_wide_csv(wide_row, args.output, csv_columns)
            total_chapters += 1

            # Track issues
            for r in chapter_results:
                if r["answer"].startswith(("API_ERROR", "ERROR", "MISSING")):
                    total_errors += 1
                elif r["answer"].startswith("[UNMATCHED]"):
                    total_unmatched += 1

    # ---------- Summary ----------
    print(f"\n{'='*60}")
    print(f"  Country:  {country_name}")
    print(f"  Books:    {len(books)}")
    print(f"  Chapters: {total_chapters} written to {args.output}")
    if total_errors:
        print(f"  ⚠ {total_errors} question(s) hit errors")
    if total_unmatched:
        print(f"  ⚠ {total_unmatched} answer(s) didn't match predefined options")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
