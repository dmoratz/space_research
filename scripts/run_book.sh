#!/usr/bin/env bash
# ============================================================================
# run_book.sh — Analyze one book with Claude Code
# ============================================================================
#
# Usage:
#   ./run_book.sh <country_code> <book_title> <chapters_dir>
#
# Examples:
#   ./run_book.sh US "Leviathan Wakes" books/US/LeviathanWakes/
#   ./run_book.sh UK "The Hitchhikers Guide" books/UK/HitchhikersGuide/
#
# This script constructs a prompt and hands it to Claude Code. Claude Code
# will read the CLAUDE.md for detailed instructions, then process each
# chapter file in the given directory.
#
# Requirements:
#   - Claude Code CLI installed (npm install -g @anthropic-ai/claude-code)
#   - data/questions.json exists (run setup_questions.py first)
# ============================================================================

set -euo pipefail

if [ $# -lt 3 ]; then
    echo "Usage: $0 <country_code> <book_title> <chapters_dir>"
    echo ""
    echo "Example:"
    echo "  $0 US \"Leviathan Wakes\" books/US/Leviathan_Wakes/"
    exit 1
fi

COUNTRY="$1"
BOOK_TITLE="$2"
CHAPTERS_DIR="$3"

# Validate inputs
if [ ! -d "$CHAPTERS_DIR" ]; then
    echo "ERROR: chapters directory not found: $CHAPTERS_DIR"
    exit 1
fi

if [ ! -f "data/questions.json" ]; then
    echo "ERROR: data/questions.json not found."
    echo "Run setup_questions.py first:"
    echo "  python setup_questions.py --input data/nlp_question_answer_set.xlsx"
    exit 1
fi

# Count chapter files
CHAPTER_COUNT=$(find "$CHAPTERS_DIR" -maxdepth 1 \( -name "*.txt" -o -name "*.pdf" \) | wc -l | tr -d ' ')
echo "Found $CHAPTER_COUNT chapter file(s) in $CHAPTERS_DIR"
echo "Book:    $BOOK_TITLE"
echo "Country: $COUNTRY"
echo ""

# Build the prompt
PROMPT="Analyze the book \"${BOOK_TITLE}\" (country: ${COUNTRY}).

The chapter files are in: ${CHAPTERS_DIR}

Follow the instructions in CLAUDE.md. Process each chapter file in that directory, answer all questions from data/questions.json, and append results to data/nlp_analysis_results.csv.

Use resume mode — skip any chapters already recorded in the CSV for this country/book combination."

# Run Claude Code
echo "Starting Claude Code..."
echo "---"
claude --print "$PROMPT"
