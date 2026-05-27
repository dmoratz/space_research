# =============================================================================
# source_analysis.R
# Analysis-specific helpers for Task 3 (analysis.Rmd).
# =============================================================================
# Sourced AFTER scripts/source.R by analysis.Rmd.  Provides:
#
#   1. Constants
#        DEFAULT_COLLECTION_WEIGHT_MODE
#        ORDINAL_PALETTE_5             -- 5-color shared gradient (light->dark)
#        nominal_palettes              -- per-question Q09 / Q11 palettes
#   2. Chapter -> book -> country aggregation
#        2a. split_collections()                -- expand collection rows
#        2b. aggregate_chapter_to_book()        -- mode + median + mean + peak + end
#        2c. aggregate_book_to_country()        -- distributions + country aggregates
#        2d. collapse_collections_to_books()    -- 4 collections -> 4 single rows
#                                                  via mode-of-per-story-modes
#   3. Visualization helpers (ggplot2)
#        3a. canonical_answer_order()           -- factor level order
#        3b. build_color_lookup()               -- named (answer -> hex)
#        3c. q_label_short() / q_label_long()   -- "Q01" + "Q01: short"
#        3d. plot_legend_reference()            -- top-of-doc colour key
#        3e. plot_book_fingerprint()            -- books x questions heatmap
#        3f. plot_country_distribution()        -- stacked bars by question
#        3g. plot_trajectory_per_book()         -- per-book 12-panel
#        3h. plot_trajectory_per_question()     -- per-Q 46-panel
#        3i. plot_country_divergence()          -- which countries diverge most
#
# Style: matches scripts/source.R (4-space inside multi-line calls; %>%
# pipe; snake_case).  All public objects are defined at top level so they
# can be inspected interactively after sourcing.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Constants
# -----------------------------------------------------------------------------

# Default country-level collection weighting.  Overridden in analysis.Rmd
# by setting `collection_weight_mode <- "..."` BEFORE calling
# aggregate_book_to_country().
#
# Modes:
#   "weighted" (default) -- each story in an N-story collection contributes
#                           1/N of a book's weight at country level
#   "equal"              -- each story counts as a full book
#   "merged"             -- collections stay as one book row (no split);
#                           same as not calling split_collections() at all
DEFAULT_COLLECTION_WEIGHT_MODE <- "weighted"


# Shared ordinal gradient.  Position 1 = light / safe / familiar,
# Position 5 = dark / extreme / alien.  Used uniformly across all 10
# ordinal questions thanks to the reordering encoded in
# answer_options_ordinal_lookup (Q2 / Q7 inverted, Q8 reordered).
ORDINAL_PALETTE_5 <- grDevices::hcl.colors(5, palette = "viridis")

# Color for "Other / Unsure" across the entire pipeline.
OTHER_UNSURE_COLOR <- "#9CA3AF"

# Qualitative palettes for the two nominal questions.  Each maps the
# canonical answer string (matches questions.json / ordinal lookup) to
# a fixed hex color.  Reference chart at the top of analysis.Rmd lists
# these explicitly so plots can suppress legends.
nominal_palettes <- list(

    `9` = c(
        "Adventure / exploration"       = "#3B82F6",  # blue
        "Drama"                         = "#10B981",  # green
        "Political / diplomatic"        = "#F59E0B",  # amber
        "Military / war"                = "#EF4444",  # red
        "Thriller / Horror / Survival"  = "#8B5CF6",  # purple
        "Comedy / satire"               = "#EC4899",  # pink
        "Other / Unsure"                = OTHER_UNSURE_COLOR
    ),

    `11` = c(
        "Totally unique domain"                          = "#3B82F6",
        "Like the ocean / naval"                         = "#10B981",
        "Like the air / airpower"                        = "#F59E0B",
        "Like the frontier / colonial expansion"         = "#EF4444",
        "Like cyberspace / networked or abstract domain" = "#8B5CF6",
        "Other / Unsure"                                 = OTHER_UNSURE_COLOR
    )
)


# -----------------------------------------------------------------------------
# 2. Chapter -> book -> country aggregation
# -----------------------------------------------------------------------------


# Helper: weighted_median(x, w, na.rm)
#     Base-R-only weighted median.  Returns NA when x is empty after
#     NA-removal.  Uses the "lower median" convention when cumulative
#     weight crosses 0.5 exactly between two adjacent values.
weighted_median <- function(x, w, na.rm = TRUE) {

    if (na.rm) {
        keep <- !is.na(x) & !is.na(w)
        x <- x[keep]; w <- w[keep]
    }

    if (length(x) == 0L) return(NA_real_)

    o <- order(x)
    x <- x[o]; w <- w[o]
    cw <- cumsum(w) / sum(w)
    idx <- which(cw >= 0.5)[1]
    x[idx]
}


