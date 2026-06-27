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
swot
pitch
roadmap

Select the minimum required agents.

At least one agent must be selected.

Rules:
IMPORTANT:
- Return ONLY valid JSON.
- Do not wrap the JSON in ```json.
- Do not include explanations.
- Do not include markdown.
- Output must be parseable using Python json.loads().

Example:
["business","competitor","market","finance","swot","pitch","roadmap"]
"""

    try:

        response = ask_gemini(prompt)

        plan = json.loads(response)

        if not isinstance(plan, list):
            raise ValueError("Plan must be a list")

        valid_agents = {
            "business",
            "competitor",
            "market",
            "finance",
            "swot",
            "pitch",
            "roadmap"
        }

        execution_plan = list(dict.fromkeys(
            agent.strip().lower()
            for agent in plan
            if agent.strip().lower() in valid_agents
        ))

        if not execution_plan:
            raise ValueError("Empty execution plan")

        # Fixed execution order
        ordered_agents = [
            "business",
            "competitor",
            "market",
            "finance",
            "swot",
            "pitch",
            "roadmap"
        ]

        state["execution_plan"] = [
            agent
            for agent in ordered_agents
            if agent in execution_plan
        ]

    except Exception as e:

        print("Planner Agent Failed:", e)

        state["execution_plan"] = [
            "business",
            "competitor",
            "market",
            "finance",
            "swot",
            "pitch",
            "roadmap"
        ]

    return state