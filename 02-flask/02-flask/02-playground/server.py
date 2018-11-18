from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

 @app.route('/play')
 def play():
     return render_template('index.html', times=3)

@app.route('/play/<x>')
def playx(x):
    num=int(x)
    return render_template('index.html', times=num)

@app.route('/play/<x>/<boxcolor>')   
def playbox(x, boxcolor):
    num=int(x)
    return render_template('index.html', times=num, boxcolor)

    