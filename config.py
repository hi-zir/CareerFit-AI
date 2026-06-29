from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def validate_config():
    """
    Checks whether required environment variables are available.

    Returns:
        list[str]: A list of missing or invalid configuration messages.
    """
    errors = []

    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_api_key_here":
        errors.append("OPENAI_API_KEY is missing or not set correctly in .env")

    if not OPENAI_MODEL:
        errors.append("OPENAI_MODEL is missing in .env")

    return errors