#!/usr/bin/python3
"""Handles all default RESTful API actions on Volunteer objects"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.volunteer import Volunteer


@app_views.route('/volunteers', methods=['GET'],
                 strict_slashes=False)
def get_volunteers():
    """Retrieves the list of all Volunteer objects"""
    volunteers = [volunteer.to_dict()
                  for volunteer in storage.all(Volunteer).values()]
    return jsonify(volunteers)


@app_views.route('/volunteers/<volunteer_id>',
                 methods=['GET'], strict_slashes=False)
def get_volunteer(volunteer_id):
    """Retrieves a specific Volunteer object by ID"""
    volunteer = storage.get(Volunteer, volunteer_id)
    if volunteer is None:
        abort(404)
    return jsonify(volunteer.to_dict())


@app_views.route('/volunteers/<volunteer_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_volunteer(volunteer_id):
    """Deletes a specific Volunteer object by ID"""
    volunteer = storage.get(Volunteer, volunteer_id)
    if volunteer is None:
        abort(404)
    storage.delete(volunteer)
    storage.save()
    return jsonify({}), 200


@app_views.route('/volunteers', methods=['POST'], strict_slashes=False)
def create_volunteer():
    """Creates a new Volunteer object"""
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    if 'email' not in req_json:
        abort(400, 'Missing email')
    if 'password' not in req_json:
        abort(400, 'Missing password')
    new_volunteer = Volunteer(**req_json)
    new_volunteer.save()
    return jsonify(new_volunteer.to_dict()), 201


@app_views.route('/volunteers/<volunteer_id>',
                 methods=['PUT'], strict_slashes=False)
def update_volunteer(volunteer_id):
    """Updates a specific Volunteer object by ID"""
    volunteer = storage.get(Volunteer, volunteer_id)
    if volunteer is None:
        abort(404)
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    for key, value in req_json.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(volunteer, key, value)
    volunteer.save()
    return jsonify(volunteer.to_dict()), 200
