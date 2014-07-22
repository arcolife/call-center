# Import flask and template operators
from flask import Flask, render_template
# Import MongoEngine
from flask.ext.mongoengine import MongoEngine
# # Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
import sys
import os

# Define the WSGI application object
app = Flask(__name__)

####### User Login Hack BEGINS
# from flask.ext.login import LoginManager
# from flask.ext.openid import OpenID
# from config import BASE_DIR

# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(BASE_DIR, 'tmp'))
####### User Login Hack ENDS

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
#db = SQLAlchemy(app)
# # Build the database:
# # This will create the database file using SQLAlchemy
# db.create_all()

app.config["MONGODB_SETTINGS"] = { 
    "DB": os.environ.get("PLIVO_DB"),
    "USERNAME": os.environ.get("PLIVO_USER"),
    "PASSWORD": os.environ.get("PLIVO_PASS"),
    "HOST": "127.0.0.1",
    "PORT": 27017 }
db = MongoEngine(app)

def install_secret_key(app, filename='secret_key'):
    """Configure the SECRET_KEY from a file
    in the instance directory.

    If the file does not exist, print instructions
    to create it from a shell with a random key,
    then exit.
    """
    filename = os.path.join(app.instance_path, filename)

    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
        print('head -c 24 /dev/urandom > {filename}'.format(filename=full_path))
        sys.exit(1)

if not app.config['DEBUG']:
    install_secret_key(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)
