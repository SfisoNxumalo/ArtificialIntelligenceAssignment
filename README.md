## Practice Chatbot

This repository contains a practice chatbot project developed as part of my academic assignment.
It was created to explore how AI and chatbots can support business communication and customer engagement.

The project is not a real product and does not represent an official 1Nebula system.

#### About 1Nebula
[1Nebula](https://www.1nebula.com/) is a software development company that that operates in the field of cloud-native software development and technology expense management. 
They offer multiple SAAS solutions, an example is OneView, which is a Software-as-a-Service (SaaS) platform that allows organizations to track and manage all their IT costs and infrastructure on one platform.
Some Facts about 1Nebula:
- Microsoft Partner since 2014 and won SA ISV Partner of the Year in 2020
- Highly focused SaaS solutions available through Azure Marketplace.
- Focus on FinOps, Technology Expense Management and Software Development.
- Primary industries include technology, retail, energy, professional services and finance.
 -- 
## Project Purpose:
The chatbot demonstrates:
Basic text classification with TensorFlow/Keras
Preprocessing text using NLTK (tokenization + bag-of-words)
Generating simple responses to user inputs
This aligns with the assignment goal of exploring how AI tools like chatbots can be used to enhance customer engagement and feedback collection in organizations.

## Features

Recognizes simple intents:
Greetings (e.g., "Hello")
Farewells (e.g., "Bye")
Thanks (e.g., "Thank you")
Returns predefined responses

Provides a foundation to expand with 1Nebula-specific use cases, such as:

Explaining services
Capturing feedback during campaigns
Sentiment analysis for customer insights

## Setup
Clone this repo or copy the code into a Python file (e.g., chatbot.py).

Install dependencies:

pip install tensorflow nltk

Download NLTK data:

import nltk
nltk.download('punkt')


Run the chatbot:

python chatbot.py

#### Example Conversation
1Nebula Chatbot ready! Type 'quit' to exit.
You: Hello
Bot: Hi there!
You: Thank you
Bot: You're welcome!
You: Bye
Bot: See you!

# Disclaimer
This chatbot is only for practice and learning purposes.
It was created as a submission for an assignment.
It is not an official 1Nebula product and should not be used in production.
This project was built with the help of ChatGPT (OpenAI) to explore how AI can be applied in customer engagement and feedback analysis. All training data used in this project is synthetic.
