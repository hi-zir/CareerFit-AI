from pydantic import BaseModel, Field


class ResumeMatchRequest(BaseModel):
    """
    Request body for resume and job description analysis.
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
    """

    report: str = Field(
        ...,
        description="The generated CareerFit AI match report.",
    )