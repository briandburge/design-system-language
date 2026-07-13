# AI writing patterns audit prompt

Audit the supplied content for patterns covered by DL-011, DL-054, and DL-060 through DL-066.

Look for repeated patterns, not isolated words alone.

Do not treat every em dash, triad, transition, or marketing term as proof of AI authorship. The goal is editorial quality, not detection.

Report a directional human-authorship signal score from 0 to 10 in half-point increments. This score measures how strongly the writing demonstrates concrete experience, specificity, constraints, tradeoffs, uncertainty, evidence, and individual point of view. It is not a probability, detection result, or claim about who wrote the content.

Accompany the score with a short interpretation in this pattern:

> Overall, I would rate the page [score]/10 for human-authorship signals. [Brief evidence-based explanation of what reads as experience-driven and which limited passages contain formulaic patterns associated with AI-assisted polishing.]

Do not convert the score into a percentage of human-written or AI-written content. When useful, identify the approximate number of sentences that contain relevant patterns, but describe the patterns rather than attributing their origin.

Treat repeated em-dash use as a meaningful signal under DL-011. Treat one necessary em dash as an isolated punctuation finding, not authorship evidence.

For each finding:

- cite the rule ID
- show the smallest useful excerpt
- explain the pattern
- state whether it is isolated or repeated
- suggest an editing direction without rewriting the full passage
