#!/usr/bin/python3
"""This module defines the Notification class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Notification(BaseModel, Base):
    """Represents a Notification"""
    __tablename__ = 'notifications'

    volunteer_id = Column(String(60), nullable=False)
    message = Column(String(1024), nullable=False)
    status = Column(String(60), nullable=False, default="unread")

    def __init__(self, *args, **kwargs):
        """Initializes Notification"""
        super().__init__(*args, **kwargs)

    def mark_as_read(self):
        """Marks the notification as read"""
        self.status = "read"
        self.save()

    def mark_as_dismissed(self):
        """Marks the notification as dismissed"""
        self.status = "dismissed"
        self.save()
