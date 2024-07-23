import sys
import os
from dotenv import load_dotenv
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from __init__ import app, db

# Load environment variables
load_dotenv()

# Add the project directory to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print("System path:", sys.path)

# Import the Flask app
from __init__ import app, db

# Initialize the database
#db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080))  
    )




app = Flask(__name__)
app.config.from_object('flask_blog.settings')


from blog import views  
from author import views

