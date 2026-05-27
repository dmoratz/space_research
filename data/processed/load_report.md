# Data Load Report

Generated: 2026-05-25 15:04:55 EDT
Script:    scripts/data_loading.Rmd

## Files

- Total CSVs found:        46
- Files dropped (skip list): 0
- Files loaded:            46

No files were skipped via `file_drop_list`.

## Rows

- Raw rows (after file load):     1158
- Paratext rows dropped:          29
- Clean wide rows:                1129
- Long-format rows (wide x 12 Qs): 13548

## Books

- Distinct books in clean frame: 46
- Distinct countries:            6

Per-country book counts:

- China: 8 books
- Finland: 4 books
- France: 6 books
- Japan: 9 books
- Russia: 8 books
- US: 11 books

## Validation

- Answer-validation mismatches: 0
- Unparseable chapter labels:   157

## Outputs

Files written to `data/processed/`:

- `space_chapters_wide.rds`
- `space_chapters_wide.csv`
- `space_chapters_long.rds`
- `space_chapters_long.csv`
- `load_report.md` (this file)

