#!/usr/bin/env bash
# ============================================================================
# run_all_books.sh — Loop through all books and analyze each one
# ============================================================================
#
# Expects the directory structure:
#   books/<CountryCode>/<BookTitle>/ch01.txt, ch02.txt, ...
#
# Usage:
#   ./run_all_books.sh              # run everything
#   ./run_all_books.sh --dry-run    # just list what would be processed
#
# The resume logic in CLAUDE.md means re-running is always safe — chapters
# already in the CSV are skipped automatically.
# ============================================================================

set -euo pipefail

DRY_RUN=false
if [ "${1:-}" = "--dry-run" ]; then
    DRY_RUN=true
    echo "=== DRY RUN — listing books that would be processed ==="
    echo ""
fi

BOOKS_DIR="books"
LOG_DIR="logs"

if [ ! -d "$BOOKS_DIR" ]; then
    echo "ERROR: books/ directory not found."
    echo "Expected structure: books/<CountryCode>/<BookTitle>/"
    exit 1
fi

mkdir -p "$LOG_DIR"

TOTAL=0
FAILED=0

for country_dir in "$BOOKS_DIR"/*/; do
    COUNTRY=$(basename "$country_dir")

    for book_dir in "$country_dir"*/; do
        BOOK_TITLE=$(basename "$book_dir")
        CHAPTER_COUNT=$(find "$book_dir" -maxdepth 1 \( -name "*.txt" -o -name "*.pdf" \) | wc -l | tr -d ' ')

        if [ "$CHAPTER_COUNT" -eq 0 ]; then
            echo "SKIP: $COUNTRY / $BOOK_TITLE (no chapter files found)"
            continue
        fi

        TOTAL=$((TOTAL + 1))
        echo "[$TOTAL] $COUNTRY / $BOOK_TITLE ($CHAPTER_COUNT chapters)"

        if [ "$DRY_RUN" = true ]; then
            continue
        fi

        LOG_FILE="$LOG_DIR/${COUNTRY}_${BOOK_TITLE// /_}.log"

        echo "     → logging to $LOG_FILE"
        if ./run_book.sh "$COUNTRY" "$BOOK_TITLE" "$book_dir" 2>&1 | tee "$LOG_FILE"; then
            echo "     ✓ done"
        else
            echo "     ✗ FAILED (see log)"
            FAILED=$((FAILED + 1))
        fi

        echo ""
    done
done

echo "============================================"
echo "Total books: $TOTAL"
if [ "$DRY_RUN" = false ]; then
    echo "Failed:      $FAILED"
fi
echo "============================================"
