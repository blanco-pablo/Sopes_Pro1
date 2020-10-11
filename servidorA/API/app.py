# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os
import json
import pymongo
import urllib.parse

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('rootpassword')
myclient = pymongo.MongoClient('mongodb://%s:%s@34.122.6.193:27017/' % (username, password))
mydb = myclient['mydatabase']
mycol = mydb["ram"]

app = Flask(__name__)

@app.route('/ram', methods=['POST'])
def ram():
    with open('/proc/mem_grupo18') as f:
        for line in f:
            a = json.loads(line)
        
        listaRAM = []
        for x in mycol.find():
            cad = x['ram']
        return str(a["total"]) + str(cad)
    return ""


@app.route('/')
def hello_world():
    return 'SERVIDOR A ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
