from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, EmailField
#from wtforms.fields.html5 import EmailField

# create a class that creates fields that are rendered
class RegisterForm(FlaskForm):
    fullname = StringField('Full Name', [validators.InputRequired()])
    email = EmailField('Email', [validators.InputRequired()])
    username = StringField('Username',[
        validators.InputRequired(),
        validators.Length(min=4, max=25)
        ])
    password = PasswordField('New Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=4, max=80)
        ])
    confirm = PasswordField('Repeat Password')