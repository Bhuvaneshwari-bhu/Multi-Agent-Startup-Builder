import json

from utils.gemini_helper import ask_gemini


def business_agent(state):

    prompt = f"""
You are a startup business analyst.

Startup Idea:
{state["startup_idea"]}

Return ONLY this JSON:

{{
    "business_type":"one line",
    "target_audience":"one line",
    "value_proposition":"one line"
}}

Rules:
- Return valid JSON only.
- No markdown.
- No explanations.
- Maximum 50 words.
"""

    try:

        response = ask_gemini(prompt)

        data = json.loads(response)

        state["business_report"] = {
            "business_type": str(
                data.get("business_type", "Unknown")
            ).strip(),

            "target_audience": str(
                data.get("target_audience", "Unknown")
            ).strip(),

            "value_proposition": str(
                data.get("value_proposition", "Analysis unavailable")
            ).strip(),
        }

    except Exception as e:

        print("Business Agent Failed:", e)

        state["business_report"] = {
            "business_type": "Unknown",
            "target_audience": "Unknown",
            "value_proposition": "Analysis unavailable",
        }

    return state