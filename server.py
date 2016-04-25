from flask import Flask, render_template
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
    return render_template("login.html")

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
