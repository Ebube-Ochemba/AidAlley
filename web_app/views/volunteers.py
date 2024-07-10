#!/usr/bin/python3
"""xxx"""

from web_app.views import web_views
from flask import Flask, render_template
from models import storage
from models.volunteer import Volunteer


@web_views.route('/volunteers', strict_slashes=False)
def display_dashboard():
    """"""
    pass