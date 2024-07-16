import sys
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Ensure the settings module is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



app = Flask(__name__)
app.config.from_object('flask_blog.settings') 

db = SQLAlchemy(app)

from flask_blog.author import views  # Import your views here

# Add some debug prints to ensure routes are being registered. 
print("Registered routes:")
for rule in app.url_map.iter_rules():
    print(rule)

# Use 'flask_blog.settings' for absolute import

# Import any other necessary modules here
# from . import other_modules

# For example, if you have a view module
# from .views import some_view_function





# Import views to register routes
from flask_blog.blog import views  
# Adjust the import if the structure is different

from flask_blog.author import views

# Print registered routes for debugging
print("Registered routes:")
for rule in app.url_map.iter_rules():
    print(rule)
