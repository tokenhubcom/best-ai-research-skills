---
name: research-translation
description: Translate research papers, reports, transcripts, tables, citations, and source notes while preserving meaning, terminology, uncertainty, and structure. Use when translation is the primary task. Do not use to summarize, rewrite, or independently verify the source unless the user explicitly requests those separate operations.
---

# Research Translation

Translate for semantic fidelity first and target-language readability second. Do not silently change the source's claims.

## Establish the translation contract

1. Confirm source language, target locale, audience, deliverable format, and desired mode: literal, polished, bilingual, or publication-ready.
2. Identify formatting that must survive: headings, tables, citations, links, equations, code, placeholders, and reference identifiers.
3. Determine whether material is confidential or regulated before using any external translation service. Use only tools authorized by the user and runtime.

## Prepare terminology

1. Inspect the document for recurring technical terms, names, abbreviations, units, and do-not-translate items.
2. Copy [`assets/termbase.csv`](assets/termbase.csv) when a reusable glossary is needed.
3. Prefer an approved glossary or standard domain translation. Otherwise retain the original term at first mention when ambiguity would impair traceability.

## Translate and review

1. Preserve section order and citation identifiers unless localization requires a documented change.
2. Preserve modality, negation, comparison direction, statistical uncertainty, and quoted status.
3. Localize units, dates, and punctuation only when requested; retain original values when conversion could create ambiguity.
4. Run a reverse factual check for names, numbers, units, polarity, references, and conclusions.
5. Mark unresolved ambiguity with `[translator note: ...]` rather than guessing.

## Completion checks

- Do not add, remove, fact-check, or strengthen source claims during translation.
- Flag likely transcription or source errors instead of silently correcting them.
- Keep terminology consistent with the termbase.
- Use paired sections instead of a wide bilingual table when readability would suffer.
- Require qualified review for legal, medical, certified, or regulated translations.

