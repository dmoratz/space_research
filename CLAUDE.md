# Space Portrayal NLP Analysis — Claude Code Instructions

## What This Project Does

This project analyzes sci-fi book chapters to study how outer space is portrayed.
Each chapter is read and evaluated against a set of structured research questions
with predefined answer options. Each book gets its own CSV file in `data/results/`.

## File Layout

```
project/
├── CLAUDE.md              ← you are here
├── combine_results.py     ← merges per-book CSVs into one
├── data/
│   ├── questions.json     ← research questions + valid answer options
│   └── results/           ← one CSV per book (never conflicts on merge)
│       ├── US_Leviathan_Wakes.csv
│       ├── US_The_Martian.csv
│       └── ...
├── books/
│   └── <CountryCode>/
│       └── <BookTitle>/
│           ├── ch01.txt   ← one file per chapter (.txt or .pdf)
│           ├── ch02.txt
│           └── ...
```

## How to Analyze a Book

When the user asks you to analyze a book, follow this procedure exactly:

### 1. Load the questions

Read `data/questions.json`. It contains an array of question objects, each with:
- `number` — question ID (integer)
- `criteria` — the full research question
- `criteria_short` — abbreviated label
- `answer_options` — the ONLY valid answers (list of strings)

### 2. Identify the chapter files

The user will tell you the country code and book title, and point you to the
chapter files. List them and confirm the count before proceeding.

### 3. Process each chapter ONE AT A TIME

For each chapter file:

**a) Read the file contents.**
   - For `.txt` files: read the text directly.
   - For `.pdf` files: extract readable text (use `pdftotext` or similar).

**b) Analyze the chapter against ALL questions.**

   You are acting as a literary-analysis assistant. Read the chapter carefully,
   then for EACH question, choose exactly ONE answer from its predefined options.

   Your role and rules:
   - You are studying how science-fiction novels portray outer space.
   - You MUST pick from the provided answer options only — do not invent answers.
   - If genuinely unsure, pick "Other / Unsure" (if available in the options).
   - Provide a 1–3 sentence justification for each answer, citing specific
     details from the chapter.

**c) Format your answers as a JSON array**, one object per question:
   ```json
   [
     {
       "question_number": 1,
       "answer": "Exact text of chosen option",
       "justification": "Brief explanation citing chapter details."
     },
     ...
   ]
   ```

**d) Validate each answer** against the question's `answer_options` list.
   If your chosen answer doesn't exactly match one of the options, correct it
   before recording.

**e) Append a row to the CSV** (see output format below), then move to the
   next chapter.

### 4. Output Format

Each book gets its own CSV file in `data/results/`, named
`<CountryCode>_<BookTitle>.csv` (spaces replaced with underscores).
Create the `data/results/` directory if it doesn't exist.

The CSV uses wide format — one row per chapter:

```
country,book,chapter,q1,q2,...,qN,q1_justification,q2_justification,...,qN_justification
```

- `country` — country code provided by the user (e.g., "US", "UK", "JP")
- `book` — book title provided by the user
- `chapter` — a clean chapter label derived from the filename. Strip the file
  extension, remove the book title if it appears in the filename, and normalize
  casing. For example, a file named `Chapter 3_ The Martian.txt` should become
  `Chapter 3`, not `Chapter 3_ The Martian`. A file named `ch03.txt` becomes
  `ch03`.
- `q1` through `qN` — the validated answer for each question
- `q1_justification` through `qN_justification` — the justification text

**CRITICAL: Use Python's `csv` module to write the CSV.** Many answer options
and justifications contain commas (e.g., "stations, missions, outposts").
Writing raw comma-separated strings will break the column alignment.

Always write the CSV using a script like this:

```python
import csv
import os

csv_path = f"data/results/{country}_{book_title.replace(' ', '_')}.csv"
os.makedirs("data/results", exist_ok=True)

fieldnames = ["country", "book", "chapter"]
for q in questions:
    fieldnames.append(f"q{q['number']}")
for q in questions:
    fieldnames.append(f"q{q['number']}_justification")

file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0

with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()
    writer.writerow(row_dict)
```

Do NOT write CSV rows by manually joining strings with commas. The `csv`
module handles quoting fields that contain commas, newlines, or quotes.

### 5. Resume Support

Before analyzing a chapter, check if a row with the same chapter label
already exists in this book's CSV. If so, skip it and print a message. This
lets the user safely re-run after an interruption.

### 6. After All Chapters

Print a summary:
- How many chapters were analyzed
- How many were skipped (already in CSV)
- Any questions where the answer didn't match an option (flag for review)

## Important Guidelines

- Process chapters sequentially, not all at once — this keeps context focused.
- After finishing each chapter, write the CSV row immediately (checkpoint).
- Do NOT carry context between chapters — each chapter is independent.
- Be conservative: if a chapter doesn't clearly address a question, choose
  the most neutral/default option or "Other / Unsure".
- The justification should reference specific scenes, dialogue, descriptions,
  or narrative elements from the chapter text.
