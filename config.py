#!/usr/bin/python
# -*- coding: utf-8 -*-

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "#%^@^%^*THD33SDFCVWRB%vergsdpxry02%%"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

# Secret key for signing cookies
SECRET_KEY = "#$FSDFSETE^$TFEFV#$%$&"

###################
# Template settings
###################

# Dictionary that holds all the template configuration
TEMPLATE_CONFIGURATION = {

    # The title of the application as shown by the browser
    "title" : "Plivo call center demo",

    # # Define the category and subcategory font-weifht CSS attribute [normal|bold]
    # "category_font_weight" : "normal",
    # "subcategory_font_weight" : "normal",
}

##########################
# Web Application settings
##########################

# Should we restrict the access to specific IPs?
RESTRICT_BY_IP = False

# List of safe IPs to access the application
IPS = ("127.0.0.1") #,
       #"",)

# The host IP to run the application from
#HOST = "127.0.0.1"
HOST = "0.0.0.0"

# The port to run the application from
PORT = 5000
