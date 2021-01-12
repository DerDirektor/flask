from flask import Flask, url_for, request, render_template, redirect, jsonify
from werkzeug.utils import secure_filename
import werkzeug
import os
import json #json empfangne

app = Flask(__name__)
folder = r"C:\Users\Administrator\PycharmProjects\flask"  #os und redirect
extentions = {'png', 'PNG', 'pdf'}




# prüfe ob datei erlaubt ist:
def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extentions



@app.route('/', methods =['POST', 'GET'])
def index():
    return "SSL"


@app.route('/logging/')
def loog():
    app.logger.info('Hier ist ein loog')# zum aktivitäten loog
    return "SSL"

@app.route('/postme/', methods=['POST'])
def postme():
        postedjson = json.loads(request.data.decode('uft-8')) # jsondaten ausleden actung hier entsteht ein string
        print(postedjson)
        return ('passt')

@app.errorhandler(werkzeug.exceptions.NotFound)
def notfound(e):
    return jsonify (error=str(e)), e.code

if __name__ == '__main__':
    app.run(port=1337,  debug= True, threaded = True)