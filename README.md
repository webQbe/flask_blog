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

Create ```author/forms.py```. 
Create ```RegisterForm``` class in ```forms.py```
Define a new app route in ```author/views.py```

Create folder ```templates/author```
Create file ```templates/author/register.html``` where 
  ```base.html``` will be extended.
 

