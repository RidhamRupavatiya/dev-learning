# Rule Based ChatBot
import datetime
import time

# Chatbot Memory Creation (Dictionary of Responses)
responses = {
    "hello": "Hi, Welcome. How can I help you?",
    "how are you?": "I am very fine. Thank you.",
    "who are you?": "I am a smart AI ChatBot.",
    "motivate me": "Keep going. Every bug of your project makes you a better developer. Best!",
    "happy": "Great to hear that.",
    "functions": "Go and read Chapter 7."
}

# Function to get chatbot response
def get_response(user_question):
    user_question = user_question.lower()

    for each_key in responses:
        if each_key in user_question:  # Check if the key is present in the user's question
            return responses[each_key]

    # If no match is found
    return "I am not able to tell that yet. I am still in learning mode. I will learn that soon."

if __name__ == "__main__":
    # Welcome message
    print("Welcome to your ChatBot.")
    name = input("Enter Your Name: ")
    print(f"You can ask me basic questions and type 'bye' to exit from the bot.")

    # Time-based greeting
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 11:
        print(f"Good Morning {name}!")
    elif 11 <= current_hour < 17: # Assuming 24-hour format, 5 PM is 17
        print(f"Good Afternoon {name}!")
    elif 17 <= current_hour < 20: # Assuming 24-hour format, 8 PM is 20
        print(f"Good Evening {name}!")
    else:
        print(f"Good Night {name}!")

    # Main chat loop
    while True:
        user_input = input("Please ask your question: ")

        if "bye" in user_input.lower():
            break # Exit the loop if user types 'bye'

        reply = get_response(user_input)
        print(f"Bot Response: {reply}")