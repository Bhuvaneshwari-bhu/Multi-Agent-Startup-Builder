import AnalysisCard from "./AnalysisCard";

function SwotCard({ swot }) {

    if (!swot || typeof swot !== "object") return null;

    return (

        <AnalysisCard title="🎯 SWOT Analysis">

            <div className="grid md:grid-cols-2 gap-6">

                <div>
                    <p className="font-bold text-green-600">Strength</p>
                    <p>{swot.strength}</p>
                </div>

                <div>
                    <p className="font-bold text-red-600">Weakness</p>
                    <p>{swot.weakness}</p>
                </div>

                <div>
                    <p className="font-bold text-blue-600">Opportunity</p>
                    <p>{swot.opportunity}</p>
                </div>

                <div>
                    <p className="font-bold text-orange-600">Threat</p>
                    <p>{swot.threat}</p>
                </div>

            </div>

        </AnalysisCard>

    );

}

export default SwotCard;