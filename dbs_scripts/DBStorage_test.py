#!/usr/bin/python3
"""Script to create various instances using DBStorage"""

from models import storage
from models.event import Event
from models.event_volunteer import EventVolunteer
from models.notification import Notification
from models.volunteer import Volunteer
from models.volunteer_hours import VolunteerHours

def main():
    # Create a new Volunteer instance
    new_volunteer = Volunteer(
        first_name="Clark",
        last_name="Kent",
        email="clark.kent@example.com",
        phone="123-456-7890",
        availability="Everyday",
        password="Superman"
    )

    # Create a new Event instance
    new_event = Event(
        title="Charity Run",
        description="A charity run event to raise funds",
        date="2024-12-31T10:00:00+00:00",
        location="Metropolis",
        creator_id=new_volunteer.id
    )

    # Create a new EventVolunteer instance
    new_event_volunteer = EventVolunteer(
        event_id=new_event.id,
        volunteer_id=new_volunteer.id,
        status="confirmed"
    )

    # Create a new VolunteerHours instance
    new_volunteer_hours = VolunteerHours(
        volunteer_id=new_volunteer.id,
        event_id=new_event.id,
        hours=5.0,
        verified=True
    )

    # Create a new Notification instance
    new_notification = Notification(
        volunteer_id=new_volunteer.id,
        message="You have been confirmed for the Charity Run event."
    )

    # Add objects to the session
    storage.new(new_volunteer)
    storage.new(new_event)
    storage.new(new_event_volunteer)
    storage.new(new_volunteer_hours)
    storage.new(new_notification)

    # Save changes to the database
    storage.save()

    # Retrieve all instances from the database
    database = storage.all()
    # Print information about each instance
    for key, value in database.items():
        print("{}={}".format(key, value))

if __name__ == "__main__":
    main()
