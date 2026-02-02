"""
Simple utility to load records from a JSON file and filter them by grade.

Assumptions:
- The JSON file contains a list of objects.
- Each object may have a numeric "grade" field.

Example JSON structure in data.json:
[
  {"name": "Alice", "grade": 85},
  {"name": "Bob", "grade": 72},
  {"name": "Charlie", "grade": 91}
]

Usage:
    python filter_by_grade.py --json-path data.json --min-grade 80
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, List


def load_records(path: str) -> List[Dict[str, Any]]:
    """Load a list of records from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list at {path}, got {type(data).__name__}")

    return data


def filter_by_min_grade(records: List[Dict[str, Any]], min_grade: float) -> List[Dict[str, Any]]:
    """Return only records whose 'grade' field is present and >= min_grade."""
    filtered: List[Dict[str, Any]] = []
    for record in records:
        grade = record.get("grade")
        if isinstance(grade, (int, float)) and grade >= min_grade:
            filtered.append(record)
    return filtered


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filter JSON records by a minimum grade.",
    )
    parser.add_argument(
        "--json-path",
        default="data.json",
        help="Path to the input JSON file (default: data.json).",
    )
    parser.add_argument(
        "--min-grade",
        type=float,
        required=True,
        help="Minimum grade threshold to include a record.",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv)

    try:
        records = load_records(args.json_path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error loading data from {args.json_path}: {exc}", file=sys.stderr)
        return 1

    filtered = filter_by_min_grade(records, args.min_grade)

    # Output filtered records as pretty-printed JSON to stdout
    json.dump(filtered, sys.stdout, indent=2, ensure_ascii=False)
    print()  # newline after JSON

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

