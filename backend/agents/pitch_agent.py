import json

from utils.gemini_helper import ask_gemini


def pitch_agent(state):

    prompt = f"""
You are a startup investor.

Startup Idea:
{state["startup_idea"]}

Business Analysis:
{state["business_report"]}

Market Analysis:
{state["market_report"]}

Finance Analysis:
{state["finance_report"]}

Return ONLY this JSON:

{{
    "problem": "one sentence",
    "solution": "one sentence",
    "business_model": "one sentence",
    "why_now": "one sentence"
}}

Rules:
- Return valid JSON only.
- No markdown.
- No explanations.
- Maximum 60 words.
"""

    try:

        response = ask_gemini(prompt)

        data = json.loads(response)

        state["pitch_report"] = {
            "problem": str(
                data.get("problem", "Unknown")
            ).strip(),

            "solution": str(
                data.get("solution", "Unknown")
            ).strip(),

            "business_model": str(
                data.get("business_model", "Unknown")
            ).strip(),

            "why_now": str(
                data.get("why_now", "Unknown")
            ).strip(),
        }

    except Exception as e:

        print("Pitch Agent Failed:", e)

        state["pitch_report"] = {
            "problem": "Analysis unavailable",
            "solution": "Analysis unavailable",
            "business_model": "Analysis unavailable",
            "why_now": "Analysis unavailable",
        }

    return state