# =============================================================================
# source_analysis.R
# Analysis-specific helpers for Task 3 (analysis.Rmd).
# =============================================================================
# Sourced AFTER scripts/source.R by analysis.Rmd.  Provides:
#
#   1. Constants
#        DEFAULT_COLLECTION_WEIGHT_MODE
#   2. Chapter -> book -> country aggregation
#        2a. split_collections()           -- expand collection rows
#        2b. aggregate_chapter_to_book()   -- mode + median + mean + peak + end
#        2c. aggregate_book_to_country()   -- distributions + country aggregates
#   3. Visualization helpers (ggplot2)
#        3a. answer_palette()              -- named color vector per question
#        3b. plot_book_fingerprint()       -- books x questions heatmap
#        3c. plot_country_distribution()   -- stacked bars faceted by question
#        3d. plot_trajectory_per_book()    -- per-book 12-panel small-multiples
#        3e. plot_trajectory_per_question()-- per-Q 46-panel small-multiples
#        3f. plot_country_divergence()     -- which countries diverge most
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


# -----------------------------------------------------------------------------
# 3. Visualization helpers
# -----------------------------------------------------------------------------


# 3a. answer_palette(qn, questions)
#     Build a named color vector for the canonical answer_options of one
#     question.  Ordinal Qs get a viridis-style gradient; nominal Qs get
#     a qualitative palette.  "Other / Unsure" is always grey.
answer_palette <- function(qn, questions) {

    q <- questions[[qn]]
    if (is.null(q$number) || q$number != qn) {
        # questions may be indexed by 1..length(questions), not by Q number.
        match_idx <- purrr::detect_index(questions,
                                          ~ identical(.x$number, qn))
        if (match_idx > 0L) q <- questions[[match_idx]]
    }

    opts <- unlist(q$answer_options)
    substantive <- setdiff(opts, "Other / Unsure")
    n <- length(substantive)

    if (qn %in% ordinal_question_numbers) {
        # Base-R viridis avoids pulling in viridisLite as a dependency.
        cols <- grDevices::hcl.colors(n, palette = "viridis")
    } else {
        cols <- scales::hue_pal()(n)
    }

    full <- c(stats::setNames(cols, substantive),
              "Other / Unsure" = "#9CA3AF")

    full[opts]   # preserve canonical order
}


# 3b. plot_book_fingerprint(book_level, questions, use_field)
#     Heatmap with books on y, questions on x, fill = answer.  `use_field`
#     selects which book-level coding to display: "mode_answer" (default)
#     or "peak_answer".  Short labels from answer_options_short_lookup
#     are used in the legend.
plot_book_fingerprint <- function(book_level, questions,
                                  use_field = "mode_answer") {

    stopifnot(use_field %in% c("mode_answer", "peak_answer",
                               "median_answer", "end_answer"))

    df <- book_level %>%
        dplyr::mutate(
            answer = .data[[use_field]],
            answer_short = get_answer_short(question_number, answer)
        ) %>%
        dplyr::mutate(
            answer = factor(answer, levels = canonical_answer_order(questions))
        )

    # Build a country-ordered book factor for stable y-axis ordering.
    book_order <- book_level %>%
        dplyr::distinct(country, book) %>%
        dplyr::arrange(country, book) %>%
        dplyr::pull(book)
    df$book <- factor(df$book, levels = rev(book_order))

    # Build a single palette covering ALL canonical answers across Qs.
    pal_list <- purrr::map(seq_along(questions), function(i) {
        answer_palette(questions[[i]]$number, questions)
    })
    full_pal <- unlist(pal_list)
    # Deduplicate (Other / Unsure shows up 12 times)
    full_pal <- full_pal[!duplicated(names(full_pal))]

    ggplot2::ggplot(df,
        ggplot2::aes(x = factor(paste0("Q", question_number),
                                levels = paste0("Q", sort(unique(question_number)))),
                     y = book,
                     fill = answer)) +
        ggplot2::geom_tile(color = "white", linewidth = 0.2) +
        ggplot2::scale_fill_manual(values = full_pal, na.value = "#E5E7EB",
                                   guide = "none") +
        ggplot2::facet_grid(country ~ ., scales = "free_y", space = "free_y",
                            switch = "y") +
        ggplot2::labs(
            title = paste0("Book fingerprints (", use_field, ")"),
            x = NULL, y = NULL
        ) +
        ggplot2::theme_minimal() +
        ggplot2::theme(
            strip.placement   = "outside",
            strip.text.y.left = ggplot2::element_text(angle = 0, hjust = 1),
            panel.grid        = ggplot2::element_blank(),
            axis.text.y       = ggplot2::element_text(size = 7)
        )
}


# Helper: canonical_answer_order(questions)
#     Returns a unique vector of all canonical answer strings across all
#     questions, preserving each question's ordinal order.  Used to lock
#     the factor level order in heatmaps and bar charts.
canonical_answer_order <- function(questions) {
    out <- character(0)
    for (q in questions) {
        for (a in unlist(q$answer_options)) {
            if (!a %in% out) out <- c(out, a)
        }
    }
    out
}


