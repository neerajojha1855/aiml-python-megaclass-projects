import sys
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sys.stdout.reconfigure(encoding='utf-8')

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "Positive 🙂"
    elif sentiment < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

text = "I hated the movie"
print(f"Sentiment: {analyze_sentiment_textblob(text)}")

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_vader(text):
    sentiment_score = analyzer.polarity_scores(text)["compound"]

    if sentiment_score >= 0.05:
        return "Positive 😊"
    elif sentiment_score <= -0.05:
        return "Negative 😠"
    else:
        return "Neutral 😐"

text = "I loved the movie"
print(f"Sentiment: {analyze_sentiment_vader(text)}")

def analyze_user_input():
    while True:
        text = input("Enter a sentence for sentiment analysis (or type 'exit' to quit): ")
        if text.lower() == "exit":
            print("Exiting Sentiment Analyzer...")
            break

        print(f"TextBlob Sentiment Analysis: {analyze_sentiment_textblob(text)}")
        print(f"VADER Sentiment Analysis: {analyze_sentiment_vader(text)}")

analyze_user_input()