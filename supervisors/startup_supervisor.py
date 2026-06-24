from agents.planner_agent import planner_agent
from agents.business_agent import business_agent
from agents.competitor_agent import competitor_agent
from agents.market_agent import market_agent
from agents.finance_agent import finance_agent


def startup_supervisor(startup_idea):

    state = {
        "startup_idea": startup_idea,
        "execution_plan": [],

        "business_report": "",
        "competitor_report": "",
        "market_report": "",
        "finance_report": ""
    }

    state = planner_agent(state)

    print("\nExecution Plan:")
    print(" -> ".join(state["execution_plan"]))

    agent_map = {
        "business": business_agent,
        "competitor": competitor_agent,
        "market": market_agent,
        "finance": finance_agent
    }

    for agent_name in state["execution_plan"]:

        if agent_name in agent_map:

            try:
                state = agent_map[agent_name](state)
                print(f"{agent_name.title()} Agent Done")

            except Exception as e:
                print(f"{agent_name.title()} Agent Failed:", e)

    return state




# #
# (venv) (base) user@user-TravelMate-P214-53:~/startup-builder$ python main.py
# Loaded key: AQ.Ab8RN6I
# Enter startup idea: ai tutor
# gemini-2.5-flash failed
# 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
# Business Agent Done
# Market Agent Done
# gemini-2.5-flash failed
# 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
# gemini-2.5-flash-lite failed
# 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
# gemini-2.0-flash failed
# 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model: gemini-2.0-flash\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model: gemini-2.0-flash\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_input_token_count, limit: 0, model: gemini-2.0-flash\nPlease retry in 29.455368527s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash'}}, {'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash'}}, {'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_input_token_count', 'quotaId': 'GenerateContentInputTokensPerModelPerMinute-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash'}}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '29s'}]}}
# Finance Agent Failed: All Gemini models unavailable
# Finance Agent Done

# ===== BUSINESS ANALYSIS =====

# Business Type: EdTech (Education Technology) Software as a Service (SaaS)

# Target Audience: Students (K-12, university, lifelong learners), Educators (teachers, tutors, professors), Educational Institutions (schools, universities, training centers)

# Value Proposition: Personalized and adaptive learning experiences that improve academic performance, increase engagement, and make education more accessible and efficient through AI-powered tutoring, feedback, and content delivery.

# ===== COMPETITOR ANALYSIS =====



# ===== MARKET ANALYSIS =====

# This is an exciting and highly relevant startup idea. The EdTech space is ripe for disruption, and AI is the primary catalyst. Here's a detailed analysis:

# ---

# ## AI Tutor: Business Analysis

# **Startup Idea:** AI Tutor
# **Business Type:** EdTech Software as a Service (SaaS)
# **Target Audience:** Students (K-12, university, lifelong learners), Educators (teachers, tutors, professors), Educational Institutions (schools, universities, training centers)
# **Value Proposition:** Personalized and adaptive learning experiences that improve academic performance, increase engagement, and make education more accessible and efficient through AI-powered tutoring, feedback, and content delivery.

# ---

# ### Competition Level: **Very High**

# The AI Tutor space is rapidly becoming one of the most crowded and competitive segments within EdTech.

# 1.  **Incumbent EdTech Platforms:** Existing players are rapidly integrating AI.
#     *   **Knowledge Bases:** Khan Academy, Coursera, edX, Duolingo, Chegg, Quizlet, Wolfram Alpha. Many of these already offer massive content libraries, practice problems, and some level of personalization. They are now adding generative AI features for tutoring and feedback.
#     *   **Learning Management Systems (LMS):** Canvas, Blackboard, Moodle. While not direct tutoring, they are integrating AI tools for educators (grading, feedback) and often partner with or acquire AI solutions.
#     *   **Dedicated Tutoring Services:** Chegg (already leveraging AI), Varsity Tutors, Kumon, Sylvan Learning. These traditional and online human-led tutoring services are exploring how AI can augment their offerings or compete directly.

# 2.  **Generalist AI Giants:** These companies have the resources and foundational models to quickly pivot or offer powerful educational tools.
#     *   **OpenAI:** ChatGPT (especially with custom GPTs and GPT-4o's multimodal capabilities), and its dedicated "ChatGPT Edu" initiatives.
#     *   **Google:** Gemini (with its educational applications), Google Classroom enhancements, and dedicated AI research into learning.
#     *   **Microsoft:** Copilot, integration into Microsoft 365 Education, and potential educational services.
#     *   **Amazon:** AWS offers the infrastructure and potentially AI services that could power competitors.

