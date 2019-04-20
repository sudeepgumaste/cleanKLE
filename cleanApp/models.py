from datetime import datetime
from flask_login import UserMixin
from cleanApp import db,login_manager


@login_manager.user_loader
def load_user(usn):
    return User.query.get(usn)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usn = db.Column(db.String(12), unique = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    branch = db.Column(db.String(2), nullable = False)
    sem = db.Column(db.Integer, nullable = False)
    phone = db.Column(db.String(10), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.usn}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column( db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    location = db.Column(db.String(15), nullable=False,)
    severity= db.Column(db.String(1), nullable=False)
    image_file = db.Column(db.String(30), nullable = False, default = 'default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"