Call-Center Demo
================

An attempt to develop a browser-based call-center demo.

[Demo page](http://callcenter1.herokuapp.com/) <-- currently not fully functional

[![wercker status](https://app.wercker.com/status/87d785e8ae74f2f010b036369a4ae76c/m "wercker status")](https://app.wercker.com/project/bykey/87d785e8ae74f2f010b036369a4ae76c)

** Useful information

- /agent
  
  This is the agent's login portal

- /customer

  This is the customer's sample call generation / login portal

- /call/status/<CLID>
  
  This checks the caller ID's status (busy/free)

- /call/reset/<CLID>

  This resets the caller ID's status to Free

- /call/set/<CLID>

  This sets the caller ID's status to Busy