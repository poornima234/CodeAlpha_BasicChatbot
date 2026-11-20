
def chatbot_response(user_input):

    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I am a Python chatbot."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."

print("===== WELCOME TO PYTHON CHATBOT =====")
print("Type 'bye' to exit the chat.")

while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye":
        break

print("\nChat ended. Thank you!")
