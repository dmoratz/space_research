"""
split_all.py
------------
Master script that runs the generic chapter splitter (split_books.py)
and all dedicated book-specific splitters in one go.

Usage:
    # Dry run — show what would be split, don't write anything:
    python scripts/splitters/split_all.py --dry-run

    # Split everything:
    python scripts/splitters/split_all.py
"""

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent

# All splitter scripts in recommended execution order.
# The generic script runs first, then dedicated scripts for books
# that can't be handled generically.
SPLITTERS = [
    # Generic chapter splitter (handles most books)
    "split_books.py",
    # Dedicated splitters for books needing special handling
    "split_broken_stars.py",
    "split_aelita.py",
    "split_administrator.py",
    "split_orbital_cloud.py",
    "split_view_from_stars.py",
    "split_wandering_earth.py",
    "split_vagabonds.py",
    "split_ten_billion.py",
    "split_roadside_picnic.py",
    "split_three_body.py",
    "split_quantum_thief.py",
    "split_dune.py",
]


def main():
    parser = argparse.ArgumentParser(
        description="Run all book splitter scripts")
    parser.add_argument("--dry-run", action="store_true",
                        help="Pass --dry-run to all splitter scripts")
    args = parser.parse_args()

    failed = []
    succeeded = []

    for script_name in SPLITTERS:
        script_path = SCRIPTS_DIR / script_name
        if not script_path.exists():
            print(f"\n  SKIP: {script_name} (not found)")
            continue

        print(f"\n{'=' * 60}")
        print(f"  Running: {script_name}")
        print(f"{'=' * 60}")

        cmd = [sys.executable, str(script_path)]
        if args.dry_run:
            cmd.append("--dry-run")

        result = subprocess.run(cmd, cwd=str(SCRIPTS_DIR.parent.parent))

        if result.returncode != 0:
            print(f"  FAILED: {script_name} (exit code {result.returncode})")
            failed.append(script_name)
        else:
            succeeded.append(script_name)

    # Summary
    print(f"\n{'=' * 60}")
    print(f"  SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Succeeded: {len(succeeded)}")
    if failed:
        print(f"  Failed:    {len(failed)}")
        for name in failed:
            print(f"    - {name}")
    print()


if __name__ == "__main__":
    main()
