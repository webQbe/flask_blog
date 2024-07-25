from flask_wtf import FlaskForm
from wtforms import StringField, validators

# importing same fields from author/form.py 
from app.author.form import RegisterForm

class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.InputRequired(),
        validators.Length(max=80)
        ])
    