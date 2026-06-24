from utils.gemini_helper import ask_gemini


def competitor_agent(state):

    prompt = f"""
You are a startup competitor analyst.

Startup Idea:
{state["startup_idea"]}

Return ONLY:

Top Competitors:
1. <competitor>
2. <competitor>
3. <competitor>

Advantage:
<one sentence>

Rules:
- Maximum 50 words.
- No markdown.
- No explanation.
- No extra text.
"""

    try:
        state["competitor_report"] = ask_gemini(prompt)

    except Exception as e:

        print("Competitor Agent Failed:", e)

        state["competitor_report"] = """
Top Competitors:
1. Unknown
2. Unknown
3. Unknown

Advantage:
Analysis unavailable
"""

    return state