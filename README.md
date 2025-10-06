## Practice Chatbot

This repository contains a practice chatbot project developed as part of my academic assignment.
It was created to explore how AI and chatbots can support business communication and customer engagement.

The project is not a real product and does not represent an official 1Nebula system. All training data used in this project is synthetic.

#### About 1Nebula
[1Nebula](https://www.1nebula.com/) is a software development company that operates in the field of cloud-native software development and technology expense management. 
They offer multiple SAAS solutions, an example is OneView, which is a Software-as-a-Service (SaaS) platform that allows organizations to track and manage all their IT costs and infrastructure on one platform.
Some Facts about 1Nebula:
- Microsoft Partner since 2014 and won SA ISV Partner of the Year in 2020
- Highly focused SaaS solutions available through Azure Marketplace.
- Focus on FinOps, Technology Expense Management and Software Development.
- Primary industries include technology, retail, energy, professional services and finance.

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
- Explaining services
- Capturing feedback during campaigns
- Sentiment analysis for customer insights

## Setup
Clone this repo or copy the code into a Python file (e.g., chatbot.py).

Install dependencies:

`pip install tensorflow nltk`

Download NLTK data:

```
import nltk
nltk.download('punkt')
```


Run the chatbot:

python chatbot.py

#### Example Conversation
<img width="1083" height="459" alt="image" src="https://github.com/user-attachments/assets/5091debc-b775-4520-870a-0bc1ed725151" />


### Model Performance
I trained a simple neural network with two hidden Dense layers (32 neurons each) and a 20% Dropout to classify intents in my chatbot. The model achieved 100% accuracy on the training set, and the training loss was very low, indicating it learned the training data perfectly. However, the validation accuracy remained around 9%, while the validation loss was extremely high (~10.5), which clearly shows the model is overfitting and failing to generalize to new inputs. This is likely because my dataset is small, with only about 109 sentences across 13+ intents. To improve performance, I plan to expand the dataset, use stronger regularization or higher dropout, experiment with simpler models, and apply data augmentation by rephrasing sentences and adding synonyms.

# Disclaimer
This chatbot is only for practice and learning purposes.
It was created as a submission for an assignment.
It is not an official 1Nebula product and should not be used in production.

#### Resources
https://youtu.be/t933Gh5fNrc?si=UFIJ1JPcelFDSAzr \n
ChatGPT (OpenAI) to explore how AI can be applied in customer engagement and feedback analysis.
