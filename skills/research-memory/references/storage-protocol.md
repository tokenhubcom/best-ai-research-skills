# Research memory storage protocol

Use this protocol only in a user-approved writable location.

## Layout

```text
research-memory/
├── INDEX.md
├── records/
│   └── stable-topic-slug.md
└── archive/
```

`INDEX.md` contains one row per canonical record: title, relative path, aliases, status, and last-updated date.

## Write rules

1. Read the current record and index before changing either.
2. Use a stable semantic slug; never create `topic-2.md` to avoid resolving a collision.
3. Store one canonical record and point aliases to it from the index.
4. Write the record first, verify it, then update the index.
5. Use ISO dates (`YYYY-MM-DD`) and relative links.

## Truth states

- **Confirmed:** Supported by a cited source or explicit user decision.
- **Reported:** Claimed by a participant or source but not independently verified.
- **Hypothesis:** Proposed explanation awaiting evidence.
- **Superseded:** Previously current but replaced on a recorded date.
- **Disputed:** Material sources conflict.

Never upgrade a state without recording the evidence that justified it.

## Changes and conflicts

- If a fact changed over time, append the new value and move the old value to history as `Superseded`.
- If an entry was never true, delete it rather than archiving it as historical truth.
- If sources disagree, preserve both claims and mark the record `Disputed`.
- Merge duplicate records into the older canonical file and update inbound links.

## Recall and deletion

- Search the index before opening records; load only relevant files.
- Return the record date and source when freshness matters.
- On deletion, remove the record, index row, aliases, and known inbound links.
- Report the exact paths changed or removed.

