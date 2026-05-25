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

The analysis phase has four sequenced tasks:

1. **Data loading & cleaning** (`scripts/data_loading.Rmd`)
   Combine all per-book CSVs into a single cleaned dataset, drop paratext
   rows, normalize book/chapter labels, validate answers against the canonical
   options, and save tidy wide + long outputs.

2. **Intercoder reliability check** (`scripts/intercoder_reliability.Rmd`)
   Compare the Claude-coded answers against the human-coded subset
   (`data/human_coded/`) for the four books that have both. Compute agreement
   statistics (Cohen's kappa / Krippendorff's alpha as appropriate for
   ordinal/categorical questions) per question and overall, identify
   systematic disagreements, and produce a reliability report that
   establishes whether the Claude coding is fit for downstream inference.
   **Must pass before Task 3.**

3. **Descriptive analysis** (`scripts/analysis.Rmd`)
   Country-level and book-level descriptive plots and summary statistics that
   characterize how each national tradition portrays space across the 12
   dimensions.

4. **Hypothesis development** (off-Rmd, downstream)
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

- `chapter_position` — best-effort integer ordering within a book.
  Handles Arabic / Roman numerals, English & French spelled-out
  cardinals + ordinals, compound ordinals ("Twenty-First"), `Chapter`
  / `Chapitre` / `Episode` / `Interlude N`, `Part N - <rest>` (recursive),
  `Part N Act M`, `Part N Prologue/Epilogue`, date-prefixed Bradbury
  labels (encoded as `year * 12 + month`), and `The Nth <noun>` patterns.
  Labels that don't match any strategy get `chapter_position = NA`; the
  verification chunk in `data_loading.Rmd` prints the distinct unparseable
  set so we can add a new strategy if any appears.
- `part_position` — integer position of the `Part N` / `Book N` segment,
  or `NA` if the label has no part prefix.
- (Deferred) `chapter_order_fallback` and `position_inferred` flags —
  not built yet; the parser covered every observed label in the pre-flight
  Python probe (run 2026-05-25). If the R-side knit surfaces any
  unparseable labels we'll revisit and add a fallback ordering.

### 2.6 Ordinal numeric coding

Deferred to the start of Task 3 (`analysis.Rmd`). For now the cleaned data uses string answers only. Note: Task 2 (intercoder reliability) may also want to define an ordinal coding for weighted-kappa calculations; if so, we'll formalize the coding scheme there and reuse it in Task 3.

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
- [x] Create `data/processed/` directory for cleaned outputs.
- [x] Update `scripts/source.R`:
    - [x] Add path constants via `here::here()`.
    - [x] Add paratext regex (prologues + epilogues kept).
    - [x] Add helper `parse_chapter_position()`.
    - [x] Add helper `clean_book_name()` (book-title overrides).
    - [x] Add helper `drop_paratext()`.
    - [x] Add helper `load_results_csv()`.
    - [x] Add helper `validate_answers()`.
    - [x] Add helper `pivot_to_long()`.
- [x] Fix `source("00_setup.R")` → `source("source.R")` in both Rmd files.
- [x] Build `data_loading.Rmd` end-to-end:
    - [x] Setup chunk.
    - [x] Discover CSVs (skip explicit drop list).
    - [x] Load and bind into a single wide tibble.
    - [x] Normalize book column (apply rename map).
    - [x] Apply paratext drop rule.
    - [x] Validate answers against `questions.json`; flag mismatches in a table.
    - [x] Derive `chapter_position` and `part_position` (fallback ordering deferred — parser covers all observed labels per pre-flight probe).
    - [x] Pivot to long format; keep justifications.
    - [x] Save `.rds` + `.csv` for both shapes into `data/processed/`.
- [x] Verification chunk:
    - [x] Assertions on NA, empty answers, missing books.
    - [x] Per-book pre/post chapter counts (`gt` table).
    - [x] Print summary of dropped paratext rows.
    - [x] Print summary of any flagged answer mismatches.
    - [x] Parser coverage by book (`gt` table) -- bonus; flags any future label the parser misses.
- [x] Generate `data/processed/load_report.md` for human review (written by the final chunk of `data_loading.Rmd`).
- [ ] Knit `data_loading.Rmd` locally to confirm it runs end-to-end (Donald to run; sandbox has no R).
- [ ] Walk through outputs with Donald before moving to Task 2.

### Files Donald is responsible for moving

- [ ] Move `data/results/US_Enders_Game.csv` → `data/results/archive/`.

---

## 4. Task 2 — `intercoder_reliability.Rmd`

**Status:** not started. Must complete and pass before Task 3.

**Purpose:** Establish that Claude's coding of the science-fiction corpus is
reliable enough to support the descriptive and hypothesis-generation work
downstream. Compare Claude's per-chapter answers against the human-coded
subset for the four books that have both.

**Human-coded subset (`data/human_coded/`, 4 books, 3 countries):**

| Country | Book                   | Human file                                  |
|---------|------------------------|---------------------------------------------|
| US      | The Martian            | `2026_Coding_Martian_updated.xlsx`          |
| China   | The Three-Body Problem | `3_Body_problem_updated coding.xlsx`        |
| France  | Off on a Comet         | `Off_on_a_Comet_mapped_answers.xlsx`        |
| France  | Planet of the Apes     | `Planet_of_the_Apes_updated_Coding.xlsx`    |

