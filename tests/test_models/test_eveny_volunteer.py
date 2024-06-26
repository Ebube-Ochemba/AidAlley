#!/usr/bin/python3
"""Test Volunteer for expected behavior and documentation"""
from datetime import datetime
from models.event_volunteer import EventVolunteer
import models
from unittest import mock
import inspect
import pycodestyle
import unittest


class TestEventVolunteerDocs(unittest.TestCase):
    """Tests to check the documentation and style of EventVolunteer class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.event_volunteer_funcs = inspect.getmembers(EventVolunteer, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/event_volunteer.py conforms to PEP8."""
        with self.subTest(path='models/event_volunteer.py'):
            errors = pycodestyle.Checker('models/event_volunteer.py').check_all()
            self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(models.event_volunteer.__doc__, None,
                         "models/event_volunteer.py needs a docstring")
        self.assertTrue(len(models.event_volunteer.__doc__) > 1,
                        "models/event_volunteer.py needs a docstring")

    def test_class_docstring(self):
        """Test for the EventVolunteer class docstring"""
        self.assertIsNot(EventVolunteer.__doc__, None,
                         "EventVolunteer class needs a docstring")
        self.assertTrue(len(EventVolunteer.__doc__) >= 1,
                        "EventVolunteer class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in EventVolunteer methods"""
        for func in self.event_volunteer_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestEventVolunteer(unittest.TestCase):
    """Test the EventVolunteer class"""

    def test_instantiation(self):
        """Test that an EventVolunteer object is correctly created"""
        event_volunteer = EventVolunteer()
        self.assertIs(type(event_volunteer), EventVolunteer)
        event_volunteer.event_id = "event-uuid"
        event_volunteer.volunteer_id = "volunteer-uuid"
        event_volunteer.status = "pending"
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "event_id": str,
            "volunteer_id": str,
            "status": str
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, event_volunteer.__dict__)
                self.assertIs(type(event_volunteer.__dict__[attr]), typ)
        self.assertEqual(event_volunteer.status, "pending")

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        event_volunteer = EventVolunteer()
        event_volunteer.event_id = "event-uuid"
        event_volunteer.volunteer_id = "volunteer-uuid"
        event_volunteer.status = "accepted"
        event_volunteer.save()
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)