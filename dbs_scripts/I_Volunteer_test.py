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

    volunteer3 = Volunteer(
        first_name="Bruce",
        last_name="Wayne",
        email="bruce.wayne@example.com",
        phone="555-0100",
        availability="Nightly",
        password="Batman"
    )

    volunteer4 = Volunteer(
        first_name="Tony",
        last_name="Stark",
        email="tony.stark@example.com",
        phone="555-0199",
        availability="Daily",
        password="IronMan"
    )

    volunteer5 = Volunteer(
        first_name="Steve",
        last_name="Rogers",
        email="steve.rogers@example.com",
        phone="555-0188",
        availability="Weekdays",
        password="CaptainAmerica"
    )

    volunteer6 = Volunteer(
        first_name="Dinah",
        last_name="Lance",
        email="dinah.lance@example.com",
        phone="555-0111",
        availability="Flexible",
        password="BlackCanary"
    )

    volunteer7 = Volunteer(
        first_name="T'Challa",
        last_name="",
        email="tchalla.blackpanther@example.com",
        phone="555-0122",
        availability="As needed",
        password="BlackPanther"
    )

    volunteer8 = Volunteer(
        first_name="Carol",
        last_name="Danvers",
        email="carol.danvers@example.com",
        phone="555-0133",
        availability="Varies",
        password="CaptainMarvel"
    )

    volunteer9 = Volunteer(
        first_name="Selina",
        last_name="Kyle",
        email="selina.kyle@example.com",
        phone="555-0144",
        availability="Evenings",
        password="Catwoman"
    )

    volunteer10 = Volunteer(
        first_name="Conan",
        last_name="",
        email="conan.thebarbarian@example.com",
        phone="555-0155",
        availability="Traveling",
        password="ConanBarbarian"
    )

    # Add volunteers to the session
    storage.new(volunteer1)
    storage.new(volunteer2)
    storage.new(volunteer3)
    storage.new(volunteer4)
    storage.new(volunteer5)
    storage.new(volunteer6)
    storage.new(volunteer7)
    storage.new(volunteer8)
    storage.new(volunteer9)
    storage.new(volunteer10)

    # Save changes to the database
    storage.save()

    # Retrieve all volunteers from the database
    volunteers = storage.all('Volunteer')
    # Print information about each volunteer
    for key, value in volunteers.items():
        print("{}={}".format(key, value))

if __name__ == "__main__":
    create_volunteers()
