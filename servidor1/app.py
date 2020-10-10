# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/imp', methods=['POST'])
def imp():
    json = request.form.to_dict()
    
    return 'OK'


@app.route('/')
def hello_world():
    return 'api ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
