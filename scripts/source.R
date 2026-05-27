# =============================================================================
# source.R
# Shared setup for the Space Sci-Fi Analysis Pipeline
# =============================================================================
# Sourced at the top of every .Rmd in scripts/ to provide a single point of
# truth for packages, paths, project-specific constants, and helper functions.
#
# Contents
#   1. Package loading
#   2. Global settings
#   3. Path constants
#   4. Project-specific constants
#        4a. paratext_regex   (chapter labels to drop)
#        4b. file_drop_list   (per-book CSVs to skip during load)
#        4c. book_rename_map  (filename stem -> canonical book title)
#   5. Helper functions
#        5a. parse_number_token()      -> integer
#        5b. parse_chapter_position()  -> tibble(part_position, chapter_position)
#        5c. clean_book_name()         -> character
#        5d. drop_paratext()           -> tibble (filtered)
#        5e. load_results_csv()        -> tibble (one book's wide rows)
#        5f. validate_answers()        -> tibble of mismatched answers
#        5g. pivot_to_long()           -> tibble (one row per chapter x question)
#
# Style: 4-space indentation inside multi-line calls; 2-space inside function
# bodies; %>% pipe; snake_case throughout.  See PROJECT_TASKS.md §2.7.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Package loading
# -----------------------------------------------------------------------------

if (!require("pacman")) install.packages("pacman")

pacman::p_load(

  # Data manipulation
  tidyverse,
  dplyr,
  tidyr,
  purrr,
  data.table,
  lubridate,
  stringr,
  stringdist,
  readr,
  haven,
  foreign,
  jsonlite,

  # Visualization
  ggplot2,
  patchwork,
  cowplot,
  grid,
  gridExtra,
  scales,
  ggpubr,
  plotly,

  # Tables
  gt,
  knitr,
  kableExtra,
  modelsummary,
  stargazer,
  texreg,
  pander,

  # Statistical analysis
  estimatr,
  fixest,
  lfe,
  plm,
  sandwich,
  lmtest,
  rdrobust,
  AER,
  VGAM,

  # Other utilities
  here,
  broom,
  zoo,

  # Matching, sensitivity, and bootstrap
  fwildclusterboot,
  MatchIt,
  cobalt,
  rbounds,
  sensemakr,
  ggridges,

  # Spatial and inter-rater reliability
  rnaturalearth,
  rnaturalearthdata,
  sf,
  irr
)


# -----------------------------------------------------------------------------
# 2. Global settings
# -----------------------------------------------------------------------------

set.seed(3184)
options(scipen = 3, digits = 3)


# -----------------------------------------------------------------------------
# 3. Path constants
#    All paths anchored at the project root (the directory containing the
#    .Rproj file) via here::here() so the pipeline runs identically
#    regardless of which subdirectory the calling .Rmd lives in.
# -----------------------------------------------------------------------------

PROJECT_ROOT    <- here::here()
DATA_DIR        <- here::here("data")
RESULTS_DIR     <- here::here("data", "results")
PROCESSED_DIR   <- here::here("data", "processed")
HUMAN_CODED_DIR <- here::here("data", "human_coded")
QUESTIONS_JSON  <- here::here("data", "questions.json")

# Ensure processed/ exists at source-time so downstream saveRDS() /
# write_csv() calls never fail on a fresh checkout.
if (!dir.exists(PROCESSED_DIR)) {
    dir.create(PROCESSED_DIR, recursive = TRUE)
}


# -----------------------------------------------------------------------------
# 4. Project-specific constants
# -----------------------------------------------------------------------------

# 4a. Paratext drop rule.
#
# Drop a chapter row when its `chapter` label STARTS WITH any of these
# keywords (case-insensitive, leading whitespace ignored).  Prologues and
# epilogues are intentionally NOT in this list -- both are treated as
# narrative content.  See PROJECT_TASKS.md §2.1.
#
# Concrete labels this rule drops (verified against the corpus 2026-05-25):
#   front_matter
#   Introduction / INTRODUCTION / introduction
#   Essay - A Brief Introduction to Chinese SF and Fandom
#   Essay - A New Continent for China Scholars
#   Essay - Science Fiction Embarrassing No More
#   Appendix I-IV - ... (Dune)
#   Afterword
paratext_regex <- stringr::regex(
    "^\\s*(front_matter|introduction|preface|foreword|essay\\s*-|afterword|appendix\\b)",
    ignore_case = TRUE
)

