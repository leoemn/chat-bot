from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
CORS(app)

# Load the model and vectorizer
classifier = joblib.load('G:\\chat-bot\\models\\classifier.pkl')
vectorizer = joblib.load('G:\\chat-bot\\models\\vectorizer.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods = ['POST'])

def send_message():
    data = request.json
    user_message = data.get('userMessage', '')

    # Vectorize the user message using the loaded vectorizer
    user_message_vectorized = vectorizer.transform([user_message])

    # Use the loaded model to generate a response
    response_message = classifier.predict(user_message_vectorized)[0]

    return jsonify({'responseMessage': response_message})

if __name__ == '__main__':
    app.run(debug=True)
