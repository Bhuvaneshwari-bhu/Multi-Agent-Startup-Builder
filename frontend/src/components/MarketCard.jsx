import AnalysisCard from "./AnalysisCard";

function MarketCard({ market }) {

    if (!market) return null;

    return (

        <AnalysisCard title="📈 Market Analysis">

            <div className="grid md:grid-cols-2 gap-6">

                <div>
                    <p className="font-semibold text-indigo-600">Competition</p>
                    <p>{market.competition}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Demand</p>
                    <p>{market.demand}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Opportunity</p>
                    <p>{market.opportunity}</p>
                </div>

                <div>
                    <p className="font-semibold text-red-600">Risk</p>
                    <p>{market.risk}</p>
                </div>

            </div>

        </AnalysisCard>

    );

}

export default MarketCard;