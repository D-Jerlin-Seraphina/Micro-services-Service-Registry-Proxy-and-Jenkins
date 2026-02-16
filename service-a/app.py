from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Service A is running"

@app.route("/call")
def call():
    try:
        registry = json.load(open("registry.json"))
        return requests.get(registry["service-b"] + "/data").text
    except:
        return "Error calling Service B"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
