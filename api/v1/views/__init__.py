#!/usr/bin/python3
"""creates a flask Blueprint and imports all views which use Blueprint"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from api.v1.views.index import *