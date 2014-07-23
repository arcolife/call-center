Call-Center Demo
================

An attempt to develop a browser-based call-center demo.

[Demo page](http://callcenter1.herokuapp.com/) <-- currently not fully functional

[![wercker status](https://app.wercker.com/status/87d785e8ae74f2f010b036369a4ae76c/m "wercker status")](https://app.wercker.com/project/bykey/87d785e8ae74f2f010b036369a4ae76c)

***

### Basic Steps to get started.

* Step 1: Register on Plivo and add some credit to get started

* Step 2: Buy a number to test the usability.

* Step 3: Execute the following commands in console:

  1. ``` $ pip install -r requirements.txt ```

  2. To start the instance
       
   ``` $ ./start ``` 
   
   OR 
   
   ``` $ foreman start ```

* Step 4: Go to http://localhost:5000/ and start your own call center. ;]

* Step 5: Refer below for information on different URL's and their usage.

### Useful information

- /agent
  
  This is the agent's login portal

- /customer

  This is the customer's sample call generation / login portal

- /call/status/AGENT_CLID
  
  This checks Agent's caller ID status (busy/free)

- /call/reset/AGENT_CLID

  This resets Agent's caller ID's status to Free

- /call/set/AGENT_CLID

  This sets Agent's caller ID's status to Busy

- /connect/CUST_CLID/AGENT_CLID

  Connects customer's call to a free agent; sets agent's status

- /connect/CUST_CLID/AGENT_CLID
  
  Diconnects customer's call from an agent; resets agent's status

- /handle/CUST_CLID
  
  Re-routes customer's call to a busy tone if agent not free.

***

### Notes

* CLID -> Caller ID
* Use Plivo's endpoints credentials to login
* Use shell.py to debug in realtime
