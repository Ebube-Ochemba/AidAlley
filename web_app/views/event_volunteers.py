#!/usr/bin/python3
"""Entry point for Event Volunteers page"""

from web_app.views import web_views
from flask import flash, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import storage
from models.event import Event
from models.event_volunteer import EventVolunteer


@web_views.route('/register/<event_id>', methods=['POST'])
@jwt_required()
def register_event(event_id):
    """Registers the logged-in volunteer for the specified event"""
    # Get the volunteer ID from the JWT token
    volunteer_id = get_jwt_identity()

    # Check if the event exists
    event = storage.get(Event, event_id)
    if not event:
        flash('Event not found.', 'error')
        return redirect(url_for('web_views.display_dashboard'))

    # Check if the volunteer is already registered for the event
    existing_registration = storage.get_event_volunteer(event_id, volunteer_id)
    if existing_registration:
        flash('You are already registered for this event.', 'error')
        return redirect(url_for('web_views.display_dashboard'))

    # Create a new EventVolunteer record
    event_volunteer = EventVolunteer(
        event_id=event.id,
        volunteer_id=volunteer_id,
        status="confirmed"
    )
    storage.new(event_volunteer)
    storage.save()

    flash('Successfully registered for the event!', 'success')
    return redirect(url_for('web_views.display_dashboard'))