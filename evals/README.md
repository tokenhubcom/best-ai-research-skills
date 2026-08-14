# Evaluation suite

This suite checks whether the ten skills add reliable behavior rather than acting as generic prompts.

Each skill has three cases:

- `activation`: a request that should use the skill.
- `boundary`: a nearby request that should route to a different skill.
- `degraded`: a request where a required tool, source, permission, or fact is unavailable.

The expected result is defined as observable requirements, not an exact answer. A model should not see those requirements before it performs the task.

Run the structural checks with:

```bash
python3 evals/validate_cases.py
```

For behavioral evaluation, give an isolated agent only the candidate skill and the `prompt` from one case. Score the response afterward against `must` and `must_not`.

