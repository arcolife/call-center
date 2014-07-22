#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################
# Plivo Call Center Demo #
##########################

import sys
import redis

from app import app

from flask import Flask, \
    render_template, \
    Response, \
    json, \
    g, \
    session, \
    redirect, \
    url_for

from config import \
    HOST, \
    PORT, \
    DEBUG,\
    TEMPLATE_CONFIGURATION


@app.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        try:
            g.user = User.objects.get(id=session['user_id']).username
        except: 
            g.user = 'anonymous'

@app.route('/')
def home(users=None):
    """
    The web application main entry point.
    """   
    return render_template('index.html',
                           username=g.user,
                           users=users,
                           **TEMPLATE_CONFIGURATION)

@app.route('/agent')    
def receive_call():
    #resp = Response("""sent call generation request. <a href="/">Go back.</a>""")
    return render_template('agent.html')

@app.route('/customer')    
def generate_call():
    return render_template('customer.html')

@app.route("/clouds.json")
def clouds():
  data = app.redis.lrange("clouds", 0, -1)
  resp = Response(json.dumps(data), status=200, mimetype='application/json')
  return resp


if __name__ == '__main__':
    try:
        app.run(host = HOST,
                port = PORT,
                debug = DEBUG)
    except:
        raise
