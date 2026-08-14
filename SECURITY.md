# Security Policy

## Scope

Security reports may cover skill instructions, bundled scripts, evaluation fixtures, or repository documentation that could cause unsafe tool use, data disclosure, secret exposure, or misleading behavior.

The current collection contains no embedded credentials and its bundled data-analysis helper does not make network requests. Agents may still have powerful tools, so users should review requested actions and retain their agent's permission controls.

## Reporting a vulnerability

After this repository is published, use its private GitHub security-advisory channel when available. Do not disclose exploitable details or secrets in a public issue.

Include:

- The affected skill or file path.
- A minimal prompt or input that reproduces the behavior.
- The observed tool calls or output.
- The agent and environment used for testing.
- The impact and any suggested mitigation.

Never include real API keys, access tokens, confidential documents, or personal data in a report. Replace them with safe test values.

## Supported version

Security fixes target the latest revision on the default branch. Users should update their installed skill folders after a fix is released.
