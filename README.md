Call-Center Demo
================
[![wercker status](https://app.wercker.com/status/87d785e8ae74f2f010b036369a4ae76c/m "wercker status")](https://app.wercker.com/project/bykey/87d785e8ae74f2f010b036369a4ae76c)

An attempt to develop a browser-based call-center. :neckbeard:

[Demo page](http://callcenter1.herokuapp.com/) <-- currently not fully functional

***
### Basic Steps to get started.

* Step 1: Register on Plivo and add some credit to get started

* Step 2: Buy a number to test the usability.

* Step 3: Execute the following commands in console:

  1. clone this repo; go to project root; run:
   ``` $ pip install -r requirements.txt ```

  2. To start an instance:
       ``` $ ./start ``` 
   OR 
	``` $ foreman start ```

* Step 4: Go to http://localhost:5000/ and start your own call center. :sunglasses: :stuck_out_tongue_closed_eyes:

* Step 5: Refer below for information on different URLs and their usage.

### Useful information

Different URL paths and their uses:
 
- /portal/<user_type>
  
  This is the login portal for customer/agent

- /agent/login
  
  changes agent's login status in DB (based on credentials from form)

- /agent/logout
  
  logs out agent.
  
- /call/route?CLID=1234
  
  Re-routes customer's call to a busy tone if agent not free. 

  Else replies in affirmative, as XML.

- /call/music/

  Return music as XML response for call on hold

***

### Notes

* CLID -> Caller ID
* Use Plivo's endpoints credentials to login
* Use shell.py to debug in realtime
* If you liked this, go to [this awesome voicechat demo](http://voicechatapi.com/) and try a conference call :smirk:
* Refer to TODO.md if you wish to contribute.