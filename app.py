from chatbot import StudyBuddyChatbot

def main():
    chatbot = StudyBuddyChatbot()
    print("Welcome to your Personalized Study Buddy Chatbot!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Happy studying!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
