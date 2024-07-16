from flask_wtf import Form
# import validators to validate data
from wtforms import validators, StringField, PasswordField 
from wtforms.fields.html5 import EmailField

# create a class that creates fields that are rendered
class RegisterForm(Form):
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Username',[
        validators.Required(),
        validators.Length(min=4, max=25)
        ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=4, max=80)
        ])
    confirm = PasswordField('Repeat Password')