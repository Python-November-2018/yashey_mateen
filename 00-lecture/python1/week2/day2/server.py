from flask import Flask, render_template, redirect, session, request

app=Flask(__name__)
app.secret_key = "as;dlfja;sdfjlasrfsfja;sfdj;j"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/variables/<color>/<num>')
def variables(color, num):
    print(color, num)
    return render_template('variables.html', title="Variables Page", col=color, number=num)

@app.route('/process', methods=['POST']) 
def process():
    
    session['username'] = request.form['username']
    return redirect('/success')
   ## return render_template('success.html', user=username)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)








