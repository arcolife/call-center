#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################
# Plivo Call Center Demo #
##########################

import sys
import redis

from os import chmod, \
               getpid, \
               getppid
from shutil import copyfile
from time import time
from app import app

from flask import Flask, \
    render_template, \
    request, \
    Response, \
    json, \
    Blueprint, \
    flash, \
    g, \
    session, \
    redirect, \
    url_for

from config import \
    HOST, \
    PORT, \
    DEBUG

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


@app.route("/clouds.json")
def clouds():
  data = app.redis.lrange("clouds", 0, -1)
  resp = Response(json.dumps(data), status=200, mimetype='application/json')
  return resp


@app.route('/call')    
def generate():
    resp = Response("""sent call generation request. <a href="/">Go back.</a>""")
    return resp
    
def save_pid():
    """
    Get the process ID and store it in a local file.
    """
    try:
        pid = getpid()
        ppid = getppid()
        if ( ppid != 1 ):
            pid = ppid
        f = open(".pid", "w")
        f.write(str(pid))
        f.close()
        chmod(".pid", 0600)
    except:
        pass


if __name__ == '__main__':
    try:
        app.run(host = HOST,
                port = PORT,
                debug = DEBUG)
    except:
        raise
