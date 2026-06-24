import json
from utils.gemini_helper import ask_gemini


def planner_agent(state):

    prompt = f"""
You are a Startup Planning Agent.

Startup Idea:
{state["startup_idea"]}

Available Agents:

business
competitor
market
finance

Choose the agents required to analyze this startup.

Return ONLY a JSON list.

Example:
["business","competitor","market","finance"]

No explanation.
"""

    try:

        response = ask_gemini(prompt)

        plan = json.loads(response)

        if not isinstance(plan, list):
            raise ValueError("Plan must be a list")

        state["execution_plan"] = [
            agent.strip().lower()
            for agent in plan
        ]

    except Exception as e:

        print("Planner Agent Failed:", e)

        state["execution_plan"] = [
            "business",
            "competitor",
            "market",
            "finance"
        ]

    return state