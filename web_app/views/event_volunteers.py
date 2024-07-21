#!/usr/bin/python3
"""Entry point for Event Volunteers page"""

from web_app.views import web_views
from flask import flash, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import storage
from models.event_volunteer import EventVolunteer
from models.notification import Notification


@web_views.route('/register/<event_id>', methods=['POST'])
@jwt_required()
def register_event(event_id):
    """Registers the logged-in volunteer for the specified event"""
    # Get the volunteer ID from the JWT token
    volunteer_id = get_jwt_identity()

    # Check if the event exists
    event = storage.get_event_by_id(event_id)
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

    # Create a new notification for the volunteer
    notification_message = f"Registered for: {event.title}"
    notification = Notification(
        volunteer_id=volunteer_id,
        message=notification_message,
        status="unread"
    )
    storage.new(notification)

    storage.save()

    flash('Successfully registered for the event!', 'success')
    return redirect(url_for('web_views.display_dashboard'))


@web_views.route('/unregister/<event_id>', methods=['POST'])
@jwt_required()
def unregister_event(event_id):
    """Unregister a volunteer from an event"""
    volunteer_id = get_jwt_identity()

    # Find the EventVolunteer record
    event_volunteer = storage.get_event_volunteer(event_id, volunteer_id)

    if not event_volunteer:
        flash('You are not registered for this event.', 'error')
        return redirect(url_for('web_views.volunteer_dashboard'))

    # Delete the record
    storage.delete(event_volunteer)

    # Create a new notification for the volunteer
    event = storage.get_event_by_id(event_id)
    notification_message = f"Unregistered from: {event.title}"
    notification = Notification(
        volunteer_id=volunteer_id,
        message=notification_message,
        status="unread"
    )
    storage.new(notification)
    
    storage.save()

    flash('Successfully unregistered from the event.', 'success')
    return redirect(url_for('web_views.display_dashboard'))
