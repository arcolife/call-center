#!/usr/bin/python
# -*- coding: utf-8 -*-

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Wait announcement music when there is only 1 participant in the conference
HOLD_MUSIC = 'https://s3.amazonaws.com/plivocloud/music.mp3'

# Wait announcement message when there is only 1 participant in the conference
CALL_WAIT_MESSAGE = "You are currently being put on hold since the agent  is busy with another customer. Please wait. Thank you."

# Announcement message before entering the call
CALL_ANNOUNCEMENT = 'Welcome to the Plivo call-center. How may I help you?'


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

# The host IP to run the application from
#HOST = "127.0.0.1"
HOST = "0.0.0.0"

# The port to run the application from
PORT = 5000
