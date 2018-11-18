from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<x>/<y>')
def checkerboard(x,y):
    x=int(x)
    y=int(y)
    return render_template('checkerboard.html', x, y)


