from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError


class loginForm(FlaskForm):
    usn = StringField('USN', validators=[DataRequired()])

    password = PasswordField ('Password', validators=[DataRequired()])

    login = SubmitField ('Login')


class registerForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=5, max=10)])

    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password')])

    usn = StringField('USN', validators=[DataRequired()])

    branch  = StringField('Branch', validators=[DataRequired()])

    

    submit = SubmitField('Sign Up')