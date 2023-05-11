from transformers import pipeline
from flask import Flask, jsonify, request
from deep_translator import GoogleTranslator

app = Flask(__name__)
classifier = pipeline("sentiment-analysis", "./distilBert/", framework="pt")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        text = GoogleTranslator(source="hi", target="en").translate(
            request.args.get("text")
        )

        if text == request.args.get("text"):
            raise Exception("Invalid Request")

        result = classifier(text)[0]

        if result["score"] < 0.75:
            result["label"] = "NEUTRAL"

        return jsonify(result)


if __name__ == "__main__":
    app.run()
