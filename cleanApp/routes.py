from cleanApp import app
from flask import render_template
from flask import url_for
from cleanApp.forms import loginForm

@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = loginForm()
    return render_template("login.html",title="Login", form=form)

@app.route("/register")
def register():
    return render_template("register.html",title="Register")

@app.route("/works")
def works():
    return render_template("works.html",title="How it works?")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.route("/what")
def what():
    return render_template("what.html", title="What is it for?")