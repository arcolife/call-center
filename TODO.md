- [x] basic stack (flask-redis)
- [x] add plivo SDK based scripts
- [x] wercker-integrated builds / tests
- [x] landing page / web-page structures
- [x] integrate landing page, customer page and agent page using Jinja2
- [x] minimal functionalities to dial a number / SIP endpoint
- [x] skeleton of all the functionalities in run.py
- [x] plivo dashboard
  - [x] buy numbers
  - [x] add applications
  - [x] add SIP endpoints
  - [x] connect numbers to SIP endpoints
  - [x] test demo apps
    - [x] demo dial
    - [x] demo speak
    - [x] demo play 

- [x] heroku integration
  - [ ] redis based verified account

***

- [x] host on an instance (since no heroku verified account present)
- [x] add functionalities to call queue handling method
- [x] add agent login status models
- [x] associate datetime with userQueue in redis # NOT NEEDED
- [x] connect flask routes to SDK
- [ ] add threading to queue (poll status)

***

- [x] investigate busy / unavailable issue
- [x] investigate same SIP being called when different(UK/US) numbers dialed
  - [x] use of fallback URL
  - [ ] use of an alternate tone (.ogg) file

***

- [ ] test modules
  - [ ] call receive 
  - [x] call dial
  - [x] call hold
  - [x] call hangup