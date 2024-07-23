# flask_blog

# Creating SQLAlchemy Database

Rename / move 'home' directory to 'blog'

On terminal:

```mv home blog```

```python manage.py runserver```

### Access mysql database

On terminal:

```mysql -h flask-db.c9a06k6cqktv.ap-southeast-1.rds.amazonaws.com -P 3306 -u admin -p```

On MySQL CLI:

```
MySQL [(none)]> SHOW DATABASES;  
MySQL [(none)]> CREATE DATABASE blog;  
MySQL [(none)]> SHOW DATABASES;
```

Ctrl+D  to exit MySQL CLI

Add database info to ```settings.py```

Add sqlalchemy to ```init.py```

Create ```author``` module
Inside ```author``` create ```views.py``` and ```models.py```

Add placehoder things to ```views.py```

Add ```init.py``` files to ```author``` and ```blog```


# Defining a Class for Models

Define a class in ```models.py``` that defines the author object



# Discussing the ORM Interactions

Create ```Author``` class in ```author/models.py``` file.

Go to upper directory :
``` cd .. ``

Open python shell:

CLI:
```python```

Python shell:
```
>>> from flask_blog import app, db
>>> from flask_blog.author.models import *
>>> with app.app_context():
...     db.create_all()

```

Check database with another terminal window:
```mysql -h flask-db.c9a06k6cqktv.ap-southeast-1.rds.amazonaws.com -P 3306 -u admin -p```
```MySQL [(none)]> SHOW DATABASES;
MySQL [(none)]> USE blog;
MySQL [blog]> SHOW TABLES;
MySQL [blog]> SELECT * FROM author;
```

To initiate an ```Author``` object, pass the parameters:



Back to python shell:
```
>>> from flask_blog import app, db
>>> from flask_blog.author.models import *
>>> with app.app_context():
...  db.create_all()
...  author = Author(
...  'Ishan Senarath', 'ishan@webcubesolutions.lk', 'ishan', '12345', True
...  )

```
Try to call ```author```:
```
>>> author
<Author 'ishan'>
```

Username is passed into  ```__repr__()``` in ```author/models.py```.

Create a session to add the record to database:

```with app.app_context():
    db.session.add(author)
    db.session.commit()
```
    
Check database again:

``` SELECT * FROM author;```


Fetch author id:
```with app.app_context():
    db.session.add(author)
    db.session.commit()
    author.id
```

Fetch  fullname:

```
>>> from flask_blog import app, db
>>> from flask_blog.author.models import *
>>> with app.app_context():
...  db.create_all()
...  author = Author(
...  'Ishan Senarath', 'ishan@webcubesolutions.lk', 'ishan', '12345', True
...  )
...  db.session.add(author)
...  db.session.commit()
...  author.fullname
... 
'Ishan Senarath'
```

Create another author:

```
>>> with app.app_context():
...  author = Author(
...  'John Smith', 'john@example.com', 'john', '12345', True
...  )
...  author
... 
<Author 'john'>
```

Add new author:
```
with app.app_context():
...  db.session.add(author)
...  db.session.commit()

```

Check database using:
``` SELECT * FROM author;
```
    
See all authors:

```
>>> with app.app_context():
...  authors = Author.query.all()
...  authors
... 
[<Author 'ishan'>, <Author 'john'>]

```

Fetch the first item of author list:
```
>>> with app.app_context():
...  authors = Author.query.all()
...  authors[0]
... 
<Author 'ishan'>
```
Fetch the 2nd item of author list:
```
>>> with app.app_context():
...  authors = Author.query.all()
...  authors[1]
... 
<Author 'john'>
```

Get fullname of second author:
```
>>> with app.app_context():
...  authors = Author.query.all()
...  authors[1].fullname
... 
'John Smith'
``` 

Use ```query.filter_by()``` and get only the first record using ```.first()``` :
```
>>> with app.app_context():
...  authors = Author.query.filter_by(username='ishan').first()
...  authors
... 
<Author 'ishan'>
```

Erase all tables:

Open a new terminal window:

```
>>> from flask_blog import app, db
>>> from flask_blog.author.models import *
>>> with app.app_context():
...  db.session.commit()
...  db.drop_all()