# 3c. plot_country_distribution(country_distributions, questions, use_field)
#     Stacked bar chart, faceted by question, with country on x-axis and
#     answer proportion stacked.  `use_field` selects "mode" or "peak"
#     aggregation (filters the long distributions tibble).
plot_country_distribution <- function(country_distributions, questions,
                                      use_field = "mode") {

    stopifnot(use_field %in% c("mode", "peak"))

    df <- country_distributions %>%
        dplyr::filter(aggregation == use_field) %>%
        dplyr::mutate(
            answer = factor(answer,
                            levels = canonical_answer_order(questions)),
            q_label = paste0("Q", question_number, ": ", criteria_short)
        )

    # Build a single palette covering ALL canonical answers across Qs.
    pal_list <- purrr::map(seq_along(questions), function(i) {
        answer_palette(questions[[i]]$number, questions)
    })
    full_pal <- unlist(pal_list)
    full_pal <- full_pal[!duplicated(names(full_pal))]

    ggplot2::ggplot(df,
        ggplot2::aes(x = country, y = proportion, fill = answer)) +
        ggplot2::geom_col(position = "stack", color = "white",
                          linewidth = 0.1) +
        ggplot2::scale_fill_manual(values = full_pal, na.value = "#E5E7EB",
                                   name = "Answer") +
        ggplot2::scale_y_continuous(labels = scales::percent_format()) +
        ggplot2::facet_wrap(~ q_label, ncol = 3, scales = "free_y") +
        ggplot2::labs(
            title = paste0("Country distributions (", use_field, ")"),
            x = NULL,
            y = "Share of books"
        ) +
        ggplot2::theme_minimal() +
        ggplot2::theme(
            legend.position = "bottom",
            legend.text     = ggplot2::element_text(size = 7),
            strip.text      = ggplot2::element_text(size = 8),
            axis.text.x     = ggplot2::element_text(angle = 30, hjust = 1)
        )
}


# 3d. plot_trajectory_per_book(claude_long, book_name, questions)
#     One figure for a single book: 12 small-multiples panels, x =
#     chapter_position, y = ordinal_position (or strip plot for nominal
#     Qs).  Returns a ggplot object.
plot_trajectory_per_book <- function(claude_long, book_name, questions) {

    df <- claude_long %>%
        dplyr::filter(book == book_name) %>%
        dplyr::mutate(
            q_label = paste0("Q", question_number, ": ",
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
                                                "TRUE"  = "#9CA3AF"),
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


# 3e. plot_trajectory_per_question(claude_long, qn, questions)
#     One figure for a single question: small-multiples panels (one per
#     book), x = chapter_position, y = ordinal_position (or answer for
#     nominal).
plot_trajectory_per_question <- function(claude_long, qn, questions) {

    df <- claude_long %>%
        dplyr::filter(question_number == qn) %>%
        dplyr::arrange(country, book, chapter_position)

    is_ord <- qn %in% ordinal_question_numbers

    q_meta <- purrr::detect(questions, ~ identical(.x$number, as.integer(qn)))
    qshort <- q_meta$criteria_short

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
                title = paste0("Q", qn, " (", qshort,
                               "): chapter trajectories by book"),
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
                title = paste0("Q", qn, " (", qshort,
                               "): chapter trajectories by book"),
                x = "Chapter position", y = "Answer"
            ) +
            ggplot2::theme_minimal() +
            ggplot2::theme(
                strip.text  = ggplot2::element_text(size = 7),
                axis.text.y = ggplot2::element_text(size = 7)
            )
    }
}


# 3f. plot_country_divergence(country_aggregates, questions, use_field)
#     Heatmap: countries x questions, color by (country position -
#     corpus mean position) for ordinal Qs.  Highlights which countries
#     are systematically high/low on each dimension.  `use_field` is one
#     of "mean_position" (mode-based), "mean_peak_position", or
#     "median_position".
plot_country_divergence <- function(country_aggregates, questions,
                                    use_field = "mean_position") {

    stopifnot(use_field %in% c("mean_position", "mean_peak_position",
                                "median_position", "mean_end_position"))

    ord_qs <- country_aggregates %>%
        dplyr::filter(scale == "ordinal") %>%
        dplyr::mutate(value = .data[[use_field]]) %>%
        dplyr::filter(!is.na(value))

    if (nrow(ord_qs) == 0L) {
        return(ggplot2::ggplot() +
                   ggplot2::labs(title = "No ordinal data for divergence plot"))
    }

    corpus_mean <- ord_qs %>%
        dplyr::group_by(question_number) %>%
        dplyr::summarise(corpus_mean = mean(value, na.rm = TRUE),
                         .groups = "drop")

    df <- ord_qs %>%
        dplyr::left_join(corpus_mean, by = "question_number") %>%
        dplyr::mutate(divergence = value - corpus_mean,
                      q_label = paste0("Q", question_number))

    ggplot2::ggplot(df,
        ggplot2::aes(x = q_label, y = country, fill = divergence)) +
        ggplot2::geom_tile(color = "white", linewidth = 0.3) +
        ggplot2::geom_text(ggplot2::aes(label = sprintf("%+.1f", divergence)),
                           size = 3, color = "black") +
        ggplot2::scale_fill_gradient2(
            low      = "#2563EB",
            mid      = "#F9FAFB",
            high     = "#DC2626",
            midpoint = 0,
            name     = "+/- vs corpus"
        ) +
        ggplot2::labs(
            title    = paste0("Country divergence from corpus average (",
                              use_field, ")"),
            subtitle = "Cells show country position - corpus mean position; ordinal Qs only.",
            x = NULL, y = NULL
        ) +
        ggplot2::theme_minimal() +
        ggplot2::theme(panel.grid = ggplot2::element_blank())
}
