"""Handles the homepage view"""

from web_app.views import web_views
from flask import render_template
from datetime import datetime, timezone
from dateutil import parser
from models import storage
from models.event import Event
from uuid import uuid4


@web_views.route('/', strict_slashes=False)
def display_homepage():
    """Handles request for homepage"""
    # Fetch upcoming events from the storage
    events = storage.all(Event).values()
    # Sort events and get the first 8
    upcoming_events = sorted(events, key=lambda event: event.date)[:8]
    
    # Process dates for the upcoming events
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
    
    return render_template('homepage.html',
                           cache_id=uuid4(),
                           events=processed_events)


@web_views.route('/learn-more', strict_slashes=False)
def learn_more():
    """Handles request for learn more page"""
    return render_template('learn-more.html',
                           cache_id=uuid4())


@web_views.route('/login', strict_slashes=False)
def login():
    """Handles request for login page"""
    return render_template('login.html',
                           cache_id=uuid4())


@web_views.route('/create-account', strict_slashes=False)
def create_account():
    """Handles request for create account page"""
    return render_template('create-account.html',
                           cache_id=uuid4())
