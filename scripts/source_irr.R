# =============================================================================
# source_irr.R
# IRR-specific helpers, loaders, and constants for Task 2 (intercoder
# reliability) of the Space Sci-Fi Analysis Pipeline.
# =============================================================================
# Sourced AFTER scripts/source.R by intercoder_reliability.Rmd.  Provides:
#
#   1. Manifest of the 5 human-coded books
#   2. Per-book chapter alignment (human integer chapter -> Claude chapter label)
#   3. Mapped-answer correction table (mechanical fixes approved 2026-05-25)
#   4. Per-book coverage overrides (drop OoC "General notes"; move OoC Q4 -> Q12;
#      record Apes Q12 as not covered)
#   5. Schema-specific loaders
#        5a. load_human_long_xlsx()    -- Martian, 3BP, Apes
#        5b. load_human_wide_xlsx_ooc()-- Off on a Comet
#        5c. load_human_csv_eg()       -- Ender's Game
#   6. Cleaners
#        6a. apply_mapped_answer_corrections()
#        6b. coerce_human_na_to_other_unsure()
#        6c. canonicalize_residuals_to_other_unsure()
#        6d. validate_human_answers()
#        6e. align_human_chapter_to_claude()
#   7. Load-all wrapper: load_all_human_coded()
#   8. IRR computation
#        8a. compute_irr_per_question()    -- per (book, question)
#        8b. compute_irr_overall()         -- per question pooled across books
#        8c. format_irr_table()            -- gt-ready summary
#
# Style: matches scripts/source.R (4-space inside multi-line calls; %>%
# pipe; snake_case).  All public objects are defined at top level so they
# can be inspected interactively after sourcing.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Manifest of human-coded books
# -----------------------------------------------------------------------------
#
# Each entry tells the loader where the file is, what schema it uses, and
# (for the three long-format xlsx files) which sheet and which "Mapped
# Answer" column to read.  `book` matches the canonical title in Claude's
# processed wide frame (i.e., after book_rename_map normalization).

human_coded_files <- tibble::tribble(
    ~book,                    ~schema,    ~filename,                                ~sheet,           ~header_row, ~mapped_col,
    "The Martian",            "long_xlsx", "2026_Coding_Martian_updated.xlsx",      "Coding Sheet",   2L,          "Mapped Answer (from Answer Set)",
    "The Three-Body Problem", "long_xlsx", "3_Body_problem_updated coding.xlsx",    "Sheet1",         2L,          "Mapped Answer",
    "Planet of the Apes",     "long_xlsx", "Planet_of_the_Apes_updated_Coding.xlsx","Coding Sheet",   1L,          "Mapped Answer (from Answer Set)",
    "Off on a Comet",         "wide_ooc",  "Off_on_a_Comet_mapped_answers.xlsx",    "Mapped Chapters",NA_integer_, NA_character_,
    "Ender's Game",           "csv_eg",    "enders_game.csv",                       NA_character_,    NA_integer_, NA_character_
)


# -----------------------------------------------------------------------------
# 2. Per-book chapter alignment
# -----------------------------------------------------------------------------
#
# Function returning the Claude chapter label for a human integer chapter
# number.  Four of five books are trivial 1:1 on `chapter_position`; only
# Off on a Comet needs a per-book lookup because Claude's chapter labels
# carry a "Book 1 - " prefix.  Each rule returns either a chapter LABEL
# (matched directly to claude$chapter) or NA when the human chapter has
# no corresponding Claude row.
#
# Behavior: given a `book` and integer `human_chapter`, returns the Claude
# chapter label as a string.  The IRR pipeline joins on that label, not
# on chapter_position, because chapter_position can be NA for some
# date-prefixed labels and we want the alignment to be explicit.

chapter_alignment_rules <- list(

    "The Martian" = function(human_chapter, claude_chapters) {
        # Trivial 1:1 -- human ch N corresponds to "Chapter N"
        label <- paste0("Chapter ", human_chapter)
        if (label %in% claude_chapters) label else NA_character_
    },

    "The Three-Body Problem" = function(human_chapter, claude_chapters) {
        label <- paste0("Chapter ", human_chapter)
        if (label %in% claude_chapters) label else NA_character_
    },

    "Planet of the Apes" = function(human_chapter, claude_chapters) {
        label <- paste0("Chapter ", human_chapter)
        if (label %in% claude_chapters) label else NA_character_
    },

    "Ender's Game" = function(human_chapter, claude_chapters) {
        # Claude's labels are "Chapter N - <TITLE>"; match by prefix.
        prefix <- paste0("Chapter ", human_chapter, " -")
        hits   <- claude_chapters[startsWith(claude_chapters, prefix)]
        if (length(hits) == 1) hits else NA_character_
    },

    "Off on a Comet" = function(human_chapter, claude_chapters) {
        # Human coded only ch 1..10; map to "Book 1 - Chapter N".
        if (human_chapter < 1L || human_chapter > 10L) return(NA_character_)
        label <- paste0("Book 1 - Chapter ", human_chapter)
        if (label %in% claude_chapters) label else NA_character_
    }
)


