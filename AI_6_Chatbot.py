# AI CHATBOT FOR CUSTOMER SUPPORT

import re

# KNOWLEDGE BASE (DICTIONARY)
responses = {

    'hello|hi|hey':
    'Hello! Welcome to TechSupport Bot.\n'
    'How can I help you today?',

    'price|cost|plan|subscription':
    'We offer three plans:\n'
    '1. Basic Plan  : $9 per month\n'
    '2. Pro Plan    : $19 per month\n'
    '3. Enterprise Plan : $49 per month\n'
    'Please tell me which plan you are interested in.',

    'refund|money back':
    'You can request a refund within 7 days of purchase.\n'
    'The amount will be returned within 5 to 7 working days.',

    'cancel|unsubscribe':
    'You can cancel your subscription anytime.\n'
    'No extra charges will be applied.\n'
    'Please provide your registered email to continue.',

    'feature|features|services':
    'Our services include:\n'
    '- Cloud Storage\n'
    '- Real-Time Collaboration\n'
    '- Analytics Dashboard\n'
    '- 24/7 Customer Support',

    'problem|issue|error|bug':
    'Please describe your issue in detail.\n'
    'Include any error message and device information.',

    'internet|network|wifi':
    'Please restart your router and check the network cable.\n'
    'If the issue continues, contact technical support.',

    'slow|hanging|lag':
    'Your system may be running slowly due to low memory.\n'
    'Please restart the computer and clear temporary files.',

    'printer':
    'Please check printer connection, paper availability,\n'
    'and printer driver installation.',

    'keyboard|mouse':
    'Please reconnect the device or replace the battery.\n'
    'You can also try another USB port.',

    'password|login':
    'Please click on "Forgot Password" to reset your password.',

    'payment|transaction':
    'Your payment may take a few minutes to process.\n'
    'Please check your bank statement once.',

    'delivery|shipping':
    'Your order will be delivered within 3 to 5 working days.',

    'human|agent|representative':
    'Connecting you to a human support agent.\n'
    'Please wait...',

    'help':
    'You can ask about:\n'
    '- Pricing\n'
    '- Refund\n'
    '- Cancellation\n'
    '- Features\n'
    '- Internet Problems\n'
    '- Printer Issues\n'
    '- Login Problems\n'
    '- Payment Issues',

    'thank|thanks':
    'You are welcome!\n'
    'Let me know if you need anything else.',

    'bye|goodbye|exit':
    'Thank you for contacting TechSupport Bot.\n'
    'Goodbye!'
}


# FUNCTION TO GET RESPONSE
def get_response(user_input):

    user_input = user_input.lower().strip()

    for pattern, reply in responses.items():

        if re.search(pattern, user_input):
            return reply

    return "Sorry! I did not understand your query.\nPlease type 'help' for available options."


# MAIN CHATBOT FUNCTION
def chatbot():

    print("=====================================")
    print("        TECH SUPPORT CHATBOT")
    print("=====================================")

    print("Type 'bye' to exit the chatbot.\n")

    while True:

        user_input = input("You: ")

        response = get_response(user_input)

        print("\nBot:", response, "\n")

        # EXIT CONDITION
        if re.search(r'bye|goodbye|exit', user_input.lower()):
            break


# DRIVER CODE
chatbot()
