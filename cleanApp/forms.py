from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError


class loginForm(FlaskForm):
    usn = StringField('usn', validators=[DataRequired()])

    password = PasswordField ('password', validators=[DataRequired()])

    login = SubmitField ('Login')