# 2a. split_collections(claude_long, collection_meta, mode)
#     Expand chapter rows belonging to `is_collection = TRUE` books into
#     separate book rows -- each chapter becomes its own "book" with name
#     "<parent book> | <chapter label>".  Fix-up novels (is_collection =
#     FALSE) stay as single books per locked-in decision.
#
#     When `mode = "merged"`, this function is a no-op (returns the input
#     unchanged) so collections stay as one book.
#
#     Returns `claude_long` with possibly more rows; same column names
#     plus an added `parent_book` column carrying the original collection
#     title (NA for non-collection books).
split_collections <- function(claude_long, collection_meta,
                              mode = DEFAULT_COLLECTION_WEIGHT_MODE) {

    stopifnot(mode %in% c("weighted", "equal", "merged"))

    if (mode == "merged") {
        return(claude_long %>% dplyr::mutate(parent_book = NA_character_))
    }

    coll_books <- collection_meta %>%
        dplyr::filter(is_collection) %>%
        dplyr::pull(book)

    if (length(coll_books) == 0L) {
        return(claude_long %>% dplyr::mutate(parent_book = NA_character_))
    }

    not_collections <- claude_long %>%
        dplyr::filter(!book %in% coll_books) %>%
        dplyr::mutate(parent_book = NA_character_)

    collections <- claude_long %>%
        dplyr::filter(book %in% coll_books) %>%
        dplyr::mutate(
            parent_book = book,
            book        = paste0(book, " | ", chapter)
        )

    dplyr::bind_rows(not_collections, collections) %>%
        dplyr::arrange(country, parent_book, book)
}


# 2b. aggregate_chapter_to_book(claude_long, questions)
#     For each (book, question), produce a one-row summary with:
#       country, book, parent_book, question_number, question_id,
#       criteria_short, scale, n_chapters_total, n_chapters_committed,
#       all_other_unsure (boolean),
#       mode_answer, mode_position, tie_broken,
#       median_position, median_answer,
#       mean_position,
#       peak_position, peak_answer,
#       end_answer, end_position
#
#     Rules (from PROJECT_TASKS §5.1):
#       * If 100% of chapters are Other / Unsure -> mode = Other / Unsure.
#       * Otherwise, filter out Other / Unsure chapters and take the mode
#         of the remaining cells (Donald's "big reveal" rule).
#       * Tie-breaking when mode is multi-modal:
#         - Ordinal Qs: use the integer median of the tied positions
#         - Nominal Qs: pick the lower-index canonical option among tied
#       * `end_answer` is the answer at the largest `chapter_position`
#         (ignoring NA), or NA if chapter_position is missing for all rows.
aggregate_chapter_to_book <- function(claude_long, questions) {

    canonical <- purrr::map(questions, ~ unlist(.x$answer_options))
    names(canonical) <- purrr::map_int(questions, "number")

    # Attach ordinal_position if not already present.
    if (!"ordinal_position" %in% names(claude_long)) {
        claude_long <- add_ordinal_position(claude_long, questions)
    }

    claude_long %>%
        dplyr::group_by(country, book, question_number, question_id,
                        criteria_short) %>%
        dplyr::group_modify(function(g, key) {

            qn       <- key$question_number
            lvls     <- canonical[[as.character(qn)]]
            is_ord   <- qn %in% ordinal_question_numbers
            scale    <- if (is_ord) "ordinal" else "nominal"
            n_total  <- nrow(g)
            n_other  <- sum(g$answer == "Other / Unsure", na.rm = TRUE)
            n_commit <- n_total - n_other
            all_other <- n_other == n_total

            # Pull parent_book consistently (collections all share one
            # parent_book; non-collections have NA).
            parent_b <- unique(g$parent_book)
            parent_b <- if (length(parent_b) == 1L) parent_b
                        else NA_character_

            # Compute mode_answer with the Other/Unsure rule + tie-break.
            mode_info <- compute_mode_with_tiebreak(
                answers          = g$answer,
                ordinal_pos      = g$ordinal_position,
                canonical_levels = lvls,
                is_ord           = is_ord,
                all_other        = all_other
            )

            # Median / mean / peak / end (ordinal only; nominal -> NA).
            ord_committed <- g$ordinal_position[!is.na(g$ordinal_position)]

            median_pos <- if (length(ord_committed) > 0L && is_ord) {
                as.integer(stats::median(ord_committed))
            } else NA_integer_

            mean_pos <- if (length(ord_committed) > 0L && is_ord) {
                mean(ord_committed)
            } else NA_real_

            peak_pos <- if (length(ord_committed) > 0L && is_ord) {
                as.integer(max(ord_committed))
            } else NA_integer_

            median_ans <- ordinal_position_to_answer(median_pos, qn,
                                                     lvls, is_ord)
            peak_ans   <- ordinal_position_to_answer(peak_pos, qn,
                                                     lvls, is_ord)

            # End-of-book answer: use largest chapter_position (NA-safe).
            end_info <- compute_end_answer(g)

            tibble::tibble(
                parent_book          = parent_b,
                scale                = scale,
                n_chapters_total     = as.integer(n_total),
                n_chapters_committed = as.integer(n_commit),
                all_other_unsure     = all_other,
                mode_answer          = mode_info$answer,
                mode_position        = mode_info$position,
                tie_broken           = mode_info$tie_broken,
                median_position      = median_pos,
                median_answer        = median_ans,
                mean_position        = mean_pos,
                peak_position        = peak_pos,
                peak_answer          = peak_ans,
                end_answer           = end_info$answer,
                end_position         = end_info$position
            )
        }) %>%
        dplyr::ungroup()
}


