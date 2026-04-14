"""
setup_questions.py
------------------
One-time setup: extracts the question-answer set from the xlsx file
into a plain JSON file that Claude Code can read without needing openpyxl.

Usage:
    pip install openpyxl
    python setup_questions.py --input data/nlp_question_answer_set.xlsx \
                              --output data/questions.json
"""

import argparse
import json
from pathlib import Path
import openpyxl


def extract_questions(xlsx_path: Path) -> list[dict]:
    wb = openpyxl.load_workbook(xlsx_path)
    ws = wb.active

    questions = []
    for row in ws.iter_rows(min_row=4, min_col=1, max_col=5, values_only=True):
        _, num, crit, short, opts = row
        if num is None or crit is None:
            continue

        answer_options = [o.strip() for o in opts.split(";") if o.strip()] if opts else []

        questions.append({
            "number": int(num),
            "criteria": crit.strip(),
            "criteria_short": short.strip() if short else crit.strip(),
            "answer_options": answer_options,
        })

    wb.close()
    return questions


def main():
    p = argparse.ArgumentParser(description="Extract questions from xlsx to JSON")
    p.add_argument("--input", type=Path, required=True, help="Path to nlp_question_answer_set.xlsx")
    p.add_argument("--output", type=Path, default=Path("data/questions.json"), help="Output JSON path")
    args = p.parse_args()

    questions = extract_questions(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(questions, indent=2, ensure_ascii=False))
    print(f"Extracted {len(questions)} questions to {args.output}")


if __name__ == "__main__":
    main()
