import json

from utils.gemini_helper import ask_gemini


def finance_agent(state):

    prompt = f"""
You are a startup finance analyst.

Startup Idea:
{state["startup_idea"]}

Business Analysis:
{state["business_report"]}

Market Analysis:
{state["market_report"]}

Return ONLY this JSON:

{{
    "startup_cost": "Low|Medium|High",
    "revenue_model": "one line",
    "break_even": "one line",
    "scalability": "Low|Medium|High"
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

        state["finance_report"] = {
            "startup_cost": str(
                data.get("startup_cost", "Unknown")
            ).strip(),

            "revenue_model": str(
                data.get("revenue_model", "Unavailable")
            ).strip(),

            "break_even": str(
                data.get("break_even", "Unknown")
            ).strip(),

            "scalability": str(
                data.get("scalability", "Unknown")
            ).strip(),
        }

    except Exception as e:

        print("Finance Agent Failed:", e)

        state["finance_report"] = {
            "startup_cost": "Unknown",
            "revenue_model": "Analysis unavailable",
            "break_even": "Unknown",
            "scalability": "Unknown",
        }

    return state