# 4b. Files to skip during load.  See PROJECT_TASKS.md §2.3 for justification.
file_drop_list <- c(
    "US_Enders_Game.csv"   # superseded by US_Human_Split_Enders_Game.csv
)

# 4c. Book-title overrides.  Keyed by filename stem (no extension).  Any file
# not listed here keeps whatever value is in its `book` column.  See
# PROJECT_TASKS.md §2.3.  The first four entries reflect locked-in
# duplicate-resolution decisions; the remaining four normalize title-case so
# all 46 loaded books are presented consistently in plots and tables.
book_rename_map <- c(

    # Duplicates / partial files (decisions logged 2026-05-25)
    "China_The_Three_Body_Problem_cleaned" = "The Three-Body Problem",
    "US_Human_Split_Enders_Game"           = "Ender's Game",
    "US_Hyperion_Cleaned"                  = "Hyperion",
    "US_The_Hitchhikers_Guide_to_the_Galaxy_Omnibus_A_Trilogy_of_Five_Part_1_up_to_chapter_26" =
        "The Hitchhiker's Guide to the Galaxy (Omnibus, Parts 1\u20133)",

    # Title-case clean-ups (cosmetic; do not change which rows are loaded)
    "Japan_good_luck_yukikaze"                              = "Good Luck, Yukikaze",
    "Japan_rocket_girls"                                    = "Rocket Girls",
    "Japan_ten_billion_days_and_one_hundred_billion_nights" = "Ten Billion Days and One Hundred Billion Nights",
    "Japan_Administrator_by_Taku_Mayumura"                  = "Administrator"
)