# -----------------------------------------------------------------------------
# 3. Mapped-answer correction table
# -----------------------------------------------------------------------------
#
# Approved 2026-05-25 in data/processed/human_mapped_answer_proposals.md.
# Each row says: when (question_number, raw_value) is observed in any human-
# coded file, replace it with `to_value` BEFORE validating.
#
# The Q12 "Mostly Earth-like..." -> "Almost Earth-like" rule is the only
# judgment call -- a Q4 (cultural) label was pasted into a Q12 (physical)
# slot; we remap to the parallel Q12 short-label "earth-like" which is
# canonically "Almost Earth-like".

human_mapped_answer_corrections <- tibble::tribble(
    ~question_number, ~from_value,                                                            ~to_value,
    # §A.1 Three-Body Problem: trailing semicolon
    1L,  "Moderate contestation (ongoing rivalry/disputes);",                                 "Moderate contestation (ongoing rivalry/disputes)",
    # §A.2 Three-Body Problem: trailing semicolon
    2L,  "Visiting / Temporary presence only (stations, missions, outposts);",                "Visiting / Temporary presence only (stations, missions, outposts)",
    # §A.3 Off on a Comet (Q12 after the OoC Q4->Q12 move): trailing semicolon
    12L, "Moderately different (regular adaptation needed);",                                 "Moderately different (regular adaptation needed)",
    # §A.4 Off on a Comet: shorthand "Civilian" -> canonical "Entirely civilian"
    10L, "Civilian",                                                                          "Entirely civilian",
    # §C.5 Ender's Game: shorthand 'long-distance journey'
    3L,  "long-distance journey",                                                             "Long-distance journey (years, major separation from Earth)",
    # §C.5 Ender's Game: Q4 label pasted into Q12 slot (judgment call)
    12L, "Mostly Earth-like with minor adaptations",                                          "Almost Earth-like"
)


# -----------------------------------------------------------------------------
# 4. Per-book coverage overrides
# -----------------------------------------------------------------------------
#
# Structural decisions that are NOT mechanical text replacements; baked
# into the loaders rather than the correction table.

human_coverage_overrides <- list(

    # OoC: criteria row 12 is labeled "General notes", not Q12.  Drop entirely.
    ooc_drop_general_notes_row    = TRUE,

    # OoC: criteria rows 4 use Q12's option list (not Q4's).  Move
    # q_number 4 -> 12 inside the OoC loader.
    ooc_move_q4_to_q12            = TRUE,

    # Apes: file has only Q1..Q11.  Q12 is treated as not covered for this
    # book; IRR rolls up across only the questions actually coded.
    apes_q12_not_covered          = TRUE
)


# -----------------------------------------------------------------------------
# 5. Schema-specific loaders
# -----------------------------------------------------------------------------
#
# Each loader returns a long tibble with columns:
#   book          (matches Claude's `book`)
#   chapter_human (integer; the human rater's chapter index)
#   q_number      (integer 1..12)
#   mapped_answer (character; raw value from the file, before any cleaning)
#
# Loaders DO NOT apply corrections, NA-coercion, or chapter alignment --
# those are downstream steps so the raw signal is preserved.


# Helper: find the first row in `raw` whose cells contain ANY of
# `required` (after trimming whitespace).  For long-xlsx files we
# require ALL of c("Chapter", "Question #", <mapped_col>) to coincide
# in the same row; for OoC we just look for "Criteria".  Returns the
# row index (1-based, into `raw`), or stops with a diagnostic if no
# match is found in the first `max_rows` rows.
detect_header_row <- function(raw, required, max_rows = 10L,
                              require_all = TRUE) {

    upper <- min(max_rows, nrow(raw))
    for (i in seq_len(upper)) {
        row_vals <- trimws(as.character(unlist(raw[i, ])))
        hit <- if (require_all) {
            all(required %in% row_vals)
        } else {
            any(required %in% row_vals)
        }
        if (hit) {
            return(i)
        }
    }

    # Diagnostic dump of the first few rows so the caller can see what
    # readxl actually returned.
    dump_rows <- vapply(seq_len(upper), function(i) {
        paste0("    row ", i, ": ",
               paste(shQuote(trimws(as.character(unlist(raw[i, ])))),
                     collapse = ", "))
    }, character(1))

    stop(
        "detect_header_row(): could not locate header row containing ",
        if (require_all) "ALL of " else "any of ",
        paste(shQuote(required), collapse = ", "),
        " in the first ", upper, " rows of the sheet.\n",
        paste(dump_rows, collapse = "\n")
    )
}


