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