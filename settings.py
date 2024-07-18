import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'you-will-never-guess'
DEBUG = True

DB_USERNAME = 'admin'
DB_PASSWORD = 'admin123'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = 'flask-db.c9a06k6cqktv.ap-southeast-1.rds.amazonaws.com'
DB_PORT = 3306

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{BLOG_DATABASE_NAME}"
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
#SQLALCHEMY_DATABASE_URI = DB_URI
#SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