# 5a. Long-xlsx loader (Martian, 3BP, Apes).
#
# The three long-xlsx files share a header containing "Chapter",
# "Question #", and one of two Mapped Answer column names; rows below
# are one (Chapter, Question #, Mapped Answer) record each.
#
# We force `col_types = "text"` so EVERY column comes back as character
# (otherwise readxl's type inference coerces header strings like
# "Chapter" to NA when the column body is mostly integers).
#
# We AUTO-DETECT the header row rather than hard-coding it, because
# readxl with `range = NULL` silently trims leading blank rows AND
# blank columns -- so the sheet-row index of the header can differ
# from the index readxl exposes (e.g., Martian's sheet row 2 becomes
# readxl row 1 because sheet row 1 is blank).  The `header_row`
# argument is accepted for backwards-compatibility but ignored.
load_human_long_xlsx <- function(book, path, sheet, header_row = NULL,
                                 mapped_col) {

    raw <- readxl::read_excel(
        path,
        sheet     = sheet,
        col_names = FALSE,
        col_types = "text"
    )

    required <- c("Chapter", "Question #", mapped_col)

    detected_row <- detect_header_row(raw, required, max_rows = 10L)

    header <- as.character(unlist(raw[detected_row, ]))

    # Replace NA / empty header cells with unique placeholders so the
    # subsequent `colnames(body) <- header` doesn't either fail (modern
    # tibble) or assign duplicate empty names (older tibble).  Also trim
    # whitespace so an Excel-introduced trailing space doesn't break the
    # exact-match `setdiff` below.
    blank_mask <- is.na(header) | !nzchar(trimws(header))
    if (any(blank_mask)) {
        header[blank_mask] <- paste0("__blank_",
                                     seq_len(sum(blank_mask)))
    }
    header <- trimws(header)

    body   <- raw[(detected_row + 1L):nrow(raw), , drop = FALSE]
    colnames(body) <- header

    missing  <- setdiff(required, colnames(body))
    if (length(missing) > 0) {
        stop(
            "load_human_long_xlsx(", book, "): missing column(s) ",
            paste(missing, collapse = ", "),
            "\n  detected header row (in readxl frame, 1-based) = ",
            detected_row,
            "\n  file = ", path,
            "\n  header row actually contains (", length(header),
            " cols): ",
            paste(shQuote(header), collapse = ", ")
        )
    }

    sub <- body[, required, drop = FALSE]
    colnames(sub) <- c("chapter_human", "q_number", "mapped_answer")

    sub <- sub %>%
        dplyr::filter(!(is.na(chapter_human) & is.na(q_number) &
                            is.na(mapped_answer))) %>%
        dplyr::mutate(
            book           = book,
            # Go through as.numeric() first so "1.0" -> 1L works (readxl
            # in col_types="text" mode usually returns "1", but a few
            # spreadsheets format ints as floats).
            chapter_human  = suppressWarnings(as.integer(as.numeric(chapter_human))),
            q_number       = suppressWarnings(as.integer(as.numeric(q_number))),
            mapped_answer  = as.character(mapped_answer)
        ) %>%
        dplyr::select(book, chapter_human, q_number, mapped_answer)

    # Drop rows missing the join keys (chapter_human OR q_number)
    sub %>% dplyr::filter(!is.na(chapter_human), !is.na(q_number))
}


# 5b. Wide-xlsx loader for Off on a Comet.
#
# The "Mapped Chapters" sheet stores criteria as rows and chapters as
# paired columns (Chapter N + Chapter N Answer).  Header is at sheet row
# 4 (1-based); body has 12 criteria rows.  Per §4 coverage overrides:
#   - drop criteria row 12 ("General notes")
#   - rename q_number 4 -> 12 (the rater used Q12's option list there)
#
# IMPORTANT: empty cells in a WIDE grid mean "not coded" (the human did
# not enter anything), not "deliberate Other / Unsure".  Per proposals
# §C.3, Q5/Q8/Q11 are entirely uncoded and chapters 11..43 likewise.
# We therefore drop NA mapped_answer rows AT THE LOADER, so those cells
# never enter the NA -> Other/Unsure coercion step downstream.  Long-
# format files (Martian / 3BP / Apes / EG) keep the opposite convention:
# every row is a deliberate coding event, so NaN means the rater chose
# to leave it blank -- which we then coerce to "Other / Unsure".
load_human_wide_xlsx_ooc <- function(path) {

    # See §5a comment: force every column to text so the header strings
    # survive readxl's column-type inference, then auto-detect the
    # header row (readxl trims leading blank rows / cols, so its
    # row index can differ from the spreadsheet's).
    raw <- readxl::read_excel(
        path,
        sheet     = "Mapped Chapters",
        col_names = FALSE,
        col_types = "text"
    )

    detected_row <- detect_header_row(
        raw,
        required    = c("Criteria"),
        max_rows    = 10L,
        require_all = FALSE
    )

    header <- as.character(unlist(raw[detected_row, ]))

    # Same defensive cleanup as §5a: protect colnames<- from NA / empty
    # cells in the header row, and trim whitespace for robust matching.
    blank_mask <- is.na(header) | !nzchar(trimws(header))
    if (any(blank_mask)) {
        header[blank_mask] <- paste0("__blank_",
                                     seq_len(sum(blank_mask)))
    }
    header <- trimws(header)

    body   <- raw[(detected_row + 1L):nrow(raw), , drop = FALSE]
    colnames(body) <- header

    # Add q_number from the row index; record the Criteria label too so we
    # can audit the General notes row drop in the report.
    body$q_number       <- seq_len(nrow(body))
    body$criteria_label <- body[["Criteria"]]

    # Drop "General notes" row (criteria row 12) -- not a real Q12
    if (isTRUE(human_coverage_overrides$ooc_drop_general_notes_row)) {
        body <- body %>%
            dplyr::filter(!grepl("^General notes", criteria_label,
                                 ignore.case = TRUE))
    }

    # Move Q4 -> Q12 (rater used Q12's option list in the Q4 slot)
    if (isTRUE(human_coverage_overrides$ooc_move_q4_to_q12)) {
        body <- body %>%
            dplyr::mutate(q_number = dplyr::if_else(q_number == 4L, 12L,
                                                   as.integer(q_number)))
    }

    # Reshape: keep "Chapter N Answer" columns, pivot long
    answer_cols <- grep("^Chapter \\d+ Answer$", colnames(body),
                        value = TRUE)
    long <- body %>%
        dplyr::select(q_number, dplyr::all_of(answer_cols)) %>%
        tidyr::pivot_longer(
            cols      = dplyr::all_of(answer_cols),
            names_to  = "ch_label",
            values_to = "mapped_answer"
        ) %>%
        dplyr::mutate(
            chapter_human = as.integer(
                sub("^Chapter (\\d+) Answer$", "\\1", ch_label)
            ),
            book          = "Off on a Comet",
            mapped_answer = as.character(mapped_answer)
        ) %>%
        dplyr::select(book, chapter_human, q_number, mapped_answer) %>%
        # Wide-grid empties are "not coded", not "deliberate Other/Unsure";
        # drop here so they don't survive into the IRR pipeline.
        dplyr::filter(
            !is.na(chapter_human),
            !is.na(q_number),
            !is.na(mapped_answer),
            nzchar(trimws(mapped_answer))
        )

    long
}


