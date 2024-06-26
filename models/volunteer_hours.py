#!/usr/bin/python3
"""This module defines the VolunteerHours class"""

from models.base_model import BaseModel


class VolunteerHours(BaseModel):
    """Represents Volunteer Hours"""
    volunteer_id = ""
    event_id = ""
    hours = 0.0
    verified = False

    def __init__(self, *args, **kwargs):
        """Initializes VolunteerHours"""
        super().__init__(*args, **kwargs)
        if "hours" in kwargs and isinstance(kwargs["hours"], (int, float)):
            if kwargs["hours"] < 0:
                raise ValueError("Hours must be a positive number")
            self.hours = kwargs["hours"]

    def __setattr__(self, name, value):
        """Sets attributes, ensuring hours are positive"""
        if name == "hours":
            if isinstance(value, (int, float)):
                if value < 0:
                    raise ValueError("Hours must be a positive number")
        super().__setattr__(name, value)
