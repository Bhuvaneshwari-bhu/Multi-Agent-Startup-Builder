import json


def safe_json(response, default_data):
    """
    Safely converts a JSON string into a Python dictionary.
    Returns default_data if parsing fails.
    """

    try:

        if isinstance(response, dict):
            return response

        return json.loads(response)

    except Exception:

        return default_data


def clean_text(response, default_text="Analysis unavailable."):
    """
    Returns cleaned text output.
    """

    if not response:
        return default_text

    response = str(response).strip()

    if response == "":
        return default_text

    return response


def print_header(title):
    """
    Prints a formatted console section.
    """

    print("\n" + "=" * 50)
    print(title.upper())
    print("=" * 50)


def success(message):
    """
    Success message.
    """

    print(f"✓ {message}")


def failure(message):
    """
    Failure message.
    """

    print(f"✗ {message}")