# Helper: compute_mode_with_tiebreak()
#     Implements the locked-in book-level mode rule, including the
#     "100% Other / Unsure -> Other / Unsure" override and the
#     median-of-tied-positions (ordinal) / lower-index (nominal)
#     tie-breaker.  Returns a list(answer, position, tie_broken).
compute_mode_with_tiebreak <- function(answers, ordinal_pos,
                                       canonical_levels, is_ord,
                                       all_other) {

    if (all_other) {
        # 100% Other / Unsure -> book is Other / Unsure.
        pos <- match("Other / Unsure", canonical_levels)
        return(list(answer = "Other / Unsure",
                    position = if (is_ord) NA_integer_ else as.integer(pos),
                    tie_broken = FALSE))
    }

    # Drop Other / Unsure cells (Donald's "any non-Other chapter wins")
    keep <- answers != "Other / Unsure" & !is.na(answers)
    a_keep <- answers[keep]

    if (length(a_keep) == 0L) {
        # Shouldn't reach here because all_other is FALSE, but guard anyway.
        return(list(answer = NA_character_,
                    position = NA_integer_,
                    tie_broken = FALSE))
    }

    # Frequency table over the surviving chapter answers.
    tab <- sort(table(a_keep), decreasing = TRUE)
    top_count <- as.integer(tab[1])
    tied      <- names(tab)[tab == top_count]

    if (length(tied) == 1L) {
        ans <- tied
        pos <- match(ans, canonical_levels)
        return(list(answer = ans,
                    position = if (is_ord) as.integer(pos) else NA_integer_,
                    tie_broken = FALSE))
    }

    # Multi-modal -- apply the tie-breaking rule.
    if (is_ord) {
        # Median of the tied positions.  ordinal_pos is NA for
        # Other/Unsure, so we look up positions from canonical_levels.
        tied_positions <- match(tied, canonical_levels)
        med <- as.integer(stats::median(tied_positions))
        ans <- canonical_levels[med]
        return(list(answer = ans,
                    position = as.integer(med),
                    tie_broken = TRUE))
    }

    # Nominal: pick the lower-index canonical option among tied.
    tied_positions <- match(tied, canonical_levels)
    winner_idx     <- min(tied_positions)
    ans            <- canonical_levels[winner_idx]
    list(answer = ans,
         position = NA_integer_,
         tie_broken = TRUE)
}


# Helper: ordinal_position_to_answer()
#     Convert an integer position back to its canonical answer string.
#     Returns NA when position is NA or the question is nominal.
ordinal_position_to_answer <- function(pos, qn, canonical_levels, is_ord) {
    if (!is_ord || is.na(pos)) return(NA_character_)
    if (pos < 1L || pos > length(canonical_levels)) return(NA_character_)
    canonical_levels[pos]
}


# Helper: compute_end_answer()
#     Pick the chapter with the largest non-NA chapter_position; ties
#     resolved by stable order in the input.  Returns list(answer,
#     position) where position is the ordinal_position of that final
#     answer (NA for nominal Qs / Other / Unsure).
compute_end_answer <- function(g) {

    valid <- !is.na(g$chapter_position)
    if (!any(valid)) {
        return(list(answer = NA_character_,
                    position = NA_integer_))
    }

    last_idx <- which(valid)[which.max(g$chapter_position[valid])]
    list(
        answer   = g$answer[last_idx],
        position = if (is.na(g$ordinal_position[last_idx])) NA_integer_
                   else as.integer(g$ordinal_position[last_idx])
    )
}


# 2c. aggregate_book_to_country(book_level, collection_meta, weight_mode)
#     Produce country-level summaries from book-level codings.  Returns a
#     list with two tibbles:
#
#       $distributions -- one row per (country, question, answer);
#                         columns: weight_sum (sum of book weights coded
#                         as this answer), book_count_unweighted,
#                         proportion (weight_sum / total country weight
#                         for this question).
#       $aggregates    -- one row per (country, question); columns:
#                         total_weight, n_books, n_books_committed,
#                         mode_answer (weighted mode), median_position,
#                         mean_position (weighted), peak_position
#                         (weighted, ordinal only), end_position
#                         (weighted).
#
#     Weighting rules per `weight_mode`:
#       * "weighted" -- each story in an N-story collection contributes
#                       1/N of a unit weight.  Non-collection books = 1.
#       * "equal"    -- every book / story row gets weight = 1.
#       * "merged"   -- same as "equal" but assumes book_level already has
#                       collections un-split (call split_collections(...,
#                       mode = "merged") before aggregate_chapter_to_book).
aggregate_book_to_country <- function(book_level, collection_meta,
                                      weight_mode = DEFAULT_COLLECTION_WEIGHT_MODE) {

    stopifnot(weight_mode %in% c("weighted", "equal", "merged"))

    # Compute per-book weights based on parent_book and weight_mode.
    weights <- if (weight_mode == "weighted") {
        # Each story in a split collection counts as 1/N of a book.
        book_level %>%
            dplyr::distinct(country, book, parent_book) %>%
            dplyr::group_by(parent_book) %>%
            dplyr::mutate(
                weight = dplyr::if_else(
                    is.na(parent_book),
                    1,
                    1 / dplyr::n()
                )
            ) %>%
            dplyr::ungroup()
    } else {
        book_level %>%
            dplyr::distinct(country, book, parent_book) %>%
            dplyr::mutate(weight = 1)
    }

    bw <- book_level %>%
        dplyr::left_join(weights,
                         by = c("country", "book", "parent_book"))

    # Distributions over mode_answer (and parallel for peak_answer).
    dist_mode <- bw %>%
        dplyr::group_by(country, question_number, question_id,
                        criteria_short, scale) %>%
        dplyr::group_modify(function(g, key) {
            total_w <- sum(g$weight, na.rm = TRUE)
            g %>%
                dplyr::group_by(answer = mode_answer) %>%
                dplyr::summarise(
                    weight_sum            = sum(weight, na.rm = TRUE),
                    book_count_unweighted = dplyr::n(),
                    .groups = "drop"
                ) %>%
                dplyr::mutate(
                    proportion = weight_sum / total_w,
                    aggregation = "mode"
                )
        }) %>%
        dplyr::ungroup()

    dist_peak <- bw %>%
        dplyr::filter(scale == "ordinal", !is.na(peak_answer)) %>%
        dplyr::group_by(country, question_number, question_id,
                        criteria_short, scale) %>%
        dplyr::group_modify(function(g, key) {
            total_w <- sum(g$weight, na.rm = TRUE)
            g %>%
                dplyr::group_by(answer = peak_answer) %>%
                dplyr::summarise(
                    weight_sum            = sum(weight, na.rm = TRUE),
                    book_count_unweighted = dplyr::n(),
                    .groups = "drop"
                ) %>%
                dplyr::mutate(
                    proportion = weight_sum / total_w,
                    aggregation = "peak"
                )
        }) %>%
        dplyr::ungroup()

    distributions <- dplyr::bind_rows(dist_mode, dist_peak)

    # Country-level aggregates: weighted mean/median/peak/end positions.
    aggregates <- bw %>%
        dplyr::group_by(country, question_number, question_id,
                        criteria_short, scale) %>%
        dplyr::summarise(
            total_weight       = sum(weight, na.rm = TRUE),
            n_books            = dplyr::n(),
            n_books_committed  = sum(!is.na(mode_position),
                                     na.rm = TRUE),
            mean_position      = stats::weighted.mean(mode_position,
                                                      weight,
                                                      na.rm = TRUE),
            median_position    = weighted_median(mode_position, weight,
                                                 na.rm = TRUE),
            mean_peak_position = stats::weighted.mean(peak_position,
                                                      weight,
                                                      na.rm = TRUE),
            mean_end_position  = stats::weighted.mean(end_position,
                                                      weight,
                                                      na.rm = TRUE),
            .groups = "drop"
        )

    list(distributions = distributions, aggregates = aggregates)
}


