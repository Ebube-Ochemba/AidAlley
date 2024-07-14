"""Handles the events listing view"""

from web_app.views import web_views
from flask import render_template, jsonify, request, abort
from datetime import datetime, timezone
from dateutil import parser
from models import storage
from models.event import Event
from uuid import uuid4


@web_views.route('/events', strict_slashes=False)
def events():
    """Handles request for events"""
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
    
    return render_template('events.html',
                           cache_id=uuid4(),
                           events=processed_events)


@web_views.route('/load-more-events', strict_slashes=False)
def load_more_events():
    """Handles request to load more events"""
    offset = int(request.args.get('offset', 0))
    events = storage.all(Event).values()
    more_events = sorted(events, key=lambda event: event.date)[offset:offset + 8]
    events_data = []
    for event in more_events:
        try:
            if isinstance(event.date, datetime):
                event_datetime = event.date
            else:
                event_datetime = parser.parse(str(event.date))
            
            event_date = event_datetime.date().isoformat()  # Format as YYYY-MM-DD
            event_time = event_datetime.strftime("%H:%M")
            
            events_data.append({
                'title': event.title,
                'date': event_date,
                'time': event_time,
                'location': event.location,
                'description': event.description,
                'id': event.id
            })
        except Exception as e:
            print(f"Error processing event {event.id}: {e}")
    
    return jsonify(events=events_data)


@web_views.route('/events/<event_id>', strict_slashes=False)
def event_detail(event_id):
    """Handles request for a specific event detail page"""
    event = storage.get(Event, event_id)
    if event is None:
        abort(404)
    try:
        if isinstance(event.date, datetime):
            event_datetime = event.date
        else:
            event_datetime = parser.parse(str(event.date))
        
        event_datetime = event_datetime.replace(tzinfo=timezone.utc)
        event_date = event_datetime.date()
        event_time = event_datetime.time()
        # Format time to show only hours and minutes
        event_time = event_datetime.strftime("%H:%M")
    except Exception as e:
        print(f"Error parsing date: {e}")

    return render_template('event-details.html',
                           cache_id=uuid4(),
                           event=event,
                           event_date=event_date,
                           event_time=event_time)
