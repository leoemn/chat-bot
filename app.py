from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods = ['POST'])

def send_message():
    data = request.json
    user_message = data.get('userMessage', '')
    response_message = f"{user_message}"
    return jsonify({'responseMessage': response_message})

if __name__ == '__main__':
    app.run(debug=True)