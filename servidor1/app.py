# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os
import requests
servidorA = 'http://34.122.6.193/'
servidorB = 'http://34.122.6.193/consulta'
app = Flask(__name__)

@app.route('/imp', methods=['POST'])
def imp():
    json = request.form.to_dict()
    # Consultar A y B
    # espero {'cantidad': 5, 'minRam': 4.5,'minCpu':1.2, status:200}
    response = requests.post(servidorA+"consulta")
    
    if response.text == 'OK': 
        print("DATO ENVIADO")
    else:
        print("ERROR en ENVIO")
    return 'OK'


@app.route('/')
def hello_world():
    return 'api ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
