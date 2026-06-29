from fastapi import FastAPI, HTTPException
from api.schemas import ResumeMatchRequest, ResumeMatchResponse
from services.resume_matcher import analyze_resume_match


app = FastAPI(
    title="CareerFit AI API",
    description="AI Resume and Job Match Assistant API",
    version="2.0.0",
)


@app.get("/")
def root():
    """
    Health check endpoint for the CareerFit AI API.

    Returns:
        dict: Basic API status information.
    """
    return {
        "app": "CareerFit AI",
        "version": "v2",
        "status": "running",
    }

@app.get("/health")
def health_check():
    """
    Health check endpoint for monitoring the API.

    Returns:
        dict: API health status.
    """
    return {
        "status": "healthy",
        "service": "CareerFit AI API",
    }

@app.post("/analyze", response_model=ResumeMatchResponse)
def analyze_resume(request: ResumeMatchRequest):
    """
    Analyzes resume text against job description text.

    Args:
        request (ResumeMatchRequest): Resume and job description input text.

    Returns:
        ResumeMatchResponse: The generated CareerFit AI match report.
    """
    try:
        report = analyze_resume_match(
            resume_text=request.resume_text,
            job_description_text=request.job_description_text,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return ResumeMatchResponse(report=report)