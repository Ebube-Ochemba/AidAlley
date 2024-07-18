#!/usr/bin/python3
"""Script to create events using DBStorage"""

from models import storage
from models.event import Event
from models.volunteer import Volunteer

def create_events():
    # Fetch a volunteer to assign as the creator
    volunteer1 = storage.get(Volunteer, 'volunteer1_id')  # Replace 'volunteer1_id' with actual ID
    volunteer2 = storage.get(Volunteer, 'volunteer2_id')  # Replace 'volunteer2_id' with actual ID
    volunteer3 = storage.get(Volunteer, 'volunteer3_id')  # Replace 'volunteer3_id' with actual ID

    print(volunteer1.id)
    print(volunteer2.id)
    print(volunteer3.id)

    # List of events to create
    events_data = [
        {
            "title": "Charity Run",
            "description": "A charity run event to raise funds",
            "date": "2024-12-31T10:00:00+00:00",
            "location": "Metropolis",
            "creator_id": volunteer1.id
        },
        {
            "title": "Food Drive",
            "description": "A food drive event to help the needy",
            "date": "2024-11-15T10:00:00+00:00",
            "location": "Gotham",
            "creator_id": volunteer1.id
        },
        {
            "title": "Book Drive",
            "description": "Collecting books for local libraries",
            "date": "2024-10-20T14:00:00+00:00",
            "location": "Smallville",
            "creator_id": volunteer1.id
        },
        {
            "title": "Clean-Up Day",
            "description": "Community clean-up initiative",
            "date": "2024-09-25T08:00:00+00:00",
            "location": "Central City",
            "creator_id": volunteer1.id
        },
        {
            "title": "Art Workshop",
            "description": "An art workshop for kids",
            "date": "2024-08-30T16:00:00+00:00",
            "location": "Star City",
            "creator_id": volunteer1.id
        },
        {
            "title": "Health Fair",
            "description": "A health fair offering free screenings",
            "date": "2024-07-28T09:00:00+00:00",
            "location": "Bludhaven",
            "creator_id": volunteer2.id
        },
        {
            "title": "Music Festival",
            "description": "A music festival featuring local bands",
            "date": "2024-06-24T12:00:00+00:00",
            "location": "National City",
            "creator_id": volunteer2.id
        },
        {
            "title": "Tech Workshop",
            "description": "A tech workshop for beginners",
            "date": "2024-05-19T10:00:00+00:00",
            "location": "Ferris Aircraft",
            "creator_id": volunteer2.id
        },
        {
            "title": "Pet Adoption Day",
            "description": "A pet adoption day at the shelter",
            "date": "2024-04-14T13:00:00+00:00",
            "location": "Coast City",
            "creator_id": volunteer2.id
        },
        {
            "title": "Cooking Class",
            "description": "A cooking class teaching healthy recipes",
            "date": "2024-03-09T15:00:00+00:00",
            "location": "Happy Harbor",
            "creator_id": volunteer2.id
        },
        {
            "title": "Science Fair",
            "description": "A science fair for students",
            "date": "2024-02-04T11:00:00+00:00",
            "location": "New Genesis",
            "creator_id": volunteer3.id
        },
        {
            "title": "Craft Fair",
            "description": "A craft fair showcasing local artisans",
            "date": "2024-01-27T17:00:00+00:00",
            "location": "Earth",
            "creator_id": volunteer3.id
        },
        {
            "title": "Movie Night",
            "description": "A movie night screening classic films",
            "date": "2023-12-22T19:00:00+00:00",
            "location": "Oa",
            "creator_id": volunteer3.id
        },
        {
            "title": "Winter Wonderland",
            "description": "A winter-themed celebration",
            "date": "2023-11-17T18:00:00+00:00",
            "location": "Apokolips",
            "creator_id": volunteer3.id
        }
    ]

    # Iterate over the events data to create and save each event
    for event_data in events_data:
        event = Event(**event_data)
        storage.new(event)
    # Save changes to the database
    storage.save()

    # Retrieve all events from the database
    events = storage.all('Event')
    # Print information about each event
    for key, value in events.items():
        print("{}={}".format(key, value))

if __name__ == "__main__":
    create_events()
