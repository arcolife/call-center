#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################
# Plivo Call Center Demo #
##########################

import sys
from os import chmod, \
               getpid, \
               getppid
from shutil import copyfile
from time import time

from app import app, db
from app.users.decorators import requires_login
from app.users.models import User

from flask import Flask, \
                  render_template, \
                  request, \
                  Blueprint, \
                  flash, \
                  g, \
                  session, \
                  redirect, \
                  url_for

from config import \
    TEMPLATE_CONFIGURATION, \
    RESTRICT_BY_IP, \
    IPS, \
    HOST, \
    PORT, \
    DEBUG

@app.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    # # For SQLAlchemy based queries
    if 'user_id' in session:
        try:
            g.user = User.objects.get(id=session['user_id']).username
        except: 
            g.user = 'anonymous'
    for user in User.objects:
        print user.username
 
@app.route('/')
def home(users=None):
    """
    The web application main entry point.
    """   
    users = User.objects
    return render_template('index.html',
                           username=g.user,
                           users=users,
                           **TEMPLATE_CONFIGURATION)
    
@app.route('/call/')
def new():
    """
    The web application main entry point.
    """   
    return render_template('call.html',
                           user=g.user,
                           **TEMPLATE_CONFIGURATION)

@app.route('/<user_id>/')
def show(user_id):
    try:
        return render_template('profiles/'+user_id+'.html', user=user_id )
    except:
        return render_template('404.html')

@app.route('/test/')
@app.route('/test/<pg>/')
def test(pg='1'):
    """
    test page.
    """
    if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        return render_template('test'+pg+'.html', name="Human")
    else:
        return "Access denied."

@app.route('/save/', methods=['POST'])
def save_state():
    """
    Save the current state to a local file.
    """
    try:
        state = request.form.get('state')
        state = state.encode('utf-8')
        f = open(".state", "w")
        f.write(state)
        f.close()
        return "1"
    except:
        print e
        return "0"

@app.route('/load/', methods=['GET'])
def load_state():
    """
    Load the last state from a local file.
    """
    try:
        f = open(".state", "r")
        state = f.read()
        state = state.decode('utf-8')
        f.close()
        chmod(".state", 0600)
        return state
    except:
        return "|||"

@app.route('/reset/', methods=['GET'])
def reset_state():
    """
    Version the current state in a local file and reset it.
    """
    try:
        version = str(time())
        copyfile(".state", ".state.%s" % (version,))
        chmod(".state.%s" % (version,), 0600)
        f = open(".state", "w")
        f.write("")
        f.close()
        chmod(".state", 0600)
        return "1"
    except:
        return "0"

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
        # First, store the process ID
        save_pid()
        # Configure and start the web application 
        # with the given settings.
        app.run(host = HOST,
                port = PORT,
                #debug = True)
                debug = True)
    except:
        raise
