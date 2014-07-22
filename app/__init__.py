# Import flask and template operators
from flask import Flask, render_template
import sys
import os
import redis

# Define the WSGI application object
app = Flask(__name__)
app.redis = redis.StrictRedis(host=os.getenv('WERCKER_REDIS_HOST', 'localhost'),
      port= 6379, db=0)

# Configurations
app.config.from_object('config')

# def install_secret_key(app, filename='secret_key'):
#     """Configure the SECRET_KEY from a file
#     in the instance directory.

#     If the file does not exist, print instructions
#     to create it from a shell with a random key,
#     then exit.
#     """
#     filename = os.path.join(app.instance_path, filename)

#     try:
#         app.config['SECRET_KEY'] = open(filename, 'rb').read()
#     except IOError:
#         print('Error: No secret key. Create it with:')
#         full_path = os.path.dirname(filename)
#         if not os.path.isdir(full_path):
#             print('mkdir -p {filename}'.format(filename=full_path))
#         print('head -c 24 /dev/urandom > {filename}'.format(filename=full_path))
#         sys.exit(1)

# if not app.config['DEBUG']:
#     install_secret_key(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# from app.users.views import mod as usersModule
# app.register_blueprint(usersModule)
