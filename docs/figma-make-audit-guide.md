# Audit a Figma Make webpage with Design Language

This guide explains how to audit a single webpage created in Figma Make using Design Language v1.0.1.

The workflow separates evaluation from revision. Figma Make should report findings first and make changes only after you approve specific findings.

## Important limitation

Do not rely on Figma Make to retrieve the knowledge files by pasting their GitHub URLs into a prompt. Use the URLs to download the Markdown files, then attach the downloaded files to the Figma Make prompt.

The URLs provide:

- A canonical source
- A download location
- Version traceability
- A way to check for updates

The attached Markdown files provide the audit context.

## Required knowledge files

A complete audit with scoring and human-authorship signals uses five files:

1. Rule reference
2. Website audit instructions
3. Audit report template
4. Scoring rubric
5. AI writing-pattern audit instructions

### Current files

These URLs always point to the latest files on `main`:

- [Rule reference](https://raw.githubusercontent.com/briandburge/design-language/main/docs/rule-reference.md)
- [Website audit prompt](https://raw.githubusercontent.com/briandburge/design-language/main/audit/prompts/website-audit.md)
- [Audit report template](https://raw.githubusercontent.com/briandburge/design-language/main/audit/report-template.md)
- [Audit rubric](https://raw.githubusercontent.com/briandburge/design-language/main/audit/rubric.md)
- [AI writing-pattern audit prompt](https://raw.githubusercontent.com/briandburge/design-language/main/audit/prompts/ai-tells-audit.md)

### Version-pinned files

Use these links for a reproducible audit. They will not change when `main` changes:

- [Rule reference, pinned](https://raw.githubusercontent.com/briandburge/design-language/43b8cedbea3a69100fd23469a819ed97bf3f2ded/docs/rule-reference.md)
- [Website audit prompt, pinned](https://raw.githubusercontent.com/briandburge/design-language/43b8cedbea3a69100fd23469a819ed97bf3f2ded/audit/prompts/website-audit.md)
- [Audit report template, pinned](https://raw.githubusercontent.com/briandburge/design-language/43b8cedbea3a69100fd23469a819ed97bf3f2ded/audit/report-template.md)
- [Audit rubric, pinned](https://raw.githubusercontent.com/briandburge/design-language/43b8cedbea3a69100fd23469a819ed97bf3f2ded/audit/rubric.md)
- [AI writing-pattern audit prompt, pinned](https://raw.githubusercontent.com/briandburge/design-language/43b8cedbea3a69100fd23469a819ed97bf3f2ded/audit/prompts/ai-tells-audit.md)

Use the pinned files for portfolio, client, or other audits that need a record of the exact rules used.

## Step 1: Open the webpage project

Open the Figma Make file containing the webpage you want to audit.

Make sure the preview displays the page and state you want reviewed. Plan separate audits for menus, dialogs, errors, or form states that are not visible in the current page state.

## Step 2: Download the knowledge files

Open each of the five version-pinned URLs.

Save the files with these names:

```text
rule-reference.md
website-audit.md
report-template.md
rubric.md
ai-tells-audit.md
```

If your browser adds `.txt`, rename the files so they end in `.md`.

## Step 3: Attach the knowledge files

In the Figma Make prompt box:

1. Click **Add context**.
2. Select **Upload from computer**.
3. Select all five Markdown files.
4. Confirm that all five files appear as prompt attachments.

You do not need to attach the Figma Make design separately when you are auditing the webpage in the current project.

## Step 4: Run the audit

Paste the following prompt into Figma Make with the five knowledge files attached:

```text
Audit the webpage currently implemented and displayed in this Figma Make project against Design Language v1.0.1.

Audit source

- Source: Current Figma Make project and preview
- Scope: Single webpage
- Pages reviewed: Current page only
- Navigation followed: None

Use the five attached files as the authority for this audit:

1. rule-reference.md
2. website-audit.md
3. report-template.md
4. rubric.md
5. ai-tells-audit.md

Before beginning, confirm that all five files are available. If any file is missing or unreadable, stop and identify the missing file.

Run the AI writing-pattern audit mode as part of this broader webpage audit.

Always include the “Human-authorship signals” section immediately after the Summary. Provide a directional score from 0 to 10 in half-point increments, an evidence-based interpretation, the approximate number of affected sentences when reasonable, the strongest human-authorship evidence, and the strongest formulaic pattern.

Do not describe this score as a probability, percentage, detection result, or proof of who wrote the content.

Audit only.

Do not modify:

- the design
- the code
- the components
- the content
- the project files
- the published webpage

Review:

- page title
- headings
- navigation
- body copy
- links
- calls to action
- buttons
- forms
- form labels
- errors
- empty states
- captions
- accessibility
- terminology consistency
- language hierarchy
- consistency between visual and language hierarchy
- repeated formulaic writing patterns

For every finding, include:

- rule ID
- rule title
- severity
- location
- smallest useful excerpt
- plain-language meaning
- why it matters
- suggested editing direction
- whether the pattern is isolated or repeated

Use the attached rubric for scoring.

Do not follow links or audit other pages.

Do not infer content, functionality, user states, or product behavior that cannot be inspected in the current project.

If a component or state cannot be reviewed, identify it under “Not reviewed.”

Return the results using the attached report template.

Do not rewrite copy or implement changes until I review the findings and explicitly approve revisions.

Immediately after the priority list, ask exactly:

“Would you like to see the recommendations (before and after) for the priority items?”

Then stop and wait for my response. Do not include before-and-after recommendations unless I answer yes.

If I answer yes, show before-and-after recommendations for the priority items only. Treat them as previews and do not modify the project. If I answer no, end the audit without showing them.
```

## Step 5: Verify the audit scope

Before reviewing the findings, confirm that Figma Make reports:

```text
Source: Current Figma Make project and preview
Scope: Single webpage
Pages reviewed: Current page only
Navigation followed: None
```

If the audit claims to have reviewed other pages or invisible states, reject the audit and restate the scope.

## Step 6: Review the findings

Confirm that every finding includes a rule ID found in `rule-reference.md`.

Do not accept:

- Invented rule IDs
- Claims that punctuation proves AI authorship
- Findings about invisible components or states
- Recommendations that invent or change product behavior
- Automatic rewrites
- Findings without a location or excerpt

Use this prompt to challenge an unclear finding:

```text
Recheck finding [rule ID] at [location].

Show the exact rule definition, the smallest relevant excerpt, and the evidence supporting the finding.

Do not modify the project.
```

## Step 7: Approve selected changes

After reviewing the audit, identify only the findings you want Figma Make to apply.

Use a separate prompt:

```text
Apply only these approved Design Language findings:

- [Rule ID]: [location]
- [Rule ID]: [location]
- [Rule ID]: [location]

Preserve:

- the existing visual design
- layout and spacing
- component structure
- product behavior
- factual meaning
- domain terminology
- author intent

Do not apply findings that are not listed above.

After making the changes, provide a compact changelog organized by rule ID.
```

## Step 8: Re-audit the webpage

After the approved changes are applied, use:

```text
Re-audit the current webpage against the same attached Design Language files.

Scope: Current single page only.

Compare the result with the previous audit.

Do not make additional changes.

Report:

- previous score
- current score
- resolved findings
- remaining findings
- any new findings
- three highest-value remaining improvements
```

## Step 9: Record the audit

Save the following information with the project or audit report:

```text
Design Language version: 1.0.1
Repository commit: 43b8cedbea3a69100fd23469a819ed97bf3f2ded
Audit date:
Figma Make file:
Page or route:
Initial score:
Final score:
Approved findings:
Deferred findings:
```

## Optional persistent setup

Figma Make creates a `guidelines` folder for instructions that should remain available throughout a project. Files in this folder influence future Make iterations, so persistent guidance is useful when the same webpage will be audited repeatedly.

Persistent guidelines are not a replacement for the five versioned knowledge files. Use them to define **how Make should conduct an audit**, while the attached files define **which rules, reporting format, scoring rubric, and human-authorship method apply**.

### When to use persistent guidelines

Use this setup when:

- You expect to audit the same Make project more than once.
- You want Make to consistently separate auditing from editing.
- Multiple collaborators need to follow the same audit procedure.
- You want a reusable activation phrase for starting an audit.

Skip this setup when:

- You are running a one-time audit.
- The project already has extensive guidelines that may conflict with the audit instructions.
- You cannot review how the new instructions affect normal Make prompts.

### Why the audit instructions should be conditional

A permanent instruction such as “Do not modify the project” could interfere with normal requests to design or revise the webpage. The safer approach is to activate the audit protocol only when a prompt contains a specific phrase:

```text
Run Design Language audit
```

Outside that mode, Make can continue handling ordinary design and development requests.

### Step 1: Open the guidelines folder

In the Figma Make project:

1. Click **Code** at the top of Make.
2. Find and open the `guidelines` folder in the file explorer.
3. Keep the existing `guidelines.md` file if it already contains useful project instructions.
4. Create a separate file named `design-language-audit.md` in the same folder.

Using a separate file makes the audit behavior easier to review, update, or remove without disturbing the project's other guidelines.

### Step 2: Add the persistent audit protocol

Paste the following into `design-language-audit.md`:

```markdown
# Design Language audit protocol

Apply this protocol only when the user includes the exact phrase:

`Run Design Language audit`

For all other prompts, do not activate this audit protocol.

## Required audit context

Before starting an audit, confirm that these five files are available and readable:

1. `rule-reference.md`
2. `website-audit.md`
3. `report-template.md`
4. `rubric.md`
5. `ai-tells-audit.md`

Treat the attached files as the authority for rule definitions, audit procedure, report structure, and scoring.

If a required file is missing or unreadable, stop and identify it. Do not perform a partial audit.

## Audit mode

When the protocol is active:

- Audit the current webpage and visible state only.
- Do not follow links or claim to review other pages.
- Do not infer hidden states, content, functionality, or product behavior.
- Do not modify code, design, components, content, project files, or the published webpage.
- Do not rewrite copy unless the user later approves specific findings.
- Cite only rule IDs that exist in `rule-reference.md`.
- Include a precise location and the smallest useful excerpt for every finding.
- Use `rubric.md` for scoring.
- Run the AI writing-pattern mode defined in `ai-tells-audit.md` as part of every Design Language audit.
- Always include `Human-authorship signals` immediately after the Summary, with a directional score from 0 to 10 in half-point increments.
- Treat the score as an editorial signal, not a probability, percentage, detection result, or proof of authorship.
- Format the result with `report-template.md`.
- Put anything that cannot be inspected under “Not reviewed.”
- Immediately after the priority list, ask exactly: “Would you like to see the recommendations (before and after) for the priority items?”
- Stop and wait for the user's response. Do not include before-and-after recommendations unless the user answers yes.
- If the user answers yes, show before-and-after recommendations for the priority items only. These are previews, not permission to modify the project.
- If the user answers no, end the audit without showing the recommendations.

## Revision mode

Audit findings are recommendations, not approval to edit.

Apply changes only when the user explicitly lists the approved rule IDs and locations. Do not apply unlisted findings. Preserve the existing visual design, layout, component structure, product behavior, factual meaning, domain terminology, and author intent unless the user explicitly requests otherwise.
```

### Step 3: Keep the knowledge files versioned

For each audit, attach the five version-pinned files from this guide to the prompt. This preserves a record of the exact Design Language release and repository commit used.

Do not assume files in a Make project automatically synchronize with GitHub. When Design Language is updated, download and attach the new release files, then update the version and commit in the audit record.

You can upload the five knowledge files into the `guidelines` folder instead, because Figma supports multiple Markdown guideline files. However, attaching them per audit is recommended for this workflow because it makes the selected version explicit and reduces the chance of silently auditing against an outdated rule set.

### Step 4: Test the persistent setup

Attach the five knowledge files and send this small verification prompt before requesting a full audit:

```text
Run Design Language audit.

Do not begin the audit yet. Confirm:

1. The audit protocol is active.
2. All five required knowledge files are readable.
3. The Design Language version and repository commit being used.
4. The current page and visible state that will be audited.
5. That no project changes will be made during the audit.
6. That AI writing-pattern mode is active and the report will include Human-authorship signals.
```

If Make cannot confirm any item, correct the context before continuing.

### Step 5: Start the audit

Once the verification is correct, send:

```text
Run Design Language audit.

Proceed with the audit of the current webpage and visible state. Use the attached knowledge files and return the result using the attached report template. Do not modify the project.
```

### Updating or disabling the setup

- To revise the process, edit only `design-language-audit.md`.
- To update Design Language, replace the attached knowledge files and update the recorded version and commit.
- To disable the persistent audit behavior, remove `design-language-audit.md` from the `guidelines` folder.
- After any change, run the verification prompt again before auditing.

Figma recommends keeping guidelines focused because excessive or conflicting context can confuse the model. It also recommends reviewing multiple Markdown guideline files for conflicts. See [Add guidelines to Figma Make](https://help.figma.com/hc/en-us/articles/33665861260823-Add-guidelines-to-Figma-Make) for Figma's current setup instructions.

## Share feedback

When testing this workflow, record:

- Whether Figma Make read all five files
- Whether it modified the project during the audit
- Whether it respected the single-page scope
- Whether all cited rule IDs were valid
- Whether the score followed the rubric
- Which findings were useful
- Which findings were incorrect, incomplete, or too strict
- Whether the second audit recognized the approved changes

This feedback can guide improvements to the Figma Make adapter and future Design Language releases.
