<<<<<<< HEAD
homepage-gen
============

This is a hack of the original repository - http://www.github.com/kasioumis/wemig

- Ref: http://homepagegen.tk
- Demo: http://minimalist.herokuapp.com

This is a tool supposed to help hackers and builders generate minimalistic homepages.

***

ORIGINAL IDEA

*** 

What is wemig?
--------------

### Introduction

"wemig" stands for "WEekly MInutes Generator". It's a small web application
that provides an intuitive interface to write and manage your weekly minutes.
It offers 2-level categorization (categories --> subcategories --> text) for
the minutes and produces the corresponding HTML code using unordered lists and
list items.

### Features

* New categories, subcategories and text can be added anywhere in the minutes.
* Autocompletion is offered for all category and subcategory names.
* All text can be edited and deleted simply by clicking on it.
* Categories, subcategories and all text can be moved around and reordered.
* All changes are saved and loaded automatically.
* Deployed locally and accessible (to specific IPs) through a web broswer.

Installation
------------

### Dependencies

* Python - http://www.python.org/
* Git - http://git-scm.com/
* Flask - http://flask.pocoo.org/
    * Jinja2 - http://jinja.pocoo.org/
    * Werkzeug - http://werkzeug.pocoo.org/

### Installation

Clone the latest development sources:
"$ git clone https://github.com/kasioumis/wemig.git"

### Configuration

All configuration options can be found in the python configuration fule:
"minutes_config.py"

Running
-------

### Deployment

If you simply want to run the web application as the current user you should run:

"$ python minutes.py"

If you want to permanently run the web application in the background you should
login as root, change the "USER" variable in the "start" bash script (to the
user you want to run the web application as) and run:

"# ./start"

Still as root, you my stop the web application by running:

"# ./stop"

### Tested with

* Debian 6.0.6
* Python 2.7.3
* Flask 0.8
* Jinja2 2.6
* Werkzeug 0.8.3
* Opera 12.14
* Chrome 24.0.1312.56
* Iceweasel (Firefox) 10.0.12
* Debian Web 3.4.2
=======
call-center
===========

demo implementation for a call center.
>>>>>>> b170fbbd09bec748a0959ef5af424f7470f64343
