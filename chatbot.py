import random
import json
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import get_close_matches
from transformers import pipeline

nltk.download('punkt')
nltk.download('stopwords')

with open("intents.json", "r") as file:
    intents = json.load(file)

def preprocess(text):
    tokens = word_tokenize(text.lower(), preserve_line=True)
    tokens = [t for t in tokens if t not in stopwords.words('english') and t not in string.punctuation]
    return " ".join(tokens)

def match_intent(user_input):
    user_input = preprocess(user_input)
    all_patterns = {}
    for intent in intents:
        for pattern in intent["patterns"]:
            all_patterns[pattern.lower()] = intent["tag"]

    best_match = get_close_matches(user_input, all_patterns.keys(), n=1, cutoff=0.5)
    if best_match:
        return all_patterns[best_match[0]]
    return None

def get_response(tag):
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "I'm not sure how to respond to that."

# Load only once (outside function)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    try:
        # BART works best with max ~1024 tokens (~600–700 words)
        if len(text.split()) < 50:
            return "The text is too short to summarize."

        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Something went wrong while summarizing: {str(e)}"
    
def chat():
    print("ChatBot: Hello! Type 'exit' to quit.")
    awaiting_text = False

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("ChatBot: Bye! Have a great day!")
            break

        if awaiting_text:
            summary = summarize_text(user_input)
            print("ChatBot: Here's the summary:")
            print(summary)
            awaiting_text = False
            continue

        # Check if this is a request to summarize
        if "summarize" in user_input.lower():
            print("ChatBot: Sure! Please paste the text you'd like summarized.")
            awaiting_text = True
            continue

        intent = match_intent(user_input)
        if intent:
            response = get_response(intent)
        else:
            response = "Sorry, I didn't get that. Can you rephrase?"
        print("ChatBot:", response)

if __name__ == "__main__":
    chat()
