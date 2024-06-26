#!/usr/bin/python3
"""This module defines the Notification class"""

from models.base_model import BaseModel


class Notification(BaseModel):
    """Represents a Notification"""
    volunteer_id = ""
    message = ""
    status = "unread"  # Default status

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
