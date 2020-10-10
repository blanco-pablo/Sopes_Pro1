# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os
app = Flask(__name__)

@app.route('/imp', method=['POST'])
def imp():
    nombre = request.form
    return nombre


@app.route('/')
def hello_world():
    return 'Hell!o, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
