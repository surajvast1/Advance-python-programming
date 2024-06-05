from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)
nlp = pipeline("sentiment-analysis")

@app.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.json
    text = data["text"]
    result = nlp(text)[0]
    return jsonify({"text": text, "sentiment": result["label"], "confidence": result["score"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
