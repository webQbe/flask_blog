import sys
import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

load_dotenv()

app = Flask(__name__)
app.config.from_object('config') 


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Debugging output
    print("SQLALCHEMY_DATABASE_URI:", app.config['SQLALCHEMY_DATABASE_URI'])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    #migrate = Migrate(app, db)
        
    # Register Blueprints
    from app.author import author as author_blueprint
    app.register_blueprint(author_blueprint)

    from app.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)
    
    # Ensure models are imported
    #with app.app_context():
    #    from app.models import Author, Blog  # Import your models here

    return app

# Import models here to avoid circular imports
from app.models import Author
from app.models import Blog


print("Registered routes:")
for rule in app.url_map.iter_rules():
    print(rule)

# Enable SQLAlchemy logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


# Ensure the settings module is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
