from flask import Flask, render_template, request, redirect
import requests
import json
import flask.ext.login as flask_login
app = Flask(__name__)

login_manager = flask_login.LoginManager()
login_manager.init_app(app);

app.debug = True

@app.route('/')
def index():
    return render_template("labs.html")

@app.route('/login', methods=['POST'])
def login():
    redirect('/');

@app.route('/login')
def login_page():
    redirect('/');

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/verify/<username>')
def verify(username):
    req = requests.post('https://mc15.cs.purdue.edu:5001/user/verify/',
                                verify='server.cer',
                                data = json.dumps({'username': username,
                                        'verify': request.args.get("v")
                                        }))

    return render_template("verify.html", status=req.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
