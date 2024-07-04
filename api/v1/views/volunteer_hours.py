#!/usr/bin/python3
"""Handles all default RESTful API actions on VolunteerHours objects"""

from flask import jsonify, abort, request
from models import storage
from models.volunteer_hours import VolunteerHours
from api.v1.views import app_views


@app_views.route('/volunteer_hours', methods=['GET'], strict_slashes=False)
def get_volunteer_hours():
    """Retrieves the list of all VolunteerHours objects"""
    volunteer_hours = [hours.to_dict()
                       for hours in storage.all(VolunteerHours).values()]
    return jsonify(volunteer_hours)


@app_views.route('/volunteer_hours/<hours_id>', methods=['GET'],
                 strict_slashes=False)
def get_volunteer_hour(hours_id):
    """Retrieves a specific VolunteerHours object by ID"""
    hours = storage.get(VolunteerHours, hours_id)
    if hours is None:
        abort(404)
    return jsonify(hours.to_dict())


@app_views.route('/volunteer_hours/<hours_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_volunteer_hour(hours_id):
    """Deletes a specific VolunteerHours object by ID"""
    hours = storage.get(VolunteerHours, hours_id)
    if hours is None:
        abort(404)
    storage.delete(hours)
    storage.save()
    return jsonify({}), 200


@app_views.route('/volunteer_hours', methods=['POST'], strict_slashes=False)
def create_volunteer_hour():
    """Logs new VolunteerHours object"""
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    if 'volunteer_id' not in req_json:
        abort(400, 'Missing volunteer_id')
    if 'event_id' not in req_json:
        abort(400, 'Missing event_id')
    if 'hours' not in req_json:
        abort(400, 'Missing hours')
    if 'verified' not in req_json:
        req_json['verified'] = False
    new_hours = VolunteerHours(**req_json)
    new_hours.save()
    return jsonify(new_hours.to_dict()), 201


@app_views.route('/volunteer_hours/<hours_id>', methods=['PUT'],
                 strict_slashes=False)
def update_volunteer_hour(hours_id):
    """Updates a specific VolunteerHours object by ID"""
    hours = storage.get(VolunteerHours, hours_id)
    if hours is None:
        abort(404)
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    for key, value in req_json.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(hours, key, value)
    hours.save()
    return jsonify(hours.to_dict()), 200
