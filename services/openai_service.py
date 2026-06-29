from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL, validate_config


def create_openai_client():
    """
    Creates and returns an OpenAI client.

    Returns:
        OpenAI: A configured OpenAI client.

    Raises:
        ValueError: If required configuration is missing.
    """
    config_errors = validate_config()

    if config_errors:
        raise ValueError("Invalid configuration: " + "; ".join(config_errors))

    return OpenAI(api_key=OPENAI_API_KEY)


def ask_ai(prompt):
    """
    Sends a prompt to the OpenAI model and returns the model's text response.

    Args:
        prompt (str): The instruction or question we want to send to the AI.

    Returns:
        str: The AI-generated response text.

    Raises:
        ValueError: If required configuration is missing.
    """
    client = create_openai_client()

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )

    return response.output_text