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

* Python application structure
* OpenAI API integration
* Prompt engineering
* Resume/job description analysis
* File-based input and output workflow
* CLI argument handling
* FastAPI backend development
* API request and response validation
* Unit testing with mocks
* GitHub Actions automated testing
* Git and GitHub project organization

## Project Structure

```text
CareerFit-AI/
├── app.py
├── config.py
├── prompts.py
├── requirements.txt
├── README.md
├── AGENTS.md
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── data/
│   ├── sample_resume.txt
│   └── sample_job_description.txt
├── services/
│   ├── openai_service.py
│   └── resume_matcher.py
├── tests/
│   ├── test_api.py
│   ├── test_app_workflow.py
│   ├── test_core.py
│   └── test_schemas.py
└── outputs/
    └── .gitkeep
```

## How It Works

CareerFit AI has two entry points:

1. A command-line interface
2. A FastAPI backend API

Both use the same core resume matching service.

The application compares resume text against job description text, sends both to an AI analysis workflow, and generates a CareerFit AI Match Report.

The report includes a match score, strong matches, missing skills, keyword gaps, tailored resume bullet suggestions, and interview prep questions.

## Setup

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```

You can use `.env.example` as a template.

## Run the CLI App

Run with the default sample files:

```bash
python app.py
```

Run with custom input and output files:

```bash
python app.py --resume data/sample_resume.txt --job data/sample_job_description.txt --output outputs/custom_report.md
```

Show CLI help:

```bash
python app.py --help
```

The CLI version prints the report in the terminal and saves it as a Markdown file.

Default output path:

```text
outputs/careerfit_match_report.md
```

## Run the FastAPI Backend

Start the API server:

```bash
uvicorn api.main:app --reload
```

Open the API in your browser:

```text
http://127.0.0.1:8000
```

Open the interactive API docs:

```text
http://127.0.0.1:8000/docs
```

The API currently includes:

```text
GET /          Health check endpoint
POST /analyze  Analyze resume text against job description text
```

Example `POST /analyze` request body:

```json
{
  "resume_text": "Big Data Software Engineer with Python, SQL, Spark, and ETL experience.",
  "job_description_text": "We are hiring an AI Backend Engineer with Python, REST APIs, SQL, cloud, and machine learning basics."
}
```

Example `POST /analyze` response body:

{
  "report": "# CareerFit AI Match Report...",
  "summary": "CareerFit AI analysis completed successfully.",
  "match_score": null
}

## Run Tests

Run all tests:

```bash
python -m unittest discover -s tests -v
```

The tests use Python's built-in `unittest` library.

The workflow and API tests use mocks so they do not call the OpenAI API.

## GitHub Actions

This project includes a GitHub Actions workflow that automatically runs the test suite when code is pushed to the `main` branch or when a pull request targets `main`.

Workflow file:

```text
.github/workflows/tests.yml
```

## Prompt Safety

CareerFit AI is designed to avoid inventing resume details.

The prompt tells the model:

* Do not invent skills.
* Do not invent metrics, percentages, project scale, or business impact.
* Do not claim tools, APIs, cloud platforms, or AI/ML experience unless supported by the resume.
* Use conditional suggestions under "Only Add If True."

## Current Version

This version includes:

* CLI resume/job matching
* FastAPI backend
* OpenAI API integration
* Request and response schemas
* Friendly CLI error handling
* API validation
* API error handling
* Unit tests
* Mock-based tests
* GitHub Actions automated tests

Future improvements may include:

* Structured JSON report output
* Streamlit or React frontend
* Resume upload support
* Job description paste/upload support
* PDF and DOCX parsing
* Better scoring logic
* Saved report history

## Skills Demonstrated

* Python
* OpenAI API
* Prompt engineering
* CLI development with argparse
* FastAPI backend development
* Pydantic request and response models
* Backend-style service architecture
* Environment variable management
* Unit testing
* Mocking external AI calls
* GitHub Actions
* Git version control
* Markdown report generation
