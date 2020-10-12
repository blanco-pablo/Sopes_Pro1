# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
from flask import jsonify

import os
import json
import pymongo
import urllib.parse

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('rootpassword')
myclient = pymongo.MongoClient('mongodb://%s:%s@34.122.6.193:27017/' % (username, password))
mydb = myclient['mydatabase']
mycol = mydb["ram"]
mycpu = mydb["cpu"]

app = Flask(__name__)

@app.route('/consulta', methods=['GET'])
def consulta():
    listaRAM = []
    listaCPU = []
    #consulto la coleccion de RAM y agrego a un array
    for x in mycol.find():
        listaRAM.append(x['ram'])
    for x in mycpu.find():
        listaCPU.append(x['cpu'])

    #mando {'cantidad': 5, 'minRam': 4.5,'minCpu':1.2,status:200}
    return json.dumps({
        'cantidad' : len(listaRAM),
        'minRam' : min(listaRAM),
        'minCpu' : min(listaCPU)
    })

@app.route('/insert', methods=['POST'])
def ram():
    with open('/proc/mem_grupo18') as f:
        for line in f:
            a = json.loads(line)
            mydict = { "ram": a["total"] }
            x = mycol.insert_one(mydict)
    
    with open('/proc/cpu_grupo18') as f:
        for line in f:
            a = json.loads(line)
            cpu_usage = (a['TOTAL'] / 1000) / a['SEG']
            
            mydict = { "cpu": (cpu_usage/100) }
            x = mycpu.insert_one(mydict)

    return


@app.route('/')
def hello_world():
    return 'SERVIDOR A ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
