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


#@app.before_request
@app.route('/call/set/<CLID>', methods=['GET','POST'])
def set_call_status(CLID=None):
    """
    set call status
    """
    #data = dict(call_id=CLID, call_status=1)
    app.redis.set(CLID, 1)
    print "%s status set to busy" % (CLID)
    return Response("Status set to Busy for <b>CLID:<b> " + CLID)

#@app.before_request
@app.route('/call/reset/<CLID>', methods=['GET','POST'])
def reset_call_status(CLID=None):
    """
    reset call status
    """
    app.redis.set(CLID, 0)
    print "Agent %s's status set to Ready" % (CLID)
    return Response("Status set to Ready for <b>CLID:<b> " + CLID)
    
@app.route('/call/status/<CLID>', methods=['GET','POST'])
def check_call_status(CLID=None):
    """
    check call status
    """
    call_status = app.redis.get(CLID)
    if call_status=='1':
        print "Agent %s is busy!" % (CLID)
        return Response("busy")
    elif call_status=='0':
        print "Agent %s is free to consult!" % (CLID)
        return Response("free")
    else:
        return Response("does not exist")

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
