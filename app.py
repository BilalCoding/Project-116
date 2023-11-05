# Importing modules from flask library
from flask import Flask , render_template

# Creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# Write the routes using decorator functions
# Default route or 'URL'
@app.route("/")

def home():
    # Write your name
    name = "Bilal"
    # Write your age
    age = "14"
    return render_template('index.html' , name = name , age = age)

# Define the route to father webpage
@app.route("/father")

def father():
    name = "Asim"
    age = "51"
    return render_template('father.html', name = name, age = age)

# Define the route to mother webpage
@app.route("/mother")

def mother():
    name = "Sana"
    age = "47"
    return render_template('mother.html', name = name, age = age)

# Define the route to friends webpage
@app.route("/friend")

def friend():
    name = "Khashan"
    age = "14"
    return render_template('friend.html', name = name, age = age)

# Run the file
if __name__  ==  '__main__':
    app.run(debug=True)