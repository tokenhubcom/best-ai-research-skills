---
name: deep-research
description: Conduct new, evidence-based multi-source research for a complex question, comparison, claim evaluation, or decision briefing. Use when the task requires finding and assessing external sources. Do not use merely to summarize supplied documents or format an existing evidence set; use document-summarization or research-reporting for those tasks.
---

# Deep Research

Investigate a focused question with a reproducible research trail. Match the strength of every conclusion to source quality and coverage.

## Establish the research contract

1. Restate the primary question and the decision it supports.
2. Record audience, geography, date range, exclusions, required depth, and deadline.
3. Split the question into non-overlapping subquestions.
4. Define a stopping rule: answer coverage reached, evidence converged, material disagreement documented, or budget exhausted.
5. Ask only for missing information that would materially change the research direction.

## Choose the operating mode

- **Tools available:** Search the web, databases, or repositories with the agent's authorized tools. Record URLs, publication dates, and access dates.
- **No retrieval tools:** Use only user-supplied sources. Label the result `Source-limited research` and list the evidence still needed. Never simulate search results.
- **High-stakes topic:** Prefer primary and authoritative sources, narrow claims, and identify the professional review still required.

## Research workflow

1. Create query families for each subquestion: direct terms, synonyms, named entities, primary-source domains, and disconfirming terms.
2. Search broad-to-narrow. Follow important citations back to primary material.
3. Score material sources using [`references/source-quality.md`](references/source-quality.md). Exclude low-value duplicates and explain consequential exclusions.
4. Copy [`assets/evidence-matrix.md`](assets/evidence-matrix.md) into the working output and track every decision-relevant claim.
5. Seek counterevidence before concluding. Treat repeated reporting of one underlying source as one evidence chain.
6. Synthesize agreements, disagreements, boundary conditions, and unknowns.
7. Run a citation audit: each material factual claim must map to a real source; each inference must be labelled.

## Deliverable

```markdown
# Research briefing: [question]

## Bottom line
## Scope and operating mode
## Key findings
## Evidence and source assessment
## Counterevidence and disagreements
## Implications
## Limitations and unresolved questions
## Method and stopping reason
## Sources
```

## Completion checks

- Answer the stated question rather than the broader topic.
- Include source dates for volatile claims and access dates for web sources.
- Report material negative findings and missing evidence.
- Avoid confidence labels unsupported by the evidence matrix.
- Do not fabricate citations, quotations, statistics, or search activity.

