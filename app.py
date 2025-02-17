from flask import Flask, redirect, render_template, request, jsonify
import os
import sys
from src.textsummarizer.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

# Home route
# @app.route("/")
# def index():
#     return redirect("/docs")

# Mock docs route (you can replace this with actual API documentation)
# @app.route("/docs")
# def docs():
#     return render_template("docs.html")


@app.route("/")
def index():
    return redirect("/predict")

# Training route
@app.route("/train", methods=["GET"])
def training():
    try:
        os.system("python main.py")
        return jsonify({"message": "Training completed successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"Error while training: {str(e)}"}), 500

# Prediction route\
@app.route("/predict", methods=["GET", "POST"])
def predict_route():
    summary = None
    if request.method == "POST":
        try:
            text = request.form.get("text", "")
            pipeline = PredictionPipeline()
            summary = pipeline.predict(text)
        except Exception as e:
            summary = f"Error: {str(e)}"
    return render_template("predict.html", summary=summary)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)