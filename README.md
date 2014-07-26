Call-Center Demo
================
[![wercker status](https://app.wercker.com/status/87d785e8ae74f2f010b036369a4ae76c/m "wercker status")](https://app.wercker.com/project/bykey/87d785e8ae74f2f010b036369a4ae76c)

An attempt to develop a browser-based call-center. :neckbeard:

[Demo page](http://callcenter1.herokuapp.com/) <-- currently not fully functional 
      
(since it's not a verified account, hence RedisDB integration not possible)

***
### Basic Steps to get started.

* Step 1: Register on Plivo and add some credit to get started

* Step 2: Buy a number to test the usability.

* Step 3: Connect number to applitcation-type: DirectDial, 

       	  Config: Answer_url - http://URL_OR_IP_WHERE_HOSTED/call/route

* Step 4: Add an endpoint and connect it to the number you bought.

* Step 5: Execute the following commands in console:

  1. clone this repo; go to project root; run:
   ``` $ pip install -r requirements.txt ```

  2. To start an instance:
       ``` $ ./start ``` 
   OR 
	``` $ foreman start ```

* Step 6: Go to http://localhost:5000/ and start your own call center. :sunglasses: :stuck_out_tongue_closed_eyes:

* Step 7: Refer below for information on different URLs and their usage.

### Useful information

Different URL paths and their uses:
 
- /portal/<user_type>
  
  This is the login portal for customer/agent

- /call/route?CLID=9999999999
  
  Re-routes customer's call to a busy tone if agent not free. And adds to queue.

  Else gets connected to the free agent and wait for an answer.

- /call/music/

  Return music (in XML response) for call on hold.

***

### Notes

* CLID -> Caller ID
* Use Plivo's endpoints credentials to login
* Use shell.py to debug in realtime
* If you liked this, go to [this awesome voicechat demo](http://voicechatapi.com/) and try a conference call :smirk:
* Refer to TODO.md if you wish to contribute.