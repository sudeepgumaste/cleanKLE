from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from cleanApp import db
from cleanApp.models import User
from flask_login import current_user

class loginForm(FlaskForm):
    usn = StringField('USN', validators=[DataRequired()])

    password = PasswordField ('Password', validators=[DataRequired()])

    login = SubmitField ('Login')

class adminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField ('Password', validators=[DataRequired()])

    login = SubmitField ('Login')


class registerForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators = [DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password')])

    usn = StringField('USN', validators=[DataRequired()])

    profile_pic = FileField('Choose your profile picture', validators=[FileAllowed(['jpg','jpeg', 'png', 'bmp'])])

    branch  = SelectField('Branch', choices = [('CS','Computer Sci'), ('ME', 'Mechanical'), ('CV','Civil'),
                                         ('EC', 'E and C'), ('EE', 'E and E'), ('AC', 'Architecture')
                                         , ('AR', 'A and R')])
    
    sem = SelectField('Semester', choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')])

    phone = StringField('Phone no.', validators=[DataRequired(), Length(min=10, max=10)])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is already taken, please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data.lower()).first()
        if user:
            raise ValidationError('That email is already taken, please choose a different email.')

    def validate_usn(self, usn):
        user = User.query.filter_by(usn = usn.data.lower()).first()
        if user:
            raise ValidationError('That USN is already taken. please contact us if it is yours.')


class postForm(FlaskForm):
    shortDesc = StringField('Title', validators=[DataRequired(),Length(min=5,max=25)])

    location = SelectField('Location', choices=[('CL','Clite'), ('ME','Mech. Building'), ('CV','Civil'), ('LH','LHC'),
                                                ('MB','Main Building'), ('BT','Bio Tech.'), ('AC','Architecture'), 
                                                ('EC','E and C'), ('MC','Main Canteen'), ('OT','Others'),] )

    degree = RadioField('Degree of discomfort', validators=[DataRequired()],choices=[('1', '<i class="fas fa-frown-open text-info h3"></i>'), ('2', '<i class="fas fa-sad-tear text-info h3"></i>'),
                         ('3', '<i class="fas fa-sad-cry text-info h3"></i>'), ('4', '<i class="fas fa-dizzy h3 text-info"></i>') , ('5', '<i class="fas fa-radiation-alt h3 text-info"></i>')])

    picture = FileField('Choose the image file', validators=[FileAllowed(['jpg','jpeg', 'png']),DataRequired()])

    briefDesc = TextAreaField('Brief Description', validators=[DataRequired()])

    submit = SubmitField('Post')


class updateForm(FlaskForm):
    shortDesc = StringField('Title', validators=[DataRequired(),Length(min=5,max=25)])

    location = SelectField('Location', choices=[('CL','Clite'), ('ME','Mech. Building'), ('CV','Civil'), ('LH','LHC'),
                                                ('MB','Main Building'), ('BT','Bio Tech.'), ('AC','Architecture'), 
                                                ('EC','E and C'), ('MC','Main Canteen'), ('OT','Others'),] )

    degree = RadioField('Degree of discomfort', validators=[DataRequired()],choices=[('1', '<i class="fas fa-frown-open text-info h3"></i>'), ('2', '<i class="fas fa-sad-tear text-info h3"></i>'),
                         ('3', '<i class="fas fa-sad-cry text-info h3"></i>'), ('4', '<i class="fas fa-dizzy h3 text-info"></i>') , ('5', '<i class="fas fa-radiation-alt h3 text-info"></i>')])

    picture = FileField('Choose the image file', validators=[FileAllowed(['jpg','jpeg', 'png'])])

    briefDesc = TextAreaField('Brief Description', validators=[DataRequired()])

    submit = SubmitField('Post')

class commentForm(FlaskForm):
    comment = StringField('comment', validators=[DataRequired()])
    submit = SubmitField('Comment')
