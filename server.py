from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template("labs.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.after_request
def cors(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
