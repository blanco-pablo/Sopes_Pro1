# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/ram', methods=['POST'])
def ram():
    f = open("/proc/mem_grupo18", "r")
    print(f.read())
    return f.read()


@app.route('/')
def hello_world():
    return 'api ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
