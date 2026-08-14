# Best AI Research Workflow Skills for AI Agents

Ten portable Agent Skills for the complete research workflow: discover evidence, understand it, organize it, and turn it into reliable deliverables.

Every skill follows the open `SKILL.md` format and stays model-, provider-, and gateway-neutral. The instructions use tools already available in the user's agent; they do not contain API keys or assume network access.

## Workflow map

| Stage | Skill | Use it for |
|---|---|---|
| Discover | [`deep-research`](skills/deep-research/) | Investigate a question using new external sources. |
| Discover | [`seo-research`](skills/seo-research/) | Observe live search results and build an SEO research brief. |
| Understand | [`document-summarization`](skills/document-summarization/) | Compress supplied material without performing new research. |
| Understand | [`research-translation`](skills/research-translation/) | Translate research while preserving terminology and evidence. |
| Understand | [`data-analysis`](skills/data-analysis/) | Inspect structured data and produce reproducible findings. |
| Organize | [`research-memory`](skills/research-memory/) | Maintain an explicit, durable research record. |
| Organize | [`meeting-research-notes`](skills/meeting-research-notes/) | Turn meetings and interviews into decisions and research follow-ups. |
| Deliver | [`research-reporting`](skills/research-reporting/) | Turn an existing evidence set into a decision-ready report. |
| Deliver | [`research-writing`](skills/research-writing/) | Draft non-academic content from existing research. |
| Deliver | [`academic-research-writing`](skills/academic-research-writing/) | Create scholarly outlines, synthesis, and citation-aware drafts. |

## Tool-aware behavior

These skills do not pretend that every agent has the same tools.

- With search or browser tools, research skills retrieve current sources and preserve URLs and access dates.
- Without search tools, they work only from user-supplied material and label the result `source-limited`.
- With a code runtime, data analysis uses deterministic calculations and records the method.
- Without a code runtime, data analysis may explain a method but must not invent computed results.
- Persistent storage is used only when the user requests it and the agent has an authorized writable location.

## Install

Copy each desired skill folder into a skill root supported by your agent:

| Agent | Typical location |
|---|---|
| Codex | `$CODEX_HOME/skills/<skill-name>/` |
| Claude Code | `.claude/skills/<skill-name>/` or `~/.claude/skills/<skill-name>/` |
| OpenClaw | `<workspace>/skills/<skill-name>/` or `<workspace>/.agents/skills/<skill-name>/` |
| Other Agent Skills clients | Use the client's configured skill root. |

This is a multi-skill repository. If an installer expects a repository-level `SKILL.md`, install or copy the individual subdirectory instead of treating the repository root as one skill.

For example, after cloning the repository, install one skill in Codex with:

```bash
cp -R skills/deep-research "$CODEX_HOME/skills/deep-research"
```

Repeat with any other folder under `skills/` that you want to use. Restart or reload the agent if it does not discover newly installed skills automatically.

## Example requests

```text
Research whether small language models are practical for offline customer support.
Summarize these three papers and preserve all reported limitations.
Analyze this CSV and explain which findings are descriptive versus causal.
Turn this interview transcript into decisions, claims to verify, and next actions.
Write a literature synthesis from these sources without inventing citations.
```

## Quality principles

- Keep sourced facts separate from inference and recommendation.
- Preserve provenance, dates, numbers, uncertainty, and disagreement.
- Never fabricate sources, citations, measurements, or tool results.
- State source coverage, methodology, limitations, and unresolved questions.
- Require qualified review for high-stakes legal, medical, financial, or safety decisions.

## Quality and evaluation

The repository includes a portable evaluation set covering activation, boundary routing, and degraded-tool behavior for all ten skills.

- 30 structured cases across 10 skills and 3 evaluation types.
- 10/10 activation-routing checks passed.
- 10/10 boundary-routing checks passed.
- 10/10 isolated behavior checks passed after review and correction.
- The data-analysis helper includes three passing unit tests.

See the [evaluation guide](evals/README.md), [scorecard](evals/scorecard.md), and [latest forward-test report](evals/results/forward-test-2026-08-14.md).

## Contributing and security

Contributions are welcome when they preserve the collection's provider-neutral, evidence-first behavior. Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing a skill or adding a script.

Do not place API keys, access tokens, private datasets, or confidential source material in issues, pull requests, examples, or evaluation fixtures. See [SECURITY.md](SECURITY.md) for reporting guidance.
