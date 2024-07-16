from flask_blog import app
from flask import render_template, redirect, url_for
from author.form import RegisterForm

@app.route('/login')
def login():
    print("Login route accessed")
    return "Hello, User!"
    
#define app route for registration
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    print("Register route accessed")
    # checking if form is submitted
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)
    
@app.route('/success')
def success():
    return "Author registered!"
    
    
@app.route('/test')
def test():
    print("Test route accessed")
    return "Test route is working!"