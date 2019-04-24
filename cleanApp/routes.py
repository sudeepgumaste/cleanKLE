from cleanApp import app, db, bcrypt
from flask import render_template, abort, request
from flask import url_for, flash, redirect
from cleanApp.forms import loginForm,registerForm,adminLoginForm, postForm, updateForm, commentForm
from flask_login import login_user,current_user, logout_user, login_required
from cleanApp.models import User,Post
from PIL import Image
import os,secrets


#generic routes
@app.route("/works")
def works():
    return render_template("works.html",title="How it works?")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.route("/what")
def what():
    return render_template("what.html", title="What is it for?")

#All authentication routes
@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(usn=form.usn.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=True)
            flash(f'logged in as {user.usn}','success')
            return redirect(url_for('posts')) 
        else:
            flash('Check your USN and password and login again!', 'danger')
    return render_template("login.html",title="Login", form=form)


@app.route('/logout')
def logout():
    if current_user.actype=='student':
        to='login'
    else:
        to='admin'
    logout_user()
    return redirect(url_for(to))


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

#end of authentication routes
#All post related routes

@app.route("/posts")
@login_required
def posts():
    posts=Post.query.all()
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
    return render_template("newPost.html", title="New Post", form=form, legend='Post')

@app.route("/post/<int:post_id>")
def iso_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = commentForm()
    return render_template('post.html', title=post.title, post=post, form=form)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    form = updateForm()
    if form.validate_on_submit():
        post.title = form.shortDesc.data
        post.content = form.briefDesc.data
        post.location = form.location.data
        post.severity = form.degree.data
        if form.picture.data:
            post.image_file = resize(form.picture.data)
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('iso_post', post_id=post.id))
    elif request.method == 'GET':
        form.shortDesc.data=post.title
        form.briefDesc.data=post.content
        form.degree.data = post.severity
        form.picture.data = post.image_file
    else:
        print(form.errors)
    return render_template('newPost.html', title='Update Post', form=form, legend = 'Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author!=current_user and current_user=='student' :
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted",'success')
    return redirect(url_for('posts'))

#End of post related routes

#All admin related routes
@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    form = adminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print(True)
            login_user(user,remember=True)
            flash(f'logged in as {user.username}','success')
            return redirect(url_for('location')) 
        else:
            flash('Check your username and password and login again!', 'danger')
    return render_template("admin.html",title="Admin", form=form)

@app.route("/admin/location")
@login_required
def location():
    if current_user.actype=='student':
        abort(403)
    locs = [['MB','Main Building'],['ME','Mechanical Building'],['CV','Civil Department'],
            ['MC','Main Canteen'],['EC', 'E and C Building'],['CL','C-Lite'],['LH','LHC Area'],
            ['AC','Architecture'],['BT','Bio Tech Building']]

    for i in range(len(locs)):
        locs[i].append(len(Post.query.filter(Post.location==locs[i][0] and Post.resolved==False).all()))

    print(locs)
    return render_template('locations.html', locs=locs)

@app.route("/admin/location/<string:loc_name>")
@login_required
def panel(loc_name):
    if current_user.actype=='student':
        abort(403)
    posts=Post.query.filter_by(location=loc_name)
    return render_template("admin-panel.html", title="Admin Panel", posts=posts)

