from flask import Flask,render_template,jsonify,request,redirect,url_for

print("Testing Addition of FILE")
app = Flask(__name__)

@app.route('/') #Home API
def hello_Flask():
    print("Welcome to Flask")
    return render_template('login.html')


@app.route('/result/<name>')
def result(name):
    return f'Hello {name} you are in Result API'


@app.route('/login',methods =['POST','GET'])


def login():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        print("We are in Login API")
        print("NAME:",name)
        return redirect(url_for('result',name=name))


app.run()