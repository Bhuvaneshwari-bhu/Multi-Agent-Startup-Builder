import { useState } from "react";
import AnalysisCard from "./components/AnalysisCard";
import BusinessCard from "./components/BusinessCard";
import CompetitorCard from "./components/CompetitorCard";
import MarketCard from "./components/MarketCard";
import FinanceCard from "./components/FinanceCard";
import SwotCard from "./components/SwotCard";
import PitchCard from "./components/PitchCard";
import RoadmapCard from "./components/RoadmapCard";
import AgentStatusCard from "./components/AgentStatusCard";


function App() {

  const [startupIdea, setStartupIdea] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
const [error, setError] = useState("");

async function analyzeStartup() {

  if (!startupIdea.trim()) {
      setError("Please enter a startup idea.");
      return;
  }

  setLoading(true);
  setError("");
  setResult(null);

  try {

      const response = await fetch(
          "http://127.0.0.1:8000/analyze",
          {
              method: "POST",

              headers: {
                  "Content-Type": "application/json",
              },

              body: JSON.stringify({
                  startup_idea: startupIdea,
              }),
          }
      );

      if (!response.ok) {
          throw new Error("Server Error");
      }

      const data = await response.json();

      setResult(data);

  }
  catch (err) {

      console.error(err);

      setError(
          "Failed to analyze startup. Please try again."
      );

  }
  finally {

      setLoading(false);

  }

}

  return (
    <div className="min-h-screen bg-slate-100">
  
      {/* Header */}
      <div className="bg-indigo-700 text-white shadow-lg">
  
        <div className="max-w-6xl mx-auto py-10 px-6">
  
          <h1 className="text-5xl font-bold text-center">
             AI Startup Builder
          </h1>
  
          <p className="text-center text-indigo-200 mt-3 text-lg">
            Multi-Agent AI Startup Analysis Platform
          </p>
  
        </div>
  
      </div>
  
      {/* Main Content */}
      <div className="max-w-6xl mx-auto px-6 py-10">
  
        {/* Input Section */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
  
          <h2 className="text-2xl font-semibold mb-6">
            Analyze Your Startup Idea
          </h2>
  
          <input
            type="text"
            value={startupIdea}
            onChange={(e) => setStartupIdea(e.target.value)}
            placeholder="Enter your startup idea..."
  
            className="
              w-full
              p-4
              text-lg
              rounded-xl
              border
              border-gray-300
              shadow-sm
              focus:outline-none
              focus:ring-4
              focus:ring-indigo-300
              transition
            "
          />
  
          <button
            onClick={analyzeStartup}
            disabled={loading}
            className="
              mt-6
              bg-indigo-600
              hover:bg-indigo-700
              text-white
              font-semibold
              px-8
              py-3
              rounded-xl
              shadow-md
              transition-all
              duration-300
            "
          >
            {loading ? "Analyzing..." : "Analyze Startup"}
          </button>
          {loading && (

<div className="mt-6 flex items-center gap-3">

    <div
        className="
            h-6
            w-6
            rounded-full
            border-4
            border-indigo-600
            border-t-transparent
            animate-spin
        "
    ></div>

    <p className="text-indigo-700 font-medium">

        AI Agents are analyzing your startup...

    </p>

</div>

)}
  {error && (

<div
    className="
        mt-5
        bg-red-100
        text-red-700
        border
        border-red-300
        rounded-xl
        p-4
    "
>

    {error}

</div>

)}
        </div>
  
        {/* Results */}
        {result && (
          <>
            <AgentStatusCard status={result.agent_status} />
            <BusinessCard business={result.business_report} />
  
            <CompetitorCard competitor={result.competitor_report} />
  
            <MarketCard market={result.market_report} />
  
            <FinanceCard finance={result.finance_report} />
  
            <SwotCard swot={result.swot_report} />
  
            <PitchCard pitch={result.pitch_report} />
  
            <RoadmapCard roadmap={result.roadmap_report} />
  
            <div className="flex justify-center mt-10">
  
              <button
                onClick={() =>
                  window.open(
                    "http://localhost:8000/download-pdf",
                    "_blank"
                  )
                }
  
                className="
                  bg-green-600
                  hover:bg-green-700
                  text-white
                  font-semibold
                  px-8
                  py-3
                  rounded-xl
                  shadow-lg
                  transition-all
                  duration-300
                "
              >
                📄 Download PDF
              </button>
  
            </div>
  
          </>
        )}
  
      </div>
  
    </div>
  );
}

export default App;