# 2d. collapse_collections_to_books(book_level_split, questions)
#     Take a book-level frame produced by aggregate_chapter_to_book() on
#     the SPLIT claude_long, and collapse collection rows back to one
#     row per parent_book using "mode of per-story modes" -- the same
#     majoritarian rule + tie-breaking we used at chapter -> book, but
#     applied across the stories of each collection.
#
#     For non-collection books (parent_book = NA), the input row is
#     passed through unchanged.  For collection books, the columns are
#     aggregated as follows:
#
#       mode_answer           -- mode of the stories' mode_answer
#       peak_position         -- MAX of the stories' peak_position
#                                (matches the original "peak of book"
#                                semantics: any story can pull peak up)
#       peak_answer           -- canonical level for that position
#       median_position       -- median of the stories' median_position
#       mean_position         -- mean of the stories' mean_position
#       end_answer            -- last story's end_answer (last by name)
#       end_position          -- ordinal position of end_answer
#       n_chapters_total      -- SUM across stories
#       n_chapters_committed  -- SUM across stories
#       all_other_unsure      -- TRUE only if EVERY story was all-Other
#       tie_broken            -- TRUE if either story-level rows
#                                required tie-breaking OR the collapse
#                                step did
#       parent_book           -- set to NA after collapse (the row IS
#                                the parent)
#
# Used for the headline book fingerprint heatmap.  Country aggregation
# still uses the split book_level so the weighting parameter works.
collapse_collections_to_books <- function(book_level_split, questions) {

    # Books that are NOT collections: pass through unchanged.
    pass_through <- book_level_split %>%
        dplyr::filter(is.na(parent_book))

    # Books that ARE collections (parent_book is set): collapse.
    coll <- book_level_split %>%
        dplyr::filter(!is.na(parent_book))

    if (nrow(coll) == 0L) {
        return(pass_through)
    }

    collapsed <- coll %>%
        dplyr::group_by(country, parent_book, question_number,
                        question_id, criteria_short, scale) %>%
        dplyr::group_modify(function(g, key) {

            qn       <- key$question_number
            lvls     <- get_factor_levels(qn, questions)
            is_ord   <- qn %in% ordinal_question_numbers

            all_other <- all(g$mode_answer == "Other / Unsure",
                             na.rm = TRUE)

            mode_info <- compute_mode_with_tiebreak(
                answers          = g$mode_answer,
                ordinal_pos      = g$mode_position,
                canonical_levels = lvls,
                is_ord           = is_ord,
                all_other        = all_other
            )

            peak_pos <- if (is_ord) {
                v <- g$peak_position[!is.na(g$peak_position)]
                if (length(v) > 0L) as.integer(max(v)) else NA_integer_
            } else NA_integer_

            peak_ans <- if (is_ord && !is.na(peak_pos) &&
                            peak_pos >= 1L && peak_pos <= length(lvls)) {
                lvls[peak_pos]
            } else NA_character_

            median_pos <- if (is_ord) {
                v <- g$median_position[!is.na(g$median_position)]
                if (length(v) > 0L) as.integer(stats::median(v))
                else NA_integer_
            } else NA_integer_

            median_ans <- if (is_ord && !is.na(median_pos) &&
                              median_pos >= 1L &&
                              median_pos <= length(lvls)) {
                lvls[median_pos]
            } else NA_character_

            mean_pos <- if (is_ord) {
                mean(g$mean_position, na.rm = TRUE)
            } else NA_real_

            # End-of-collection: last story alphabetically (the only
            # stable proxy we have for "collection ordering" since
            # individual story-books have chapter_position = 1).
            ordered <- g %>% dplyr::arrange(book)
            end_ans <- ordered$end_answer[nrow(ordered)]
            end_pos <- ordered$end_position[nrow(ordered)]

            # Return everything EXCEPT the grouping columns (those come
            # back from `key` automatically).  Crucially we don't include
            # parent_book or book here -- those get derived after the
            # group_modify call.
            tibble::tibble(
                n_chapters_total      = sum(g$n_chapters_total),
                n_chapters_committed  = sum(g$n_chapters_committed),
                all_other_unsure      = all(g$all_other_unsure),
                mode_answer           = mode_info$answer,
                mode_position         = mode_info$position,
                tie_broken            = any(g$tie_broken) ||
                                            mode_info$tie_broken,
                median_position       = median_pos,
                median_answer         = median_ans,
                mean_position         = mean_pos,
                peak_position         = peak_pos,
                peak_answer           = peak_ans,
                end_answer            = end_ans,
                end_position          = end_pos
            )
        }) %>%
        dplyr::ungroup() %>%
        # The collapsed rows ARE the parent book; promote parent_book
        # to book and clear parent_book so the result matches
        # pass_through's schema.
        dplyr::mutate(
            book        = parent_book,
            parent_book = NA_character_
        ) %>%
        dplyr::select(dplyr::all_of(names(pass_through)))

    dplyr::bind_rows(pass_through, collapsed) %>%
        dplyr::arrange(country, book, question_number)
}


