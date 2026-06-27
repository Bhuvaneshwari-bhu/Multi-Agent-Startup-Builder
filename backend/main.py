from supervisors.startup_supervisor import startup_supervisor
from utils.pdf_generator import generate_pdf


LINE = "=" * 60


def print_section(title):
    print(f"\n{LINE}")
    print(title)
    print(LINE)


def print_competitor_report(report):

    if isinstance(report, dict):

        print("Summary:")
        print(report.get("summary", "N/A"))

        print("\nTop Competitors:")

        competitors = report.get("key_points", [])

        if competitors:
            for competitor in competitors:
                print(f"• {competitor}")
        else:
            print("N/A")

        print("\nRisk / Notes:")
        print(report.get("risk_or_notes", "N/A"))

    else:
        print(report)


def main():

    print(LINE)
    print("🚀 AI Startup Builder")
    print(LINE)

    startup_idea = input("\nEnter Startup Idea: ").strip()

    if not startup_idea:
        print("\nStartup idea cannot be empty.")
        return

    state = startup_supervisor(startup_idea)

    print_section("STARTUP ANALYSIS REPORT")

    print("\n[BUSINESS]")
    print(state.get("business_report", "N/A"))

    print("\n[COMPETITORS]")
    print_competitor_report(state.get("competitor_report", {}))

    print("\n[MARKET]")
    print(state.get("market_report", "N/A"))

    print("\n[FINANCE]")
    print(state.get("finance_report", "N/A"))

    print("\n[SWOT]")
    print(state.get("swot_report", "N/A"))

    print("\n[PITCH]")
    print(state.get("pitch_report", "N/A"))

    print("\n[ROADMAP]")
    print(state.get("roadmap_report", "N/A"))

    print_section("EXECUTION SUMMARY")

    metadata = state.get("metadata", {})

    print(f"Generated At   : {metadata.get('generated_at', 'N/A')}")
    print(f"Agents Run     : {metadata.get('agents_executed', 0)}")
    print(f"Execution Time : {metadata.get('total_execution_time', 0)} sec")

    print("\nAgent Status")

    statuses = state.get("agent_status", {})
    timings = state.get("agent_execution_time", {})

    if statuses:
        for agent in statuses:
            status = statuses.get(agent, "Unknown")
            timing = timings.get(agent, "-")
            print(f"{agent:<12} {status:<10} {timing}s")

    generate_pdf(state)

    print("\nPDF Generated Successfully")
    print("reports/startup_report.pdf")

    print("\n" + LINE)
    print("Analysis Complete")
    print(LINE)


if __name__ == "__main__":
    main()