Call-Center Demo
================

An attempt to develop a browser-based call-center demo.

[Demo page](http://callcenter1.herokuapp.com/) <-- currently not fully functional

[![wercker status](https://app.wercker.com/status/87d785e8ae74f2f010b036369a4ae76c/m "wercker status")](https://app.wercker.com/project/bykey/87d785e8ae74f2f010b036369a4ae76c)

***

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
