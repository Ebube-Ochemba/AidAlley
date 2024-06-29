#!/usr/bin/python3
"""This module defines the EventVolunteer class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class EventVolunteer(BaseModel, Base):
    """Represents the association between an Event and a Volunteer"""
    __tablename__ = 'event_volunteers'

    event_id = Column(String(60), nullable=False)
    volunteer_id = Column(String(60), nullable=False)
    status = Column(String(60), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initializes EventVolunteer"""
        super().__init__(*args, **kwargs)
