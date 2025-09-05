training_sentences = [
    # ---- Greetings ----
    "Hello", "Hi there", "Hey", "Good day", "Hello there", "Hey!", "Hi!", "Greetings", "Good morning", "Good afternoon", "Yo", "Hiya", "Hey buddy",

    # ---- Farewells ----
    "Bye", "Goodbye", "See you later", "Catch you later", "Bye bye", "See ya", "Good night", "Talk soon", "Farewell", "Later",

    # ---- Thanks ----
    "Thanks", "Thank you", "Much appreciated", "Thanks a lot", "Thank you very much", "Much obliged", "Thanks!", "Cheers", "I appreciate it",

    # ---- Company / Product info ----
    "What does 1Nebula do?", "What is 1Nebula?", "Tell me about one nebula", "Who are you?",
    "What is OneView?", "Tell me about OneView", "How can I track cloud expenses?", "How do I manage technology spend?",
    "Tell me about 1Nebula", "Who founded 1Nebula?", "What services does OneView offer?", "Can you explain OneView?", "What is 1Nebula's main product?", "Describe OneView",

    # ---- Integrations / Vendors ----
    "Do you integrate with Microsoft?", "Do you support AWS?", "Which vendors do you support?", "Do you work with ISP?",
    "Do you work with Amazon Web Services?", "Is Azure supported?", "Which cloud providers are compatible?", "Can I connect OneView with Microsoft 365?", "Do you integrate with telecoms?",

    # ---- Demo / Trial / Promotions ----
    "I want to see a demo", "Can I book a demo?", "Do you offer a trial?", "Show me current offers", "Any promotions running?",
    "Schedule a demo", "Sign me up for a trial", "I'd like a walkthrough", "Show me how it works", "Are there any promotions?",

    # ---- Support / Human ----
    "I need help", "Can I talk to someone?", "How do I contact support?", "I need support", "Connect me with someone", "Who can I contact for assistance?", "I have a problem", "How do I get help?", "I do not understand",

    # ---- Feedback / Sentiment ----
    # Positive
    "I love your product", "This looks great", "Awesome", "Great product", "I love OneView", "Fantastic!", "Amazing experience", "Awesome platform",
    # Negative
    "It's too expensive", "We overspend often", "I'm not sure this will work for me", "Too expensive", "Not user-friendly", "I'm concerned about costs", "This might not work for us", "I don't like this", "Problems with the system",

    # ---- Pricing / Finance ----
    "Pricing", "How much does it cost?", "I have a billing question", "How much is it?", "What's the cost?", "Can you give me pricing details?", "Is there a subscription fee?", "I want a quote", "Tell me the price",

    # ---- Privacy / Security ----
    "How do you handle data?", "What about privacy?", "Is my data secure?", "Is my data safe?", "How is my information protected?", "Do you follow GDPR?", "Tell me about data privacy", "Is OneView secure?", "How do you protect customer data?"
]

training_labels = [
    # Greetings
    "greeting","greeting","greeting","greeting","greeting","greeting","greeting","greeting","greeting","greeting","greeting","greeting","greeting",

    # Farewells
    "farewell","farewell","farewell","farewell","farewell","farewell","farewell","farewell","farewell","farewell",

    # Thanks
    "thanks","thanks","thanks","thanks","thanks","thanks","thanks","thanks","thanks",

    # Company / Product
    "company_info","company_info","company_info","company_info","product_info","product_info","product_info","product_info",
    "company_info","company_info","product_info","product_info","product_info","product_info",

    # Integrations
    "integrations","integrations","integrations","integrations","integrations","integrations","integrations","integrations","integrations",

    # Demo / Trial / Promotions
    "demo_request","demo_request","demo_request","demo_request","demo_request","demo_request","demo_request","demo_request","demo_request","demo_request",

    # Support / Human
    "support","support","support","support","support","support","support","support","support",

    # Feedback / Sentiment
    # Positive
    "positive_feedback","positive_feedback","positive_feedback","positive_feedback","positive_feedback","positive_feedback","positive_feedback","positive_feedback",
    # Negative
    "negative_feedback","negative_feedback","negative_feedback","negative_feedback","negative_feedback","negative_feedback","negative_feedback","negative_feedback","negative_feedback",

    # Pricing / Finance
    "pricing","pricing","pricing","pricing","pricing","pricing","pricing","pricing","pricing",

    # Privacy / Security
    "privacy","privacy","privacy","privacy","privacy","privacy","privacy","privacy","privacy"
]