# -----------------------------------------------------------------------------
# 3. Visualization helpers
# -----------------------------------------------------------------------------


# 3a. canonical_answer_order(questions)
#     Returns a unique vector of all canonical answer strings across all
#     questions, in display order: ordinal Qs use answer_options_ordinal_lookup
#     order (1..5 then NA last); nominal Qs use questions.json answer_options
#     order.  Used to lock factor levels in heatmaps and bar charts.
canonical_answer_order <- function(questions) {

    out <- character(0)
    qns <- sort(c(ordinal_question_numbers, nominal_question_numbers))

    for (qn in qns) {
        lvls <- get_factor_levels(qn, questions)
        for (a in lvls) {
            if (!a %in% out) out <- c(out, a)
        }
    }

    out
}


# 3b. build_color_lookup()
#     Build the single named character vector (answer -> hex color) used
#     across the whole document.  Ordinal answers share the 5-color
#     ORDINAL_PALETTE_5 keyed by ordinal_position; nominal answers use
#     the per-question palettes in `nominal_palettes`; "Other / Unsure"
#     is always grey.  Answer strings are unique across questions
#     (verified) except for "Other / Unsure", so the named vector has
#     no name collisions that would cause scale_fill_manual to silently
#     mis-map.
build_color_lookup <- function() {

    out <- character(0)

    for (qn in ordinal_question_numbers) {
        ql <- answer_options_ordinal_lookup %>%
            dplyr::filter(question_number == qn)
        for (i in seq_len(nrow(ql))) {
            ans <- ql$answer[i]
            pos <- ql$ordinal_position[i]
            out[ans] <- if (is.na(pos)) OTHER_UNSURE_COLOR
                        else ORDINAL_PALETTE_5[pos]
        }
    }

    for (qn in nominal_question_numbers) {
        pal <- nominal_palettes[[as.character(qn)]]
        for (i in seq_along(pal)) {
            out[names(pal)[i]] <- unname(pal[i])
        }
    }

    out
}


# 3c. q_label_short(n) / q_label_long(n, questions)
#     Build zero-padded question labels for display.  "Q01" ... "Q12"
#     for the short form; "Q01: <criteria_short>" for the long form.
q_label_short <- function(n) {
    sprintf("Q%02d", as.integer(n))
}

q_label_long <- function(n, questions) {
    q <- purrr::detect(questions,
                       ~ identical(as.integer(.x$number), as.integer(n)))
    if (is.null(q)) return(q_label_short(n))
    sprintf("Q%02d: %s", as.integer(n), q$criteria_short)
}


