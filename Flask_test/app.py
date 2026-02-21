from flask import Flask, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "emp.json"
@app.route("/api", methods=["GET"])
def api():
    # Check if file exists
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "Data file not found"}), 404

    # Read data from file
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)
