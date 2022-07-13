import pickle
import numpy as np
from flask import Flask, Response, request

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
    # array = np.frombuffer(bytes(request.form["array"], 'utf-8'), dtype=np.uint8).copy()
    # dims = pickle.loads(bytes(request.form["dims"], 'utf-8'))
    req = pickle.loads(request.get_data())
    array = req["array"]
    dims = req["dims"]

    print(array.reshape(dims), dims)
    array[0] = 0

    data = pickle.dumps({"array": array, "dims": dims}, 0)

    return Response(data)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
