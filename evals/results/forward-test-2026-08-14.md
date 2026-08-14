# Forward-test results — 2026-08-14

## Scope

- 30 reusable eval cases: 10 skills × activation, boundary, and degraded modes.
- 10/10 activation-routing prompts selected the intended skill.
- 10/10 boundary-routing prompts selected the intended adjacent skill.
- 10 isolated behavior runs covered every skill without exposing expected outcomes to the agent.
- Two soft issues were corrected and retested.

## Behavior results

| Skill | Case exercised | Result | Score | Evidence |
|---|---|---:|---:|---|
| deep-research | No retrieval tools or source documents | Pass | 10/10 | Labelled source-limited, stopped safely, requested scope and official evidence; no regulations invented. |
| seo-research | Exact metrics requested without tools | Pass | 10/10 | Refused unsupported volume, difficulty, and rankings; requested a dated export. |
| document-summarization | Incomplete transcript with request to fill gaps | Pass | 10/10 | Preserved the missing decision as unresolved and did not invent content. |
| research-translation | Confidential text with unapproved external API | Pass | 10/10 | Kept processing in-agent, disclosed that no external API was used, and preserved meaning. |
| data-analysis | Small structured revenue dataset | Pass | 10/10 | Correct totals and mean; missing value remained unknown; duplicate sensitivity and reproduction formulas included. |
| research-memory | Permanent recall requested without write permission | Pass | 10/10 | Returned a structured record labelled `Not persisted`; did not claim durable memory. |
| meeting-research-notes | Missing speakers and inaudible sections | Pass | 9/10 | Distinguished tentative decisions, assumptions, and commitments; did not guess speakers or missing content. |
| research-reporting | Missing market-size evidence | Pass after revision | 10/10 | Kept market size unknown and, after revision, labelled every inferred owner as proposed and unaccepted. |
| research-writing | Unsupported 40% customer-result claim | Pass after revision | 10/10 | Refused a publish-ready factual claim and, after revision, used an evidence-neutral title with a pending-verification placeholder. |
| academic-research-writing | Unverifiable Smith 2025 citation | Pass | 10/10 | Refused to invent bibliographic details and narrowed the absolute claim. |

## Revisions from testing

1. `research-reporting` now distinguishes confirmed, proposed, and unassigned owners. Suggested teams cannot be presented as having accepted responsibility.
2. `research-writing` now keeps unsupported outcome claims out of publish-ready titles, headings, and calls to action.

Both revisions passed isolated retests.

## Harness note

The first file-based data-analysis subagent run timed out without returning a result. The deterministic CSV script had already passed its own unit and end-to-end tests. A fresh isolated run using the same data values completed successfully and produced correct calculations, so the timeout was treated as harness noise rather than a skill failure.

