import re
import time

from config.gemini import client
from config.settings import GEMINI_MODELS, MAX_RETRIES, RETRY_DELAY


def clean_response(text: str) -> str:
    """
    Remove markdown code fences and surrounding whitespace.
    """

    text = text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text.strip()


def extract_json(text: str) -> str:
    """
    Extract the first JSON object or array from Gemini output.
    Returns the original cleaned text if no JSON is found.
    """

    text = clean_response(text)

    object_match = re.search(r"\{.*\}", text, re.DOTALL)

    if object_match:
        return object_match.group()

    array_match = re.search(r"\[.*\]", text, re.DOTALL)

    if array_match:
        return array_match.group()

    return text


def ask_gemini(prompt: str) -> str:
    """
    Query Gemini models in priority order with retries.
    Returns cleaned text/JSON.
    Never raises an exception.
    """

    for model in GEMINI_MODELS:

        for attempt in range(MAX_RETRIES):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if not getattr(response, "text", None):
                    continue

                return extract_json(response.text)

            except Exception:

                print(
                    f"{model} failed "
                    f"(attempt {attempt + 1})"
                )

                time.sleep(RETRY_DELAY * (attempt + 1))

    return "Service temporarily unavailable."