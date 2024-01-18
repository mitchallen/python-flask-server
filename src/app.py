from flask import Flask,jsonify
from src.api.uptime import Uptime

# poetry run python -m server

app = Flask(__name__)

# Create an instance of Uptime
uptime_instance = Uptime()

@app.route('/', methods = ['GET'])
def health():
    data = {
        'app': __name__,
        'uptime': uptime_instance.toHHMMSS()
    }
    return jsonify(data)

@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"