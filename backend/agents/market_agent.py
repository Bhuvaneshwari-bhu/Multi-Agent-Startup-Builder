import json

from utils.gemini_helper import ask_gemini


def market_agent(state):

    prompt = f"""
You are a startup market analyst.

Startup Idea:
{state["startup_idea"]}

Business Analysis:
{state["business_report"]}

Competitor Analysis:
{state["competitor_report"]}

Return ONLY this JSON:

{{
    "competition": "Low|Medium|High",
    "demand": "Low|Medium|High",
    "opportunity": "one sentence",
    "risk": "one sentence"
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

        state["market_report"] = {
            "competition": str(
                data.get("competition", "Unknown")
            ).strip(),

            "demand": str(
                data.get("demand", "Unknown")
            ).strip(),

            "opportunity": str(
                data.get("opportunity", "Unavailable")
            ).strip(),

            "risk": str(
                data.get("risk", "Unavailable")
            ).strip(),
        }

    except Exception as e:

        print("Market Agent Failed:", e)

        state["market_report"] = {
            "competition": "Unknown",
            "demand": "Unknown",
            "opportunity": "Analysis unavailable",
            "risk": "Analysis unavailable",
        }

    return state