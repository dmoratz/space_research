# Space Portrayal NLP Analysis — Claude Code Instructions

## What This Project Does

This project analyzes sci-fi book chapters to study how outer space is portrayed.
Each chapter is read and evaluated against a set of structured research questions
with predefined answer options. Results are appended to a single CSV file.

## File Layout

```
project/
├── CLAUDE.md              ← you are here
├── data/
│   ├── questions.json     ← research questions + valid answer options
│   └── nlp_analysis_results.csv  ← output (appended to, never overwritten)
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

The CSV file (`data/nlp_analysis_results.csv`) uses wide format — one row per chapter:

```
country, book, chapter, q1, q2, ..., qN, q1_justification, q2_justification, ..., qN_justification
```

- `country` — country code provided by the user (e.g., "US", "UK", "JP")
- `book` — book title provided by the user
- `chapter` — the chapter file stem (e.g., "ch01", "ch02")
- `q1` through `qN` — the validated answer for each question
- `q1_justification` through `qN_justification` — the justification text

When appending, check if the CSV already exists:
- If it exists: read the header, append the new row (do NOT rewrite the header).
- If it doesn't exist: write the header first, then the row.

### 5. Resume Support

Before analyzing a chapter, check if a row with the same (country, book, chapter)
triple already exists in the CSV. If so, skip it and print a message. This lets
the user safely re-run after an interruption.

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
