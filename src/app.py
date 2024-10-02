"""
Application main service
"""

import os

from flask import Flask, request, jsonify
import pandas as pd

from src.inference import load_model, predict


app = Flask(__name__)

MODEL_PATH = os.path.join("models", "model_in_docker.joblib")
MODEL = load_model(MODEL_PATH)


@app.route("/")
def helthcheck():
    return "Iris prediction service is running!"

# {
#     "sepal_length": 5.1,
#     "sepal_width": 3.3,
#     "petal_length": 1.7,
#     "petal_width": 0.5,
# }


@app.route("/predict", methods=["POST"])
def prediction():
    """
    Function to predict the iris species

    Returns
    -------
    prediction
        The predicted iris species
    """
    try: 
        data = request.json
        df = pd.DataFrame(data, index=[0])
        df = df.reset_index(drop=True)
        prediction = predict(MODEL, df)
        
        return jsonify({"prediction": str(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})
