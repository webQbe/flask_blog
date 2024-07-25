#from __init__ import app
from flask import render_template, redirect, url_for, session, request
from app.author.form import RegisterForm, LoginForm
from app.models import Author
from app import db
from . import author
from app.author.decorators import login_required

@author.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)
    if form.validate_on_submit():
        author = Author.query.filter_by(
            username = form.username.data,
            password = form.password.data
            ).limit(1)
        if author.count(): # if author count is not 0  
            session['username'] = form.username.data  
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
                return redirect(url_for('login_success'))
        else:
            error = "Incorrect username and password"
    return render_template('author/login.html', form=form, error=error)
    #print("Login route accessed")
    #return "Hello, User!"
    
#define app route for registration
@author.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print("Register route accessed")
    # checking if form is submitted
    if form.validate_on_submit():
        return redirect(url_for('author.success'))
    return render_template('author/register.html', form=form)
    
@author.route('/success')
def success():
    return "Author registered!"
    

@author.route('/login_success')
@login_required # you need to log in before landing on login_success
def login_success():
    return "Author logged in!"
    
    
@author.route('/test')
def test():
    print("Test route accessed")
    return "Test route is working!"