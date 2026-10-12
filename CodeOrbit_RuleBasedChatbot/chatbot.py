# Rule-Based Chatbot
# CodeOrbit Tech - Artificial Intelligence Internship

def chatbot_response(user_input):
    # Convert the user's message to lowercase
    # so that "Hello", "HELLO", and "hello" are treated the same.
    user_input = user_input.lower().strip()

    # Check for greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    # Check if the user asks how the chatbot is doing
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    # Check if the user asks for the chatbot's name
    elif "your name" in user_input:
        return "My name is CodeBot. I'm a simple rule-based chatbot."

    # Check for internship-related questions
    elif "internship" in user_input:
        return "This chatbot is created as part of the CodeOrbit Tech AI Internship."

    # Check if the user asks for help
    elif "help" in user_input:
        return "I can respond to greetings, questions about my name, and internship-related questions."

    # Check for goodbye
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    # Fallback response for unknown input
    else:
        return "Sorry, I don't understand that. Please try asking something else."


# Start the chatbot
print("===================================")
print("       Welcome to CodeBot!")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")


# Keep asking for user input until they say goodbye
while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("CodeBot:", response)

    # Exit the chatbot when the user says bye or goodbye
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break