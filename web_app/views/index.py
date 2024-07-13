"""Handles the homepage view"""

from web_app.views import web_views
from flask import render_template
from models import storage
from models.event import Event
from uuid import uuid4


@web_views.route('/', strict_slashes=False)
def display_homepage():
    """Handles request for homepage"""
    # Fetch upcoming events from the storage
    events = storage.all(Event).values()
    # Show top 3 upcoming events
    upcoming_events = sorted(events, key=lambda event: event.date)[:8]
    return render_template('homepage.html',
                           cache_id=uuid4(),
                           events=upcoming_events)


@web_views.route('/learn-more', strict_slashes=False)
def learn_more():
    """Handles request for learn more page"""
    return render_template('learn-more.html')


@web_views.route('/events', strict_slashes=False)
def events():
    """Handles request for events"""
    return render_template('events.html')


@web_views.route('/login', strict_slashes=False)
def login():
    """Handles request for login page"""
    return render_template('login.html')


@web_views.route('/create-account', strict_slashes=False)
def create_account():
    """Handles request for create account page"""
    return render_template('create-account.html')
