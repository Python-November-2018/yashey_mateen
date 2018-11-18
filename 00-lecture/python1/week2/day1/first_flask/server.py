from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', color="Blue", my_list=["one", "two", "three"])

@app.route('/other')
def other():
    return render_template('other.html')

@app.route('/process', methods=["POST"])
def process():
    print("*"*80)
    print(request.form)
    print("*"*80)
    return redirect('/')

 
if __name__=="__main__":
    app.run(debug=True)



