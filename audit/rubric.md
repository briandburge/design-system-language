# Audit rubric

## Severity

### Error

A clear violation that may reduce trust, accessibility, accuracy, or task completion.

### Warning

A meaningful inconsistency or pattern that weakens clarity, tone, or authorship.

### Recommendation

A refinement that may improve quality but depends on context.

## Scoring

Start at 100.

- Error: subtract 5 points per unique issue, up to 25 points per rule.
- Warning: subtract 2 points per unique issue, up to 10 points per rule.
- Recommendation: subtract 1 point per unique issue, up to 5 points per rule.

Do not award false precision. Scores are directional and should always be paired with findings.

## Human-authorship signal score

Use this optional score only for AI writing-pattern audits.

Rate the content from 0 to 10 in half-point increments based on editorial evidence:

- 9–10: Strong specificity, experience, evidence, constraints, and individual point of view with few formulaic patterns.
- 7–8.5: Credible and distinctive overall with several polished or repeatable AI-associated patterns.
- 5–6.5: Mixed evidence, with substantial generic fluency, abstraction, repetition, or formulaic structure.
- 0–4.5: Predominantly generic or templated language with little concrete authorship evidence.

Consider DL-011, DL-054, and DL-060 through DL-066. Repeated patterns weigh more than isolated findings. Concrete evidence, constraints, tradeoffs, uncertainty, and point of view are positive signals.

The score is not a probability, detection result, or estimate of how much content was written by a human. Always pair it with a short evidence-based interpretation.

## Categories

- Grammar and mechanics
- Editorial structure
- Voice and evidence
- Natural writing
- Accessibility
- Component language
- Cross-document consistency
