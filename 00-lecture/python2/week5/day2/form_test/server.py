from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
#this route will handle our form submission
#notice how we defined which HTTP methods are allowed by this route
# the server is listening for a POST request to: localhost:5000/users
# we define the route below such that the route matches the action of our form = '/users'
# similarly we need to allow specific methods - 'POST' in this case
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # recall the name attributes we added to our form inputs
    # to accesss the data that the user input into the fields we use request.form['name_of_input']
    name = request.form['name']
    email = request.form['email']
    # redirects back to the '/' route
    return redirect('/')
if __name__=="__main__":
    # run our server
    app.run(debug=True)

# my_data = request.form['name_of_input']

# Important! Always redirect after handling POST data to avoid data being handled more than once! 


