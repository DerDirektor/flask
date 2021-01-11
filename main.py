from flask import Flask, url_for, request, render_template, redirect,flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
folder = r"C:\Users\Administrator\PycharmProjects\flask"  #os und redirect
extentions = {'png', 'PNG', 'pdf'}




# prüfe ob datei erlaubt ist:
def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extentions



@app.route('/', methods =['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No File')
            return redirect(request.url)  # wenn keineDatei hochgeladen wird, dann wird zur zurückgeletut
        file = request.files['file']
        if file.filename =='':
            return redirect(request.url) # wenn filename leer
        if allowed(file.filname):
            filename = secure_filename(file.filname) # wenn file ja, und Endung stimmt
            file.save(os.path.join(folder, filename))
            return redirect(request.url)

    return '''
        <h1>Lade</h1>
        <form methode =post enctype= multipart/form-data>
        <input type=file name=file>
        <input type=submit value= hochladen>
    '''



@app.route('/global', methods = ['POST','GET'])
def global_site():
    kw ='1'
    if request.method == 'POST':
        kw = request.form ['KW']
    else:
        kw = request.args.get('KW')

    return " Es ist die " + kw +". Kalenderwoche"



if __name__ == '__main__':
    app.run(port=1337,  debug= True)