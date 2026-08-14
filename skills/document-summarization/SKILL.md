---
name: document-summarization
description: Faithfully summarize supplied articles, documents, reports, transcripts, notes, or conversations into a TLDR, executive summary, key points, risks, or custom format. Use when no new external research is required. For meeting decisions and owner tracking use meeting-research-notes; for creating a report from multiple evidence sources use research-reporting.
---

# Document Summarization

Compress supplied material while preserving meaning, evidence boundaries, and important exceptions.

## Set the summary contract

1. Identify audience, purpose, output language, format, and length.
2. Identify whether the user wants faithful compression, decision support, comparison, action extraction, or simplification.
3. Use only the supplied material unless the user explicitly requests external verification; route that request to deep research.

## Build a coverage map

1. Segment long material by logical section rather than arbitrary character count.
2. For each section, record the main claim, supporting evidence, decisions, dates, quantities, named entities, caveats, and unresolved issues.
3. Merge duplicates while preserving meaningful disagreement and chronology.
4. Separate source statements from your interpretation. Retain qualifiers such as `may`, `reported`, and `according to`.
5. For very long inputs, summarize sections first and synthesize only from those checked section summaries.

## Produce the requested format

Default to:

```markdown
## TL;DR
Two to four sentences.

## Key points
- ...

## Decisions or actions
- ...

## Risks, caveats, and open questions
- ...
```

For comparisons, use shared dimensions and distinguish absence of evidence from disagreement. For simplification, retain the original technical meaning and define unavoidable terms.

## Fidelity audit

- Check every name, date, number, unit, polarity, and causal statement against the source.
- Preserve material limitations and minority viewpoints.
- Do not create citations, quotations, action owners, or recommendations absent from the source.
- State when the input is incomplete, anecdotal, garbled, or internally inconsistent.
- Minimize sensitive details not needed for the requested summary.