# 5c. CSV loader for Ender's Game.
#
# The file has the long-format coding block on the left (columns chapter,
# question, answer, explanation) and a shorthand reference block on the
# right -- we only read the left block here, since the shorthand map was
# extracted by hand into answer_options_short_lookup in source.R.
load_human_csv_eg <- function(path) {

    df <- readr::read_csv(
        path,
        show_col_types = FALSE,
        progress       = FALSE,
        na             = c("", "NA")
    )

    required <- c("chapter", "question", "answer")
    missing  <- setdiff(required, names(df))
    if (length(missing) > 0) {
        stop("load_human_csv_eg: missing column(s) ",
             paste(missing, collapse = ", "))
    }

    df %>%
        dplyr::select(chapter_human = chapter, q_number = question,
                      mapped_answer = answer) %>%
        dplyr::mutate(
            book          = "Ender's Game",
            chapter_human = suppressWarnings(as.integer(chapter_human)),
            q_number      = suppressWarnings(as.integer(q_number)),
            mapped_answer = as.character(mapped_answer)
        ) %>%
        dplyr::filter(!is.na(chapter_human), !is.na(q_number)) %>%
        dplyr::select(book, chapter_human, q_number, mapped_answer)
}


# -----------------------------------------------------------------------------
# 6. Cleaners
# -----------------------------------------------------------------------------

# 6a. Apply approved mapped-answer corrections.
apply_mapped_answer_corrections <- function(df) {
    df %>%
        dplyr::left_join(
            human_mapped_answer_corrections,
            by = c("q_number" = "question_number",
                   "mapped_answer" = "from_value")
        ) %>%
        dplyr::mutate(
            mapped_answer = dplyr::if_else(!is.na(to_value),
                                           to_value, mapped_answer)
        ) %>%
        dplyr::select(-to_value)
}


# 6b. Coerce NA / blank -> "Other / Unsure" (per locked-in IRR decision).
coerce_human_na_to_other_unsure <- function(df) {
    df %>%
        dplyr::mutate(
            mapped_answer = dplyr::case_when(
                is.na(mapped_answer)        ~ "Other / Unsure",
                trimws(mapped_answer) == "" ~ "Other / Unsure",
                TRUE                        ~ trimws(as.character(mapped_answer))
            )
        )
}


# 6c. Final residual cleanup: any value that is STILL not in the canonical
#     answer_options after corrections is coerced to "Other / Unsure"
#     (and surfaced via attr() so the report can show what was coerced).
canonicalize_residuals_to_other_unsure <- function(df, questions) {

    canonical <- purrr::map(questions, "answer_options")
    names(canonical) <- purrr::map_int(questions, "number")

    coerced <- df %>%
        dplyr::rowwise() %>%
        dplyr::mutate(
            is_canonical = mapped_answer %in% canonical[[as.character(q_number)]]
        ) %>%
        dplyr::ungroup()

    residuals <- coerced %>% dplyr::filter(!is_canonical)

    out <- coerced %>%
        dplyr::mutate(
            mapped_answer = dplyr::if_else(is_canonical,
                                           mapped_answer,
                                           "Other / Unsure")
        ) %>%
        dplyr::select(-is_canonical)

    attr(out, "coerced_residuals") <- residuals
    out
}


