---
name: research-memory
description: Create and maintain an explicit, durable research record containing facts, sources, decisions, hypotheses, terminology, and open questions. Use only when the user requests persistent project memory, a reusable knowledge base, or a research handoff. Do not use for a one-time summary or ordinary session context.
---

# Research Memory

Maintain a portable, inspectable record of what a project knows, why it believes it, and what changed over time.

## Choose a storage mode

1. Use a user-specified location when provided.
2. Otherwise, ask before creating durable files and propose a project-local `research-memory/` directory.
3. If writing is unavailable or unauthorized, return the proposed records in Markdown and label them `Not persisted`.
4. Never claim to remember information that was not written to an accessible store.

Read [`references/storage-protocol.md`](references/storage-protocol.md) before creating, updating, merging, recalling, or deleting persistent records.

## Capture

1. Copy [`assets/research-record.md`](assets/research-record.md) for each durable topic or entity.
2. Store atomic entries with a date, status, provenance, and confidence basis.
3. Separate confirmed facts, user decisions, hypotheses, interpretations, and unresolved questions.
4. Normalize entity names and record aliases.
5. Update the index only after the underlying record is successfully written.

## Recall and update

1. Search the index, then open the smallest relevant record set.
2. Cite the record and its source date when answering.
3. Mark stale entries rather than silently treating them as current.
4. Supersede changed information while preserving history; delete information that was never true.
5. On a forget request, remove the record, index entry, and known inbound references, then report exactly what was removed.

## Completion checks

- Do not store passwords, API keys, tokens, or unnecessary personal data.
- Do not convert model-generated statements into confirmed facts.
- Preserve contradictions until evidence or the user resolves them.
- Keep the store understandable without the original chat history.
- Report every file created, changed, or deleted.

