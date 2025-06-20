from flask import Flask, jsonify, Response
from src.api.uptime import Uptime

# poetry run python -m server

app = Flask(__name__)

# Create an instance of Uptime
uptime_instance: Uptime = Uptime()


@app.route("/", methods=["GET"])
def health() -> Response:
    data = {"app": __name__, "uptime": uptime_instance.toHHMMSS()}
    return jsonify(data)


@app.route("/hello")
def hello_world() -> str:
    return "<p>Hello, World!</p>"
