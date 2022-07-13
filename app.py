import pickle
import numpy as np
from requests import Response
from flask import Flask, request

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
    array = np.frombuffer(bytes(request.form["array"], 'utf-8'), dtype=np.uint8)
    dims = pickle.loads(bytes(request.form["dims"], 'utf-8'))
    print(array.reshape(dims), dims)
    return np.ones((100, 100, 3), dtype=np.uint8).tobytes()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
