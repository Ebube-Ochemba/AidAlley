#!/usr/bin/python3
"""This module creates the Volunteer class"""

import bcrypt
from models.base_model import BaseModel


class Volunteer(BaseModel):
    """Represents a volunteer in the application"""
    first_name = ""
    last_name = ""
    email = ""
    phone = ""
    availability = ""
    password = ""

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