# Project Tasks — Space Portrayal NLP Analysis

**Last updated:** 2026-05-25
**Target venue:** Nature
**Owner:** Donald Moratz (`dmoratz@sas.upenn.edu`)

This document is the durable plan of record for the analysis phase of the
project. It tracks decisions, sub-task progress, and known issues so any
collaborator (or a fresh Claude session) can pick up where work stopped.

---

## 1. Project Goal

We are analyzing how outer space is portrayed in science-fiction novels from
six countries (China, Finland, France, Japan, Russia, US). Each chapter of
each book has been coded against 12 structured research questions (see
`data/questions.json`). The coded answers live in per-book CSVs under
`data/results/`.

The analysis phase has three sequenced tasks:

1. **Data loading & cleaning** (`scripts/data_loading.Rmd`)
   Combine all per-book CSVs into a single cleaned dataset, drop paratext
   rows, normalize book/chapter labels, validate answers against the canonical
   options, and save tidy wide + long outputs.

2. **Descriptive analysis** (`scripts/analysis.Rmd`)
   Country-level and book-level descriptive plots and summary statistics that
   characterize how each national tradition portrays space across the 12
   dimensions.

3. **Hypothesis development** (off-Rmd, downstream)
   Use the descriptive picture to generate testable hypotheses about how
   differences in national science-fiction depictions of space shape the
   heuristics people use when thinking about space — especially from a
   war / security perspective.

---

## 2. Decisions Log (locked-in)

Decisions made in conversation, with brief justifications. Update only by
re-opening the question with the project owner.

### 2.1 Paratext drop rule

Drop a row when its `chapter` label (case-insensitive, trimmed) matches any
of the following patterns:

- `front_matter`
- `introduction` / `preface` / `foreword`
- `essay - …` (rows literally prefixed `Essay -`)
- `afterword`
- `appendix …` (e.g., `Appendix I - The Ecology of Dune`)

**Keep** prologues and epilogues — both are treated as narrative content.

This rule is applied uniformly to all files, including short-story / essay
collections. (E.g., `China_Broken_Stars` loses its 3 `Essay -` rows + its
`Introduction` row, but keeps all story chapters; `China_A_View_from_the_Stars`
keeps every row because none of its labels match the drop keywords.)

### 2.2 Short-story / essay collections

Kept in full (subject to the paratext rule above). Each story or essay counts
as one "chapter" for the purposes of the analysis. Affected files include
`China_A_View_from_the_Stars`, `China_Broken_Stars`, `US_The_Martian_Chronicles`,
`Japan_Administrator_by_Taku_Mayumura`.

### 2.3 Duplicate / partial files

| Book                  | Kept                                                                                          | Dropped                                                                |
|-----------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Three-Body Problem    | `data/results/China_The_Three_Body_Problem_cleaned.csv` (richer answers, lower Other/Unsure)  | `archive/China_Human_Split_Three_Body_Problem.csv` (already moved)     |
| Ender's Game          | `data/results/US_Human_Split_Enders_Game.csv` (newer, richer answers)                          | `data/results/US_Enders_Game.csv` — owner to move to `archive/`        |
| Hitchhiker's Guide    | The 92-chapter file; book column renamed to `The Hitchhiker's Guide to the Galaxy (Omnibus, Parts 1–3)` | — (filename was misleading; coverage is actually full)        |
| Hyperion              | The single file as-is (PROLOGUE + 6 Tales + EPILOGUE). Note: epilogues are now kept globally, so no per-file exception is needed. | — |

### 2.4 Output shape

`data_loading.Rmd` produces both a wide tidy frame and a long tidy frame:

- **Wide:** one row per chapter, columns `country`, `book`, `chapter`, `chapter_position`, `q1`–`q12`, `q1_justification`–`q12_justification`, plus derived metadata.
- **Long:** one row per chapter × question, with `question_number`, `criteria_short`, `answer`, `justification`. Justifications are retained for spot-checks.

Both shapes saved as `.rds` (canonical for downstream R) and `.csv` (portability for collaborators). Saved to `data/processed/`.

### 2.5 Derived columns

- `chapter_position` — best-effort numeric ordering within a book. Handles Arabic numerals, Roman numerals, spelled-out numbers, and optional `Part N` / `Book N` prefixes. Unparseable labels (e.g., `The Eighth Letter`) get `chapter_position = NA` and a separate `chapter_order_fallback` integer derived from alphabetical sort within book, with `position_inferred = TRUE`.
- `country_book` — convenience join key.

### 2.6 Ordinal numeric coding

Deferred to the start of Task 2 (`analysis.Rmd`). For now the cleaned data uses string answers only.

### 2.7 Style conventions

- 4-space indentation inside multi-line calls (matching Python guidance and Donald's Taylor Series chunk in `election_math_graphs.Rmd`).
- `%>%` pipe (magrittr), not `|>`.
- snake_case variables.
- Setup chunk pattern: `rm(list = ls())` → `library(pacman)` → `p_load(...)` → `options(...)` → `set.seed(3184)` → `source("source.R")`.
- Markdown headers between code chunks for outline navigation (`#` top, `###` sub).
- Helpers live in `scripts/source.R`; analysis code lives in `scripts/*.Rmd`.

