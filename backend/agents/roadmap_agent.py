import json

from utils.gemini_helper import ask_gemini


def roadmap_agent(state):

    prompt = f"""
You are a startup growth advisor.

Startup Idea:
{state["startup_idea"]}

Create a practical 90-day execution roadmap.

Return ONLY this JSON:

{{
    "month_1":"one sentence",
    "month_2":"one sentence",
    "month_3":"one sentence",
    "goal":"one sentence"
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

        state["roadmap_report"] = {
            "month_1": str(
                data.get("month_1", "Unknown")
            ).strip(),

            "month_2": str(
                data.get("month_2", "Unknown")
            ).strip(),

            "month_3": str(
                data.get("month_3", "Unknown")
            ).strip(),

            "goal": str(
                data.get("goal", "Unknown")
            ).strip(),
        }

    except Exception as e:

        print("Roadmap Agent Failed:", e)

        state["roadmap_report"] = {
            "month_1": "Validate startup idea",
            "month_2": "Build MVP",
            "month_3": "Acquire early users",
            "goal": "Achieve product-market fit",
        }

    return state