# 4d. Short labels for the canonical answer_options.
#
# Source: the right-side reference block in
# data/human_coded/enders_game.csv (rows 1..12, cols 5..12), authored by
# Donald on 2026-05-25 and tidied up here (Q5 spelling fix
# `france -> franca`; Q7 typo fix `moderatecommon -> moderately common`;
# Q7 5th level interpolated `Common -> common`, `Normalized -> widespread`).
#
# Use case: plot axis labels, gt table cells, and IRR per-question facets
# where the full canonical text ("High contestation (frequent conflict or
# strategic struggle)") is too long.
#
# Shape: a long tibble with three columns:
#   question_number  -- integer 1..12
#   answer           -- the canonical text (exact match to questions.json)
#   answer_short     -- the abbreviated label for display
#
# Helper get_answer_short(q, a) below wraps a join-free lookup.
answer_options_short_lookup <- tibble::tribble(
    ~question_number, ~answer,                                                                                              ~answer_short,
    # Q1 -- contestation
    1L, "No contestation",                                                                                                  "no contestation",
    1L, "Low contestation (minor competition, little open conflict)",                                                       "low contestation",
    1L, "Moderate contestation (ongoing rivalry/disputes)",                                                                 "moderate contestation",
    1L, "High contestation (frequent conflict or strategic struggle)",                                                      "high contestation",
    1L, "Total war / constant conflict",                                                                                    "total war",
    1L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q2 -- inhabitable
    2L, "Cannot inhabit or hold territory",                                                                                 "cannot inhabit",
    2L, "Visiting / Temporary presence only (stations, missions, outposts)",                                                "visiting/temporary only",
    2L, "Limited settlement (small colonies, hard to sustain/control)",                                                     "limited settlement",
    2L, "Habitable and governable (permanent settlements can hold territory)",                                              "habitable and governable",
    2L, "Extensive territorial occupation (many settled worlds/regions held like states or empires)",                       "extensive occupation",
    2L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q3 -- journey distance
    3L, "Near-Earth / very short journey",                                                                                  "near-earth/very short",
    3L, "Short interplanetary journey",                                                                                     "short journey",
    3L, "Moderate journey (months/meaningful separation)",                                                                  "moderate journey",
    3L, "Long-distance journey (years, major separation from Earth)",                                                       "long-distance journey",
    3L, "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",               "extreme/unreachable",
    3L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q4 -- cultural difference
    4L, "Basically Earth society in space",                                                                                 "earth in space",
    4L, "Mostly Earth-like with minor adaptations",                                                                         "earth-like",
    4L, "Mixed / hybrid culture",                                                                                           "hybrid culture",
    4L, "Distinct space culture",                                                                                           "distinct space culture",
    4L, "Radically different / alien social order",                                                                         "radically different culture",
    4L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q5 -- language
    5L, "Same languages as Earth",                                                                                          "earth language",
    5L, "Mostly same, with dialect/slang differences",                                                                      "dialect differences",
    5L, "Shared lingua franca plus local variation",                                                                        "shared lingua franca + local variation",
    5L, "Distinct space language(s)",                                                                                       "distinct languages",
    5L, "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)", "translation-mediated",
    5L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q6 -- geographic hostility
    6L, "Benign / easily survivable",                                                                                       "benign",
    6L, "Manageable but risky",                                                                                             "risky",
    6L, "Harsh and resource-intensive",                                                                                     "harsh",
    6L, "Extremely hostile (constant survival pressure)",                                                                   "hostile",
    6L, "Nearly uninhabitable / lethal without major intervention",                                                         "uninhabitable/lethal",
    6L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q7 -- common experience
    7L, "Exceptionally rare (few astronauts/explorers)",                                                                    "rare",
    7L, "Uncommon (small specialist population)",                                                                           "uncommon",
    7L, "Moderately common (noticeable settlements/populations)",                                                           "moderately common",
    7L, "Common (many people live/work there)",                                                                             "common",
    7L, "Normalized / widespread (space habitation is ordinary for humanity)",                                              "widespread",
    7L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q8 -- different countries
    8L, "No political order / ungoverned",                                                                                  "ungoverned",
    8L, "Single unified authority",                                                                                         "single authority",
    8L, "Earth nation-states extend into space",                                                                            "Earth nation-states extend into space",
    8L, "Multiple distinct space polities",                                                                                 "distinct polities",
    8L, "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",      "high fragmentation",
    8L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q9 -- genre
    9L, "Adventure / exploration",                                                                                          "adventure",
    9L, "Drama",                                                                                                            "drama",
    9L, "Political / diplomatic",                                                                                           "political",
    9L, "Military / war",                                                                                                   "military/war",
    9L, "Thriller / Horror / Survival",                                                                                     "thriller/horror",
    9L, "Comedy / satire",                                                                                                  "comedy",
    9L, "Other / Unsure",                                                                                                   "Other / Unsure",
    # Q10 -- military or civilian domain
    10L, "Entirely civilian",                                                                                               "civilian",
    10L, "Mostly civilian with some military presence",                                                                     "mostly civilian",
    10L, "Mixed civilian-military domain",                                                                                  "mixed",
    10L, "Mostly military",                                                                                                 "mostly military",
    10L, "Entirely military / war-focused",                                                                                 "military",
    10L, "Other / Unsure",                                                                                                  "Other / Unsure",
    # Q11 -- nearest neighbor
    11L, "Totally unique domain",                                                                                           "unique",
    11L, "Like the ocean / naval",                                                                                          "ocean/naval",
    11L, "Like the air / airpower",                                                                                         "air/airpower",
    11L, "Like the frontier / colonial expansion",                                                                          "frontier/colonial",
    11L, "Like cyberspace / networked or abstract domain",                                                                  "cyberspace",
    11L, "Other / Unsure",                                                                                                  "Other / Unsure",
    # Q12 -- physical differences
    12L, "Almost Earth-like",                                                                                               "earth-like",
    12L, "Somewhat different (manageable environmental differences)",                                                       "minor differences",
    12L, "Moderately different (regular adaptation needed)",                                                                "moderately different",
    12L, "Very different (human bodies/technology constantly challenged)",                                                  "very different",
    12L, "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",                            "radically different environment",
    12L, "Other / Unsure",                                                                                                  "Other / Unsure"
)


