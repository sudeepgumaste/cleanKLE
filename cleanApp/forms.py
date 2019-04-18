from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from cleanApp import db

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

    password = PasswordField('Password', validators = [DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password')])

    usn = StringField('USN', validators=[DataRequired()])

    branch  = SelectField('Branch', choices = [('CS','Computer Sci'), ('ME', 'Mechanical'), ('CV','Civil'),
                                         ('EC', 'E and C'), ('EE', 'E and E'), ('AC', 'Architecture')
                                         , ('AR', 'A and R')], validators = [DataRequired()])
    
    sem = SelectField('Semester', choices = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8')],
                        validators = [DataRequired()])

    phone = StringField('Phone no.', validators=[DataRequired(), Length(min=10, max=10)])

    submit = SubmitField('Sign Up')

class postForm(FlaskForm):
    shortDesc = StringField('Short Description', validators=[DataRequired(),Length(min=5,max=25)])

    location = SelectField('Location', choices=[('CL','Clite'), ('ME','Mech. Building'), ('CV','Civil'), ('LH','LHC'),
                                                ('MB','Main Building'), ('BT','Bio Tech.'), ('AC','Architecture'), 
                                                ('EC','E and C'), ('MC','Main Canteen'), ('OT','Others'),] )

    degree = RadioField('Degree of discomfort', validators=[DataRequired()],choices=[(1, ''), (2, ''), (3, ''), (4, '') , (5, '')])

    image = FileField('Image file', validators=[FileAllowed(['jpg','jpeg', 'png'])])

    briefDesc = TextAreaField('Brief Description', validators=[DataRequired()])

    submit = SubmitField('Post')