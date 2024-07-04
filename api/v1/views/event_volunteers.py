#!/usr/bin/python3
"""Handles all default RESTful API actions on EventVolunteer objects"""

from flask import jsonify, abort, request
from models import storage
from models.event_volunteer import EventVolunteer
from api.v1.views import app_views


@app_views.route('/event_volunteers', methods=['GET'],
                 strict_slashes=False)
def get_event_volunteers():
    """Retrieves the list of all EventVolunteer objects"""
    event_volunteers = [ev.to_dict()
                        for ev in storage.all(EventVolunteer).values()]
    return jsonify(event_volunteers)


@app_views.route('/event_volunteers/<event_id>/<volunteer_id>',
                 methods=['GET'], strict_slashes=False)
def get_event_volunteer(event_id, volunteer_id):
    """Retrieves a specific EventVolunteer object by event_id and
    volunteer_id"""
    ev = storage.get(EventVolunteer, (event_id, volunteer_id))
    if ev is None:
        abort(404)
    return jsonify(ev.to_dict())


@app_views.route('/event_volunteers/<event_id>/<volunteer_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_event_volunteer(event_id, volunteer_id):
    """Deletes a specific EventVolunteer object by event_id and
    volunteer_id"""
    ev = storage.get(EventVolunteer, (event_id, volunteer_id))
    if ev is None:
        abort(404)
    storage.delete(ev)
    storage.save()
    return jsonify({}), 200


@app_views.route('/event_volunteers', methods=['POST'],
                 strict_slashes=False)
def create_event_volunteer():
    """Registers a volunteer for an event
    (creates an EventVolunteer object)"""
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    if 'event_id' not in req_json:
        abort(400, 'Missing event_id')
    if 'volunteer_id' not in req_json:
        abort(400, 'Missing volunteer_id')
    if 'status' not in req_json:
        abort(400, 'Missing status')
    new_ev = EventVolunteer(**req_json)
    new_ev.save()
    return jsonify(new_ev.to_dict()), 201


@app_views.route('/event_volunteers/<event_id>/<volunteer_id>',
                 methods=['PUT'], strict_slashes=False)
def update_event_volunteer(event_id, volunteer_id):
    """Updates a specific EventVolunteer object by event_id and
    volunteer_id"""
    ev = storage.get(EventVolunteer, (event_id, volunteer_id))
    if ev is None:
        abort(404)
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    for key, value in req_json.items():
        if key not in ['event_id', 'volunteer_id', 'created_at', 'updated_at']:
            setattr(ev, key, value)
    ev.save()
    return jsonify(ev.to_dict()), 200
