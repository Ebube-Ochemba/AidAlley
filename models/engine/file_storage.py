#!/usr/bin/python3
"""
Contains the FileStorage class for the AidAlley project
"""

import json
from models.base_model import BaseModel
from models.event import Event
from models.event_volunteer import EventVolunteer
from models.notification import Notification
from models.volunteer import Volunteer
from models.volunteer_hours import VolunteerHours

classes = {
    "BaseModel": BaseModel,
    "Volunteer": Volunteer,
    "Event": Event,
    "VolunteerHours": VolunteerHours,
    "EventVolunteer": EventVolunteer,
    "Notification": Notification
}


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"

    # empty dictionary - stores all objects: "key=<class name>.id"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects or filtered by class"""
        if cls is not None:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from datetime import datetime
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
            for key, obj_dict in json_objects.items():
                class_name = obj_dict.pop("__class__", None)
                if class_name in classes:
                    obj = classes[class_name](**obj_dict)
                    # Convert timestamps to datetime objects if they are str.
                    if isinstance(obj.created_at, str):
                        obj.created_at = datetime.fromisoformat(obj.created_at)
                    if isinstance(obj.updated_at, str):
                        obj.updated_at = datetime.fromisoformat(obj.updated_at)
                    if class_name == 'Event' and isinstance(obj.date, str):
                        obj.date = datetime.fromisoformat(obj.date)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID,
        or None if not found or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value

        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        if cls is None:
            return len(self.__objects)
        else:
            return len(self.all(cls))
