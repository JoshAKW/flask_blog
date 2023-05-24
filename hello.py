from flask import Flask, render_template

# create a flask instance

app = Flask(__name__)  # helps Flask find all the files in the directory

# create a route decorator

'''
safe - utilizes and hides the html
capitalize, captitalize first letter of first word
lower, all lower case text
upper, all upper case text
title, capitalize every first letter of ever word
trim, removes trailing spaces from the end
striptags, completely strips tags in jinja message, can be good for stripping hackers html
Can see list of built in filters on jinja
'''


@app.route('/')
def index():
    first_name = "Josh"
    stuff = "This is <strong> Bold</strong> Text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

# localhost:5000/user/John


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# set environement in command line, export FLASK_ENV=development    then type export FLASK_APP=hello.py
# This allows us to flask run

# create custom error pages

# Invalid URL


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


'''
 making an ssh, if we mkdir .ssh the dot makes it a hidden directory
 to creat an ssh key, ssh-keygen.exe (in the git bash terminal)
 enter for place, enter twice through the passwords... don't neccessarily need a password.
 generates a public and private key.

 then type cat (catalog command) so cat id_rsa.pub (for the public key)
 copy the key
 go to git hub, settings, look for ssh and GPG keys, enter new SSH, it will now recognize you from the terminal

 Now we make a gitignore file (for things like our virt) 
 type touch .gitignore
'''