# 3d. plot_legend_reference(questions)
#     Top-of-document color key.  Produces a patchwork composition with
#     three panels: (i) the shared ordinal gradient labeled "safe ->
#     extreme" plus a small per-question endpoint table; (ii) the Q9
#     genre palette; (iii) the Q11 metaphor palette.  Designed to be
#     rendered ONCE at the top of the Visualizations section so all
#     subsequent plots can suppress their legends.
plot_legend_reference <- function(questions) {

    # (i) Shared ordinal gradient strip + per-Q endpoint table.
    gradient_df <- tibble::tibble(
        ordinal_position = 1:5,
        color            = ORDINAL_PALETTE_5,
        label            = c("safe /\nfamiliar", "", "", "",
                             "extreme /\nalien / chaotic")
    )

    p_gradient <- ggplot2::ggplot(
            gradient_df,
            ggplot2::aes(x = ordinal_position, y = 1, fill = color)
        ) +
        ggplot2::geom_tile(color = "white", linewidth = 1) +
        ggplot2::geom_text(ggplot2::aes(label = label),
                           vjust = -1.2, size = 3.4, lineheight = 0.85) +
        ggplot2::geom_text(ggplot2::aes(label = ordinal_position),
                           color = "white", size = 4, fontface = "bold") +
        ggplot2::scale_fill_identity() +
        ggplot2::scale_x_continuous(breaks = 1:5,
                                     expand = ggplot2::expansion(add = 0.5)) +
        ggplot2::scale_y_continuous(limits = c(0.4, 1.8)) +
        ggplot2::labs(
            title    = "Shared ordinal scale (Q01-Q08, Q10, Q12)",
            subtitle = "Same 5-color gradient is reused for all ordinal questions; lower position = safer / more familiar"
        ) +
        ggplot2::theme_void() +
        ggplot2::theme(
            plot.title    = ggplot2::element_text(size = 11,
                                                   face = "bold"),
            plot.subtitle = ggplot2::element_text(size = 9,
                                                   color = "#4B5563"),
            plot.margin   = ggplot2::margin(8, 8, 8, 8)
        )

    # (i-b) Endpoint table: question -> "pos 1 ... pos 5" pair.
    endpoint_rows <- lapply(ordinal_question_numbers, function(qn) {
        ql <- answer_options_ordinal_lookup %>%
            dplyr::filter(question_number == qn,
                          !is.na(ordinal_position)) %>%
            dplyr::arrange(ordinal_position)
        if (nrow(ql) < 2L) return(NULL)
        tibble::tibble(
            q_label = q_label_short(qn),
            pos_1   = ql$answer[1],
            pos_5   = ql$answer[nrow(ql)]
        )
    })
    endpoint_df <- dplyr::bind_rows(endpoint_rows) %>%
        dplyr::mutate(
            pos_1 = stringr::str_trunc(pos_1, 40),
            pos_5 = stringr::str_trunc(pos_5, 40)
        )

    p_endpoints <- ggplot2::ggplot(endpoint_df) +
        ggplot2::geom_text(ggplot2::aes(x = 0, y = q_label,
                                        label = paste0(q_label, "  ",
                                                       pos_1)),
                           hjust = 0, size = 3.1,
                           color = ORDINAL_PALETTE_5[1]) +
        ggplot2::geom_text(ggplot2::aes(x = 0.6, y = q_label,
                                        label = paste0("→  ",
                                                       pos_5)),
                           hjust = 0, size = 3.1,
                           color = ORDINAL_PALETTE_5[5]) +
        ggplot2::scale_x_continuous(limits = c(0, 1.4)) +
        ggplot2::scale_y_discrete(limits = rev(endpoint_df$q_label)) +
        ggplot2::labs(
            title    = "Per-question endpoints",
            subtitle = "Position 1 → Position 5"
        ) +
        ggplot2::theme_void() +
        ggplot2::theme(
            plot.title    = ggplot2::element_text(size = 11,
                                                   face = "bold"),
            plot.subtitle = ggplot2::element_text(size = 9,
                                                   color = "#4B5563"),
            plot.margin   = ggplot2::margin(8, 8, 8, 8)
        )

    # (ii) Q9 nominal palette.
    q9_df <- tibble::tibble(
        answer = names(nominal_palettes$`9`),
        color  = unname(nominal_palettes$`9`)
    )
    p_q9 <- ggplot2::ggplot(q9_df,
            ggplot2::aes(x = 1, y = answer, fill = color)) +
        ggplot2::geom_tile(color = "white", linewidth = 1) +
        ggplot2::geom_text(ggplot2::aes(x = 1.6, label = answer),
                           hjust = 0, size = 3.2) +
        ggplot2::scale_fill_identity() +
        ggplot2::scale_x_continuous(limits = c(0.5, 6)) +
        ggplot2::scale_y_discrete(limits = rev(q9_df$answer)) +
        ggplot2::labs(
            title    = "Q09: genre of the book (nominal)",
            subtitle = "Each color = one genre category"
        ) +
        ggplot2::theme_void() +
        ggplot2::theme(
            plot.title    = ggplot2::element_text(size = 11,
                                                   face = "bold"),
            plot.subtitle = ggplot2::element_text(size = 9,
                                                   color = "#4B5563"),
            plot.margin   = ggplot2::margin(8, 8, 8, 8)
        )

    # (iii) Q11 nominal palette.
    q11_df <- tibble::tibble(
        answer = names(nominal_palettes$`11`),
        color  = unname(nominal_palettes$`11`)
    )
    p_q11 <- ggplot2::ggplot(q11_df,
            ggplot2::aes(x = 1, y = answer, fill = color)) +
        ggplot2::geom_tile(color = "white", linewidth = 1) +
        ggplot2::geom_text(ggplot2::aes(x = 1.6, label = answer),
                           hjust = 0, size = 3.2) +
        ggplot2::scale_fill_identity() +
        ggplot2::scale_x_continuous(limits = c(0.5, 6)) +
        ggplot2::scale_y_discrete(limits = rev(q11_df$answer)) +
        ggplot2::labs(
            title    = "Q11: nearest-neighbor metaphor (nominal)",
            subtitle = "Each color = one metaphorical framing"
        ) +
        ggplot2::theme_void() +
        ggplot2::theme(
            plot.title    = ggplot2::element_text(size = 11,
                                                   face = "bold"),
            plot.subtitle = ggplot2::element_text(size = 9,
                                                   color = "#4B5563"),
            plot.margin   = ggplot2::margin(8, 8, 8, 8)
        )

    # Compose: top half = shared gradient + endpoints (side by side);
    # bottom half = Q9 + Q11 nominal palettes side by side.
    top    <- patchwork::wrap_plots(p_gradient, p_endpoints,
                                     ncol = 2,
                                     widths = c(1, 1.4))
    bottom <- patchwork::wrap_plots(p_q9, p_q11, ncol = 2)

    patchwork::wrap_plots(top, bottom, ncol = 1, heights = c(1, 1.1))
}


