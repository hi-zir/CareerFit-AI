from typing import Optional

from pydantic import BaseModel, Field


class ResumeMatchRequest(BaseModel):
    """
    Request body for resume and job description analysis.

    This model validates the text that the API receives from the user.
    Both fields are required and must contain at least one character.
    """

    resume_text: str = Field(
        ...,
        min_length=1,
        description="The candidate's resume text.",
    )

    job_description_text: str = Field(
        ...,
        min_length=1,
        description="The target job description text.",
    )


class ResumeMatchResponse(BaseModel):
    """
    Response body for resume and job description analysis.

    match_score is optional for now because the current AI workflow returns
    a Markdown report. A future version can extract or generate this score
    as structured data.
    """
    report_id: str = Field(
        ...,
        description="Unique identifier for this analysis report.",
    )

    report: str = Field(
        ...,
        description="The generated CareerFit AI match report.",
    )

    summary: str = Field(
        ...,
        description="Short summary of the analysis result.",
    )

    match_score: Optional[int] = Field(
        default=None,
        ge=0,
        le=100,
        description="Optional resume/job match score from 0 to 100.",
    )