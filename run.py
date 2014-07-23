#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################
# Plivo Call Center Demo #
##########################

import sys
import redis
import plivo 

from app import app

from flask import Flask, \
    render_template, \
    Response, \
    json, \
    make_response

from config import \
    HOST, \
    PORT, \
    DEBUG,\
    TEMPLATE_CONFIGURATION, \
    CALL_WAIT_MESSAGE, \
    CALL_ANNOUNCEMENT, \
    HOLD_MUSIC

#@app.before_request
@app.route('/')
def index(users=None):
    """
    Landing Page: contains links to login portals.
    """
    return render_template('home.html',
                           username=None,
                           users=users,
                           landing_page=True,
                           **TEMPLATE_CONFIGURATION)


@app.route('/portal/<user_type>')    
def portal(user_type):
    """
    login portal.
    """
    return render_template('portal.html', user_type=user_type)


@app.route('/call/status/set/<CLID>', methods=['GET','POST'])
def call_status_set(CLID=None):
    """
    set agent status to busy
    """
    #data = dict(CLID=CLID, status=1)
    app.redis.set(CLID, 1)
    return Response("Status set to <u>Busy</u> for <b>CLID:<b> " + CLID)


@app.route('/call/status/reset/<CLID>', methods=['GET','POST'])
def call_status_reset(CLID=None):
    """
    reset agent status to free
    """
    if app.redis.exists(CLID):
        app.redis.set(CLID, 0)
        return Response("Status set to <u>Ready</u> for <b>CLID:<b> " + CLID)
    else:
        return Response("Agent " + CLID + " Does Not Exist!")


@app.route('/call/status/check/<CLID>', methods=['GET','POST'])
def call_status_check(CLID=None):
    """
    check call status
    """
    call_status = app.redis.get(CLID)
    if call_status=='1':
        return Response("busy")
    elif call_status=='0':
        return Response("free")
    else:
        return Response("does not exist")


@app.route('/call/connect/<cust_CLID>/<agent_CLID>', methods=['GET','POST'])
def call_connect(cust_CLID=None, agent_CLID=None):
    """
    connect customer's call to agent.
    """
    set_call_status(CLID=agent_CLID)
    return Response("skeleton that is supposed to connect customer's call to agent")


@app.route('/call/disconnect/<cust_CLID>/<agent_CLID>', methods=['GET','POST'])
def call_disconnect(cust_CLID=None, agent_CLID=None):
    """
    disconnect customer's call from agent.
    """
    reset_call_status(CLID=agent_CLID)
    return Response("skeleton that is supposed to disconnect customer's call from agent")


@app.route('/call/music/', methods=['GET', 'POST'])
def call_music():
    """
    Renders the XML to be used for hold music in the call.
    """
    plivo_response = plivo.XML.Response()
    plivo_response.addSpeak(CALL_WAIT_MESSAGE)
    plivo_response.addPlay(HOLD_MUSIC, loop=1)
    response = make_response(render_template('response_template.xml', 
                                             response=plivo_response))
    response.headers['content-type'] = 'text/xml'
    return response


@app.route('/call/route/CLID', methods=['GET','POST'])
def call_reroute_customer(CLID=None):
    """
    Re-routes customer to busy tone.
    """
    return Response("skeleton that is supposed to reroute customer to a busy tone.")


@app.route("/clouds.json")
def clouds():
    """
    test method.
    """    
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
