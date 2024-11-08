import nltk 
from nltk.chat.util import Chat, reflections  

#pre-trained tokenizer model used specifically for sentence splitting and word tokenization
nltk.download('punkt')

response = input("What is your name: ")
patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you(.*)', ['I am a chatbot, so I don’t have feelings, but thank you for asking!', 'Doing well! How about you?']),
    (r'what is your name', ['I am Chatbot! Nice to meet you']),
    (r'what is my name(.*)' , [f"Your name is {response}! how can i assist you today?"]),
    (r'how can you help me(.*)', ['I can chat with you and try to answer your questions.', 'I am here to have a conversation with you.']),
    (r'tell me a joke', ['Why did the developer go broke? Because they used up all their cache!', 'Why do programmers prefer dark mode? Because light attracts bugs!']),
    (r'bye|exit|quit', ['Goodbye!', 'It was nice talking to you. See you again soon!']),
    (r'(.*)', ["I'm not sure how to respond to that.", "Can you tell me more?", "Interesting... Tell me more!"])
]

# Use NLTK's reflection dictionary to handle variations in user input (like "I am" -> "you are")
chatbot = Chat(patterns, reflections) 


def start_chat():
    print("Hello! I'm Chatbot. Type 'bye', 'exit', or 'quit' to end the conversation.") 
    while True:
        user_input = input("You: ").lower() 

        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!") 
            break 
        
        # Get a response from the chatbot based on the input patterns
        response = chatbot.respond(user_input)  
        print(f"Chatbot: {response}") 


start_chat()
