from flask_blog import app
from flask import render_template, redirect, url_for, session
from author.form import RegisterForm, LoginForm
from author.models import Author

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None
    
    if form.validate_on_submit():
        author = Author.query.filter_by(
            username = form.username.data,
            password = form.password.data
            ).limit(1)
        if author.count(): # if author count is not 0  
            session['username'] = form.username.data  
            return redirect(url_for('login_success'))
    return render_template('author/login.html', form=form, error=error)
    #print("Login route accessed")
    #return "Hello, User!"
    
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
    

@app.route('/login_success')
def login_success():
    return "Author logged in!"
    
    
@app.route('/test')
def test():
    print("Test route accessed")
    return "Test route is working!"