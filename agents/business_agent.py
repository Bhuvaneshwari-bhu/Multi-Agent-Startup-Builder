from utils.gemini_helper import ask_gemini


def business_agent(state):

    prompt = f"""
You are a startup business analyst.

Startup Idea:
{state["startup_idea"]}

Return ONLY:

Business Type: <one line>

Target Audience: <one line>

Value Proposition: <one line>

Rules:
- Keep total response under 50 words.
- No markdown.
- No explanation.
- No bullet points.
"""

    try:
        state["business_report"] = ask_gemini(prompt)

    except Exception as e:

        print("Business Agent Failed:", e)

        state["business_report"] = """
Business Type: Unknown
Target Audience: Unknown
Value Proposition: Analysis unavailable
"""

    return state