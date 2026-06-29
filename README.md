# CareerFit AI

CareerFit AI is an AI-powered resume and job description matching assistant.

It helps software engineers, data engineers, and AI/backend engineering candidates compare a resume against a job description and generate a practical career-readiness report.

## Features

CareerFit AI generates:

1. Match score
2. Strong resume/job matches
3. Missing skills
4. Resume keyword gaps
5. Tailored resume bullet suggestions
6. Interview prep questions

## Why I Built This

I built this project as part of my transition from Big Data Software Engineering into AI and Backend Engineering.

The goal is to practice real-world AI application development while building a useful portfolio project that demonstrates:

- Python application structure
- OpenAI API integration
- Prompt engineering
- Resume/job description analysis
- File-based input and output workflow
- Git and GitHub project organization

## Project Structure

```text
CareerFit-AI/
├── app.py
├── config.py
├── prompts.py
├── requirements.txt
├── README.md
├── data/
│   ├── sample_resume.txt
│   └── sample_job_description.txt
├── services/
│   ├── openai_service.py
│   └── resume_matcher.py
└── outputs/
    └── .gitkeep