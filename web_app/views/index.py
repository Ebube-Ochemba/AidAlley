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
    upcoming_events = sorted(events, key=lambda event: event.date)[:3]
    return render_template('homepage.html',
                           cache_id=uuid4(),
                           events=upcoming_events)
