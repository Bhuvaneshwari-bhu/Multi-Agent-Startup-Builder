import AnalysisCard from "./AnalysisCard";

function RoadmapCard({ roadmap }) {

    if (!roadmap || typeof roadmap !== "object") return null;

    return (

        <AnalysisCard title="🗺️ 90-Day Roadmap">

            <div className="space-y-5">

                <div>
                    <p className="font-semibold text-indigo-600">Month 1</p>
                    <p>{roadmap.month_1}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Month 2</p>
                    <p>{roadmap.month_2}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Month 3</p>
                    <p>{roadmap.month_3}</p>
                </div>

                <div>
                    <p className="font-semibold text-green-600">Goal</p>
                    <p>{roadmap.goal}</p>
                </div>

            </div>

        </AnalysisCard>

    );

}

export default RoadmapCard;