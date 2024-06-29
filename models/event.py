#!/usr/bin/python3
"""This module creates the Event class"""

from models.base_model import BaseModel, Base
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime


class Event(BaseModel, Base):
    """Represents an Event"""
    __tablename__ = 'events'

    title = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                  nullable=False)
    location = Column(String(256), nullable=True)
    creator_id = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes event"""
        super().__init__(*args, **kwargs)
        if 'date' in kwargs:
            self.date = kwargs['date']

    def __setattr__(self, name, value):
        """Sets a date with validation"""
        if name == "date":
            if isinstance(value, str):
                # Try to parse the date string
                try:
                    value = datetime.fromisoformat(value)
                except ValueError:
                    raise ValueError("Invalid date format. Use ISO 8601")
            elif not isinstance(value, datetime):
                raise TypeError("date must be a datetime object")
            if value.tzinfo is None:
                value = value.replace(tzinfo=timezone.utc)
        super().__setattr__(name, value)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        new_dict = super().to_dict()
        if "date" in new_dict and isinstance(new_dict["date"], datetime):
            new_dict["date"] = new_dict["date"].isoformat()
        return new_dict
