function AnalysisCard({ title, children }) {

    return (

        <div
            className="
                bg-white
                rounded-2xl
                shadow-lg
                p-8
                mb-8
                border-l-8
                border-indigo-600
                hover:shadow-xl
                transition-all
                duration-300
            "
        >

            <h2
                className="
                    text-2xl
                    font-bold
                    text-indigo-700
                    mb-5
                "
            >
                {title}
            </h2>

            <div className="space-y-3 text-gray-700 leading-7">

                {children}

            </div>

        </div>

    );

}

export default AnalysisCard;