# 6d. Validate -- after cleaning, every mapped_answer should be canonical.
#     Returns tibble of rows that are STILL non-canonical (should be empty).
validate_human_answers <- function(df, questions) {
    canonical <- purrr::map(questions, "answer_options")
    names(canonical) <- purrr::map_int(questions, "number")

    df %>%
        dplyr::rowwise() %>%
        dplyr::mutate(
            ok = mapped_answer %in% canonical[[as.character(q_number)]]
        ) %>%
        dplyr::ungroup() %>%
        dplyr::filter(!ok) %>%
        dplyr::select(-ok)
}


# 6e. Align human integer chapter to Claude's chapter label.
#     `claude_wide` is the cleaned wide frame from data_loading.Rmd
#     (must have columns book, chapter).  Returns df with an added
#     `chapter` column (the Claude label).  Rows that cannot be aligned
#     get chapter = NA and are dropped (with a warning).
align_human_chapter_to_claude <- function(df, claude_wide) {

    aligned <- df %>%
        dplyr::group_by(book) %>%
        dplyr::group_modify(function(book_df, key) {
            book_name <- key$book
            rule <- chapter_alignment_rules[[book_name]]
            if (is.null(rule)) {
                stop("No chapter_alignment_rules entry for book ", book_name)
            }
            claude_chapters <- claude_wide %>%
                dplyr::filter(book == book_name) %>%
                dplyr::pull(chapter)

            book_df$chapter <- vapply(book_df$chapter_human, function(n) {
                rule(n, claude_chapters)
            }, character(1))
            book_df
        }) %>%
        dplyr::ungroup()

    dropped <- aligned %>% dplyr::filter(is.na(chapter))
    if (nrow(dropped) > 0) {
        warning("align_human_chapter_to_claude(): ", nrow(dropped),
                " rows could not be aligned and will be dropped (",
                paste(unique(dropped$book), collapse = ", "), ")",
                call. = FALSE)
    }

    aligned %>% dplyr::filter(!is.na(chapter))
}


# -----------------------------------------------------------------------------
# 7. Load-all wrapper
# -----------------------------------------------------------------------------
#
# Convenience: read all 5 human-coded files, apply the corrections /
# NA-coercion / residual cleanup / chapter alignment, and return a tidy
# long tibble joined to Claude's per-chapter answers.  Output columns:
#   book, chapter, q_number, claude_answer, human_answer
#
# `claude_long` must come from data_loading.Rmd
# (data/processed/space_chapters_long.rds).

load_all_human_coded <- function(claude_wide, claude_long, questions) {

    raw_list <- lapply(seq_len(nrow(human_coded_files)), function(i) {
        row <- human_coded_files[i, ]
        path <- file.path(HUMAN_CODED_DIR, row$filename)
        switch(row$schema,
            "long_xlsx" = load_human_long_xlsx(
                book        = row$book,
                path        = path,
                sheet       = row$sheet,
                header_row  = row$header_row,
                mapped_col  = row$mapped_col
            ),
            "wide_ooc"  = load_human_wide_xlsx_ooc(path),
            "csv_eg"    = load_human_csv_eg(path),
            stop("Unknown schema: ", row$schema)
        )
    })
    raw <- dplyr::bind_rows(raw_list)

    cleaned <- raw %>%
        apply_mapped_answer_corrections() %>%
        coerce_human_na_to_other_unsure() %>%
        canonicalize_residuals_to_other_unsure(questions)

    aligned <- align_human_chapter_to_claude(cleaned, claude_wide)

    claude_pairs <- claude_long %>%
        dplyr::select(book, chapter, q_number = question_number,
                      claude_answer = answer)

    paired <- aligned %>%
        dplyr::inner_join(claude_pairs,
                          by = c("book", "chapter", "q_number")) %>%
        dplyr::rename(human_answer = mapped_answer) %>%
        dplyr::select(book, chapter, q_number,
                      claude_answer, human_answer)

    attr(paired, "raw")               <- raw
    attr(paired, "cleaned")           <- cleaned
    attr(paired, "aligned")           <- aligned
    attr(paired, "coerced_residuals") <- attr(cleaned, "coerced_residuals")

    paired
}


# -----------------------------------------------------------------------------
# 8. IRR computation
# -----------------------------------------------------------------------------
#
# We compute four metrics per (book, question), per pooled question, AND
# one corpus-wide pooled summary:
#
#   - exact_agreement  -- proportion of pairs where claude == human
#                         (always includes "Other / Unsure" matches)
#   - kappa            -- Cohen's UNWEIGHTED kappa (nominal; always
#                         includes Other / Unsure)
#   - kappa_weighted   -- Cohen's SQUARED-WEIGHTED kappa, ordinal
#                         questions only (Q1-Q8, Q10, Q12).  Pairs
#                         where EXACTLY ONE coder said Other / Unsure
#                         are dropped before this calc (Other / Unsure
#                         isn't on the ordinal scale); both-Other pairs
#                         are kept and contribute zero distance.
#   - alpha            -- Krippendorff's alpha.  For ordinal questions
#                         method = "ordinal" and the same one-sided-
#                         Other / Unsure drop applies.  For nominal
#                         questions (Q9, Q11) method = "nominal" and
#                         all pairs are kept.
#
# Locked-in design decisions (2026-05-25):
#   - Other / Unsure being a match counts as a match in EVERY metric.
#   - For ordinal metrics, pairs where EXACTLY ONE coder said
#     "Other / Unsure" are dropped (so Other / Unsure is never
#     treated as if it sat at position 6 of the ordinal scale).
#   - The corpus-wide pooled summary reports three things together:
#     pooled exact agreement, mean kappa across questions, and a
#     pooled Krippendorff's alpha computed on (question, answer)
#     re-encoded data so each (q, level) tuple is its own nominal
#     category.

