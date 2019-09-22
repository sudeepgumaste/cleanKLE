from datetime import datetime
from flask_login import UserMixin
from cleanApp import db,login_manager


@login_manager.user_loader
def load_user(username):
        return User.query.get(username)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    profile_pic = db.Column(db.String(30), nullable = False, default = "default.jpg")
    usn = db.Column(db.String(12), unique = True, default=None)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = True, default=None)
    password = db.Column(db.String(60), nullable = False)
    branch = db.Column(db.String(2), nullable = True, default=None)
    sem = db.Column(db.Integer, nullable = True, default=None)
    phone = db.Column(db.String(10), nullable = True, default=None)
    actype = db.Column(db.String(7), nullable = True, default='student')
    posts = db.relationship('Post', backref = 'author', lazy = True)
    comments = db.relationship('Comments', backref = 'quoter', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.usn}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column( db.String(19), nullable = False, default = str(datetime.now())[:19])
    content = db.Column(db.Text, nullable = False)
    location = db.Column(db.String(15), nullable=False,)
    severity= db.Column(db.String(1), nullable=False)
    image_file = db.Column(db.String(30), nullable = False, default = 'default.jpg')
    resolved = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    admin_comment = db.Column(db.String(100),nullable=False, default = '')
    comments_all = db.relationship('Comments', backref = 'quote_on', lazy = True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(150),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)
    
    def __repr__(self):
        return f"Comment('{self.comment}',{self.user_id}, {self.post_id})"
        