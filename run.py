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
    AGENT_CALLER_ID

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


# def agent_status_update():
#     if app.redis.exists(SIP_ENDPOINT):
#         app.redis.set(SIP_ENDPOINT, 0)
#     else:
#         return False
#     return True

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


@app.route('/call/route', methods=['GET','POST'])
def call_route(CLID=None):
    """
    Re-routes customer to busy tone or to the agent.
    """
    plivo_response = plivo.XML.Response()
    if app.redis.exists(SIP_ENDPOINT): # if agent logged in
        if not int(app.redis.get(SIP_ENDPOINT)): #if agent available
            plivo_response.addWait(length=2)
            plivo_response.addSpeak(CALL_ANNOUNCEMENT)

            app.redis.set(SIP_ENDPOINT, 1) #set to busy
            # forward call to SIP endpoint
            plivo_response.addDial(callerId=AGENT_CALLER_ID)\
                          .addUser('sip:'+SIP_ENDPOINT+'@phone.plivo.com')
        else:
            # increment queued users count
            app.redis.incr('queuedUsers')
            # add user to queued list
            cust_CLID = request.args.get('custID') # TODO: add datetime
            app.redis.rpush('userQueue', cust_CLID)
            # put user on hold
            return redirect('/call/music')
    else:
        # no such agent found
        plivo_response.addSpeak('Agent does not exist or not logged in!')
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
