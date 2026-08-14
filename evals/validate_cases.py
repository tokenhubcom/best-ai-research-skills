#!/usr/bin/env python3
"""Validate coverage and structure of the repository's behavioral eval cases."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = Path(__file__).with_name("cases.json")
KINDS = {"activation", "boundary", "degraded"}


def main() -> int:
    skills = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    ids: set[str] = set()

    for index, case in enumerate(cases):
        label = case.get("id", f"case[{index}]")
        if label in ids:
            errors.append(f"duplicate id: {label}")
        ids.add(label)
        if case.get("target_skill") not in skills:
            errors.append(f"{label}: unknown target_skill")
        if case.get("expected_skill") not in skills:
            errors.append(f"{label}: unknown expected_skill")
        if case.get("kind") not in KINDS:
            errors.append(f"{label}: invalid kind")
        if not str(case.get("prompt", "")).strip():
            errors.append(f"{label}: prompt missing")
        if not case.get("must") or not case.get("must_not"):
            errors.append(f"{label}: must and must_not are required")

    by_skill_kind = Counter((case.get("target_skill"), case.get("kind")) for case in cases)
    for skill in sorted(skills):
        for kind in sorted(KINDS):
            if by_skill_kind[(skill, kind)] != 1:
                errors.append(
                    f"{skill}: expected one {kind} case, found {by_skill_kind[(skill, kind)]}"
                )

    if len(cases) != len(skills) * len(KINDS):
        errors.append(f"expected {len(skills) * len(KINDS)} cases, found {len(cases)}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(cases)} cases cover {len(skills)} skills across {len(KINDS)} eval kinds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

