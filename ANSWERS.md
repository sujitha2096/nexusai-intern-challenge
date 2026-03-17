Q1: Handling Partial vs. Final Transcripts
I recommend a Hybrid Trigger approach.

The Logic: Querying the database on every partial transcript (e.g., every 200ms) creates massive unnecessary load and "UI Flicker." Instead, I would trigger read-only fetches (like getting user account status) only when high-confidence "intent keywords" are detected in a partial.

The Rule: All write actions (updating a record) or high-stakes logic (escalating to a human) must strictly wait for the final transcript to ensure the STT engine has fully corrected the grammar and context.

Q2: Risks of an Automated Knowledge Base
Data Poisoning (The "Polite but Wrong" Risk): If an agent is very friendly but gives a technically incorrect solution, and the customer provides a 5-star rating, the AI might "learn" that incorrect solution as a success.

Prevention: Implement an "Expert-in-the-Loop" review where a senior human agent must flag a case as "Technically Accurate" before it is indexed into the vector database.

Context Drift: Telecom policies change frequently. A solution from six months ago might be illegal or outdated today.

Prevention: Attach a Time-to-Live (TTL) metadata tag to every KB entry. Anything older than 90 days must be re-verified by a human or automatically archived.

Q3: AI Logic for Service Cancellation
Intent Detection: The AI identifies the intent as service_cancellation.

Context Retrieval: The system fetches the customer's history (3 previous calls) and current status (VIP, 4 days of service outage).

Rule Execution: Rule 4 (Always escalate cancellations) and Rule 3 (Repeat complaint) are triggered.

The Handoff: The AI should say: "I’m very sorry for the frustration. I see you've called three times regarding your outage. I'm connecting you immediately to a loyalty specialist who can resolve this and discuss your account."

Q4: Improving the System (Sentiment-Based Routing)
I would implement Real-time Sentiment-Based Routing.

Implementation: Instead of just looking at keywords, I’d use a rolling window of the last 3 messages to calculate a vibe_score. If the score drops significantly (indicating rising frustration), the call is bumped to the top of the human agent's queue.

Measurement: We would measure success by a reduction in "Churn Rate" for customers who started the call with high frustration and an improvement in "First Call Resolution" (FCR).