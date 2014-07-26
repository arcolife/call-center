#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################
# Plivo Call Center Demo #
##########################

import sys
import redis
import plivo 
import datetime

from app import app, q
from werkzeug import check_password_hash

from flask import Flask, \
    render_template, \
    Response, \
    json, \
    make_response, \
    request, \
    redirect

from config import \
    HOST, \
    PORT, \
    DEBUG,\
    TEMPLATE_CONFIGURATION, \
    CALL_WAIT_MESSAGE, \
    CALL_ANNOUNCEMENT, \
    HOLD_MUSIC, \
    SIP_ENDPOINT, \
    AGENT_CALLER_ID, \
    AGENT_NOT_LOGGEDIN, \
    AGENT_DOESNT_EXIST


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

@app.route('/agent/hangup', methods=['GET','POST'])
@app.route('/agent/login', methods=['GET','POST'])
def agent_set():
    # plivo_user = app.redis.hget('agent','username')
    # plivo_pass = app.redis.hget('agent','password')
    # resp_user = request.args.get('username')
    # resp_pass = request.args.get('password')
    # if plivo_user == resp_user:
    #     if check_password_hash(plivo_pass, resp_pass):
    #         app.redis.set('agentLoggedIn',1)
    app.redis.set('agentLoggedIn',1)
    app.redis.set('agentReady',1)
    return Response('1')

@app.route('/agent/busy', methods=['GET','POST'])
def agent_busy():
    app.redis.set('agentLoggedIn',1)
    app.redis.set('agentReady',0)
    return Response('0')

@app.route('/agent/logout', methods=['GET','POST'])
def agent_reset():
    app.redis.set('agentLoggedIn',0)
    app.redis.set('agentReady',0)
    return Response('0')

@app.route('/query/queue')
def query_queue():
    if q.qsize():
        return q.get()

@app.route('/call/route', methods=['GET','POST'])
def call_route(CLID=None):
    """
    Re-routes customer to busy tone or to the agent.
    """
    # if app.redis.exists(SIP_ENDPOINT): # if agent exists
    # else:
    #     plivo_response.addSpeak(AGENT_DOESNT_EXIST)
    # temp_val = int((datetime.datetime.now() - \
    #                 datetime.datetime(2014, 7, 7))\
    #                .total_seconds() * 1000)
    plivo_response = plivo.XML.Response()
    if app.redis.get('agentLoggedIn') == '1': # if agent logged in
        if app.redis.get('agentReady') == '1': # if agent available
            # app.redis.set('agentReady', 0) # agent set to busy
            plivo_response.addWait(length=3) # build XML response
            plivo_response.addSpeak(CALL_ANNOUNCEMENT) # begin call forwarding
            plivo_response.addDial(callerId=AGENT_CALLER_ID)\
                          .addUser('sip:'+SIP_ENDPOINT+'@phone.plivo.com')
        else:
            cust_CLID = request.args.get('CLID')
            if cust_CLID:
                q.put(cust_CLID) # add user to queue
            return redirect('/call/music') # put user on hold
    else:
        plivo_response.addSpeak(AGENT_NOT_LOGGEDIN)            
    response = make_response(render_template('response_template.xml',
                                             response=plivo_response))
    response.headers['content-type'] = 'text/xml'
    return response

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
