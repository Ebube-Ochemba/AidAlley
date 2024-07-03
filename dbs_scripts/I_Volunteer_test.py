#!/usr/bin/python3
"""Script to create volunteers using DBStorage"""

from models import storage
from models.volunteer import Volunteer

def create_volunteers():
    # Create a new Volunteer instance
    volunteer1 = Volunteer(
        first_name="Clark",
        last_name="Kent",
        email="clark.kent@example.com",
        phone="123-456-7890",
        availability="Everyday",
        password="Superman"
    )

    volunteer2 = Volunteer(
        first_name="Diana",
        last_name="Prince",
        email="diana.prince@example.com",
        phone="098-765-4321",
        availability="Weekends",
        password="WonderWoman"
    )

    # Add volunteers to the session
    storage.new(volunteer1)
    storage.new(volunteer2)

    # Save changes to the database
    storage.save()

    # Retrieve all volunteers from the database
    volunteers = storage.all('Volunteer')
    # Print information about each volunteer
    for key, value in volunteers.items():
        print("{}={}".format(key, value))

if __name__ == "__main__":
    create_volunteers()