# 4e. Ordinal vs nominal question identifiers.
#
# The 10 ordinal questions get integer codes 1..5 from each question's
# canonical `answer_options` order (which is already low->high in
# questions.json), with "Other / Unsure" -> NA for any ordinal-only
# operation (mean, median, peak, alpha-ordinal).
#
# The 2 nominal questions (Q9 genre, Q11 nearest-neighbor metaphor) get
# NA for ordinal_position regardless of answer.  See PROJECT_TASKS §2.6
# and §5.4.
ordinal_question_numbers <- c(1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L, 10L, 12L)
nominal_question_numbers <- c(9L, 11L)


# -----------------------------------------------------------------------------
# 5. Helper functions
# -----------------------------------------------------------------------------

# 5a. parse_number_token(tok)
#     tok:     a single character token (e.g., "Eight", "VIII", "8",
#              "premier", "twenty-first").
#     Returns: integer position (>= 0) or NA_integer_ if not parseable.
#
#     Strategies tried, in order:
#       (i)   pure digits
#       (ii)  Roman numerals (case-insensitive, via base::as.roman)
#       (iii) compound ordinals split on hyphen, summed ("twenty-first" -> 21)
#       (iv)  English/French spelled-out cardinals & ordinals (lookup)
#
# Covers all spelled-out numbers we have observed in the corpus (0-30 plus
# compound ordinals 21-29).  Extend word_lookup if a future corpus uses
# higher numbers.
parse_number_token <- function(tok) {

    if (is.null(tok) || is.na(tok) || !nzchar(tok)) {
        return(NA_integer_)
    }

    tok_lc <- tolower(stringr::str_trim(tok))

    # Strip surrounding punctuation like "(2)" -> "2" but keep internal
    # hyphens so we can still split "twenty-first".
    tok_lc <- stringr::str_remove_all(tok_lc, "[^a-z0-9-]")

    if (!nzchar(tok_lc)) {
        return(NA_integer_)
    }

    # (i) Arabic
    if (stringr::str_detect(tok_lc, "^\\d+$")) {
        return(suppressWarnings(as.integer(tok_lc)))
    }

    # (ii) Roman numerals -- as.roman() returns NA silently for non-Roman
    # strings, so we restrict to the legal character set first.
    if (stringr::str_detect(tok_lc, "^[ivxlcdm]+$")) {
        n <- suppressWarnings(as.integer(as.roman(toupper(tok_lc))))
        if (!is.na(n)) {
            return(n)
        }
    }

    # (iii) Compound ordinals like "twenty-first" -> 20 + 1 = 21
    if (stringr::str_detect(tok_lc, "-")) {
        parts <- stringr::str_split(tok_lc, "-", simplify = TRUE)
        nums  <- vapply(parts, parse_number_token, integer(1))
        if (all(!is.na(nums)) && length(nums) >= 2) {
            return(as.integer(sum(nums)))
        }
    }

    # (iv) Spelled-out English & French
    word_lookup <- c(

        # English cardinals 0-20 plus 30 (the highest we observe)
        zero      = 0L,  one      = 1L,  two       = 2L,  three     = 3L,
        four      = 4L,  five     = 5L,  six       = 6L,  seven     = 7L,
        eight     = 8L,  nine     = 9L,  ten       = 10L, eleven    = 11L,
        twelve    = 12L, thirteen = 13L, fourteen  = 14L, fifteen   = 15L,
        sixteen   = 16L, seventeen = 17L, eighteen = 18L, nineteen  = 19L,
        twenty    = 20L, thirty   = 30L,

        # English ordinals 1st-20th plus 30th
        first     = 1L,  second    = 2L,  third     = 3L,  fourth    = 4L,
        fifth     = 5L,  sixth     = 6L,  seventh   = 7L,  eighth    = 8L,
        ninth     = 9L,  tenth     = 10L, eleventh  = 11L, twelfth   = 12L,
        thirteenth = 13L, fourteenth = 14L, fifteenth = 15L, sixteenth = 16L,
        seventeenth = 17L, eighteenth = 18L, nineteenth = 19L, twentieth = 20L,
        thirtieth  = 30L,

        # French ordinals (used in Les Guerriers du Silence)
        premier   = 1L, premiere  = 1L, deuxieme  = 2L, troisieme = 3L,
        quatrieme = 4L, cinquieme = 5L, sixieme   = 6L, septieme  = 7L,
        huitieme  = 8L, neuvieme  = 9L, dixieme   = 10L
    )

    if (tok_lc %in% names(word_lookup)) {
        return(unname(word_lookup[tok_lc]))
    }

    NA_integer_
}


