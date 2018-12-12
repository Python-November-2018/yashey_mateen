from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/danger')
def danger():
    print("a user tried to visit /danger. we have redirected the user to /")
    return redirect('/')

@app.route('/process', methods=['POST'])
def dojo_survey():
    survey = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'message': request.form['message']
    }
    print(survey)
    return render_template('results.html')

if __name__=='__main__':
    app.run(debug=True)