import time
from config.gemini import client


def ask_gemini(prompt):

    models = [
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash"
    ]

    for model_name in models:

        for attempt in range(2):

            try:

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                if response.text:
                    return response.text.strip()

            except Exception as e:

                print(
                    f"{model_name} failed "
                    f"(attempt {attempt + 1})"
                )

                time.sleep(2)

    return "Service temporarily unavailable."