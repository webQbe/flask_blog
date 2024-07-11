import sys
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_blog import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()

app = Flask(__name__)
app.config.from_object('flask_blog.settings')

db = SQLAlchemy(app)

from flask_blog.blog import views  
from flask_blog.author import views

if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080))  
    )
