#!/usr/bin/python3
"""Handles all default RESTful API actions on Event objects"""

from flask import jsonify, abort, request
from models import storage
from models.event import Event
from api.v1.views import app_views


@app_views.route('/events', methods=['GET'], strict_slashes=False)
def get_events():
    """Retrieves the list of all Event objects"""
    events = [event.to_dict() for event in storage.all(Event).values()]
    return jsonify(events)


@app_views.route('/events/<event_id>', methods=['GET'], strict_slashes=False)
def get_event(event_id):
    """Retrieves a specific Event object by ID"""
    event = storage.get(Event, event_id)
    if event is None:
        abort(404)
    return jsonify(event.to_dict())


@app_views.route('/events/<event_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_event(event_id):
    """Deletes a specific Event object by ID"""
    event = storage.get(Event, event_id)
    if event is None:
        abort(404)
    storage.delete(event)
    storage.save()
    return jsonify({}), 200


@app_views.route('/events', methods=['POST'], strict_slashes=False)
def create_event():
    """Creates a new Event object"""
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    if 'title' not in req_json:
        abort(400, 'Missing title')
    if 'description' not in req_json:
        abort(400, 'Missing description')
    if 'date' not in req_json:
        abort(400, 'Missing date')
    if 'location' not in req_json:
        abort(400, 'Missing location')
    new_event = Event(**req_json)
    new_event.save()
    return jsonify(new_event.to_dict()), 201


@app_views.route('/events/<event_id>', methods=['PUT'], strict_slashes=False)
def update_event(event_id):
    """Updates a specific Event object by ID"""
    event = storage.get(Event, event_id)
    if event is None:
        abort(404)
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    for key, value in req_json.items():
        if key not in ['id', 'creator_id', 'created_at', 'updated_at']:
            setattr(event, key, value)
    event.save()
    return jsonify(event.to_dict()), 200
