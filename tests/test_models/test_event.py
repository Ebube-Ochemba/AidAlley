#!/usr/bin/python3
"""Test Event for expected behavior and documentation"""
from datetime import datetime, timezone
from models.event import Event
import models
import unittest
from unittest import mock
import inspect
import pycodestyle


class TestEventDocs(unittest.TestCase):
    """Tests to check the documentation and style of Event class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.event_funcs = inspect.getmembers(Event, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/event.py conforms to PEP8."""
        with self.subTest(path='models/event.py'):
            errors = pycodestyle.Checker('models/event.py').check_all()
            self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(models.event.__doc__, None,
                         "models/event.py needs a docstring")
        self.assertTrue(len(models.event.__doc__) > 1,
                        "models/event.py needs a docstring")

    def test_class_docstring(self):
        """Test for the Event class docstring"""
        self.assertIsNot(Event.__doc__, None,
                         "Event class needs a docstring")
        self.assertTrue(len(Event.__doc__) >= 1,
                        "Event class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in Event methods"""
        for func in self.event_funcs:
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


class TestEvent(unittest.TestCase):
    """Test the Event class"""

    def test_instantiation(self):
        """Test that an Event object is correctly created"""
        event = Event()
        self.assertIs(type(event), Event)
        event.title = "Community Cleanup"
        event.description = "Join us for a community cleanup event."
        event.date = datetime(2023, 7, 1, 9, 0, tzinfo=timezone.utc)
        event.location = "123 Main St, Anytown, USA"
        event.creator_id = "some-creator-uuid"
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "title": str,
            "description": str,
            "date": datetime,
            "location": str,
            "creator_id": str
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, event.__dict__)
                self.assertIs(type(event.__dict__[attr]), typ)
        self.assertEqual(event.title, "Community Cleanup")
        self.assertEqual(event.description, "Join us for a community cleanup event.")

    def test_date_validation(self):
        """Test date validation in Event class"""
        event = Event()
        event.title = "Test Event"
        with self.assertRaises(TypeError):
            event.date = "2023-07-01"
        with self.assertRaises(ValueError):
            event.date = "invalid-date-format"
        with self.assertRaises(ValueError):
            event.date = datetime(2023, 7, 1)  # Missing timezone

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        event = Event()
        event.title = "Test Event"
        event.save()
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)
