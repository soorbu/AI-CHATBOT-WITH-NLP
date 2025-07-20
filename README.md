# AI CHATBOT WITH NLP

NLP-Based Chatbot with Text Summarization
This is a Python-based chatbot built using NLP libraries like NLTK and Hugging Face Transformers. It can respond to predefined intents and also summarize long paragraphs using an AI model (facebook/bart-large-cnn).

#  NLP Chatbot with Text Summarization

This project is a simple command-line chatbot built using Natural Language Processing (NLP) techniques. It responds to user queries based on predefined intents and can summarize any large block of text using a transformer model (`facebook/bart-large-cnn`).

##  Features

- Basic conversational ability using `intents.json`
- Smart text summarization on request (powered by Hugging Face Transformers)
- Easy to extend with more features like file summarization or sentiment analysis

---

## Screenshots of dashboard

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/9e2885ef-9c55-489f-af62-f3b3b65c5e4f" />

---

##  Project Structure

```
chatbot_nlp/
├── chatbot.py # Main chatbot script
├── intents.json # Intent definitions for rule-based replies
├── requirements.txt # Python package dependencies
├── .gitignore # Git ignore rules
└── botvenv/ # (ignored) Virtual environment folder
```

---

##  How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatbot_nlp.git
   cd chatbot_nlp
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv botvenv
   botvenv\Scripts\activate  # On Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the chatbot:
   ```bash
   python chatbot.py
   ```
---

## Example Usage 
You: hello
ChatBot: Hi there!

You: summarize this text
ChatBot: Sure! Please paste the text you'd like summarized.

You: [pastes large paragraph]
ChatBot: Here's the summary: ...

---

##  Dependencies

- `nltk`
- `torch`
- `transformers`

---
