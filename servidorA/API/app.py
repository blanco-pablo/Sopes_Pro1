# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os
import json
import pymongo

myclient = pymongo.MongoClient('mongodb://34.122.6.193:27017/')
mydb = myclient['mydatabase']
mycol = mydb["ram"]

app = Flask(__name__)

@app.route('/ram', methods=['POST'])
def ram():
    with open('/proc/mem_grupo18') as f:
        for line in f:
            a = json.loads(line)
        
        cad = ''
        for x in mycol.find():
            cad = str(cad) + str(x)
        return a["total"] + str(cad)
    return ""


@app.route('/')
def hello_world():
    return 'SERVIDOR A ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
