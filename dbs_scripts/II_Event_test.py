#!/usr/bin/python3
"""Script to create events using DBStorage"""

from models import storage
from models.event import Event
from models.volunteer import Volunteer

def create_events():
    # Fetch a volunteer to assign as the creator
    volunteer = storage.get('Volunteer', '<volunteer1_id>')  # Replace 'volunteer1_id' with actual ID

    # Create a new Event instance
    event1 = Event(
        title="Charity Run",
        description="A charity run event to raise funds",
        date="2024-12-31T10:00:00+00:00",
        location="Metropolis",
        creator_id=volunteer.id
    )

    event2 = Event(
        title="Food Drive",
        description="A food drive event to help the needy",
        date="2024-11-15T10:00:00+00:00",
        location="Gotham",
        creator_id=volunteer.id
    )

    # Add events to the session
    storage.new(event1)
    storage.new(event2)

    # Save changes to the database
    storage.save()

    # Retrieve all events from the database
    events = storage.all('Event')
    # Print information about each event
    for key, value in events.items():
        print("{}={}".format(key, value))

if __name__ == "__main__":
    create_events()
