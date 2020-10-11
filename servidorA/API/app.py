# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os
import json

app = Flask(__name__)

@app.route('/ram', methods=['POST'])
def ram():
    with open('/proc/mem_grupo18') as f:
        for line in f:
            a = line
        return json.loads(a)
    #with open('/proc/mem_grupo18') as f:
    #    data = json.load(f)
    #    print(data)
    return "algo"


@app.route('/')
def hello_world():
    return 'SERVIDOR A ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
