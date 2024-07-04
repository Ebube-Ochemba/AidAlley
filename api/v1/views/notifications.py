#!/usr/bin/python3
"""Handles all default RESTful API actions on Notification objects"""

from flask import jsonify, abort, request
from models import storage
from models.notification import Notification
from api.v1.views import app_views


@app_views.route('/notifications/<volunteer_id>',
                 methods=['GET'], strict_slashes=False)
def get_notifications(volunteer_id):
    """Retrieves notifications for a specific volunteer"""
    notifications = storage.all(Notification).values()
    volunteer_notifications = [
        notification.to_dict() for notification in notifications 
        if notification.volunteer_id == volunteer_id
    ]
    return jsonify(volunteer_notifications)