# 5b. parse_chapter_position(label)
#     label:   a single chapter label string (e.g., "Chapter 3", "Part 2
#              Act V", "The Eighth Letter", "April 2000 - The Third
#              Expedition").
#     Returns: a one-row tibble with two integer columns:
#                part_position    -- numbered Part or Book, or NA
#                chapter_position -- numbered Chapter / Act / ordinal, or NA
#
#     Intended use: dplyr::mutate(parse_chapter_position(chapter)) followed by
#     tidyr::unnest_wider(), OR purrr::map_dfr() over a column.  See
#     data_loading.Rmd for the canonical call pattern.
#
#     Strategy (first match wins; tested against all 792 distinct labels in
#     the corpus as of 2026-05-25):
#       1.  "Part N Chapter M"            -> part=N, chapter=M
#       2.  "Part N Act M"                -> part=N, chapter=M
#       3.  "Part N PROLOGUE/EPILOGUE"    -> part=N, chapter=NA
#       4.  "Part N - <rest>"             -> part=N; recurse on <rest>
#       5.  "Part N" alone                -> part=NA, chapter=N
#                                            (the Part IS the unit)
#       6.  "Chapter N" / "Chapitre N" /
#           "Episode N" / "Interlude N"   -> part=NA, chapter=N
#       7.  "Act N" alone                 -> part=NA, chapter=N
#       8.  "<Month> <Year> - <rest>"     -> part=NA, chapter=year*12+month
#           (Martian Chronicles labels;
#            returns a YYYYMM-style sort key)
#       9.  "The Nth <noun>"              -> part=NA, chapter=N
#           (e.g., "The Eighth Letter",
#            "The Twenty-First Letter")
#       10. Bare Roman or Arabic at start -> part=NA, chapter=N
#       11. Fallback                      -> part=NA, chapter=NA
#
parse_chapter_position <- function(label) {

    # Return shape helper, kept local so callers don't need to remember it.
    out <- function(part = NA_integer_, chap = NA_integer_) {
        tibble::tibble(
            part_position    = as.integer(part),
            chapter_position = as.integer(chap)
        )
    }

    if (is.null(label) || is.na(label) || !nzchar(label)) {
        return(out())
    }

    s <- stringr::str_trim(label)

    month_lookup <- c(
        january   = 1L,  february = 2L,  march    = 3L,  april    = 4L,
        may       = 5L,  june     = 6L,  july     = 7L,  august   = 8L,
        september = 9L,  october  = 10L, november = 11L, december = 12L
    )

    # 1 + 2: "Part N Chapter M" / "Part N Act M" / "Part N Episode M"
    # (optional dash between the two segments).
    m <- stringr::str_match(
        s,
        stringr::regex(
            "^(part|book)\\s+(\\S+)\\s*[-:]?\\s*(chapter|chapitre|act|episode)\\s+(\\S+)\\b",
            ignore_case = TRUE
        )
    )
    if (!is.na(m[1, 2])) {
        return(out(parse_number_token(m[1, 3]), parse_number_token(m[1, 5])))
    }

    # 3: "Part N PROLOGUE/EPILOGUE" (e.g., Usurper of the Sun)
    m <- stringr::str_match(
        s,
        stringr::regex(
            "^(part|book)\\s+(\\S+)\\s*[-:]?\\s*(prologue|epilogue)\\b",
            ignore_case = TRUE
        )
    )
    if (!is.na(m[1, 2])) {
        return(out(parse_number_token(m[1, 3]), NA_integer_))
    }

    # 4: "Part N - <rest>" -> recurse on <rest> so e.g. "Book 1 - Chapter 10"
    # picks up chapter_position from the inner Chapter call.
    m <- stringr::str_match(
        s,
        stringr::regex(
            "^(part|book)\\s+(\\S+?)\\s*[-:]\\s*(.+)$",
            ignore_case = TRUE
        )
    )
    if (!is.na(m[1, 2])) {
        rec <- parse_chapter_position(m[1, 4])
        return(out(parse_number_token(m[1, 3]), rec$chapter_position))
    }

    # 5: "Part N" alone -- the Part IS the structural unit
    m <- stringr::str_match(
        s,
        stringr::regex("^(part|book)\\s+(\\S+)\\s*$", ignore_case = TRUE)
    )
    if (!is.na(m[1, 2])) {
        return(out(NA_integer_, parse_number_token(m[1, 3])))
    }

    # 6: "Chapter N" / "Chapitre N" / "Episode N" / "Interlude N"
    m <- stringr::str_match(
        s,
        stringr::regex(
            "^(chapter|chapitre|ch\\.?|episode|interlude)\\s+(\\S+)\\b",
            ignore_case = TRUE
        )
    )
    if (!is.na(m[1, 2])) {
        return(out(NA_integer_, parse_number_token(m[1, 3])))
    }

    # 7: "Act N" alone
    m <- stringr::str_match(
        s,
        stringr::regex("^act\\s+(\\S+)\\b", ignore_case = TRUE)
    )
    if (!is.na(m[1, 2])) {
        return(out(NA_integer_, parse_number_token(m[1, 2])))
    }

    # 8: Date-prefixed Bradbury labels.  Returns year*12 + month so that the
    # integer sorts chronologically across years.
    m <- stringr::str_match(
        s,
        stringr::regex(
            paste0("^(january|february|march|april|may|june|july|august|",
                   "september|october|november|december)\\s+(\\d{4})\\b"),
            ignore_case = TRUE
        )
    )
    if (!is.na(m[1, 2])) {
        month_num <- unname(month_lookup[tolower(m[1, 2])])
        year_num  <- suppressWarnings(as.integer(m[1, 3]))
        if (!is.na(month_num) && !is.na(year_num)) {
            return(out(NA_integer_, as.integer(year_num * 12L + month_num)))
        }
    }

    # 9: "The Nth <noun>" -- e.g., "The Eighth Letter", "The Twenty-First Letter"
    m <- stringr::str_match(
        s,
        stringr::regex("^the\\s+([a-z]+(?:-[a-z]+)?)\\s+\\w+", ignore_case = TRUE)
    )
    if (!is.na(m[1, 2])) {
        n <- parse_number_token(m[1, 2])
        if (!is.na(n)) {
            return(out(NA_integer_, n))
        }
    }

    # 10: Bare Roman or Arabic at start of label
    m <- stringr::str_match(s, "^([ivxlcdmIVXLCDM]+|\\d+)\\b")
    if (!is.na(m[1, 2])) {
        n <- parse_number_token(m[1, 2])
        if (!is.na(n)) {
            return(out(NA_integer_, n))
        }
    }

    # 11: Fallback -- unparseable label
    out()
}


