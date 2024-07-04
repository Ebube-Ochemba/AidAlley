#!/usr/bin/python3
"""Index view for API status"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Returns the number of each object by type"""
    stats = {
        "volunteer": storage.count('Volunteer'),
        "event": storage.count('Event'),
        "event_volunteer": storage.count('EventVolunteer'),
        "notification": storage.count('Notification'),
        "volunteer_hours": storage.count('VolunteerHours')
    }
    return jsonify(stats)
