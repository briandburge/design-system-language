# Repository instructions

Use `rules/rules.yaml` as the canonical source of truth.

When editing documentation:

- use sentence case for headings
- avoid em dashes in normal prose
- prefer concrete nouns and active verbs
- keep one main idea per paragraph
- avoid generic marketing language and AI writing patterns
- preserve rule IDs
- update `CHANGELOG.md` when behavior changes

Do not duplicate canonical rules inside adapters. Adapters should point back to the rule set and explain tool-specific use.
