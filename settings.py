import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'Admin'
DB_PASSWORD = 'admin123'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = 'flask-db.c9a06k6cqktv.ap-southeast-1.rds.amazonaws.com'
port = 3306
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI