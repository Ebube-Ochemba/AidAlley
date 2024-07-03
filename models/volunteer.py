#!/usr/bin/python3
"""This module creates the Volunteer class"""

import bcrypt
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Volunteer(BaseModel, Base):
    """Represents a volunteer in the application"""
    __tablename__ = 'volunteers'

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    availability = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)

    # Relationships
    created_events = relationship('Event',
                                  back_populates='creator',
                                  cascade="all, delete, delete-orphan")
    registered_events = relationship('EventVolunteer',
                                     back_populates='volunteer',
                                     cascade="all, delete, delete-orphan")
    hours_entries = relationship('VolunteerHours',
                                 back_populates='volunteer',
                                 cascade="all, delete, delete-orphan")
    notifications = relationship('Notification',
                                 back_populates='volunteer',
                                 cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initializes volunteer"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Sets an attribute, with bcrypt hashing for passwords"""
        if name == "password":
            # Hash the password using bcrypt
            value = bcrypt.hashpw(value.encode('utf-8'),
                                  bcrypt.gensalt()).decode('utf-8')
        super().__setattr__(name, value)

    def check_password(self, password):
        """Checks if the provided password matches the stored password"""
        return bcrypt.checkpw(password.encode('utf-8'),
                              self.password.encode('utf-8'))
