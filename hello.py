from flask import Flask, request, jsonify
import logging
from time import sleep


log_fmt  = "%(asctime)s [%(levelname)s]:  %(message)s"
date_fmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.INFO, format=log_fmt, datefmt=date_fmt)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping")
def ping():
    return ("Pong", 200)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    logging.info(f"data: {data}")

    if data is None:
        return "Need to add json content type", 400

    user_id = data.get("user_id", None)
    feature = data.get("feature", 0)
    if user_id is None:
        return "'user_id' missing", 400

    if feature is None:
        return "'feature' missing", 400


    return jsonify({"id": user_id, "predict": feature*13})
