# Import flask and template operators
from flask import Flask, render_template
import sys
import os
import redis
from werkzeug import generate_password_hash

# Define the WSGI application object
app = Flask(__name__)
app.redis = redis.StrictRedis(host=os.getenv('WERCKER_REDIS_HOST', 'localhost'),
      port= 6379, db=0)

# Configurations
app.config.from_object('config')

app.redis.set(app.config['AGENT_CALLER_ID'], app.config['SIP_ENDPOINT'])

app.redis.set('agentLoggedIn',0)
app.redis.set('agentReady',0)
app.redis.set('customerLoggedIn',0)

# app.redis.set(app.config['SIP_ENDPOINT'],0) 
# TODO: add models and set this only when logged in

app.redis.hmset('agent',{'username': app.config['SIP_ENDPOINT'],
                         'password': generate_password_hash(
                             os.environ.get('PLIVO_PASS'))
                     })


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from RedisQueue import RedisQueue as rq
#app.register_blueprint(rq)

q = rq('userQueue')
