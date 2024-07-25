import sys
import os
from dotenv import load_dotenv
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate, upgrade
#from flask_script import Manager
from app import create_app, db

app = create_app()


@app.cli.command()
def init_db():
    """Initialize the database."""
    upgrade()
    """Initialize the database.
    with app.app_context():
        # Run `flask db upgrade` to apply migrations
        from flask_migrate import upgrade
        upgrade()
    """

# Load environment variables
load_dotenv()

# Add the project directory to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print("System path:", sys.path)



#manager = Manager(app)

migrate = Migrate(app, db)


# Add the db command to the manager
# manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    app.run(
            debug=True,
            host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 8080))
        )


# Initialize Flask-Migrate and Manager
# migrate = Migrate(app, db)

# @app.cli.command()
# def init_db():
#    """Initialize the database."""
#    upgrade()

# Initialize the database
#db = SQLAlchemy(app)


#if __name__ == "__main__":
#    app.run(
#       debug=True,
#        host=os.getenv('IP', '0.0.0.0'),
#        port=int(os.getenv('PORT', 8080))  
#    )




#app = Flask(__name__)
#app.config.from_object('flask_blog.settings')


#from blog import views  
#from author import views

