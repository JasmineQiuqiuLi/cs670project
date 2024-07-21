from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    result = sentiment_analyzer(text)[0]
    return jsonify({
        'label': result['label'],
        'score': result['score']
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
