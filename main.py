from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <form action= "http://localhost:1337/global" method = "post">
                    <p> Kalderwoche </p>
                    <p> <input type = "text" name = "KW"></p>
                    <p> <input type ="submit" value = "submit"></p>
                </form>
            </body>
        </html>
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
