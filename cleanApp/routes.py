from cleanApp import app, db, bcrypt
from flask import render_template
from flask import url_for, flash, redirect
from cleanApp.forms import loginForm,registerForm,adminLoginForm, postForm
from flask_login import login_user,current_user, logout_user, login_required
from cleanApp.models import User

@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(usn=form.usn.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'logged in as {user.usn}','success')
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
        if form.validate_on_submit():
            hasshed_passwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(usn = form.usn.data.lower(), username = form.username.data, email = form.email.data.lower(), password = hasshed_passwd,
                        branch = form.branch.data, sem = form.sem.data, phone = form.phone.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}! You can login now!', 'success')
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
