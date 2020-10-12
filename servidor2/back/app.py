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
myclientB = pymongo.MongoClient('mongodb://%s:%s@35.232.235.137:27017/' % (username, password))

mydb = myclient['mydatabase']
mycol = mydb["ram"]
mycpu = mydb["cpu"]
mydata = mydb["data"]

mydbB = myclientB['mydatabase']
mycolB = mydbB["ram"]
mycpuB = mydbB["cpu"]
mydataB = mydbB["data"]

app = Flask(__name__)

@app.route('/consulta', methods=['GET'])
def consulta():
    listaRAM = []
    listaCPU = []
    listaRAMB = []
    listaCPUB = []
    #consulto la coleccion de RAM y agrego a un array
    for x in mycol.find():
        listaRAM.append(x['ram'])
    for x in mycpu.find():
        listaCPU.append(x['cpu'])
    
    for x in mycolB.find():
        listaRAMB.append(x['ram'])
    for x in mycpuB.find():
        listaCPUB.append(x['cpu'])

    #mando {'cantidad': 5, 'minRam': 4.5,'minCpu':1.2,status:200}
    return json.dumps({
        'ramA' : listaRAM[len(listaRAM)-1],
        'cpuA' : listaCPU[len(listaCPU)-1],
        'ramB' : listaRAMB[len(listaRAMB)-1],
        'cpuB' : listaCPUB[len(listaCPUB)-1]
    })

@app.route('/usu', methods=['GET'])
def usuarios():
    A = []
    B = []
    #consulto la coleccion de RAM y agrego a un array
    for x in mydata.find():
        A.append(x)
    for x in mydataB.find():
        B.append(x)

    for i in A:
        i['_id'] = 'DATO'
        print(i['_id'])

    for i in A:
        print(i)
    
    return json.dumps(A)

@app.route('/')
def hello_world():
    return 'SERVIDOR 2 ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
