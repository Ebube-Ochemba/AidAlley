#!/usr/bin/python3
"""This module defines the EventVolunteer class"""

from models.base_model import BaseModel


class EventVolunteer(BaseModel):
    """Represents the association between an Event and a Volunteer"""
    event_id = ""
    volunteer_id = ""
    status = ""

    def __init__(self, *args, **kwargs):
        """Initializes EventVolunteer"""
        super().__init__(*args, **kwargs)
