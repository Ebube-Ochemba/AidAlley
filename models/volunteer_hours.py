#!/usr/bin/python3
"""This module defines the VolunteerHours class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Boolean


class VolunteerHours(BaseModel, Base):
    """Represents Volunteer Hours"""
    __tablename__ = 'volunteer_hours'

    volunteer_id = Column(String(60), nullable=False)
    event_id = Column(String(60), nullable=False)
    hours = Column(Float, nullable=False, default=0.0)
    verified = Column(Boolean, default=False)

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
