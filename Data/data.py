training_sentences = [
    "Hello", "Hi there", "Hey", "Good day",

    # Farewells
    "Bye", "Goodbye", "See you later", "Catch you later",

    # Thanks
    "Thanks", "Thank you", "Much appreciated",

    # Company info / product info
    "What does 1Nebula do?",
    "What is 1Nebula?",
    "Tell me about one nebula",
    "Who are you?",
    "What is OneView?",
    "Tell me about OneView",
    "How can I track cloud expenses?",
    "How do I manage technology spend?",

    # Integrations / vendors
    "Do you integrate with Microsoft?",
    "Do you support AWS?",
    "Which vendors do you support?",
    "Do you work with Vodacom or Telkom?",

    # Demo / campaign
    "I want to see a demo",
    "Can I book a demo?",
    "Do you offer a trial?",
    "Show me current offers",
    "Any promotions running?",

    # Support / human
    "I need help",
    "Can I talk to someone?",
    "How do I contact support?",

    # Feedback / sentiment
    "I love your product",
    "This looks great",
    "Awesome",
    "It's too expensive",
    "We overspend often",
    "I'm not sure this will work for me",

    # Pricing / finance
    "Pricing",
    "How much does it cost?",
    "I have a billing question",

    # Privacy / security
    "How do you handle data?",
    "What about privacy?",
    "Is my data secure?",
]

training_labels = [
    # Greetings
    "greeting","greeting","greeting","greeting",
    # Farewells
    "farewell","farewell","farewell","farewell",
    # Thanks
    "thanks","thanks","thanks",
    # Company / product
    "company_info","company_info","company_info","company_info",
    "product_info","product_info","product_info","product_info",
    # Integrations
    "integrations","integrations","integrations","integrations",
    # Demo
    "demo_request","demo_request","demo_request","demo_request","demo_request",
    # Support
    "support","support","support",
    # Feedback
    "positive_feedback","positive_feedback","positive_feedback",
    "negative_feedback","negative_feedback","negative_feedback",
    # Pricing
    "pricing","pricing","pricing",
    # Privacy
    "privacy","privacy","privacy",
]

keyword_overrides = {
    "company_info":   ["1nebula", "one nebula", "nebula"],
    "product_info":   ["oneview", "one view"],
    "integrations":   ["microsoft", "aws", "azure", "vodacom", "telkom", "amazon"],
    "pricing":        ["pricing", "price", "cost", "costs", "billing", "bill", "expensive"],
    "privacy":        ["privacy", "security", "secure", "data", "gdpr", "popia"],
    "support":        ["support", "help", "agent", "human", "contact", "call"],
    "demo_request":   ["demo", "trial", "promotion", "promo", "offer"],
}

responses = {
    "greeting": [
        "Hello! How can I help today?",
        "Hi there! Ask me about OneView, pricing, or booking a demo.",
        "Hey! Looking for a demo, pricing, or integrations?"
    ],
    "farewell": [
        "Goodbye! 👋",
        "See you! Have a great day.",
        "Take care!"
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help.",
        "Anytime!"
    ],
    "company_info": [
        "1Nebula is a Cape Town–based tech company focused on cloud-native software and technology expense management. Our main product is OneView.",
        "We help businesses manage IT spend across cloud, mobile, telecom, and networking—bringing it all into one place with OneView."
    ],
    "product_info": [
        "OneView is a SaaS platform that tracks and controls technology expenses across vendors (e.g., Microsoft, AWS, Vodacom, Telkom) with dashboards, budgets, alerts, and forecasting.",
        "With OneView, you get visibility over cloud and telecom spend in one dashboard, plus tools for optimization and forecasting."
    ],
    "integrations": [
        "We commonly work with Microsoft/Azure and AWS, and ingest data from telecom providers like Vodacom and Telkom for a single view.",
        "Yes—cloud (Microsoft, AWS) and telecom (e.g., Vodacom, Telkom) sources can be integrated into OneView."
    ],
    "demo_request": [
        "Great! I can arrange a demo. Drop your email and company name and we’ll reach out.",
        "We’d love to show you OneView. Please share your email and company to book a slot."
    ],
    "support": [
        "I can connect you with a human agent. Please share your email, or reach us at support@1nebula.com.",
        "Tell me your email and a short description—I'll open a ticket for our team."
    ],
    "positive_feedback": [
        "🎉 Awesome to hear! Would you like to book a live demo?",
        "Love that! Want a tailored walkthrough for your environment?"
    ],
    "negative_feedback": [
        "Thanks for the honesty. A specialist can help with cost concerns—want me to connect you?",
        "I get it. We can tailor controls and budgets—shall I arrange a short consult?"
    ],
    "pricing": [
        "Pricing depends on usage and scope. For an accurate estimate, please share your company size and email so our team can send a quote.",
        "We don’t process sensitive billing data via the bot. I can connect you to a specialist for a tailored quote—what’s your email?"
    ],
    "privacy": [
        "We’re careful with sensitive data and follow best practices (e.g., POPIA/GDPR-aligned). The bot won’t handle financial records; we’ll route those to a human.",
        "Security and privacy matter to us. For detailed policies, I can connect you to our team—share your email if you’d like."
    ],
    "fallback": [
        "I’m not sure I understood. I can help with OneView, pricing, demos, integrations, privacy, or support.",
        "Could you rephrase that? Try: “What is OneView?”, “Book a demo”, “Pricing”, or “Integrations”."
    ]
}