# 3e. plot_book_fingerprint(book_level, questions, use_field)
#     Heatmap with books on y, zero-padded Q01..Q12 on x, fill = answer.
#     Uses the shared color lookup (suppressing the in-plot legend; the
#     top-of-doc reference chart explains the colors).
plot_book_fingerprint <- function(book_level, questions,
                                  use_field = "mode_answer") {

    stopifnot(use_field %in% c("mode_answer", "peak_answer",
                               "median_answer", "end_answer"))

    color_lookup <- build_color_lookup()
    canonical    <- canonical_answer_order(questions)

    df <- book_level %>%
        dplyr::mutate(answer = .data[[use_field]]) %>%
        dplyr::mutate(
            answer  = factor(answer, levels = canonical),
            q_label = factor(q_label_short(question_number),
                             levels = q_label_short(
                                 sort(unique(question_number))))
        )

    # y-axis: country-then-book order, with country group separators
    # via facet_grid.
    book_order <- book_level %>%
        dplyr::distinct(country, book) %>%
        dplyr::arrange(country, book) %>%
        dplyr::pull(book)
    df$book <- factor(df$book, levels = rev(book_order))

    ggplot2::ggplot(df,
        ggplot2::aes(x = q_label, y = book, fill = answer)) +
        ggplot2::geom_tile(color = "white", linewidth = 0.2) +
        ggplot2::scale_fill_manual(values = color_lookup,
                                   na.value = "#E5E7EB",
                                   guide = "none") +
        ggplot2::facet_grid(country ~ ., scales = "free_y",
                            space = "free_y", switch = "y") +
        ggplot2::labs(
            title    = paste0("Book fingerprints (", use_field, ")"),
            subtitle = "See reference chart at top of document for color key.",
            x = NULL, y = NULL
        ) +
        ggplot2::theme_minimal() +
        ggplot2::theme(
            strip.placement   = "outside",
            strip.text.y.left = ggplot2::element_text(angle = 0,
                                                      hjust = 1),
            panel.grid        = ggplot2::element_blank(),
            axis.text.y       = ggplot2::element_text(size = 7)
        )
}


# 3f. plot_country_distribution(country_distributions, questions, use_field)
#     Stacked bars faceted by zero-padded Q-label.  Suppresses the bar
#     fill legend (reference chart at top explains colors).
plot_country_distribution <- function(country_distributions, questions,
                                      use_field = "mode") {

    stopifnot(use_field %in% c("mode", "peak"))

    color_lookup <- build_color_lookup()
    canonical    <- canonical_answer_order(questions)

    df <- country_distributions %>%
        dplyr::filter(aggregation == use_field) %>%
        dplyr::mutate(
            answer  = factor(answer, levels = canonical),
            q_label = factor(
                          q_label_long(question_number, questions),
                          levels = vapply(
                              sort(unique(question_number)),
                              function(n) q_label_long(n, questions),
                              character(1)
                          )
                      )
        )

    ggplot2::ggplot(df,
        ggplot2::aes(x = country, y = proportion, fill = answer)) +
        ggplot2::geom_col(position = "stack", color = "white",
                          linewidth = 0.1) +
        ggplot2::scale_fill_manual(values = color_lookup,
                                   na.value = "#E5E7EB",
                                   guide = "none") +
        ggplot2::scale_y_continuous(labels = scales::percent_format()) +
        ggplot2::facet_wrap(~ q_label, ncol = 3, scales = "free_y") +
        ggplot2::labs(
            title    = paste0("Country distributions (", use_field, ")"),
            subtitle = "See reference chart at top of document for color key.",
            x = NULL,
            y = "Share of books"
        ) +
        ggplot2::theme_minimal() +
        ggplot2::theme(
            strip.text = ggplot2::element_text(size = 8),
            axis.text.x = ggplot2::element_text(angle = 30, hjust = 1)
        )
}


# 3g. plot_trajectory_per_book(claude_long, book_name, questions)
#     One figure for a single book: ordinal Qs in a 12-panel small-
#     multiples grid (y = ordinal_position 1..5), nominal Qs below as
#     a categorical strip.
plot_trajectory_per_book <- function(claude_long, book_name, questions) {

    df <- claude_long %>%
        dplyr::filter(book == book_name) %>%
        dplyr::mutate(
            q_label = sprintf("Q%02d: %s", question_number,
                              stringr::str_trunc(criteria_short, 40)),
            scale   = dplyr::if_else(question_number %in%
                                          ordinal_question_numbers,
                                      "ordinal", "nominal")
        )

    if (nrow(df) == 0L) {
        return(ggplot2::ggplot() +
                   ggplot2::labs(title = paste0("No data for book: ",
                                                book_name)))
    }

    df_ord <- df %>% dplyr::filter(scale == "ordinal")
    df_nom <- df %>% dplyr::filter(scale == "nominal")

    p_ord <- ggplot2::ggplot(df_ord,
        ggplot2::aes(x = chapter_position, y = ordinal_position)) +
        ggplot2::geom_step(direction = "mid", color = "#2563EB",
                           na.rm = TRUE) +
        ggplot2::geom_point(ggplot2::aes(color = is.na(ordinal_position)),
                            na.rm = TRUE, size = 1.4) +
        ggplot2::scale_color_manual(values = c("FALSE" = "#1E3A8A",
                                                "TRUE"  = OTHER_UNSURE_COLOR),
                                    guide = "none") +
        ggplot2::scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
        ggplot2::facet_wrap(~ q_label, ncol = 3) +
        ggplot2::labs(
            title    = paste0("Trajectories: ", book_name,
                              " (ordinal questions)"),
            subtitle = "Ordinal position 1-5; grey points are 'Other / Unsure' (NA)",
            x = "Chapter position", y = "Ordinal position"
        ) +
        ggplot2::theme_minimal() +
        ggplot2::theme(strip.text = ggplot2::element_text(size = 8))

    if (nrow(df_nom) > 0L) {
        p_nom <- ggplot2::ggplot(df_nom,
            ggplot2::aes(x = chapter_position, y = answer)) +
            ggplot2::geom_point(color = "#DC2626", size = 1.4) +
            ggplot2::facet_wrap(~ q_label, ncol = 2) +
            ggplot2::labs(
                title = paste0("Trajectories: ", book_name,
                               " (nominal questions)"),
                x = "Chapter position", y = "Answer"
            ) +
            ggplot2::theme_minimal() +
            ggplot2::theme(
                strip.text  = ggplot2::element_text(size = 8),
                axis.text.y = ggplot2::element_text(size = 7)
            )

        return(patchwork::wrap_plots(p_ord, p_nom, ncol = 1,
                                     heights = c(3, 1)))
    }

    p_ord
}


