from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError


class loginForm(FlaskForm):
    usn = StringField('USN', validators=[DataRequired()])

    password = PasswordField ('Password', validators=[DataRequired()])

    login = SubmitField ('Login')

class adminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField ('Password', validators=[DataRequired()])

    login = SubmitField ('Login')


class registerForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=5, max=10)])

    password = PasswordField('Password', validators = [DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password')])

    usn = StringField('USN', validators=[DataRequired()])

    branch  = SelectField('Branch', choices = [('CS','Computer Sci'), ('ME', 'Mechanical'), ('CV','Civil'),
                                         ('EC', 'E and C'), ('EE', 'E and E'), ('AC', 'Architecture')
                                         , ('AR', 'A and R')] )
    
    sem = SelectField('Semister', choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')])
    
    phone = StringField('Phone no.', validators=[DataRequired(), Length(min=5, max=10)])

    submit = SubmitField('Sign Up')
