# Simple AI Chatbot

def chatbot():
    print("AI Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("AI Chatbot: Hi! How are you?")

        elif user == "how are you":
            print("AI Chatbot: I am fine. Thanks for asking!")

        elif user == "your name":
            print("AI Chatbot: I am a Python AI Chatbot.")

        elif user == "what can you do":
            print("AI Chatbot: I can chat with you and answer simple questions.")

        elif user == "bye":
            print("AI Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("AI Chatbot: Sorry, I don't understand that.")

# Run chatbot
chatbot()