# 5c. clean_book_name(stem, default)
#     stem:    filename without the .csv extension
#              (e.g., "US_Human_Split_Enders_Game").
#     default: the value of the `book` column inside the CSV.
#     Returns: the override from book_rename_map if present, otherwise the
#              default.  Used to harmonize the `book` column across files.
#              See PROJECT_TASKS.md §2.3.
clean_book_name <- function(stem, default) {
  if (stem %in% names(book_rename_map)) {
    return(unname(book_rename_map[stem]))
  }
  default
}


# 5d. drop_paratext(df)
#     df:      a tibble with at least a character column `chapter`.
#     Returns: df with paratext rows removed.  Uses paratext_regex (§4a).
drop_paratext <- function(df) {
  df %>%
    dplyr::filter(!stringr::str_detect(chapter, paratext_regex))
}


# 5e. load_results_csv(path)
#     path:    absolute path to one per-book CSV in data/results/.
#     Returns: a wide tibble with the columns the analyzer wrote, plus
#              `source_file` and `file_stem` provenance columns.  All q* and
#              q*_justification columns are coerced to character to prevent
#              readr from guessing logical/numeric for low-cardinality columns.
load_results_csv <- function(path) {

  df <- readr::read_csv(
      path,
      show_col_types = FALSE,
      progress       = FALSE,
      na             = character(0)   # do NOT treat any string as missing
  )

  q_cols <- grep("^q\\d+(_justification)?$", names(df), value = TRUE)
  df[q_cols] <- lapply(df[q_cols], as.character)

  df$source_file <- basename(path)
  df$file_stem   <- tools::file_path_sans_ext(basename(path))

  df
}