ordinal_questions <- c(1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L, 10L, 12L)

other_unsure_label <- "Other / Unsure"

irr_threshold_kappa <- 0.60
irr_threshold_alpha <- 0.667


# 8a. compute_irr_metrics(): internal helper that computes all four
#     metrics for one (claude_answer, human_answer) vector pair sharing
#     a single question_number.  Used by both compute_irr_per_question()
#     and compute_irr_overall(); centralizes the Other / Unsure rules.
#
# Returns a one-row tibble with columns:
#   n_pairs          -- total pairs (after both coders provided a value)
#   n_both_other     -- pairs where BOTH coders said Other / Unsure
#   n_one_other      -- pairs where EXACTLY ONE coder said Other / Unsure
#                       (these are dropped from kappa_weighted / ordinal alpha)
#   exact_agreement, kappa, kappa_weighted, n_pairs_ordinal, alpha, scale
compute_irr_metrics <- function(claude_answer, human_answer, qn,
                                canonical) {

    lvls   <- canonical[[as.character(qn)]]
    is_ord <- qn %in% ordinal_questions
    scale  <- if (is_ord) "ordinal" else "nominal"

    claude_f <- factor(claude_answer, levels = lvls)
    human_f  <- factor(human_answer,  levels = lvls)

    both <- !is.na(claude_f) & !is.na(human_f)
    cf <- claude_f[both]; hf <- human_f[both]
    n  <- length(cf)

    n_both_other <- sum(cf == other_unsure_label &
                            hf == other_unsure_label)
    n_one_other  <- sum(xor(cf == other_unsure_label,
                            hf == other_unsure_label))

    base <- tibble::tibble(
        n_pairs           = n,
        n_both_other      = as.integer(n_both_other),
        n_one_other       = as.integer(n_one_other),
        exact_agreement   = if (n) mean(cf == hf) else NA_real_,
        kappa             = NA_real_,
        kappa_weighted    = NA_real_,
        n_pairs_ordinal   = NA_integer_,
        alpha             = NA_real_,
        scale             = scale
    )

    if (n < 2L) return(base)

    # Unweighted Cohen's kappa -- includes Other / Unsure as a real
    # category (both-Other counts as match; one-sided-Other counts as
    # disagreement).
    if (length(unique(c(as.character(cf), as.character(hf)))) >= 2L) {
        base$kappa <- tryCatch(
            irr::kappa2(data.frame(claude = cf, human = hf),
                        weight = "unweighted")$value,
            error = function(e) NA_real_
        )
    }

    if (is_ord) {
        # ORDINAL metrics: drop one-sided Other / Unsure pairs.
        # Both-Other pairs are kept (they contribute zero distance and
        # count as a perfect match in both weighted kappa and ordinal
        # alpha).
        keep_ord <- !xor(cf == other_unsure_label,
                         hf == other_unsure_label)
        cf_o <- cf[keep_ord]; hf_o <- hf[keep_ord]
        n_o  <- length(cf_o)
        base$n_pairs_ordinal <- as.integer(n_o)

        if (n_o >= 2L && length(unique(c(as.character(cf_o),
                                          as.character(hf_o)))) >= 2L) {
            base$kappa_weighted <- tryCatch(
                irr::kappa2(data.frame(claude = cf_o, human = hf_o),
                            weight = "squared")$value,
                error = function(e) NA_real_
            )
            mat <- rbind(as.integer(cf_o), as.integer(hf_o))
            base$alpha <- tryCatch(
                irr::kripp.alpha(mat, method = "ordinal")$value,
                error = function(e) NA_real_
            )
        }
    } else {
        # NOMINAL alpha: keep all pairs including Other / Unsure.
        if (length(unique(c(as.character(cf), as.character(hf)))) >= 2L) {
            mat <- rbind(as.integer(cf), as.integer(hf))
            base$alpha <- tryCatch(
                irr::kripp.alpha(mat, method = "nominal")$value,
                error = function(e) NA_real_
            )
        }
    }

    base
}


# 8b. compute_irr_per_question(): per (book, question) row of metrics.
compute_irr_per_question <- function(paired, questions) {

    canonical <- purrr::map(questions, "answer_options")
    names(canonical) <- purrr::map_int(questions, "number")

    paired %>%
        dplyr::group_by(book, q_number) %>%
        dplyr::group_modify(function(g, key) {
            compute_irr_metrics(g$claude_answer, g$human_answer,
                                key$q_number, canonical)
        }) %>%
        dplyr::ungroup()
}


