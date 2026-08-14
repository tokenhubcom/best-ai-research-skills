#!/usr/bin/env python3

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from profile_csv import parse_number, profile_csv


class ProfileCsvTests(unittest.TestCase):
    def test_parse_number(self) -> None:
        self.assertEqual(parse_number("1,250.5"), 1250.5)
        self.assertIsNone(parse_number(""))
        self.assertIsNone(parse_number("NaN"))
        self.assertIsNone(parse_number("hello"))

    def test_profile(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text(
                "team,score,note\nA,10,ok\nB,20,\nA,10,ok\n",
                encoding="utf-8",
            )
            result = profile_csv(path, "utf-8", ",", 3)

        self.assertEqual(result["rows"], 3)
        self.assertEqual(result["columns"], 3)
        self.assertEqual(result["duplicate_rows"], 1)
        self.assertEqual(result["column_profiles"]["note"]["missing"], 1)
        self.assertEqual(result["column_profiles"]["score"]["inferred_type"], "number")
        self.assertEqual(result["column_profiles"]["score"]["numeric"]["median"], 10.0)

    def test_empty_data_rows(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "headers.csv"
            path.write_text("a,b\n", encoding="utf-8")
            result = profile_csv(path, "utf-8", ",", 5)

        self.assertEqual(result["rows"], 0)
        self.assertEqual(result["column_profiles"]["a"]["inferred_type"], "text")


if __name__ == "__main__":
    unittest.main()

