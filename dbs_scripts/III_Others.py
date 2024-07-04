#!/usr/bin/python3
"""Script to test EventVolunteer, VolunteerHours, and Notification models"""

from models import storage
from models.event_volunteer import EventVolunteer
from models.volunteer_hours import VolunteerHours
from models.notification import Notification

def test_models():
    # Fetch a volunteer and an event
    volunteer = storage.get('Volunteer', 'ceef44a3-28c7-42f7-abc8-1fe566e98828')  # Replace 'volunteer1_id' with actual ID
    event = storage.get('Event', '65ff72a3-2338-4079-a660-c92b4cc8368e')  # Replace 'event1_id' with actual ID

    # Create a new EventVolunteer instance
    event_volunteer = EventVolunteer(
        event_id=event.id,
        volunteer_id=volunteer.id,
        status="confirmed"
    )

    # Create a new VolunteerHours instance
    volunteer_hours = VolunteerHours(
        volunteer_id=volunteer.id,
        event_id=event.id,
        hours=5.0,
        verified=True
    )

    # Create a new Notification instance
    notification = Notification(
        volunteer_id=volunteer.id,
        message="You have been confirmed for the Charity Run event."
    )

    # Add objects to the session
    storage.new(event_volunteer)
    storage.new(volunteer_hours)
    storage.new(notification)

    # Save changes to the database
    storage.save()

    # Retrieve and print all instances
    event_volunteers = storage.all('EventVolunteer')
    volunteer_hours_entries = storage.all('VolunteerHours')
    notifications = storage.all('Notification')

    print("\nEventVolunteers:")
    for key, value in event_volunteers.items():
        print("{}={}".format(key, value))

    print("\nVolunteerHours:")
    for key, value in volunteer_hours_entries.items():
        print("{}={}".format(key, value))

    print("\nNotifications:")
    for key, value in notifications.items():
        print("{}={}".format(key, value))

if __name__ == "__main__":
    test_models()