# 5f. validate_answers(df, questions)
#     df:        a wide tibble with columns country, book, chapter, q1..qN.
#     questions: parsed contents of data/questions.json (a list of lists,
#                each with $number, $criteria_short, $answer_options).
#     Returns:   a tibble of rows where the answer is NOT in the canonical
#                answer_options for that question.  Empty tibble => clean.
validate_answers <- function(df, questions) {

  mismatches <- purrr::map_dfr(questions, function(q) {

    col <- paste0("q", q$number)
    if (!col %in% names(df)) {
      return(tibble::tibble())
    }

    bad <- df %>%
      dplyr::select(country, book, chapter, !!col) %>%
      dplyr::rename(answer = !!col) %>%
      dplyr::filter(!answer %in% q$answer_options)

    if (nrow(bad) == 0) {
      return(tibble::tibble())
    }

    bad %>% dplyr::mutate(
        question_number = q$number,
        criteria_short  = q$criteria_short,
        valid_options   = paste(q$answer_options, collapse = " | ")
    )
  })

  mismatches
}


# 5g. pivot_to_long(df_wide, questions)
#     df_wide:   the cleaned wide tibble (one row per chapter, q1..qN columns
#                and q1_justification..qN_justification columns).
#     questions: parsed contents of data/questions.json (used to attach
#                criteria_short metadata in the long frame).
#     Returns:   a long tibble (one row per chapter x question) with columns:
#                  country, book, chapter, chapter_position, part_position,
#                  question_number, question_id, criteria_short,
#                  answer, justification, source_file, file_stem.
pivot_to_long <- function(df_wide, questions) {

  meta_cols <- c("country", "book", "chapter", "chapter_position",
                 "part_position", "source_file", "file_stem")
  meta_cols <- intersect(meta_cols, names(df_wide))

  answers_long <- df_wide %>%
      dplyr::select(dplyr::all_of(meta_cols), dplyr::matches("^q\\d+$")) %>%
      tidyr::pivot_longer(
          cols      = dplyr::matches("^q\\d+$"),
          names_to  = "question_id",
          values_to = "answer"
      )

  justifs_long <- df_wide %>%
      dplyr::select(dplyr::all_of(meta_cols),
                    dplyr::matches("^q\\d+_justification$")) %>%
      tidyr::pivot_longer(
          cols      = dplyr::matches("^q\\d+_justification$"),
          names_to  = "question_id",
          values_to = "justification"
      ) %>%
      dplyr::mutate(
          question_id = stringr::str_remove(question_id, "_justification")
      )

  q_meta <- tibble::tibble(
      question_number = purrr::map_int(questions, "number"),
      criteria_short  = purrr::map_chr(questions, "criteria_short")
  ) %>%
      dplyr::mutate(question_id = paste0("q", question_number))

  answers_long %>%
      dplyr::left_join(justifs_long, by = c(meta_cols, "question_id")) %>%
      dplyr::left_join(q_meta,       by = "question_id") %>%
      dplyr::select(
          dplyr::any_of(c("country", "book", "chapter",
                          "chapter_position", "part_position")),
          question_number, question_id, criteria_short,
          answer, justification,
          dplyr::any_of(c("source_file", "file_stem"))
      )
}


