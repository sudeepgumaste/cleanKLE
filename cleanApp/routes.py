from cleanApp import app
from flask import render_template
from flask import url_for

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html",title="Login")

@app.route("/works")
def works():
    return render_template("works.html",title="How it works?")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.route("/what")
def what():
    return render_template("what.html", title="What is it for?")