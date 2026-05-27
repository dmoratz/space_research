# Analysis Report

_Generated: 2026-05-27 11:45:23_

## Configuration

- `collection_weight_mode`: weighted
- Books in corpus (pre-split): 46
- Books in corpus (post-split): 106
- Countries: China, Finland, France, Japan, Russia, US

## Book-level coding statistics

- Total book-level (book x question) rows: 552
- Rows requiring tie-breaking: 27
- Books coded Other / Unsure (all chapters were Other / Unsure): 27
- Ordinal books where peak != mode: 255

## Outputs

- `data/processed/book_level.{rds,csv}`
- `data/processed/country_distributions.{rds,csv}`
- `data/processed/country_aggregates.{rds,csv}`
- `data/processed/figures/` (78 files)

## Carry-forward IRR caveats from Task 2

- Mean per-question weighted kappa across the 5 IRR books: 0.857 (ordinal questions).
- Mean per-question alpha across the 5 IRR books: 0.703.
- Where both Claude and the human committed to ordinal answers, agreement is strong; pooled nominal agreement is weaker (pooled alpha = 0.389 with all cells, 0.636 excluding one-sided Other / Unsure).
- Q9 (genre) and Q11 (nearest-neighbor metaphor) have weak chapter-level reliability (kappa ~ 0.03-0.06); present their distributions with this caveat.
- Planet of the Apes had heavy human hedging (68% Other / Unsure); the Claude-only analysis here is unaffected but cross-book comparisons that hinge on Apes should be noted.
