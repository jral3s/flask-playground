from flask import Flask, request
from requests import Response
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    dirs = '/ -> /hello -> /goodbye'
    return dirs

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/goodbye')
def goodbye():
    return 'Nope'

@app.route('/<name>')
def hello_name(name):
    return 'Hello, {}!'.format(name)

@app.route('/image', methods=['POST'])
def image():
    print(np.frombuffer(bytes(request.form["array"], 'utf-8'), dtype=np.uint8))
    return np.ones((100, 100, 3), dtype=np.uint8).tobytes()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
