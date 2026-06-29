from prompts import build_resume_match_prompt
from services.openai_service import ask_ai


def analyze_resume_match(resume_text, job_description_text):
    """
    Analyzes how well a resume matches a job description.

    Args:
        resume_text (str): The candidate's resume content.
        job_description_text (str): The target job description.

    Returns:
        str: The AI-generated resume match report.

    Raises:
        ValueError: If resume text or job description text is empty.
    """
    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description_text.strip():
        raise ValueError("Job description text cannot be empty.")

    prompt = build_resume_match_prompt(
        resume_text=resume_text,
        job_description_text=job_description_text,
    )

    return ask_ai(prompt)