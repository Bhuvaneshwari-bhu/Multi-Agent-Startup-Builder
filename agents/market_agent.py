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

Return ONLY:

Competition: Low/Medium/High

Demand: Low/Medium/High

Opportunity:
<one sentence>

Risk:
<one sentence>

Rules:
- Maximum 50 words.
- No markdown.
- No bullet points.
- No explanation.
"""

    try:
        state["market_report"] = ask_gemini(prompt)

    except Exception as e:

        print("Market Agent Failed:", e)

        state["market_report"] = """
Competition: Unknown

Demand: Unknown

Opportunity:
Analysis unavailable

Risk:
Analysis unavailable
"""

    return state