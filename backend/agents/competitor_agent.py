import json

from utils.web_search import search_competitors
from utils.gemini_helper import ask_gemini


def competitor_agent(state):

    competitors = search_competitors(state["startup_idea"])

    if not competitors:
        competitors = "No competitors found."

    prompt = f"""
You are a startup competitor analyst.

Startup Idea:
{state["startup_idea"]}

Web Search Results:
{competitors}

Return ONLY this JSON:

{{
    "summary": "one line",
    "top_competitors": [
        "competitor1",
        "competitor2",
        "competitor3"
    ],
    "market_gap": "one line",
    "risk": "one line"
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

        top_competitors = data.get("top_competitors", [])

        if not isinstance(top_competitors, list):
            top_competitors = []

        state["competitor_report"] = {
            "summary": str(data.get("summary", "Unavailable")).strip(),
            "top_competitors": [
                str(c).strip()
                for c in top_competitors[:3]
            ],
            "market_gap": str(
                data.get("market_gap", "Unavailable")
            ).strip(),
            "risk": str(
                data.get("risk", "Unavailable")
            ).strip(),
        }

    except Exception as e:

        print("Competitor Agent Failed:", e)

        state["competitor_report"] = {
            "summary": "Analysis unavailable",
            "top_competitors": [],
            "market_gap": "Unknown",
            "risk": "Unknown",
        }

    return state