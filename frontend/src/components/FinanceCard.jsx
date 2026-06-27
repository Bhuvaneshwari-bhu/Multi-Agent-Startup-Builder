import AnalysisCard from "./AnalysisCard";

function FinanceCard({ finance }) {

    if (!finance) return null;

    return (

        <AnalysisCard title="💰 Finance Analysis">

            <div className="grid md:grid-cols-2 gap-6">

                <div>
                    <p className="font-semibold text-indigo-600">Startup Cost</p>
                    <p>{finance.startup_cost}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Scalability</p>
                    <p>{finance.scalability}</p>
                </div>

                <div className="md:col-span-2">
                    <p className="font-semibold text-indigo-600">Revenue Model</p>
                    <p>{finance.revenue_model}</p>
                </div>

                <div className="md:col-span-2">
                    <p className="font-semibold text-indigo-600">Break Even</p>
                    <p>{finance.break_even}</p>
                </div>

            </div>

        </AnalysisCard>

    );

}

export default FinanceCard;