# 3.  **Emerging AI-Native EdTech Startups:** A wave of new companies are being founded specifically around AI tutoring, often with deep learning expertise and innovative approaches.
#     *   Examples: Numerous startups focusing on specific subjects (e.g., Mathway, PhotoMath using AI for problem-solving), language learning (e.g., ELSA Speak), or exam prep, all now leveraging generative AI.
#     *   Many are well-funded and quickly iterating, offering advanced features like natural language interaction, multimodal input/output, and sophisticated adaptive learning paths.

# 4.  **Open Source & DIY AI Solutions:** The proliferation of open-source AI models means some educators or tech-savvy individuals are creating their own tutoring bots, setting a baseline expectation for AI capabilities.

# **Key takeaway:** Differentiation is *paramount*. A generic AI tutor will struggle. Specialization, superior UX, unique pedagogical approaches, or deep institutional integrations will be critical.

# ### Market Demand: **Very High**

# The demand for personalized and effective learning solutions is evergreen and growing, and AI is seen as a powerful way to meet this demand at scale.

# 1.  **Unmet Needs in Traditional Education:**
#     *   **Teacher Shortages & Overburdened Educators:** Teachers often lack the time to provide individualized attention to every student. AI tutors can fill this gap, offering 24/7 support.
#     *   **Large Class Sizes:** Students often get lost in large classrooms, with diverse learning styles and paces. AI provides a tailored experience.
#     *   **Accessibility:** High-quality human tutoring is expensive and often inaccessible to lower-income students or those in remote areas. AI can democratize access.

# 2.  **Student Desire for Support:**
#     *   **Academic Performance:** Students consistently seek ways to improve grades, understand difficult concepts, and prepare for exams.
#     *   **Engagement:** Traditional methods can be disengaging. Personalized, interactive, and gamified AI experiences can significantly boost engagement.
#     *   **Flexible Learning:** Students want to learn on their own schedules and at their own pace.
#     *   **Fear of Asking Questions:** Many students hesitate to ask questions in class, fearing judgment. An AI tutor provides a judgment-free space.

# 3.  **Educator & Institutional Interest:**
#     *   **Teacher Augmentation:** Educators are increasingly interested in AI as a "co-pilot" to assist with lesson planning, content creation, feedback, and identifying student struggles.
#     *   **Data-Driven Insights:** Institutions want better data on student progress and learning gaps to inform curriculum development and intervention strategies. AI tutors can generate rich analytical data.
#     *   **Innovation & Modernization:** Schools and universities want to be at the forefront of educational technology to attract and retain students.

# 4.  **Lifelong Learning & Upskilling:** The demand for continuous learning for career advancement, skill acquisition, and personal development is booming, and AI tutors offer a scalable solution.

# **Key takeaway:** The market demand is not just for *a* tutor, but for *better, more accessible, and more effective* tutoring, which AI is uniquely positioned to deliver.

# ### Current Trend: **AI-Driven Hyper-Personalization**

# The current landscape is dominated by the rapid integration and evolution of AI in education, specifically:

# 1.  **Generative AI as a Game-Changer:** Large Language Models (LLMs) are transforming how tutoring can be delivered, enabling natural language conversations, adaptive content generation, and sophisticated feedback. This is the biggest trend.
# 2.  **Adaptive Learning Paths:** Moving beyond simple "right/wrong" answers to dynamically adjust curriculum, difficulty, and learning methods based on individual student performance, preferences, and learning styles.
# 3.  **Multimodal Learning:** AI tutors are evolving beyond text-based interactions to incorporate voice, images, video, and even haptic feedback, catering to diverse learning modalities.
# 4.  **Augmented Intelligence for Educators:** AI isn't just for students; it's increasingly being designed to empower teachers with tools for administrative tasks, differentiated instruction, and insights into student needs.
# 5.  **Focus on "Learning to Learn" Skills:** AI is being used not just to deliver content, but to teach critical thinking, problem-solving, meta-cognition, and self-regulation – skills essential for lifelong learning.
# 6.  **Ethical AI and Data Privacy:** A growing trend (and concern) is the responsible use of AI in education, including data privacy, algorithmic bias, transparency, and preventing misuse (e.g., cheating).
# 7.  **Microlearning & Gamification:** Breaking down complex topics into digestible chunks and incorporating game-like elements to increase engagement and retention, often powered by AI's ability to track progress and offer rewards.
# 8.  **B2B2C Models:** A shift towards selling AI solutions to institutions (B2B) who then offer them to their students and educators (B2C), leveraging existing distribution channels and building trust.

