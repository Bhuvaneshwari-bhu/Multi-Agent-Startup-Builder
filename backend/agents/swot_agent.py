import json

from utils.gemini_helper import ask_gemini


def swot_agent(state):

    prompt = f"""
You are a startup strategy expert.

Startup Idea:
{state["startup_idea"]}

Business Analysis:
{state["business_report"]}

Competitor Analysis:
{state["competitor_report"]}

Market Analysis:
{state["market_report"]}

Finance Analysis:
{state["finance_report"]}

Return ONLY this JSON:

{{
    "strength": "one sentence",
    "weakness": "one sentence",
    "opportunity": "one sentence",
    "threat": "one sentence"
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

        state["swot_report"] = {
            "strength": str(
                data.get("strength", "Unknown")
            ).strip(),

            "weakness": str(
                data.get("weakness", "Unknown")
            ).strip(),

            "opportunity": str(
                data.get("opportunity", "Unknown")
            ).strip(),

            "threat": str(
                data.get("threat", "Unknown")
            ).strip(),
        }

    except Exception as e:

        print("SWOT Agent Failed:", e)

        state["swot_report"] = {
            "strength": "Analysis unavailable",
            "weakness": "Analysis unavailable",
            "opportunity": "Analysis unavailable",
            "threat": "Analysis unavailable",
        }

    return state