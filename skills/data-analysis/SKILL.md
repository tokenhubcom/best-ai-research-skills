---
name: data-analysis
description: Analyze supplied structured data, tables, metrics, experiments, or CSV files with reproducible calculations and explicit assumptions. Use for exploratory analysis, KPI interpretation, trend or segment analysis, and data-backed research findings. Do not use for prose-only source synthesis or unsupported numerical estimation.
---

# Data Analysis

Produce findings that another analyst can reproduce from the same data and method.

## Establish the analysis contract

1. State the decision or question, unit of analysis, population, date range, metric definitions, and expected output.
2. Identify the source files and preserve them unchanged.
3. Record known exclusions, privacy constraints, and whether causal interpretation is requested.

## Inspect before interpreting

1. Inspect schema, row count, data types, missing values, duplicates, invalid values, outliers, and category cardinality.
2. For CSV files, run `python3 scripts/profile_csv.py <file.csv>` when a Python runtime is available. Treat its output as a starting profile, not the final analysis.
3. Copy [`assets/analysis-plan.md`](assets/analysis-plan.md) and record each metric, denominator, filter, transformation, and comparison.
4. Resolve ambiguous metric definitions before calculating them.

## Analyze reproducibly

- Use code, SQL, spreadsheet formulas, or another deterministic tool for exact calculations.
- Separate descriptive results, associations, forecasts, and causal estimates.
- Report denominators, sample sizes, time windows, and uncertainty where material.
- Compare like with like; normalize only when the transformation is documented.
- Test whether a headline result is driven by missing data, outliers, aggregation, or one segment.

If no calculation tool is available, provide an analysis plan and formulas, label the response `Not computed`, and do not invent results.

## Deliverable

```markdown
# Analysis: [question]

## Decision context
## Data and quality assessment
## Method and calculations
## Key findings
## Segment and sensitivity checks
## Limitations
## Reproduction notes
## Recommended next steps
```

## Completion checks

- Recalculate or independently verify decision-critical numbers.
- Distinguish percentage change from percentage-point change.
- Do not imply causation without a suitable design.
- Minimize exposure of personal or sensitive records.
- Never conceal missing data, exclusions, or failed analyses.

