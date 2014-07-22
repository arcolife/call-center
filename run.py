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
    json

from config import \
    HOST, \
    PORT, \
    DEBUG,\
    TEMPLATE_CONFIGURATION


#@app.before_request
@app.route('/')
def home(users=None):
    """
    Landing Page: contains links to login portals.
    """
    return render_template('index.html',
                           username=None,
                           users=users,
                           **TEMPLATE_CONFIGURATION)


@app.route('/call/set/<CLID>', methods=['GET','POST'])
def set_call_status(CLID=None):
    """
    set agent status to busy
    """
    #data = dict(call_id=CLID, call_status=1)
    app.redis.set(CLID, 1)
    print "%s status set to busy" % (CLID)
    return Response("Status set to <u>Busy</u> for <b>CLID:<b> " + CLID)


@app.route('/call/reset/<CLID>', methods=['GET','POST'])
def reset_call_status(CLID=None):
    """
    reset agent status to free
    """
    if app.redis.exists(CLID):
        app.redis.set(CLID, 0)
        print "Agent %s's status set to Ready" % (CLID)
        return Response("Status set to <u>Ready</u> for <b>CLID:<b> " + CLID)
    else:
        return Response("Agent " + CLID + " Does Not Exist!")


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


@app.route('/agent')    
def agent_portal():
    """
    Agent's login portal.
    """
    #resp = Response("""sent call generation request. <a href="/">Go back.</a>""")
    return render_template('agent.html')


@app.route('/customer')    
def customer_portal():
    """
    Customer's login portal.
    """
    return render_template('customer.html')


@app.route('/connect/<cust_CLID>/<agent_CLID>', methods=['GET','POST'])
def connect_call(cust_CLID=None, agent_CLID=None):
    """
    connect customer's call to agent.
    """
    set_call_status(CLID=agent_CLID)
    return Response("skeleton that is supposed to connect customer's call to agent")


@app.route('/disconnect/<cust_CLID>/<agent_CLID>', methods=['GET','POST'])
def disconnect_call(cust_CLID=None, agent_CLID=None):
    """
    disconnect customer's call from agent.
    """
    reset_call_status(CLID=agent_CLID)
    return Response("skeleton that is supposed to disconnect customer's call from agent")


@app.route('/handle/CLID', methods=['GET','POST'])
def reroute_customer(CLID=None):
    """
    Re-routes customer to busy tone.
    """
    return Response("skeleton that is supposed to reroute customer to a busy tone.")


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
