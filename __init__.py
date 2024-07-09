import sys
import os
from flask import Flask


# Ensure the settings module is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



app = Flask(__name__)
app.config.from_object('flask_blog.settings') 

# Use 'flask_blog.settings' for absolute import

# Import any other necessary modules here
# from . import other_modules

# For example, if you have a view module
# from .views import some_view_function


# Import views to register routes
from flask_blog.home import views  
# Adjust the import if the structure is different