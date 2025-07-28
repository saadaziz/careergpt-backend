import logging
from flask import Flask, request, jsonify
import os

# Configure logging to stderr (Passenger captures this automatically)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Flask app running on cPanel via Passenger"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    # Do your processing here
    return jsonify({"received": data, "status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
