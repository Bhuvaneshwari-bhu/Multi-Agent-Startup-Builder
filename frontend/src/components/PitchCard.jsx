import AnalysisCard from "./AnalysisCard";

function PitchCard({ pitch }) {

    if (!pitch || typeof pitch !== "object") return null;

    return (

        <AnalysisCard title="🎤 Investor Pitch">

            <div className="space-y-4">

                <div>
                    <p className="font-semibold text-indigo-600">Problem</p>
                    <p>{pitch.problem}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Solution</p>
                    <p>{pitch.solution}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Business Model</p>
                    <p>{pitch.business_model}</p>
                </div>

                <div>
                    <p className="font-semibold text-indigo-600">Why Now</p>
                    <p>{pitch.why_now}</p>
                </div>

            </div>

        </AnalysisCard>

    );

}

export default PitchCard;