import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import pipeline

nltk.download("punkt_tab")
nltk.download("stopwords")

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def ai_chatbot(user_input):
    response = chatbot(
        user_input, 
        max_new_tokens=100, 
        num_return_sequences=1,
        pad_token_id=chatbot.tokenizer.eos_token_id,
        clean_up_tokenization_spaces=False
    )

    return response[0]["generated_text"]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words("english")]

    return " ".join(tokens)

def simple_chatbot(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a nice day",
        "thanks": "You're welcome!"
    }

    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm sorry, I didn't understand that."


def chatbot_system():
    print("Chatbot: Hello! Type 'exit' to stop,")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        elif any(word in user_input.lower() for word in ["hello", "bye", "thanks", "how are you"]):
            response = simple_chatbot(user_input)
        else:
            response = ai_chatbot(user_input)
        
        print(f"Chatbot: ", {response})

chatbot_system()