---

## 3. Task 1 — `data_loading.Rmd`

**Status:** in progress.

### Sub-tasks

- [x] Survey CSV inventory in `data/results/` (46 files, 6 countries).
- [x] Reach decisions on paratext, collections, duplicates, output shape (see §2).
- [x] Create `PROJECT_TASKS.md` at repo root.
- [ ] Create `data/processed/` directory for cleaned outputs.
- [ ] Update `scripts/source.R`:
    - [ ] Add path constants via `here::here()`.
    - [ ] Add paratext regex (prologues + epilogues kept).
    - [ ] Add helper `parse_chapter_position()`.
    - [ ] Add helper `clean_book_name()` (book-title overrides).
    - [ ] Add helper `drop_paratext()`.
    - [ ] Add helper `load_results_csv()`.
    - [ ] Add helper `validate_answers()`.
    - [ ] Add helper `pivot_to_long()`.
- [ ] Fix `source("00_setup.R")` → `source("source.R")` in both Rmd files.
- [ ] Build `data_loading.Rmd` end-to-end:
    - [ ] Setup chunk.
    - [ ] Discover CSVs (skip explicit drop list).
    - [ ] Load and bind into a single wide tibble.
    - [ ] Normalize book column (apply rename map).
    - [ ] Apply paratext drop rule.
    - [ ] Validate answers against `questions.json`; flag mismatches in a table.
    - [ ] Derive `chapter_position`, `chapter_order_fallback`, `position_inferred`.
    - [ ] Pivot to long format; keep justifications.
    - [ ] Save `.rds` + `.csv` for both shapes into `data/processed/`.
- [ ] Verification chunk:
    - [ ] Assertions on NA, empty answers, missing books.
    - [ ] Per-book pre/post chapter counts (`gt` table).
    - [ ] Print summary of dropped paratext rows.
    - [ ] Print summary of any flagged answer mismatches.
- [ ] Generate `data/processed/load_report.md` for human review.
- [ ] Walk through outputs with Donald before moving to Task 2.

### Files Donald is responsible for moving

- [ ] Move `data/results/US_Enders_Game.csv` → `data/results/archive/`.

---

## 4. Task 2 — `analysis.Rmd`

**Status:** not started. Planned outline (to be refined when we get there):

- Country-level distributions of each question's answers (proportion bar charts, faceted by question).
- Book-level fingerprints (heatmaps across the 12 dimensions).
- Possible ordinal coding for Q1–Q8, Q10, Q12 (decision deferred — see §2.6).
- Comparative summary: which countries diverge most from the cross-country average on which dimensions?
- Within-book trajectories using `chapter_position`.
- Possible inter-rater reliability check if a second coder is in scope (note `irr` is loaded in `source.R`).

---

## 5. Task 3 — Hypothesis development (off-Rmd)

**Status:** downstream goal. Outputs of Task 2 feed into a hypothesis-generation
exercise focused on how national depictions of space might shape the
heuristics readers (and policymakers) bring to questions of space security
and conflict. Not implemented in code in this repo.

---

## 6. Open questions / parking lot

- Is there a second coder whose CSVs we should be loading for inter-rater
  reliability? Currently not assumed.
- For Russian/French books with idiosyncratic chapter labels (`Chapitre Premier`,
  `Chapter IX`), `parse_chapter_position()` will need a small lookup table for
  spelled-out / Roman numerals. To verify against actual data on first run.
- Should `Japan_good_luck_yukikaze` be retitled to `Good Luck, Yukikaze` in the
  book column? Will surface during the book-name normalization step and confirm.

---

## 7. File state

### `data/results/` (loaded)

46 files at last count. See `data_loading.Rmd` output `load_report.md` for
the authoritative loaded list after Donald moves `US_Enders_Game.csv`.

### `data/results/archive/` (not loaded)

- `China_Human_Split_Three_Body_Problem.csv` — superseded by `_cleaned`.
- All `write_*.py`, `validate_*.py`, `fix_*.py` scripts from the per-book
  analysis pipeline (kept for provenance, not loaded by R).
- `China_The_Three_Body_Problem_cleaned.csv` was originally here; promoted to
  `data/results/` for the analysis.

### `data/processed/` (to be created)

Will contain:

- `chapters_wide.rds`, `chapters_wide.csv`
- `chapters_long.rds`, `chapters_long.csv`
- `load_report.md`

---

## 8. Restart guide

If a fresh Claude session picks this up:

1. Read `CLAUDE.md` for project conventions.
2. Read this file (`PROJECT_TASKS.md`) to see decisions and progress.
3. Read `scripts/source.R` to see available helpers.
4. Look for the first unchecked box in §3.
5. Resume work without re-litigating settled decisions in §2.
