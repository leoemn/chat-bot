import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load cleaned data
df = pd.read_csv('G:\\chat-bot\\data\\cleaned_data.csv')

# Prepare features and labels
X = df['user_message']
y = df['bot_response']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Vectorize the text using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Save the model and vectorizer
with open('G:\\chat-bot\\models\\classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)

with open('G:\\chat-bot\\models\\vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

# Test the model (just a basic test)
test_phrase_vectorized = vectorizer.transform(["Hi, how are you?"])
predicted_response = classifier.predict(test_phrase_vectorized)

print(f"Predicted response: {predicted_response[0]}")