# **Key takeaway:** The market is past the "novelty" stage of AI; the focus is now on sophisticated, pedagogically sound, and ethically responsible applications that deliver measurable learning outcomes.

# ### Opportunities:

# 1.  **Niche Specialization:** Instead of a general AI tutor, focus on a specific subject (e.g., advanced calculus, medical terminology), age group (e.g., K-3 literacy), or learning challenge (e.g., ADHD-friendly learning aids). This allows for deeper expertise and better model training.
# 2.  **Institutional Partnerships (B2B/B2B2C):** Selling to schools, universities, or corporate training centers can provide significant revenue, distribution, and validation. Focus on integration with existing LMS and providing data insights for educators.
# 3.  **Differentiated Pedagogical Approach:** Develop a unique learning methodology powered by AI (e.g., Socratic tutoring, project-based learning support, metacognitive coaching). Go beyond just answering questions.
# 4.  **Multimodal & Highly Interactive Experiences:** Leverage the latest in AI to create immersive experiences – voice interaction, visual explanations, interactive simulations, and virtual reality integration.
# 5.  **Empowering Educators, Not Replacing Them:** Position the AI tutor as a powerful assistant for teachers, freeing up their time for higher-value activities and providing data to help them better support students.
# 6.  **Addressing Learning Gaps & Equity:** Focus on building a solution that can effectively support students with learning disabilities, English language learners, or those in underserved communities, truly democratizing access to high-quality education.
# 7.  **Data-Driven Insights for Systemic Improvement:** Offer advanced analytics to institutions to identify curriculum weaknesses, common student misconceptions, and areas for pedagogical improvement.
# 8.  **Ethical AI & Trustworthiness as a Feature:** Build strong data privacy, bias mitigation, and transparency into the core product, and market it as a key differentiator in a potentially ethically challenging space.

# ### Risks:

# 1.  **Accuracy and "Hallucinations":** AI models can still provide incorrect information or make up facts. In an educational context, this is a critical flaw that can undermine trust and harm learning. Rigorous fact-checking and robust guardrails are essential.
# 2.  **Ethical Concerns & Bias:** AI models can inherit biases from their training data, leading to unfair or inaccurate responses for certain demographics. There are also concerns about over-reliance on AI, impact on critical thinking, and data privacy.
# 3.  **User Adoption & Resistance:**
#     *   **Students:** May use it for cheating if not designed carefully, or find it less engaging than human interaction.
#     *   **Educators:** Fear of job displacement, skepticism about effectiveness, or resistance to new technology if the value proposition isn't clear and training isn't provided.
#     *   **Parents/Institutions:** Concerns about screen time, lack of human connection, or perceived dehumanization of education.
# 4.  **Data Privacy & Security:** Handling sensitive student data (academic performance, personal information) requires stringent adherence to regulations (FERPA, GDPR, COPPA) and robust cybersecurity measures. A breach could be catastrophic.
# 5.  **High Development & Maintenance Costs:** Building and continuously improving a sophisticated AI tutor requires significant investment in AI research, data scientists, engineers, subject matter experts, and computing resources.
# 6.  **"Black Box" Problem:** The lack of transparency in how AI arrives at answers can be problematic in education, where understanding the *process* of learning is as important as the correct answer.
# 7.  **Lack of Empathy & Human Connection:** While AI can simulate empathy, it cannot truly replace the motivational power, emotional support, and nuanced understanding that a human tutor provides.
# 8.  **Monetization Challenges:** Convincing individuals or institutions to pay for a SaaS solution in a competitive market, especially when free (though less sophisticated) AI tools exist, can be difficult. Long sales cycles for institutional clients.
# 9.  **Regulatory & Policy Landscape:** The regulatory environment around AI in education is still evolving and could impose new restrictions or requirements that impact product design and data handling.

# ---

# **Overall Assessment:**
# The "AI Tutor" is a high-potential, high-risk venture. The market demand is undeniable, and the technology is rapidly advancing. However, the competition is fierce, and overcoming significant ethical, technical, and adoption challenges will require a strong, differentiated product, a clear pedagogical vision, and a robust business model. Success will hinge on building trust, demonstrating measurable learning outcomes, and perhaps most importantly, finding a strategic niche or a unique value proposition that truly sets it apart.

# ===== FINANCE ANALYSIS =====


# Finance analysis temporarily unavailable.
# Gemini service overloaded.

# (venv) (base) user@user-TravelMate-P214-53:~/startup-builder$ 