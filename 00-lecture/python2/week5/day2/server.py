from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", method=['POST'])
def create():
    print(request.form)
    print('Name', request.form['name'])
    print('Email', request.form['email'])
    return render_template("created.html")

if __name__=="__main__":
    app.run(debug=True)