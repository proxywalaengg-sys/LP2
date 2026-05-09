import re

responses = {
    'hello|hi|hey': 'Hello! Welcome to TechSupport Bot. How can I help you?',

    'price|cost|plan|subscription':
    'We offer three plans:\n'
    'Basic Plan: $9 per month\n'
    'Pro Plan: $19 per month\n'
    'Enterprise Plan: $49 per month\n'
    'Please tell me which plan you are interested in.',

    'refund|money back':
    'You can request a refund within 7 days of purchase.\n'
    'The amount will be returned within 5 to 7 working days.',

    'cancel|unsubscribe':
    'You can cancel your subscription anytime.\n'
    'No extra charges will be applied.\n'
    'Please provide your registered email to proceed.',

    'feature|features|services':
    'Our product provides cloud storage, real-time collaboration,\n'
    'analytics dashboard, and 24/7 customer support.',

    'problem|issue|error|bug':
    'Please describe your issue in detail.\n'
    'Include any error message and device details.',

    'human|agent|representative':
    'Connecting you to a human agent. Please wait.',

    'help':
    'You can ask about pricing, refund, cancellation, features, or technical issues.',

    'thank|thanks':
    'You are welcome. Let me know if you need anything else.',

    'bye|goodbye|exit':
    'Thank you for contacting us. Goodbye.'
}


def get_response(user_input):
    user_input = user_input.lower().strip()

    for pattern, reply in responses.items():
        if re.search(pattern, user_input):
            return reply

    return "I did not understand your query. Please type 'help' for options."


def chatbot():
    print("TechSupport Chatbot")
    print("Type 'bye' to exit\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response, "\n")

        if re.search(r'bye|goodbye|exit', user_input.lower()):
            break


chatbot()
