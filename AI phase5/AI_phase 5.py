import random

# List of greetings
greetings = ["hi", "hello", "hey", "howdy", "good morning", "good afternoon", "good evening"]

# List of questions
questions = ["How are you doing today?", "What can I do for you?", "What would you like to talk about?", "What's on your mind?", "What's new?", "What are you interested in?", "What are your hobbies?"]

# List of responses
responses = ["I'm glad to hear that! I'm doing well, thank you for asking.", "I'm happy to help. What can I do for you?", "That sounds interesting. Tell me more.", "I'm curious about that too. Can you tell me more?", "That's great! I'm always happy to learn new things.", "That sounds like fun! What kind of hobbies do you have?", "I'm glad you asked! I'm interested in a lot of things, including artificial intelligence, machine learning, and natural language processing."]

# List of follow-up questions
follow_up_questions = ["Can you tell me more about that?", "Why are you interested in that?", "What do you know about that?", "What do you think about that?", "What are your thoughts on that?"]


# Start the chatbot
def start_chatbot():

    # Greet the user
    greeting = random.choice(greetings)
    print(f"{greeting}!")

    # Ask the user a question
    question = random.choice(questions)
    user_response = input(question)

    # Generate a response to the user
    response = random.choice(responses)
    print(response)

    # Continue the conversation by asking another question or generating a response
    continue_conversation()

# Continue the conversation
def continue_conversation():

    # Ask the user another question
    question = input("What else would you like to talk about?")

    # Generate a response to the user
    response = generate_response(question)
    print(response)

    # Continue the conversation by asking another question or generating a response
    continue_conversation()

# Generate a response to a question
def generate_response(question):

    # If the question is a greeting, respond with a greeting
    if question in greetings:
        response = random.choice(greetings)
    else:
        response = random.choice(responses)

    return response

# Start the chatbot
start_chatbot()
