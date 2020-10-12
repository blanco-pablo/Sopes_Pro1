# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os
import requests
servidorA = 'http://34.122.6.193/'
servidorB = 'http://35.232.235.137/'
app = Flask(__name__)

@app.route('/imp', methods=['POST'])
def imp():
    json = request.form.to_dict()
    # Consultar A y B
    # espero {'cantidad': 5, 'minRam': 4.5,'minCpu':1.2, status:200}
    response = requests.get(servidorA+"consulta")
    responseB = requests.get(servidorB+"consulta")
    if (response.status_code == 200 & responseB.status_code == 200):
        response_Json = response.json()
        response_JsonB = responseB.json()
        cantidadA = response_Json['cantidad']
        cantidadB = response_JsonB['cantidad']

        if  cantidadA > cantidadB:
            #Insertar en B
            print("Insert B")
            requests.post(servidorB+"insert")
        elif cantidadA == cantidadB:
            ramA = response_Json['minRam']
            ramB = response_JsonB['minRam']
            if ramA > ramB:
                #insert B
                print("Insertar B")
                requests.post(servidorB+"insert")
            elif ramA < ramB:
                #inserta A
                print("Insertar A")
                requests.post(servidorA+"insert")
            elif ramA == ramB:                
                cpuA = response_Json['minCpu']
                cpuB = response_JsonB['minCpu']
                #comparar CPU
                if cpuA > cpuB:
                    #insert B
                    print("Insertar B")
                    requests.post(servidorB+"insert")
                elif cpuA < cpuB:
                    #inserta A
                    print("Insertar A")
                    requests.post(servidorA+"insert")
                else:
                    #insert A
                    print("Insertar A")
                    requests.post(servidorA+"insert")
        else:
            #insert en A
            print("Insertar A")
            requests.post(servidorA+"insert")
        return 'OK'
    else:
        print(response.status_code)
        print(responseB.status_code)
        return 'MAL'

@app.route('/')
def hello_world():
    return 'api Servidor 1 ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
