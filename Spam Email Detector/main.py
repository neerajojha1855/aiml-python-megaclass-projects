import re
import os
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

nltk.download("stopwords")
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

# Load Dataset
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spam.csv")
df = pd.read_csv(file_path, encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "message"]
df["label"] = df["label"].map({"ham": 0, "spam": 1})

print(df.head())

def preprocess_text(text):
    text = re.sub(r"\W", " ", text)
    text = text.lower()

    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]

    return " ".join(words)

df["cleaned_message"] = df["message"].apply(preprocess_text)

vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df["cleaned_message"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print(classification_report(y_test, y_pred))

def predict_email(email_text):
    processed_text = preprocess_text(email_text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)

    return "Spam" if prediction[0] == 1 else "Not spam"

email = "Congratulations! You've won a free iPhone. Click here to claim now."
print(f"Email: {email}\nPrediction: {predict_email(email)}")