# 8c. compute_irr_overall(): pool across books, one row per question.
compute_irr_overall <- function(paired, questions) {

    canonical <- purrr::map(questions, "answer_options")
    names(canonical) <- purrr::map_int(questions, "number")

    paired %>%
        dplyr::group_by(q_number) %>%
        dplyr::group_modify(function(g, key) {
            compute_irr_metrics(g$claude_answer, g$human_answer,
                                key$q_number, canonical)
        }) %>%
        dplyr::ungroup()
}


# 8d. compute_irr_pooled(): one-row corpus-wide summary across ALL
#     books AND ALL questions.  Combines several complementary roll-ups:
#
#       n_cells                      -- total (book, chapter, question) pairs
#       n_one_other                  -- pairs where exactly one coder said
#                                       Other/Unsure (dropped by the *_excl_*
#                                       variants below)
#       n_cells_excl_one_other       -- n_cells - n_one_other
#       pooled_exact_agreement       -- sum(claude == human) / n_cells
#       mean_kappa                   -- mean per-question kappa (na.rm = TRUE)
#       mean_kappa_weighted          -- mean per-question weighted kappa
#                                       (ordinal Qs only, na.rm = TRUE)
#       mean_alpha                   -- mean per-question alpha (na.rm = TRUE)
#       pooled_alpha_all             -- Krippendorff's alpha (nominal) on the
#                                       whole paired frame after re-encoding
#                                       every (q_number, answer) tuple as a
#                                       unique nominal integer.  ALL 1372
#                                       cells included; one-sided Other /
#                                       Unsure pairs count as disagreement.
#       pooled_alpha_excl_one_other  -- Same re-encoding, but pairs where
#                                       EXACTLY ONE coder said Other / Unsure
#                                       are dropped first.  Both-Other pairs
#                                       are kept (zero distance).  Matches
#                                       the rule the per-question ordinal
#                                       metrics use.
#
# `irr_overall` is the output of compute_irr_overall(paired, questions);
# the per-question means are taken from that frame so we don't recompute
# them here.
compute_irr_pooled <- function(paired, irr_overall) {

    n_total      <- nrow(paired)
    pooled_exact <- if (n_total) {
        mean(paired$claude_answer == paired$human_answer)
    } else NA_real_

    mean_k     <- mean(irr_overall$kappa,          na.rm = TRUE)
    mean_kw    <- mean(irr_overall$kappa_weighted, na.rm = TRUE)
    mean_alpha <- mean(irr_overall$alpha,          na.rm = TRUE)

    # (q_number, answer) re-encoding: every distinct (q, level) tuple
    # from EITHER coder gets its own integer.  Then run Krippendorff's
    # alpha on the recoded data as a single nominal task.
    code_lookup <- dplyr::bind_rows(
        paired %>%
            dplyr::distinct(q_number, claude_answer) %>%
            dplyr::transmute(q_number, answer = claude_answer),
        paired %>%
            dplyr::distinct(q_number, human_answer) %>%
            dplyr::transmute(q_number, answer = human_answer)
    ) %>%
        dplyr::distinct() %>%
        dplyr::arrange(q_number, answer) %>%
        dplyr::mutate(code = dplyr::row_number())

    encoded <- paired %>%
        dplyr::left_join(code_lookup,
                         by = c("q_number",
                                "claude_answer" = "answer")) %>%
        dplyr::rename(claude_code = code) %>%
        dplyr::left_join(code_lookup,
                         by = c("q_number",
                                "human_answer" = "answer")) %>%
        dplyr::rename(human_code = code)

    # Pooled alpha on all cells
    pooled_a_all <- tryCatch(
        irr::kripp.alpha(
            rbind(encoded$claude_code, encoded$human_code),
            method = "nominal"
        )$value,
        error = function(e) NA_real_
    )

    # Identify and drop one-sided Other / Unsure pairs (both-Other kept).
    is_one_other <- xor(
        encoded$claude_answer == other_unsure_label,
        encoded$human_answer  == other_unsure_label
    )
    n_one_other <- sum(is_one_other)
    encoded_kept <- encoded[!is_one_other, , drop = FALSE]

    pooled_a_excl <- tryCatch(
        irr::kripp.alpha(
            rbind(encoded_kept$claude_code, encoded_kept$human_code),
            method = "nominal"
        )$value,
        error = function(e) NA_real_
    )

    tibble::tibble(
        n_cells                     = as.integer(n_total),
        n_one_other                 = as.integer(n_one_other),
        n_cells_excl_one_other      = as.integer(nrow(encoded_kept)),
        pooled_exact_agreement      = pooled_exact,
        mean_kappa                  = mean_k,
        mean_kappa_weighted         = mean_kw,
        mean_alpha                  = mean_alpha,
        pooled_alpha_all            = pooled_a_all,
        pooled_alpha_excl_one_other = pooled_a_excl
    )
}


