- [x] basic stack (flask-redis)
- [x] add plivo SDK based scripts
- [x] wercker-integrated builds / tests
- [x] landing page / web-page structures
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

- [ ] host on an instance (since no heroku verified account present)
- [ ] minmal functionalities to receive a call
- [ ] refine status labels (modify JS) 
- [ ] refine agent/customer interface
- [ ] integrate landing page, customer page and agent page using Jinja2
- [ ] add functionalities to call queue handling method
- [ ] investigate busy / unavailable issue
- [ ] investigate same SIP being called when different(UK/US) numbers dialed
  - [ ] use of fallback URL
  - [ ] use of an alternate tone (.ogg) file

***

- [ ] test modules
  - [ ] call receive 
  - [ ] call dial
  - [ ] call hold
  - [ ] call hangup