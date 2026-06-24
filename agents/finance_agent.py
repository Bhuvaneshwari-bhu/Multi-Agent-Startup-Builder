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

Return ONLY:

Startup Cost: Low/Medium/High

Revenue Model:
<one line>

Break-even:
<one line>

Scalability: Low/Medium/High

Rules:
- Maximum 50 words
- No markdown
- No bullet points
- No explanation
"""

    try:

        state["finance_report"] = ask_gemini(prompt)

    except Exception as e:

        print("Finance Agent Failed:", e)

        state["finance_report"] = """
Startup Cost: Unknown

Revenue Model:
Analysis unavailable

Break-even:
Unknown

Scalability:
Unknown
"""

    return state