keyword_overrides = {
    "company_info":   ["1nebula", "one nebula", "nebula"],
    "product_info":   ["oneview", "one view"],
    "integrations":   ["microsoft", "aws", "azure", "ISP"],
    "pricing":        ["pricing", "price", "cost", "costs", "billing", "bill", "expensive"],
    "privacy":        ["privacy", "security", "secure", "data", "gdpr", "popia"],
    "support":        ["support", "help", "agent", "human", "contact", "call"],
    "demo_request":   ["demo", "trial", "promotion", "promo", "offer"],
}

responses = {
    "greeting": [
        "Hello! How can I help today?",
        "Hi there! Ask me about OneView, pricing, or booking a demo.",
        "Hey! Looking for a demo, pricing, or integrations?",
        "Greetings! What would you like to know about OneView?",
        "Hi! I'm here to help with OneView, pricing, or demos.",
        "Hey there! Need info on OneView or integrations?",
        "Hello! Interested in a demo or pricing details?",
        "Hi! Ask me anything about OneView or our services.",
        "Hey! How can I assist you with OneView today?",
        "Hello! Need guidance on OneView or our offerings?"
    ],
    "farewell": [
        "Goodbye! 👋",
        "See you! Have a great day.",
        "Take care!",
        "Bye! Hope to chat again soon.",
        "Farewell! Wishing you a productive day.",
        "Catch you later! Stay safe.",
        "See ya! Don't hesitate to ask about OneView again.",
        "Goodbye! Reach out anytime for help.",
        "Take it easy! Looking forward to our next chat.",
        "Bye! Have a fantastic day ahead."
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help.",
        "Anytime!",
        "Glad I could assist.",
        "No problem! Let me know if you need anything else.",
        "My pleasure!",
        "Always happy to help.",
        "You got it! Feel free to ask more questions.",
        "No worries! I'm here for your queries.",
        "Anytime! Don't hesitate to reach out again."
    ],
    "company_info": [
        "1Nebula is a Cape Town–based tech company focused on cloud-native software and technology expense management. Our main product is OneView.",
        "We help businesses manage IT spend across cloud, mobile, telecom, and networking—bringing it all into one place with OneView.",
        "1Nebula specializes in cloud and telecom expense optimization through OneView.",
        "1Nebula empowers businesses to manage technology spend efficiently. We provide tools to track, analyze, and forecast IT and cloud costs.",
    ],
    "product_info": [
    """OneView is a SaaS platform that allows organizations to track and manage all 
    their IT costs and infrastructure expenses across different vendors. It provides 
    amazing features such as dashboards, budgets, alerts, and forecasting, allowing 
    managers to make data-driven decisions.""",
    ],
    "integrations": [
        "We commonly work with Microsoft/Azure and AWS, and ingest data from ISPs for a single view.",
        "Yes—cloud (Microsoft, AWS) and telecom (e.g., ISPs) sources can be integrated into OneView.",
        "OneView connects to Microsoft 365, Azure, AWS, and telecom vendors.",
        "Integrate your cloud and telecom accounts for a full spend overview.",
        "OneView supports major cloud and telecom platforms for unified tracking.",
        "Connect OneView with Microsoft, AWS, Azure, ISPs easily.",
        "Data from multiple vendors is ingested into OneView automatically.",
        "OneView integrates cloud and telecom data for actionable insights.",
        "Vendor integrations include Microsoft, AWS, Azure, and telecom providers.",
        "We make it easy to connect OneView to your existing cloud and telecom systems."
    ],
    "demo_request": [
        "Great! I can arrange a demo. Drop your email and company name and we’ll reach out.",
        "We’d love to show you OneView. Please share your email and company to book a slot.",
        "Schedule a demo with our team today.",
        "I can help set up a live walkthrough of OneView for you.",
        "Interested in seeing OneView in action? Let's book a demo.",
        "Our specialists can guide you through OneView with a demo.",
        "Book a session to explore OneView features firsthand.",
        "See OneView work in real-time—share your email to schedule.",
        "We offer personalized demos to understand your business needs.",
        "Want a demo? Provide your details and we’ll arrange it quickly."
    ],
    "support": [
        "I can connect you with a human agent. Please share your email, or reach us at support@1nebula.com.",
        "Tell me your email and a short description—I'll open a ticket for our team.",
        "Need assistance? Our support team is here to help.",
        "I can escalate this to our human specialists.",
        "Contact our support team directly by sharing your details.",
        "We’ll ensure a support agent reaches out to you promptly.",
        "For help, provide your email and issue description.",
        "Our team is ready to assist you with OneView issues.",
        "Reach out to our support specialists for guidance.",
        "I’ll connect you to someone who can provide direct assistance."
    ],
    "positive_feedback": [
        "🎉 Awesome to hear! Would you like to book a live demo?",
        "Love that! Want a tailored walkthrough for your environment?",
        "Glad you like it! We can arrange a demo if you want.",
        "Happy to know you’re enjoying OneView!",
        "Thanks! Would you like a quick demo to explore features?",
        "Awesome! Our team can show you advanced OneView tools.",
        "Great! Interested in a personal walkthrough?",
        "So glad! Want me to schedule a demo for you?",
        "Fantastic! Let’s set up a session to explore OneView.",
        "Excellent! We can show you more via a live demo."
    ],
    "negative_feedback": [
        "Thanks for the honesty. A specialist can help with cost concerns—want me to connect you?",
        "I get it. We can tailor controls and budgets—shall I arrange a short consult?",
        "Sorry to hear that. We can assist with solutions or optimizations.",
        "We understand your concerns—our experts can provide guidance.",
        "I hear you. Want me to connect you with a human advisor?",
        "Thanks for sharing. A short consult may help address this.",
        "We can review your situation and suggest improvements.",
        "Understood. Shall I arrange a specialist call?",
        "We’re here to help with tailored solutions for your feedback.",
        "Your feedback is valuable. Let’s see how we can assist further."
    ],
    "pricing": [
        "Pricing depends on usage and scope. For an accurate estimate, please share your company size and email so our team can send a quote.",
        "We don’t process sensitive billing data via the bot. I can connect you to a specialist for a tailored quote—what’s your email?",
        "Our pricing varies. Share your details for a personalized quote.",
        "Want an exact pricing? Please provide your company size and email.",
        "For detailed costs, our specialists can send a quote to your email.",
        "Pricing is tailored to business needs—connect with us for specifics.",
        "We can provide a quote after understanding your requirements.",
        "Need a quote? Share company info and email for details.",
        "Costs depend on scope—let’s get a specialist to assist.",
        "Our team can provide a customized pricing plan via email."
    ],
    "privacy": [
        "We’re careful with sensitive data and follow best practices (e.g., POPIA/GDPR-aligned). The bot won’t handle financial records; we’ll route those to a human.",
        "Security and privacy matter to us. For detailed policies, I can connect you to our team—share your email if you’d like.",
        "Your data is safe with us. We follow privacy regulations.",
        "OneView protects customer data rigorously according to GDPR/POPIA.",
        "We prioritize security and compliance for all user data.",
        "Our team ensures sensitive information is handled securely.",
        "Privacy is important. We route financial data to specialists.",
        "We comply with global data privacy standards for safety.",
        "Customer data is protected using industry best practices.",
        "For detailed privacy policies, we can connect you with our experts."
    ],
    "fallback": [
        "I’m not sure I understood. I can help with OneView, pricing, demos, integrations, privacy, or support.",
        "Could you rephrase that? Try: “What is OneView?”, “Book a demo”, “Pricing”, or “Integrations”.",
        "Sorry, I didn’t catch that. Try asking about OneView or pricing.",
        "I’m here to help with OneView, demos, pricing, integrations, or support.",
        "Could you clarify? You can ask about OneView, pricing, or demos.",
        "I didn’t understand. Try asking for a demo, pricing, or integrations.",
        "Hmm, I’m not sure. Try: “OneView features?”, “Pricing?”, “Book a demo?”",
        "I’m not sure I follow. Ask me about OneView, pricing, or integrations.",
        "I couldn’t understand that. Try asking about OneView or support.",
        "Please rephrase your question. I can assist with OneView, pricing, or demos."
    ]
}

