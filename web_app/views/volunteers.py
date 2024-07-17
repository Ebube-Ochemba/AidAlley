#!/usr/bin/python3
"""Entry point for User Profile page"""

from web_app.views import web_views
from flask import  flash, redirect, render_template, request, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import storage
from models.event import Event
from datetime import datetime
from dateutil import parser
from uuid import uuid4


@web_views.route('/user_profile', methods=['GET'], strict_slashes=False)
@jwt_required()
def display_dashboard():
    """Handles user profile page"""
    current_user_id = get_jwt_identity()
    user = storage.get_user_by_id(current_user_id)
    upcoming_events = storage.get_user_events(current_user_id)
    hours = storage.get_user_hours(current_user_id)
    notifications = storage.get_user_notifications(current_user_id)

    # Process events to format date and time correctly
    processed_events = []
    for event in upcoming_events:
        try:
            if isinstance(event.date, datetime):
                event_datetime = event.date
            else:
                event_datetime = parser.parse(str(event.date))
            event_date = event_datetime.date()
            event_time = event_datetime.strftime("%H:%M")
            
            # Create a new dictionary with processed date and time
            processed_event = {
                'id': event.id,
                'title': event.title,
                'description': event.description,
                'location': event.location,
                'date': event_date,
                'time': event_time
            }
            processed_events.append(processed_event)
        except Exception as e:
            print(f"Error processing event {event.id}: {e}")

    return render_template('volunteer-dashboard.html',
                           user=user,
                           events=processed_events,
                           hours=hours,
                           notifications=notifications)


@web_views.route('/creator_dashboard', methods=['GET'], strict_slashes=False)
@jwt_required()
def creator_dashboard():
    """Handles event creator dashboard page"""
    current_user_id = get_jwt_identity()
    user = storage.get_user_by_id(current_user_id)
    events = storage.get_events_created_by_user(current_user_id)
    # For each event, get the list of volunteers
    event_volunteers = {event.id: storage.get_volunteers_for_event(event.id) for event in events}

    return render_template('creator-dashboard.html',
                           user=user,
                           events=events,
                           event_volunteers=event_volunteers)


@web_views.route('/create_event', methods=['GET'], strict_slashes=False)
@jwt_required()
def create_event():
    """Renders the event creation form for a logged-in volunteer"""
    return render_template('create-event.html',
                           cache_id=uuid4())


@web_views.route('/create_event/submit', methods=['POST'], strict_slashes=False)
@jwt_required()
def create_event_submit():
    """Creates a new Event object by a logged-in volunteer"""
    req_json = request.form.to_dict()  # Use request.form to get form data
    if 'title' not in req_json:
        flash('Missing title', 'error')
        return redirect(url_for('web_views.create-event'))
    if 'description' not in req_json:
        flash('Missing description', 'error')
        return redirect(url_for('web_views.create-event'))
    if 'date' not in req_json:
        flash('Missing date', 'error')
        return redirect(url_for('web_views.create-event'))
    if 'location' not in req_json:
        flash('Missing location', 'error')
        return redirect(url_for('web_views.create-event'))

    # Get the creator_id from the JWT token
    creator_id = get_jwt_identity()

    # Add the creator_id to the request data
    req_json['creator_id'] = creator_id

    # Create a new Event object
    new_event = Event(**req_json)
    storage.new(new_event)
    storage.save()

    flash('Event created successfully!', 'success')
    return redirect(url_for('web_views.creator_dashboard'))