# 3h. plot_trajectory_per_question(claude_long, qn, questions)
#     One figure per question, small panel per book.
plot_trajectory_per_question <- function(claude_long, qn, questions) {

    df <- claude_long %>%
        dplyr::filter(question_number == qn) %>%
        dplyr::arrange(country, book, chapter_position)

    is_ord <- qn %in% ordinal_question_numbers

    q_meta <- purrr::detect(questions,
                            ~ identical(.x$number, as.integer(qn)))
    qshort <- if (!is.null(q_meta)) q_meta$criteria_short else ""

    title_text <- sprintf("Q%02d (%s): chapter trajectories by book",
                          qn, qshort)

    if (is_ord) {
        ggplot2::ggplot(df,
            ggplot2::aes(x = chapter_position, y = ordinal_position)) +
            ggplot2::geom_step(direction = "mid", color = "#2563EB",
                               na.rm = TRUE) +
            ggplot2::geom_point(na.rm = TRUE, size = 0.9,
                                color = "#1E3A8A") +
            ggplot2::scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
            ggplot2::facet_wrap(~ paste0(country, ": ",
                                          stringr::str_trunc(book, 35)),
                                ncol = 5, scales = "free_x") +
            ggplot2::labs(
                title = title_text,
                x = "Chapter position", y = "Ordinal position"
            ) +
            ggplot2::theme_minimal() +
            ggplot2::theme(strip.text = ggplot2::element_text(size = 7))
    } else {
        ggplot2::ggplot(df,
            ggplot2::aes(x = chapter_position, y = answer)) +
            ggplot2::geom_point(color = "#DC2626", size = 0.9) +
            ggplot2::facet_wrap(~ paste0(country, ": ",
                                          stringr::str_trunc(book, 35)),
                                ncol = 5, scales = "free_x") +
            ggplot2::labs(
                title = title_text,
                x = "Chapter position", y = "Answer"
            ) +
            ggplot2::theme_minimal() +
            ggplot2::theme(
                strip.text  = ggplot2::element_text(size = 7),
                axis.text.y = ggplot2::element_text(size = 7)
            )
    }
}


# 3i. plot_country_divergence(country_aggregates, questions, use_field)
#     Heatmap: countries x questions, fill = country position - corpus
#     mean position.  Ordinal Qs only.  Title and legend labels are
#     human-readable (e.g., "Mean" rather than the raw column name).
plot_country_divergence <- function(country_aggregates, questions,
                                    use_field = "mean_position") {

    stopifnot(use_field %in% c("mean_position", "mean_peak_position",
                                "median_position", "mean_end_position"))

    field_label <- switch(use_field,
        "mean_position"      = "Mean",
        "mean_peak_position" = "Mean (peak)",
        "median_position"    = "Median",
        "mean_end_position"  = "Mean (end-of-book)"
    )

    ord_qs <- country_aggregates %>%
        dplyr::filter(scale == "ordinal") %>%
        dplyr::mutate(value = .data[[use_field]]) %>%
        dplyr::filter(!is.na(value))

    if (nrow(ord_qs) == 0L) {
        return(ggplot2::ggplot() +
                   ggplot2::labs(
                       title = "No ordinal data for divergence plot"
                   ))
    }

    corpus_mean <- ord_qs %>%
        dplyr::group_by(question_number) %>%
        dplyr::summarise(corpus_mean = mean(value, na.rm = TRUE),
                         .groups = "drop")

    df <- ord_qs %>%
        dplyr::left_join(corpus_mean, by = "question_number") %>%
        dplyr::mutate(
            divergence = value - corpus_mean,
            q_label    = factor(q_label_short(question_number),
                                levels = q_label_short(
                                    sort(unique(question_number))))
        )

    ggplot2::ggplot(df,
        ggplot2::aes(x = q_label, y = country, fill = divergence)) +
        ggplot2::geom_tile(color = "white", linewidth = 0.3) +
        ggplot2::geom_text(ggplot2::aes(label = sprintf("%+.1f",
                                                        divergence)),
                           size = 3, color = "black") +
        ggplot2::scale_fill_gradient2(
            low      = "#2563EB",
            mid      = "#F9FAFB",
            high     = "#DC2626",
            midpoint = 0,
            name     = paste0(field_label,
                              "\n(vs corpus avg)")
        ) +
        ggplot2::labs(
            title    = paste0("Country divergence from corpus average (",
                              field_label, ")"),
            subtitle = "Cells show country position minus corpus mean position; ordinal Qs only.",
            x = NULL, y = NULL
        ) +
        ggplot2::theme_minimal() +
        ggplot2::theme(panel.grid = ggplot2::element_blank())
}
