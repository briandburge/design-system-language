# Changelog

## Unreleased

- Renamed the GitHub repository from `design-system-language` to `design-language`.

- Required the human-authorship signal score whenever users ask about AI or human writing indicators.
- Added a human-readable rule reference and user-facing cited-rule summaries.

- Added a directional human-authorship signal score for AI writing-pattern audits.
- Expanded AI-pattern checks to include em dashes under DL-011 and repetition under DL-054.

- Removed the GitHub Actions validation workflow.

- Registered public Design Language Auditor GPT.

- Added project charter, vision, and non-goals.
- Added Custom GPT release process.
- Expanded Codex handoff guidance.
- Preserved Sprint 1 as an explicit execution plan.

## 1.0.1

- Added audit scope specification.
- Added DL-120 Respect audit scope.
- Standardized audit scope reporting.
- Added navigation crawl guidance.
- Added reproducibility guidance for website audits.
- Added durable project context, roadmap, and Sprint 1 documents.

### Design Language Auditor GPT

- Published GPT version 1.0.1 on July 12, 2026.
- Replaced all five knowledge files with the DSL 1.0.1 bundle.
- Updated the displayed DSL version and GPT instructions to 1.0.1.
- Added explicit single-page, navigation-crawl, and entire-site scope behavior.
- Confirmed that a single supplied URL does not trigger internal-link traversal or public search.
- Added the no-auth Rendered URL Reader Action for JavaScript-dependent public pages.
- Added retrieval fallback, scope-control, privacy-disclosure, and failure-handling instructions.
- Confirmed that the Action retrieves substantive rendered copy without following links outside the requested scope.
- Retained the existing audit-mode conversation starters.
- Known limitation: the Reader Action is subject to third-party availability, rate limits, access controls, and incomplete retrieval on some pages.
- Public GPT: https://chatgpt.com/g/g-6a52996c067481919f69cde33a25b22d-design-language-auditor

## 1.0.0

- Added a complete editorial and interface language specification.
- Added stable rule IDs and severity levels.
- Added audit prompts for documents, websites, UI copy, and AI-specific writing patterns.
- Added a scoring rubric and report template.
- Added machine-readable rules and a JSON schema.
- Added adapters for Codex, Cowork, Figma Make, and generic AI tools.
- Added examples and decision records.