```
Check database:
```MySQL [blog]> SHOW TABLES;```


# Building the Base with Bootstrap

Create new folder ```templates```
(All the templates for the app is stored here.)

Create ```templates/base.html``` 

# Managing ‘Flask-wtforms’ Validators

Install Flask-wtforms:
Add ```flask-wtf``` to ```requirements.txt``` file.
On terminal, ```pip install -r requirements.txt```

Create ```author/forms.py``` file. 
Create ```RegisterForm``` class in ```forms.py```
Define a new app route in ```author/views.py```

Create folder ```templates/author```
Create file ```templates/author/register.html``` where 
  ```base.html``` will be extended.
  
  
# Adding Errors Messages into Forms
  
```flask_blog``` folder copied to ```venv/lib/python3.9/site-packages/flask_blog/```

Run ```manage.py``` using ```python manage.py```.
Preview app route ```/register```.

Add flask code to ```author/register.html``` file.
Add ```/success``` route to ```author/views.py```

Try entering invalid data to see error messages.


# Explaining Macros for Web Development

Macros allow us to make pieces of templates.

Replacing code in ```author/register.html``` file with macros:  
Create ```templates/_formhelpers.html``` file to define macros.

Run ```python manage.py``` and enter different passwords on the form to see if 
"Passwords must match" message displays.

Enter data correctly and click 'Register' button to see if you're redirected to
"Author registered!" page.

# Creating the Blog ‘SetupForm’ Class

Create ```blog/models.py``` file to create ```Blog``` class.
Create ```blog/form.py``` file to create ```SetupForm``` class.
Import similar fields from ```RegisterForm``` class in ```author/form.py``` file.



# Describing the Blog Admin and Creation Form

Working on blog's presentation layer.

Create ```templates/blog``` folder.  
Create ```admin.html``` and ```setup.html``` files inside ```templates/blog```. 

Work on ```blog/views.py```.

Run python shell:
```
from flask_blog import app, db
with app.app_context():
    db.create_all()
    db.session.commit()
```


Check whether there are ```tables``` on ```blog``` database:
```MySQL [(none)]> USE blog;  
MySQL [blog]> SHOW TABLES;
```

Run server with ```python manage.py``` command.
Go to route ```'/admin'```, to see if 'Blog Creation' form is loading.


# Associating the Database Author Forms

Before we submit the 'Blog Creation' form, we need to be able to do database operations in 
```blogs/views.py``` file.

Run  ```python manage.py``` and preview ```'/admin'```,
enter form data, leave "Full Name" blank to check error message.
re-enter data and click "Create Blog" button.

Go to mysql database and check whether data have been entered.

```
MySQL [(none)]> SHOW DATABASES;
MySQL [(none)]> USE blog;
MySQL [blog]> SHOW TABLES;
MySQL [blog]> SELECT * FROM author;
MySQL [blog]> SELECT * FROM blog; 
```

'admin id' in table 'blog' is the foreign key which acts as a pointer.


# Implementing a Login Function Form

Check the databases and tables:

```
SHOW DATABASES;
USE blog;
SHOW TABLES;
```
See records:

```SELECT * FROM author;```

Create LoginForm class in ```author/form.py```.
Create ```templates/author/login.html```.
Let's start setting up a login function in ```author/views.py```.
Run ```manage.py``` and preview ```/login```.

Start doing database operations in ```author/views.py```.
- First look up an author that has username and password that we have on the form.

Check login form error messages by :
- only filling password field.
- filling wrong password

Check if "Author logged in!" message displays by fillng correct data.

 
# Using the Decorator Function

Make sure people are logged in before they access a route.
Create your own "Login required!" decorator.

Add ```@login_required``` decorator to ```blog/views.admin()```,
to check if the person is logged in already.

Move following blog checking code from ```admin()``` to ```index()```:
    ```
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    ```
So, if you hit the homepage, it will get you to the blog setup instead of admin.

Create ```author/decorators.py``` to define ```login_required()```.
Modify ```blog/views.py ``` and ```author/views.py```.

Run ```manage.py``` and go to login form.
- Log in
- Open Developer Tools.
- Go to Application > Cookies > Session
- Delete the session and reload page to log out.

When you log out, you go into login page through a url with ```next```: 
```/login?next=http://a45792d2eebc4598aad6d843a4a4432f.vfs.cloud9.ap-southeast-1.amazonaws.com/login_success```
