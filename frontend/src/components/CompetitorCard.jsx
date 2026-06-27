import AnalysisCard from "./AnalysisCard";

function BusinessCard({ business }) {

    if (!business) return null;

    return (

        <AnalysisCard title="🏢 Business Analysis">

            <div className="space-y-4">

                <div>
                    <p className="font-semibold text-indigo-600">
                        Business Type
                    </p>
                    <p>{business.business_type}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">
                        Target Audience
                    </p>
                    <p>{business.target_audience}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">
                        Value Proposition
                    </p>
                    <p>{business.value_proposition}</p>
                </div>

            </div>

        </AnalysisCard>

    );

}

export default BusinessCard;