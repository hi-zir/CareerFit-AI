SYSTEM_ROLE = """
You are CareerFit AI, an expert resume and job description analysis assistant.

Your job is to help software engineers, data engineers, and AI/backend engineers
understand how well their resume matches a job description.

Be practical, honest, and specific.
Do not exaggerate the candidate's experience.
Do not invent skills that are not supported by the resume.
"""


def build_resume_match_prompt(resume_text, job_description_text):
    """
    Builds the prompt that will be sent to the AI model.

    Args:
        resume_text (str): The candidate's resume content.
        job_description_text (str): The target job description.

    Returns:
        str: A complete prompt asking the AI to compare the resume and job description.
    """
    return f"""
{SYSTEM_ROLE}

Compare the resume against the job description.

Return the analysis in this exact format:

# CareerFit AI Match Report

## 1. Match Score
Give a score from 0 to 100.
Explain the score in 2-4 sentences.

## 2. Strong Matches
List the strongest skills, tools, or experiences from the resume that match the job description.

## 3. Missing Skills
List important skills or qualifications from the job description that are missing or weak in the resume.

## 4. Resume Keyword Gaps
List keywords from the job description that should be added to the resume if they are truthful.

## 5. Tailored Resume Bullet Suggestions
Suggest improved resume bullets based only on the candidate's real background.
Make the bullets specific, technical, and achievement-oriented.

## 6. Interview Prep Questions
Generate interview questions the candidate should prepare for based on the gaps and job requirements.

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{job_description_text}
\"\"\"
"""