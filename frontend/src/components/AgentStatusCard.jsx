import AnalysisCard from "./AnalysisCard";

function AgentStatusCard({ status }) {

    if (!status) return null;

    return (

        <AnalysisCard title="🤖 Agent Status">

            <div className="grid md:grid-cols-2 gap-4">

                {Object.entries(status).map(([agent, value]) => (

                    <div
                        key={agent}
                        className="
                            flex
                            justify-between
                            items-center
                            bg-slate-50
                            border
                            rounded-xl
                            p-4
                            shadow-sm
                        "
                    >

                        <span className="capitalize font-semibold">

                            {agent}

                        </span>

                        <span
                            className={`
                                px-3
                                py-1
                                rounded-full
                                text-sm
                                font-semibold
                                ${
                                    value === "Success"
                                        ? "bg-green-100 text-green-700"
                                        : "bg-red-100 text-red-700"
                                }
                            `}
                        >

                            {value === "Success"
                                ? " Success"
                                : " Failed"}

                        </span>

                    </div>

                ))}

            </div>

        </AnalysisCard>

    );

}

export default AgentStatusCard;