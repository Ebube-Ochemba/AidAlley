#!/usr/bin/python3
"""Index view for API status"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.event import Event
from models.event_volunteer import EventVolunteer
from models.notification import Notification
from models.volunteer import Volunteer
from models.volunteer_hours import VolunteerHours


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Returns the number of each object by type"""
    stats = {
        "event": storage.count(Event),
        "event_volunteer": storage.count(EventVolunteer),
        "notification": storage.count(Notification),
        "volunteer": storage.count(Volunteer),
        "volunteer_hours": storage.count(VolunteerHours)
    }
    return jsonify(stats)
