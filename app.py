from flask import Flask
import requests
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
    # request_data = request.get_json()
    # print(request)
    return np.ones((100, 100, 3), dtype=np.uint8).tobytes()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
