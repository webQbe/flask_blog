from __init__ import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    is_author = db.Column(db.Boolean)
    
# When sqlalchemy runs in this app, it maps out these columns on the table to
# these properties of the Author object.

    def __init__(self, fullname, email, username, password, is_author=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.is_author = is_author
    # * What happens when object is first defined 
    # * we need to pass certain columns to create the object
    # * This __init__ will only be called when you instantiate 
    #   Author class in a new object for the first time
    
    def __repr__(self):
        return '<Author %r>' % self.username
    # reproduce (repr) method allow you to display label records


    