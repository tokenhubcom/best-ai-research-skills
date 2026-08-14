#!/usr/bin/env python3
"""Create a deterministic, dependency-free structural profile of a CSV file."""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


def parse_number(value: str) -> float | None:
    candidate = value.strip().replace(",", "")
    if not candidate:
        return None
    try:
        number = float(candidate)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def summarize_column(values: list[str], top: int) -> dict[str, Any]:
    nonempty = [value for value in values if value.strip()]
    counts = Counter(nonempty)
    numeric_values = [number for value in nonempty if (number := parse_number(value)) is not None]
    profile: dict[str, Any] = {
        "missing": len(values) - len(nonempty),
        "non_missing": len(nonempty),
        "unique_non_missing": len(counts),
        "top_values": [
            {"value": value, "count": count}
            for value, count in counts.most_common(top)
        ],
    }
    if nonempty and len(numeric_values) == len(nonempty):
        ordered = sorted(numeric_values)
        midpoint = len(ordered) // 2
        median = (
            ordered[midpoint]
            if len(ordered) % 2
            else (ordered[midpoint - 1] + ordered[midpoint]) / 2
        )
        profile["inferred_type"] = "number"
        profile["numeric"] = {
            "minimum": min(ordered),
            "maximum": max(ordered),
            "mean": sum(ordered) / len(ordered),
            "median": median,
        }
    else:
        profile["inferred_type"] = "text"
    return profile


def profile_csv(path: Path, encoding: str, delimiter: str, top: int) -> dict[str, Any]:
    with path.open("r", encoding=encoding, newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        if not reader.fieldnames:
            raise ValueError("CSV file has no header row")
        fieldnames = [name if name is not None else "" for name in reader.fieldnames]
        duplicate_headers = [name for name, count in Counter(fieldnames).items() if count > 1]
        rows = list(reader)

    columns = {
        name: summarize_column([row.get(name, "") or "" for row in rows], top)
        for name in fieldnames
    }
    row_signatures = Counter(
        tuple((row.get(name, "") or "") for name in fieldnames) for row in rows
    )
    duplicate_rows = sum(count - 1 for count in row_signatures.values() if count > 1)
    return {
        "file": str(path),
        "rows": len(rows),
        "columns": len(fieldnames),
        "headers": fieldnames,
        "duplicate_headers": duplicate_headers,
        "duplicate_rows": duplicate_rows,
        "column_profiles": columns,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--encoding", default="utf-8-sig")
    parser.add_argument("--delimiter", default=",")
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    if len(args.delimiter) != 1:
        parser.error("--delimiter must be exactly one character")
    if args.top < 0:
        parser.error("--top must be zero or greater")
    if not args.csv_file.is_file():
        parser.error(f"file not found: {args.csv_file}")

    try:
        result = profile_csv(args.csv_file, args.encoding, args.delimiter, args.top)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

