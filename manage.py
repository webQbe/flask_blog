import sys
import os
from dotenv import load_dotenv


# Ensure the project directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask_blog import app

load_dotenv()  # This loads the environment variables from .env

if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080))  
        # Use port 8080 as it's typically open in Cloud9
    )







'''import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_blog import app

manager = Manager(app)

manager.add_command("runserver", Server(
        use_debugger = True,
        use_reloader = True,
        host = os.getenv('IP', '0.0.0.0'),
        port = int(os.getenv('PORT', 5000))
    )
)

if __name__ == "__main__":
    manager.run()'''