from cleanApp import app, db, bcrypt
from flask import render_template
from flask import url_for, flash, redirect
from cleanApp.forms import loginForm,registerForm,adminLoginForm, postForm
from flask_login import login_user,current_user, logout_user, login_required
from cleanApp.models import User

@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        print (form.usn.data)
        print (form.password.data)
        usr = User.query.filter_by(usn=form.usn.data).first()
        if usr and form.password.data == usr.password:
            login_user(usr)
            flash(f'logged in as{usr.usn}','success')
            return redirect(url_for('posts')) 
        else:
            flash('Check your USN and password and login again!', 'danger')
    return render_template("login.html",title="Login", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    form = adminLoginForm()
    return render_template("admin.html",title="Admin", form=form)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}. Please login', 'success text-center')
        return redirect(url_for('login'))
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

@app.route("/posts")
@login_required
def posts():
    return render_template("posts.html", title="Posts")

@app.route("/createpost")
def newPost():
    form = postForm()
    return render_template("newPost.html", title="Posts", form=form)
