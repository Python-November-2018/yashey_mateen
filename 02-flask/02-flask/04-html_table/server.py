from flask import Flask, render_template, redirect, session, request

app=Flask(__name__)
app.secret_key="alsdjflajsf"


users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
)


@app.route('/')
def index():
    users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
    )
    return render_template('index.html', user_list=users)



if __name__== "__main__":
    app.run(debug=True)

