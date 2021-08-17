from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world(debug=True):
    return "<p>Hello, World!2</p>"

@app.route("/bye")
def bye():
    return '<h1>BYE</h1>'

