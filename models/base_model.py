#!/usr/bin/python3
"""This module creates the BaseModel class"""

from uuid import uuid4
from datetime import datetime, timezone
# from sqlalchemy import Column, String, DateTime
# from sqlalchemy.ext.declarative import as_declarative
import models


# @as_declarative()
class BaseModel:
    """A base class for all models
    Attributes:
    id (str): Unique identifier for the object
    created_at (datetime): Timestamp when the object is created
    updated_at (datetime): Timestamp when the object is last updated
    """
    # id = Column(String(60), primary_key=True, default=lambda: str(uuid4()))
    # created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    # updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
    #                     onupdate=lambda: datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        """Initializes an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)

    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict and isinstance(new_dict["created_at"],
                                                   datetime):
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict and isinstance(new_dict["updated_at"],
                                                   datetime):
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        # if "_sa_instance_state" in new_dict:
        #     del new_dict["_sa_instance_state"]
        return new_dict

    def save(self):
        """Updates public instance attribute updated_at to current datetime"""
        self.updated_at = datetime.now(timezone.utc)
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)