# 5h. get_answer_short(question_number, answer)
#     question_number: integer vector of question IDs (1..12).
#     answer:          character vector of canonical answer texts (must
#                      match `questions.json$answer_options` exactly).
#     Returns:         character vector of short labels from
#                      answer_options_short_lookup, same length as inputs.
#                      Returns NA where no short label is known and emits
#                      a warning listing the offending (q, a) pairs so
#                      typos surface immediately at the plot/table layer.
get_answer_short <- function(question_number, answer) {

    stopifnot(length(question_number) == length(answer))

    keys <- tibble::tibble(
        question_number = as.integer(question_number),
        answer          = as.character(answer)
    )

    out <- keys %>%
        dplyr::left_join(answer_options_short_lookup,
                         by = c("question_number", "answer"))

    missing <- out %>%
        dplyr::filter(!is.na(answer), is.na(answer_short)) %>%
        dplyr::distinct(question_number, answer)

    if (nrow(missing) > 0) {
        warning(
            "get_answer_short(): no short label for ", nrow(missing),
            " (question, answer) pair(s).  First few: ",
            paste(
                head(paste0("Q", missing$question_number, " ",
                            sQuote(missing$answer)), 5),
                collapse = " | "
            ),
            call. = FALSE
        )
    }

    out$answer_short
}


# 5i. build_ordinal_lookup(questions)
#     Build a long-format tibble mapping (question_number, answer) to
#     an integer ordinal_position in 1..5 for ordinal questions, NA
#     otherwise (Other / Unsure, and all answers to nominal questions).
#     `questions` is the parsed contents of data/questions.json.
build_ordinal_lookup <- function(questions) {

    purrr::map_dfr(questions, function(q) {

        qn   <- q$number
        opts <- unlist(q$answer_options)
        # Strip Other / Unsure from the substantive position assignment;
        # it always maps to NA.
        substantive <- setdiff(opts, "Other / Unsure")

        positions <- if (qn %in% ordinal_question_numbers) {
            as.integer(seq_along(substantive))
        } else {
            rep(NA_integer_, length(substantive))
        }

        tibble::tibble(
            question_number  = as.integer(qn),
            answer           = c(substantive, "Other / Unsure"),
            ordinal_position = c(positions, NA_integer_)
        )
    })
}


# 5j. add_ordinal_position(df, questions)
#     Take a long-format tibble with `question_number` and `answer`
#     columns and add an `ordinal_position` column via left-join against
#     build_ordinal_lookup(questions).  Surfaces any (question, answer)
#     pair that isn't in the lookup as a warning.
add_ordinal_position <- function(df, questions) {

    lookup <- build_ordinal_lookup(questions)

    out <- df %>%
        dplyr::left_join(lookup,
                         by = c("question_number", "answer"))

    # Sanity check: every non-NA answer should have matched.
    miss <- out %>%
        dplyr::filter(!is.na(answer), is.na(ordinal_position),
                      question_number %in% ordinal_question_numbers) %>%
        dplyr::distinct(question_number, answer)

    # Note: NA ordinal_position for Other / Unsure is EXPECTED, so we
    # only warn if a non-Other answer to an ordinal question failed to
    # match.
    miss <- miss %>% dplyr::filter(answer != "Other / Unsure")
    if (nrow(miss) > 0) {
        warning(
            "add_ordinal_position(): ", nrow(miss),
            " ordinal (q, answer) pair(s) failed to match.  First few: ",
            paste(
                head(paste0("Q", miss$question_number, " ",
                            sQuote(miss$answer)), 5),
                collapse = " | "
            ),
            call. = FALSE
        )
    }

    out
}


# 5k. load_collection_metadata(path)
#     Read data/collection_metadata.csv (or another path) and return a
#     tibble with columns: book, country, classification, is_collection,
#     n_stories, story_chapter_mapping, uncertain, agent_notes.
#     `book` is canonical and matches Claude's wide/long frames.
load_collection_metadata <- function(path = file.path(
                                         DATA_DIR,
                                         "collection_metadata.csv")) {
    readr::read_csv(
        path,
        show_col_types = FALSE,
        progress       = FALSE
    )
}
