import pickle
import flask
from flask import Flask, render_template, request
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression

# Load your Multiple Linear Regression model
with open("MLR_Model_pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)


@app.route("/")
def fun():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def prediction():
    # Explicitly extract each field to maintain strict feature order
    rnd = float(request.form["rnd"])
    admin = float(request.form["admin"])
    marketing = float(request.form["marketing"])
    state = float(request.form["state"])  # 0: New York, 1: California, 2: Florida

    # Form the 2D feature array: shape (1, 4)
    features = np.array([[rnd, admin, marketing, state]])

    # Generate prediction
    prediction_result = model.predict(features)[0]

    # Format result to 2 decimal places
    formatted_result = f"{prediction_result:,.2f}"

    return render_template("index.html", prediction_text=formatted_result)


if __name__ == "__main__":
    app.run(debug=True)