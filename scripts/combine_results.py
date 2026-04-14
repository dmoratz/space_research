"""
combine_results.py
------------------
Combines all per-book CSV files in data/results/ into a single
master CSV file for analysis.

Usage:
    python combine_results.py
    python combine_results.py --output data/all_results.csv
"""

import argparse
import csv
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description="Combine per-book CSVs into one.")
    p.add_argument(
        "--input-dir", type=Path, default=Path("data/results"),
        help="Directory containing per-book CSV files (default: data/results/)",
    )
    p.add_argument(
        "--output", type=Path, default=Path("data/nlp_analysis_results.csv"),
        help="Output path for combined CSV (default: data/nlp_analysis_results.csv)",
    )
    args = p.parse_args()

    csv_files = sorted(args.input_dir.glob("*.csv"))
    if not csv_files:
        print(f"No CSV files found in {args.input_dir}")
        return

    all_rows = []
    fieldnames = None

    for csv_file in csv_files:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if fieldnames is None:
                fieldnames = reader.fieldnames
            for row in reader:
                all_rows.append(row)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Combined {len(csv_files)} files ({len(all_rows)} total rows) → {args.output}")


if __name__ == "__main__":
    main()
