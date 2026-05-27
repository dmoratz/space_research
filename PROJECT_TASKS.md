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

**Status:** scripts/source_irr.R and scripts/intercoder_reliability.Rmd
written 2026-05-25; ready to knit. Decisions below are locked in.

**Purpose:** Establish that Claude's coding of the science-fiction corpus is
reliable enough to support the descriptive and hypothesis-generation work
downstream. Compare Claude's per-chapter answers against the human-coded
subset for the five books that have both.

**Human-coded subset (`data/human_coded/`, 5 books, 3 countries):**

| Country | Book                   | Schema     | Human file                                  |
|---------|------------------------|------------|---------------------------------------------|
| US      | The Martian            | long xlsx  | `2026_Coding_Martian_updated.xlsx`          |
| China   | The Three-Body Problem | long xlsx  | `3_Body_problem_updated coding.xlsx`        |
| France  | Planet of the Apes     | long xlsx  | `Planet_of_the_Apes_updated_Coding.xlsx`    |
| France  | Off on a Comet         | wide xlsx  | `Off_on_a_Comet_mapped_answers.xlsx`        |
| US      | Ender's Game           | long csv   | `enders_game.csv`                           |

**Locked-in decisions (2026-05-25):**

- Ender's Game: Donald canonicalized the `answer` column and embedded a
  shorthand reference block at columns 5..12.  176 / 180 cells match
  canonical labels; 4 mechanical fixes baked into the corrections table
  (`human_mapped_answer_corrections` in `source_irr.R`).  The shorthand
  block is encoded as `answer_options_short_lookup` in `source.R` for
  reuse in Task 3 plot labels.
- Mapped Answer cleaning: approved correction table (mechanical fixes for
  trailing semicolons, "Civilian" -> "Entirely civilian", 4 Ender's Game
  fixes) is applied first; remaining non-canonical values are coerced to
  "Other / Unsure".
