from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    greeting = 'Hello User'
    return render_template("index.html", greeting=greeting)


@app.route("/", methods=['POST'])
def output_interface():
    fname = request.form['fname']
    return render_template("output.html", fname=fname)
