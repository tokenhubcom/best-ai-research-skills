# Contributing

Thank you for helping improve this collection. Contributions should keep every skill portable, provider-neutral, evidence-first, and safe to use in agents with different tool capabilities.

## Before submitting a change

1. Keep the skill name and description focused on when the skill should activate.
2. Do not add API keys, secrets, vendor-specific account details, or silent network calls.
3. Distinguish sourced facts, calculations, inferences, hypotheses, and recommendations.
4. Preserve citations, dates, units, uncertainty, disagreement, and limitations.
5. Describe degraded behavior when search, code execution, or persistent storage is unavailable.
6. Add or update activation, boundary, and degraded-tool evaluation cases when behavior changes.
7. Add tests for deterministic scripts.

## Repository checks

From the repository root, run:

```bash
python3 evals/validate_cases.py
(cd skills/data-analysis/scripts && python3 -m unittest test_profile_csv.py)
```

Also verify that every `SKILL.md` has valid YAML frontmatter and that all local Markdown links resolve.

## Adding a skill

Place each standalone skill in `skills/<skill-name>/`. Include a `SKILL.md` and an `agents/openai.yaml`. Put detailed reference material in `references/` and deterministic helpers in `scripts/` only when they materially improve the workflow.

Do not add a README inside an individual skill folder. Keep user-facing collection documentation at the repository root.

## Provenance and licensing

Only contribute material that you have the right to license. Do not copy substantial wording, code, templates, or assets from another package without reviewing its license and preserving all required notices. Describe any third-party material in the pull request.
