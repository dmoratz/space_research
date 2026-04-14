# Claude Code Workflow for Book Analysis

This replaces the Gemini API pipeline with Claude Code doing the analysis
directly — no API key needed, just a Claude Pro/Team/Enterprise subscription
with Claude Code access.

## How It Works

Instead of calling an LLM API from Python, Claude Code **is** the LLM. It
reads your chapter files, answers the research questions itself, and writes
the results to your CSV. The `CLAUDE.md` file gives it all the instructions
it needs.

## One-Time Setup

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Extract your questions to JSON

Claude Code can't read `.xlsx` natively, so we convert the question set once:

```bash
pip install openpyxl
python setup_questions.py --input data/nlp_question_answer_set.xlsx \
                          --output data/questions.json
```

Inspect `data/questions.json` to verify it looks right.

### 3. Organize your chapter files

Put chapter files into this structure:

```
books/
├── US/
│   ├── Leviathan_Wakes/
│   │   ├── ch01.txt
│   │   ├── ch02.txt
│   │   └── ...
│   └── The_Martian/
│       ├── ch01.txt
│       └── ...
├── UK/
│   └── ...
```

Each book gets its own folder. Chapter files should be `.txt` (or `.pdf`,
though `.txt` will give more reliable results with Claude Code since it
can read the text directly).

## Running the Analysis

### Option A: One book at a time (recommended to start)

```bash
./run_book.sh US "Leviathan Wakes" books/US/Leviathan_Wakes/
```

This invokes Claude Code with a focused prompt. It will:
1. Read `CLAUDE.md` for instructions
2. Load the questions from `data/questions.json`
3. Read each chapter file
4. Answer all questions for that chapter
5. Append results to `data/nlp_analysis_results.csv`
6. Print a summary when done

### Option B: All books in sequence

```bash
# Preview what will be processed:
./run_all_books.sh --dry-run

# Run everything:
./run_all_books.sh
```

This loops through `books/<country>/<title>/` and calls `run_book.sh` for
each one. Logs go to `logs/`.

### Option C: Manual / interactive

Just `cd` into this directory and run `claude`:

```bash
claude
```

Then type your request directly:

> Analyze the book "Dune" (country: US). The chapters are in books/US/Dune/.
> Follow the instructions in CLAUDE.md.

This gives you the most control — you can ask follow-up questions, spot-check
answers, or have Claude Code re-do a chapter.

## Resume & Re-Running

The workflow has built-in resume support. Before analyzing each chapter, Claude
Code checks if a row with the same (country, book, chapter) already exists in
the CSV. If so, it skips that chapter. This means:

- **Crash recovery**: just re-run the same command.
- **Adding new books**: run only the new book — existing results are untouched.
- **Re-analyzing a book**: delete its rows from the CSV first, then re-run.

## Output

Results go to `data/nlp_analysis_results.csv` in wide format, identical to
what your original Gemini script produced:

```
country, book, chapter, q1, q2, ..., q1_justification, q2_justification, ...
US, Leviathan Wakes, ch01, <answer>, <answer>, ..., <justification>, ...
US, Leviathan Wakes, ch02, <answer>, <answer>, ..., <justification>, ...
```

## Tips & Gotchas

**Context window**: Claude Code's context is large but not infinite. Processing
one book at a time (rather than all 50) avoids any issues. Each chapter is
analyzed independently — no cross-chapter context is carried.

**PDF chapters**: Claude Code can read PDFs but may need to use `pdftotext`
first. Plain `.txt` chapters are more reliable and faster. If you have PDFs,
consider batch-converting them:
```bash
for f in books/US/MyBook/*.pdf; do
    pdftotext "$f" "${f%.pdf}.txt"
done
```

**Cost**: Claude Code usage counts against your subscription. Processing
~50 books with, say, 15–25 chapters each will use significant context. With
a Pro plan, you may want to spread this across several sessions.

**Consistency**: Unlike an API call with temperature=0, Claude Code's answers
may vary slightly between runs. For research purposes, consider doing a
consistency check on a few chapters (analyze them twice and compare).

**Spot-checking**: Use Option C (interactive mode) to spot-check a few
chapters before running the full batch. You can ask Claude Code to explain
its reasoning in more detail for any answer you want to verify.
