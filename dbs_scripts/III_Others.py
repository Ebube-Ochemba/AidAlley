#!/usr/bin/python3
"""Script to register all volunteers for an event"""

from models import storage
from models.event_volunteer import EventVolunteer
from models.volunteer_hours import VolunteerHours
from models.notification import Notification

def register_all_volunteers_for_event(event_id):
    # Fetch the event using its ID
    event = storage.get_event_by_id(event_id)  # Make sure to replace 'event_id' with the actual ID of the event
    
    if not event:
        print("Event not found.")
        return

    # List of volunteer IDs
    volunteer_ids = [
        '2dc0683d-860f-4c29-8872-9ff42d60ce6d',  # Replace these with actual volunteer IDs
        'ea507cee-0870-4826-b854-57e783755787',
        '592ccdd9-7766-4951-87f1-f5b90c3fef60',
        '67580b70-2395-46ef-a715-2c73144fc5bd',
        '7de6dc0e-9ad4-471f-9274-5b856a1f5192'
    ]

    print(f"Registering {len(volunteer_ids)} volunteers for event {event.title}.")

    for volunteer_id in volunteer_ids:
        # Create a new EventVolunteer instance for each volunteer
        event_volunteer = EventVolunteer(
            event_id=event.id,
            volunteer_id=volunteer_id,
            status="confirmed"
        )
        
        # Create a new VolunteerHours instance for each volunteer
        volunteer_hours = VolunteerHours(
            volunteer_id=volunteer_id,
            event_id=event.id,
            hours=5.0,  # Assuming all volunteers contribute the same number of hours
            verified=False
        )
        
        # Create a new Notification instance for each volunteer
        notification = Notification(
            volunteer_id=volunteer_id,
            message=f"You have been confirmed for the {event.title} event."
        )

        # Add objects to the session
        storage.new(event_volunteer)
        storage.new(volunteer_hours)
        storage.new(notification)

    # Save changes to the database
    storage.save()

    print("All volunteers have been registered successfully.")

if __name__ == "__main__":
    # Replace 'event_id' with the actual ID of the event you want to register volunteers for
    register_all_volunteers_for_event('205a98a2-3917-4963-8248-db2d473b86a4')