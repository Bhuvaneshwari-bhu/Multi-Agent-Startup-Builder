from supervisors.startup_supervisor import startup_supervisor


def main():

    print("=" * 50)
    print("AI Startup Builder")
    print("=" * 50)

    startup_idea = input("\nEnter Startup Idea: ")

    state = startup_supervisor(startup_idea)

    print("\n" + "=" * 50)
    print("STARTUP ANALYSIS REPORT")
    print("=" * 50)

    print("\n[BUSINESS]")
    print(state["business_report"])

    print("\n[COMPETITORS]")
    print(state["competitor_report"])

    print("\n[MARKET]")
    print(state["market_report"])

    print("\n[FINANCE]")
    print(state["finance_report"])

    print("\n" + "=" * 50)
    print("Analysis Complete")
    print("=" * 50)


if __name__ == "__main__":
    main()