from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'
if __name__=="__main__":
    app.run(debug=True)

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    if(name=="john"):
        return "Hi" + name + "!"
    print(name)
    return "Hi" + name

@app.route('/repeat/<x>/<string>')
def repeat(x, string):
    num=int(x)
    for i in range(num):
        print(string)
        return string
      
      