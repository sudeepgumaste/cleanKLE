from cleanApp import app
from flask import render_template
from flask import url_for
from cleanApp.forms import loginForm,registerForm,adminLoginForm


@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = loginForm()
    return render_template("login.html",title="Login", form=form)

@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    form = adminLoginForm()
    return render_template("admin.html",title="Admin", form=form)

@app.route("/register")
def register():
    form = registerForm()
    return render_template("register.html",title="Register", form=form)

@app.route("/works")
def works():
    return render_template("works.html",title="How it works?")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.route("/what")
def what():
    return render_template("what.html", title="What is it for?")

@app.route("/admin/panel")
def panel():
    return render_template("admin-panel.html", title="Panel")