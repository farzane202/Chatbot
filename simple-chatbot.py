

import random


intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Feel free to ask me anything."
        ]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later!",
            "Bye! Take care"
        ]
    },
    "study_question": {
        "patterns": ["study", "exam", "homework"],
        "responses": [
            "Try studying in short focused sessions with breaks.",
            "Make a simple study plan and stick to it.",
            "Review your notes daily for better results."
        ]
    },
    "daily_advice": {
        "patterns": ["advice", "tip", "recommend"],
        "responses": [
            "Start your day with one small positive goal",
            "Stay consistent — small steps lead to big results",
            "Don't forget to take breaks and rest your mind"
        ]
    },
    "thanks": {
        "patterns": ["thanks", "thank you"],
        "responses": [
            "You're welcome!",
            "Glad I could help!",
            "Anytime!"
        ]
    }
}


def detect_intent(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return intent
    return "unknown"


def get_response(intent):
    if intent in intents:
        return random.choice(intents[intent]["responses"])
    else:
        return "I'm not sure I understand  Could you rephrase?"


print("Chatbot is running! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    intent = detect_intent(user_input)
    response = get_response(intent)
    print("Bot:", response)