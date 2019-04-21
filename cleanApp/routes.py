from cleanApp import app, db, bcrypt
from flask import render_template
from flask import url_for, flash, redirect
from cleanApp.forms import loginForm,registerForm,adminLoginForm, postForm
from flask_login import login_user,current_user, logout_user, login_required
from cleanApp.models import User,Post
from PIL import Image
import os,secrets

@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(usn=form.usn.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=True)
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

@app.route("/admin/dept")
def department():
    dept=['Computer Sci','Mechanical','Civil','E and C','E and E','Architecture','A and R','Outdoors']

@app.route("/admin/panel")
def panel():
    return render_template("admin-panel.html", title="Admin Panel")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
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
    posts=loadPosts()
    return render_template("posts.html", title="Posts", posts=posts)

#function for randomizing image file names and resizing
def resize(image_file):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(image_file.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/posts', picture_fn)

    img=Image.open(image_file)
    w,h=img.size
    if w>h:
        l=(w-h)//2
        left,top,right,bottom=l,0,w-l,h
    elif h>w:
        l=(h-w)//2
        left,top,right,bottom=0,l,w,h-l
    else:
        left,top,right,bottom=0,0,w,h
    img = img.crop((left,top,right,bottom))
    img.thumbnail((500,500))
    img.save(picture_path)
    return picture_fn

@app.route("/posts/create", methods = ['GET', 'POST'])
@login_required
def newPost():
    form = postForm()
    if form.validate_on_submit:
        if form.picture.data:
            picture_file = resize(form.picture.data)
            post = Post(title=form.shortDesc.data, content=form.briefDesc.data, location=form.location.data,
                    severity=form.degree.data, user_id=current_user.id, image_file=picture_file )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('posts'))
        else:
            pass
    return render_template("newPost.html", title="New Post", form=form)


def loadPosts():
    posts=Post.query.all()
    return posts