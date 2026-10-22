# Repository maintenance guide

This repository documents actual daily cybersecurity internship activities for UniKL. If an AI assistant, script, or contributor updates it, follow these rules.

## Daily entry requirements

1. Use the actual work date, `YYYY-MM-DD`, and a zero-padded sequential day number only for logged days. Never assume work occurred on weekends or holidays.
2. Preserve the UniKL form fields in order: **Title**, **Descriptions of Jobs/Tasks/Project**, **Activities/Work Produced**, **Comments/Conclusion**.
3. Write one concise, professional **paragraph**, not bullet points, for each section. A short title may be one line.
4. Preserve evidence limits: never invent test results, completed labs, report approvals, remediation successes, or tools that were not mentioned.
5. Clearly distinguish self-study, supervised work, and delivered outputs. Use terms such as *reviewed*, *studied*, *assisted*, *performed retesting*, and *formatted* where accurate.
6. Omit client names, real assets and endpoints, credentials, unredacted screenshots, internal work product, or confidential findings unless expressly cleared by authorized stakeholders; default to omission.
7. Use neutral, professional English. Keep cybersecurity terminology precise: a missing `Content-Security-Policy` HTTP response header is a header configuration issue, not a missing protocol.
8. For a new daily entry, create `logbook/YYYY/MM-month-name/YYYY-MM-DD-day-NN.md` and update the month README, year README, root README, links, counts, and date ranges in the same change.
9. Verify markdown paths and dates using `python3 scripts/validate_logbook.py`; inspect the rendered GitHub Markdown when possible.
10. This repository is **public**. Publish only high-level, anonymized learning and internship summaries; omit any material not cleared for external sharing.

## Formatting

- Keep paragraphs short and avoid marketing language, exaggerated conclusions, and decorative elements inside the actual UniKL form sections.
- Emojis and custom SVGs are welcome in README navigation and entry headings, but do not distract from professional logbook content.
- Use the provided template and consistent prev/next navigation.
- Do not retrospectively change work descriptions unless correcting factual errors with the user's input.

## Update behavior

The journal is updated when the user submits a new daily entry and the GitHub connection is available. This is not a continuous background synchronization service. If GitHub writes fail, say so and preserve the new content without claiming it was committed.
