from fastapi import FastAPI


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