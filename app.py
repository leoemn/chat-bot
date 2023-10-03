from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/send_message', methods = ['POST'])

def send_message():
    data = request.json
    user_message = data.get('userMessage', '')
    response_message = f"{user_message}"
    return jsonify({'responseMessage': response_message})

if __name__ == '__main__':
    app.run(debug=True)