**Sub-tasks (to be refined when we open the xlsx files together):**

- [ ] Inspect each human-coded `.xlsx` to understand its schema (sheet
      structure, column names, chapter ID format, answer encoding).
- [ ] Build a loader that reads the human sheets into the same long format
      as Claude's coding (one row per chapter × question).
- [ ] Map human chapter labels to Claude chapter labels (this may require a
      small per-book lookup if naming differs).
- [ ] Confirm both codings draw from the same answer options listed in
      `data/questions.json`. Flag any human answers that don't match the
      canonical option set.
- [ ] Join human and Claude codings on (book, chapter, question).
- [ ] Compute per-question reliability statistics:
    - Cohen's kappa (or weighted kappa for ordinal questions Q1–Q8, Q10, Q12).
    - Krippendorff's alpha as a robustness check (`irr::kripp.alpha`).
    - Exact-agreement rate.
    - For ordinal questions, mean absolute distance between scale positions.
- [ ] Compute overall agreement and a per-book breakdown.
- [ ] Produce a disagreement audit table: every chapter × question where
      Claude and the human differ, with both answers and Claude's
      justification, so disagreements can be inspected qualitatively.
- [ ] Write `data/processed/intercoder_reliability_report.md` summarizing
      reliability levels, which questions are weakest, and a go/no-go
      recommendation for Task 3.
- [ ] Walk through the report with Donald and decide whether any questions
      should be flagged with caveats, re-coded, or excluded from Task 3.

**Methodological notes (parked, to discuss when we start):**

- Whether to treat "Other / Unsure" as agreement-when-matched or as a
  separate category (defaults will likely follow standard IRR conventions
  but worth confirming).
- Whether to compute reliability on the full overlapping chapter set per
  book or on a chapter sample (depends on completeness of human coding).
- Threshold for acceptable agreement (commonly κ ≥ 0.60 / α ≥ 0.667 for
  ordinal coding; we may justify a different threshold given the inherent
  interpretive latitude of literary criticism).

---

## 5. Task 3 — `analysis.Rmd`

**Status:** not started. Planned outline (to be refined when we get there):

- Country-level distributions of each question's answers (proportion bar charts, faceted by question).
- Book-level fingerprints (heatmaps across the 12 dimensions).
- Possible ordinal coding for Q1–Q8, Q10, Q12 (decision deferred — see §2.6).
- Comparative summary: which countries diverge most from the cross-country average on which dimensions?
- Within-book trajectories using `chapter_position`.
- Carry forward any caveats from the Task 2 reliability report (e.g., questions where Claude/human disagreement was high should be presented with appropriate humility).

---

## 6. Task 4 — Hypothesis development (off-Rmd)

**Status:** downstream goal. Outputs of Task 3 (informed by Task 2's
reliability findings) feed into a hypothesis-generation exercise focused on
how national depictions of space might shape the heuristics readers (and
policymakers) bring to questions of space security and conflict. Not
implemented in code in this repo.

---

## 7. Open questions / parking lot

- For Russian/French books with idiosyncratic chapter labels (`Chapitre Premier`,
  `Chapter IX`), `parse_chapter_position()` will need a small lookup table for
  spelled-out / Roman numerals. To verify against actual data on first run.
- Should `Japan_good_luck_yukikaze` be retitled to `Good Luck, Yukikaze` in the
  book column? Will surface during the book-name normalization step and confirm.
- Acceptable reliability threshold for Task 2 (κ / α) — to set with Donald
  before running the IRR analysis.

---

## 8. File state

### `data/results/` (loaded)

46 files at last count. See `data_loading.Rmd` output `load_report.md` for
the authoritative loaded list after Donald moves `US_Enders_Game.csv`.

### `data/results/archive/` (not loaded)

- `China_Human_Split_Three_Body_Problem.csv` — superseded by `_cleaned`.
- All `write_*.py`, `validate_*.py`, `fix_*.py` scripts from the per-book
  analysis pipeline (kept for provenance, not loaded by R).
- `China_The_Three_Body_Problem_cleaned.csv` was originally here; promoted to
  `data/results/` for the analysis.

### `data/human_coded/` (loaded by Task 2 only)

Human-coded answer sheets for the intercoder reliability subset. Schema
will be inspected when Task 2 starts.

- `2026_Coding_Martian_updated.xlsx`
- `3_Body_problem_updated coding.xlsx`
- `Off_on_a_Comet_mapped_answers.xlsx`
- `Planet_of_the_Apes_updated_Coding.xlsx`

### `data/processed/` (created)

Will contain:

- From Task 1: `space_chapters_wide.rds`, `space_chapters_wide.csv`, `space_chapters_long.rds`, `space_chapters_long.csv`, `load_report.md`
- From Task 2: `intercoder_reliability_report.md`, plus optionally a joined human-vs-Claude long frame for the audit.

---

## 9. Restart guide

If a fresh Claude session picks this up:

1. Read `CLAUDE.md` for project conventions.
2. Read this file (`PROJECT_TASKS.md`) to see decisions and progress.
3. Read `scripts/source.R` to see available helpers.
4. Find the first task section (§3, §4, §5, or §6) whose status is not yet `done`, and resume from the first unchecked box inside it. Tasks are sequenced and gated on each other — do not skip ahead.
5. Resume work without re-litigating settled decisions in §2.