- NA / blank coercion: human NaN -> "Other / Unsure".
- Per-book coverage overrides (also in `source_irr.R`):
    - Off on a Comet: drop the "General notes" row (criteria row 12);
      move Q4 -> Q12 (the rater used Q12's option list in the Q4 slot).
    - Planet of the Apes: accept Q12 as not covered.
- Chapter alignment: per-book lookup table (`chapter_alignment_rules`).
  Four of the five books are trivially `human N -> "Chapter N"`; Ender's
  Game uses a prefix match against `"Chapter N -"`; Off on a Comet uses
  `human N -> "Book 1 - Chapter N"` for N in 1..10.
- Metrics: all three -- Cohen's kappa (nominal), Cohen's weighted kappa
  with squared weights (ordinal questions only: Q1-Q8, Q10, Q12),
  Krippendorff's alpha (ordinal for ordinal questions, nominal else),
  plus exact-agreement rate.
- "Other / Unsure": kept as a real category (both-Other -> agreement).
- Thresholds: kappa >= 0.60, alpha >= 0.667.

**Sub-tasks:**

- [x] Inspect each human-coded file to understand schema (Python probes
      in /sessions/.../probe_human_mapped_answers.py,
      probe_chapter_alignment.py, probe_eg_updated.py, inspect_deeper.py).
- [x] Confirm both codings draw from the same answer options in
      `data/questions.json`. Surface mismatches in
      `data/processed/human_mapped_answer_proposals.md` and get Donald's
      approval on each.
- [x] Build schema-specific loaders for the three formats
      (`load_human_long_xlsx`, `load_human_wide_xlsx_ooc`,
      `load_human_csv_eg`) in `scripts/source_irr.R`.
- [x] Map human chapter labels to Claude chapter labels via
      `chapter_alignment_rules` (per-book closure).
- [x] Encode shorthand label map from Ender's Game CSV as
      `answer_options_short_lookup` in `source.R` (with `get_answer_short()`
      helper for downstream plotting).
- [x] Join human and Claude codings on (book, chapter, question) via
      `load_all_human_coded()`.
- [x] Implement per-question reliability via `compute_irr_per_question()`
      and pooled-by-question via `compute_irr_overall()`.
- [x] Implement `format_irr_table()` for gt rendering with threshold
      pass/fail color coding.
- [ ] Knit `scripts/intercoder_reliability.Rmd` and walk through results
      with Donald.
- [ ] Produce a disagreement audit table for the qualitative review
      (chapter x question where Claude and human differ, with both
      answers and Claude's justification).
- [ ] Decide whether any questions should be flagged with caveats,
      re-coded, or excluded from Task 3.

---

## 5. Task 3 — `analysis.Rmd`

**Status:** in progress as of 2026-05-26.  Locked-in design below; code in
`scripts/source.R` (additions), `scripts/source_analysis.R` (new), and
`scripts/analysis.Rmd` (rewrite).

**Purpose:** Descriptive analysis of how each country's sci-fi corpus
portrays outer space, rolling up Claude's per-chapter codings to book and
country levels.  Explicitly hypothesis-generating, not hypothesis-testing
(no inferential tests).

### 5.1 Aggregation pipeline (chapter -> book -> country)

**Chapter -> Book** (per (book, question)):

- **Mode** (primary book-level coding): majoritarian vote among non-
  "Other / Unsure" chapters; book gets "Other / Unsure" only when 100%
  of chapters are Other / Unsure (Donald's "big reveal" rule, locked
  2026-05-25).
- **Median, mean, peak, end**: alternative summaries available alongside.
  Median is robust central tendency for ordinal Qs.  Mean uses ordinal
  positions.  Peak = max ordinal position any chapter reached.  End =
  last chapter's coding (by `chapter_position`).
- **Tie-breaking** (when mode is multi-modal):
  - Ordinal Qs (Q1-Q8, Q10, Q12): use median of tied positions
  - Nominal Qs (Q9, Q11): pick the lower-index canonical option
- **Collection split**: books with `is_collection = TRUE` in
  `data/collection_metadata.csv` (currently 3 single-author collections
  + 1 anthology = 4 books) are split into separate book rows, one per
  story.  Fix-up novels (5 of them) stay as single books.

**Book -> Country**: distributions of book codings per category, plus
country-level mode/median/mean/peak/end aggregated over books.  Apply
`collection_weight_mode` (set in `analysis.Rmd`):

- `"weighted"` (default): each story in an N-story collection contributes
  1/N of a book's weight in country aggregates.
- `"equal"`: each story counts as a full book.
- `"merged"`: collections stay as one book row (no split).

### 5.2 Visualizations (Donald wants ALL of these)

- **Book fingerprint heatmaps × 2** — one for `mode_answer`, one for
  `peak_answer`.  Books × 12 questions; cells colored by answer using
  `answer_options_short_lookup` for labels.
- **Country distribution stacked bars × 2** — faceted by question;
  country on x-axis; color = answer.  Mode and peak versions side-by-side.
- **Cross-country divergence summary × 2** — table or radar showing
  which countries diverge most from the corpus average on which
  dimensions.
- **Per-book trajectories (46 figures)** — one figure per book, 12
  small-multiples panels (one per question), `chapter_position` on x,
  answer on y (ordinal as line, nominal as strip plot below).
- **Per-question trajectories (12 figures)** — one figure per question,
  one panel per book, same axes.  Useful for spotting cross-book arc
  patterns.

Total: 58 trajectory figures plus 6 summary visualizations.

### 5.3 Sub-tasks

- [x] Spawn Agent to classify books and produce `data/collection_metadata.csv`.
- [x] Donald reviews collection metadata (final: 42 novels/fix-ups + 4
      collections totaling 64 stories).
- [ ] Add to `source.R`: `answer_options_ordinal_lookup`, `to_ordinal()`,
      `add_ordinal_position()`, `load_collection_metadata()`,
      `ordinal_question_numbers` / `nominal_question_numbers` constants.
- [ ] Create `scripts/source_analysis.R`:
      - `split_collections()` — expand collection rows
      - `aggregate_chapter_to_book()` — mode + median + mean + peak + end
      - `aggregate_book_to_country()` — apply `collection_weight_mode`
      - Plot helpers: `plot_book_fingerprint()`,
        `plot_country_distribution()`, `plot_trajectory_per_book()`,
        `plot_trajectory_per_question()`,
        `plot_country_divergence()`.
- [ ] Rewrite `scripts/analysis.Rmd`:
      - Setup chunk sets `collection_weight_mode`
      - Build book-level + country-level frames
      - Render heatmaps + distributions + divergence + 58 trajectories
      - Save outputs to `data/processed/`
      - Auto-generate `analysis_report.md`
- [ ] Carry forward Task 2 caveats (Q9 / Q11 IRR weak; ordinal signal
      strong; flag in report).
- [ ] Donald knits and we walk through the figures together.

### 5.4 Locked-in design decisions (2026-05-25 / 2026-05-26)

- Ordinal coding adopted: Q1-Q8, Q10, Q12 mapped to integers 1-5 from
  canonical answer_options order; "Other / Unsure" -> NA for ordinal-
  only operations.
- Both mode AND peak versions of every chart, side-by-side (no per-
  question pre-commit to which is "right"; trajectories make the arc
  visible so we revisit per question after seeing data).
- Hypothesis testing skipped (purely descriptive; the Nature submission
  is hypothesis-generating).
- Fix-up novels (Foundation, Hyperion, Noon: 22nd Century, Hitchhiker's
  Omnibus, Good Luck Yukikaze) treated as single books, NOT split into
  stories.  Logged in metadata for future reference.

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
