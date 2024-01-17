from flask import Flask,jsonify

# flask run

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def health():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    data = {
        'app': __name__,
        'uptime': uptime_seconds
    }
    return jsonify(data)

@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"