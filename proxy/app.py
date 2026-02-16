from flask import Flask
import requests

app = Flask(__name__)

@app.route("/service-a")
def a():
    return requests.get("http://service-a-container:5001").text

@app.route("/service-b")
def b():
    return requests.get("http://service-b-container:5002/data").text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
