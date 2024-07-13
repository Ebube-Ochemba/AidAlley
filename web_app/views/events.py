"""Handles the events listing view"""

from web_app.views import web_views
from flask import render_template, jsonify, request
from models import storage
from models.event import Event
from uuid import uuid4


@web_views.route('/events', strict_slashes=False)
def events():
    """Handles request for events"""
    # Fetch upcoming events from the storage
    events = storage.all(Event).values()
    # Show top 3 upcoming events
    upcoming_events = sorted(events, key=lambda event: event.date)[:8]
    return render_template('events.html',
                           cache_id=uuid4(),
                           events=upcoming_events)


@web_views.route('/load-more-events', strict_slashes=False)
def load_more_events():
    """Handles request to load more events"""
    offset = int(request.args.get('offset', 0))
    events = storage.all(Event).values()
    more_events = sorted(events, key=lambda event: event.date)[offset:offset + 8]
    events_data = [{'title': event.title,
                    'date': event.date,
                    'location': event.location,
                    'description': event.description,
                    'id': event.id}
                    for event in more_events]
    return jsonify(events=events_data)