# 8e. format_irr_table(): turn a per-(book,question) or overall tibble
#     into a gt object with thresholds highlighted.  `caption` is required
#     so each rendered table self-documents.  Set `group_by_book = TRUE`
#     for the per-(book,question) frame.
#
# The new diagnostic columns (`n_both_other`, `n_one_other`,
# `n_pairs_ordinal`) are HIDDEN from the rendered table by default --
# they're useful at the data layer for auditing but clutter the
# headline display.  Pass `show_diagnostics = TRUE` to keep them.
format_irr_table <- function(irr_df, caption, group_by_book = FALSE,
                             show_diagnostics = FALSE) {

    tbl <- irr_df %>%
        dplyr::mutate(
            exact_agreement = round(exact_agreement, 3),
            kappa           = round(kappa, 3),
            kappa_weighted  = round(kappa_weighted, 3),
            alpha           = round(alpha, 3)
        )

    if (!show_diagnostics) {
        tbl <- tbl %>%
            dplyr::select(-dplyr::any_of(c("n_both_other", "n_one_other",
                                           "n_pairs_ordinal")))
    }

    if (group_by_book) {
        tbl <- tbl %>% dplyr::arrange(book, q_number)
        gt_tbl <- gt::gt(tbl, groupname_col = "book")
    } else {
        tbl <- tbl %>% dplyr::arrange(q_number)
        gt_tbl <- gt::gt(tbl)
    }

    gt_tbl %>%
        gt::tab_header(title = caption) %>%
        gt::cols_label(
            q_number        = "Q",
            n_pairs         = "n",
            exact_agreement = "% agree",
            kappa           = "kappa",
            kappa_weighted  = "kappa (w)",
            alpha           = "alpha",
            scale           = "scale"
        ) %>%
        gt::data_color(
            columns = c(kappa, kappa_weighted),
            fn      = function(x) {
                ifelse(is.na(x), "#f3f4f6",
                       ifelse(x >= irr_threshold_kappa, "#bbf7d0", "#fecaca"))
            }
        ) %>%
        gt::data_color(
            columns = alpha,
            fn      = function(x) {
                ifelse(is.na(x), "#f3f4f6",
                       ifelse(x >= irr_threshold_alpha, "#bbf7d0", "#fecaca"))
            }
        ) %>%
        gt::tab_source_note(
            paste0("Green: meets threshold (kappa >= ",
                   irr_threshold_kappa, " / alpha >= ",
                   irr_threshold_alpha,
                   ").  Weighted kappa & alpha shown for ordinal Qs ",
                   "(Q1-Q8, Q10, Q12) and drop pairs where exactly one ",
                   "coder said 'Other / Unsure'; nominal alpha (Q9, Q11) ",
                   "keeps all pairs.  Both-Other matches always count.")
        )
}


# 8f. format_irr_pooled_table(): render the one-row corpus-wide pooled
#     summary from compute_irr_pooled() as a small gt table.
format_irr_pooled_table <- function(pooled_df, caption) {

    tbl <- pooled_df %>%
        dplyr::mutate(
            pooled_exact_agreement      = round(pooled_exact_agreement, 3),
            mean_kappa                  = round(mean_kappa, 3),
            mean_kappa_weighted         = round(mean_kappa_weighted, 3),
            mean_alpha                  = round(mean_alpha, 3),
            pooled_alpha_all            = round(pooled_alpha_all, 3),
            pooled_alpha_excl_one_other = round(pooled_alpha_excl_one_other, 3)
        )

    gt::gt(tbl) %>%
        gt::tab_header(title = caption) %>%
        gt::cols_label(
            n_cells                     = "n cells",
            n_one_other                 = "n one-sided Other",
            n_cells_excl_one_other      = "n cells (excl. one-sided)",
            pooled_exact_agreement      = "% agree (pooled)",
            mean_kappa                  = "mean kappa",
            mean_kappa_weighted         = "mean kappa (w)",
            mean_alpha                  = "mean alpha",
            pooled_alpha_all            = "pooled alpha (all)",
            pooled_alpha_excl_one_other = "pooled alpha (excl. one-sided Other)"
        ) %>%
        gt::data_color(
            columns = c(mean_kappa, mean_kappa_weighted),
            fn      = function(x) {
                ifelse(is.na(x), "#f3f4f6",
                       ifelse(x >= irr_threshold_kappa, "#bbf7d0", "#fecaca"))
            }
        ) %>%
        gt::data_color(
            columns = c(mean_alpha, pooled_alpha_all,
                        pooled_alpha_excl_one_other),
            fn      = function(x) {
                ifelse(is.na(x), "#f3f4f6",
                       ifelse(x >= irr_threshold_alpha, "#bbf7d0", "#fecaca"))
            }
        ) %>%
        gt::tab_source_note(
            paste0(
                "Roll-ups across all books & questions.  ",
                "pooled exact agreement = sum(matches) / n_cells.  ",
                "mean kappa / alpha = simple mean of the per-question ",
                "values.  Both pooled alphas re-encode each ",
                "(question, answer) tuple as a unique nominal code; ",
                "the 'all' version runs Krippendorff's alpha on the ",
                "whole corpus (one-sided Other/Unsure counts as ",
                "disagreement), while 'excl. one-sided Other' drops ",
                "pairs where exactly one coder said Other/Unsure ",
                "(both-Other pairs are kept and contribute zero ",
                "distance) -- matching the rule the per-question ",
                "ordinal metrics use."
            )
        )
}
