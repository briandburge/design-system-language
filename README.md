# Design Language

Design Language is a portable editorial and interface language system for human and AI-assisted workflows.

Its purpose is practical: make content more consistent, easier to scan, and less likely to carry generic AI writing patterns.

## Use it today

Use the audit prompts in `audit/prompts/` with a document, website, interface, presentation, or case study. The auditor reports findings by rule ID and does not rewrite unless asked.

## Repository model

- `spec/` explains the language system for people.
- `rules/rules.yaml` is the canonical machine-readable rule set.
- `audit/` defines scoring, severity, report structure, and reusable prompts.
- `adapters/` provides thin instructions for AI-assisted tools.
- `examples/` shows preferred and discouraged patterns.
- `decisions/` records why important rules exist.

## Core principle

Markdown explains the system. Structured data defines it. Adapters distribute it.

## Version

Current version: `1.0.0`
