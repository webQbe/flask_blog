# flask_blog

##3.03 - Creating SQLAlchemy Database

### Rename / move 'home' directory to 'blog'

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




##3.04 - Defining a Class for Models

### Define a class in ```models.py``` that defines the author object







 
