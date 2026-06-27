from datetime import datetime
import time

from agents.planner_agent import planner_agent
from agents.business_agent import business_agent
from agents.competitor_agent import competitor_agent
from agents.market_agent import market_agent
from agents.finance_agent import finance_agent
from agents.swot_agent import swot_agent
from agents.pitch_agent import pitch_agent
from agents.roadmap_agent import roadmap_agent


def startup_supervisor(startup_idea):

    state = {
        "startup_idea": startup_idea,
        "execution_plan": [],

        "business_report": "Analysis unavailable.",
        "competitor_report": "Analysis unavailable.",
        "market_report": "Analysis unavailable.",
        "finance_report": "Analysis unavailable.",
        "swot_report": "Analysis unavailable.",
        "pitch_report": "Analysis unavailable.",
        "roadmap_report": "Analysis unavailable.",

        "agent_status": {},
        "agent_execution_time": {},
        "metadata": {}
    }

    total_start = time.time()

    state = planner_agent(state)

    print("\nExecution Plan:")

    if state["execution_plan"]:
        print(" -> ".join(state["execution_plan"]))
    else:
        print("No execution plan generated")

    agent_map = {
        "business": business_agent,
        "competitor": competitor_agent,
        "market": market_agent,
        "finance": finance_agent,
        "swot": swot_agent,
        "pitch": pitch_agent,
        "roadmap": roadmap_agent,
    }

    for agent_name in state["execution_plan"]:

        if agent_name not in agent_map:
            continue

        start = time.time()

        try:

            state = agent_map[agent_name](state)

            elapsed = round(time.time() - start, 2)

            state["agent_status"][agent_name] = "Success"
            state["agent_execution_time"][agent_name] = elapsed

            print(f"✅ {agent_name.title()} Agent ({elapsed}s)")

        except Exception as e:

            elapsed = round(time.time() - start, 2)

            state["agent_status"][agent_name] = "Failed"
            state["agent_execution_time"][agent_name] = elapsed

            print(f"❌ {agent_name.title()} Agent Failed")
            print(e)

    state["metadata"] = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "agents_executed": len(state.get("execution_plan", [])),
        "total_execution_time": round(
            time.time() - total_start,
            2
        ),
    }

    return state