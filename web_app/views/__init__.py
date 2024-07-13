#!/usr/bin/python3
"""creates a flask Blueprint and imports all views which use Blueprint"""
from flask import Blueprint

web_views = Blueprint('web_views', __name__)

# Importing all the view modules
from web_app.views.index import *
# from web_app.views.volunteers import *
# from web_app.views.event_volunteers import *
# from web_app.views.notifications import *
# from web_app.views.volunteer_hours import *
