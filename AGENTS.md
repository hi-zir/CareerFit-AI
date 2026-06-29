# CareerFit AI - Codex Instructions

This project is a learning-focused AI portfolio project.

## Project Goal

CareerFit AI compares a resume against a job description and generates:

1. Match score
2. Strong matches
3. Missing skills
4. Resume keyword gaps
5. Tailored resume bullet suggestions
6. Interview prep questions

## Developer Learning Preference

The developer wants to learn while building.

When helping:

- Explain changes before making them.
- Prefer small, focused changes.
- Do not rewrite large parts of the project unless explicitly asked.
- Do not hide complexity.
- Explain important Python code clearly.
- Keep the existing simple architecture unless there is a strong reason to change it.

## Safety Rules

Do not modify these files:

- .env
- .venv/
- outputs/careerfit_match_report.md

Do not expose or print API keys.

Do not install new packages unless explicitly asked.

Do not make Git commits automatically.

After making changes, summarize:

1. Which files changed
2. Why they changed
3. How to test the change
4. Any risks or assumptions

## Current Architecture

- app.py runs the CLI workflow.
- config.py loads environment variables.
- prompts.py builds the AI prompt.
- services/openai_service.py sends prompts to OpenAI.
- services/resume_matcher.py connects prompt building with OpenAI analysis.
- data/ contains sample input files.
- outputs/ contains generated reports.
