#!/usr/bin/python3
"""Test Volunteer for expected behavior and documentation"""
from datetime import datetime
from models.volunteer_hours import VolunteerHours
import models
from unittest import mock
import inspect
import pycodestyle
import unittest


class TestVolunteerHoursDocs(unittest.TestCase):
    """Tests to check the documentation and style of VolunteerHours class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.volunteer_hours_funcs = inspect.getmembers(VolunteerHours, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/volunteer_hours.py conforms to PEP8."""
        with self.subTest(path='models/volunteer_hours.py'):
            errors = pycodestyle.Checker('models/volunteer_hours.py').check_all()
            self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(models.volunteer_hours.__doc__, None,
                         "models/volunteer_hours.py needs a docstring")
        self.assertTrue(len(models.volunteer_hours.__doc__) > 1,
                        "models/volunteer_hours.py needs a docstring")

    def test_class_docstring(self):
        """Test for the VolunteerHours class docstring"""
        self.assertIsNot(VolunteerHours.__doc__, None,
                         "VolunteerHours class needs a docstring")
        self.assertTrue(len(VolunteerHours.__doc__) >= 1,
                        "VolunteerHours class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in VolunteerHours methods"""
        for func in self.volunteer_hours_funcs:
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


class TestVolunteerHours(unittest.TestCase):
    """Test the VolunteerHours class"""

    def test_instantiation(self):
        """Test that a VolunteerHours object is correctly created"""
        volunteer_hours = VolunteerHours()
        self.assertIs(type(volunteer_hours), VolunteerHours)
        volunteer_hours.volunteer_id = "volunteer-uuid"
        volunteer_hours.event_id = "event-uuid"
        volunteer_hours.hours = 5.5
        volunteer_hours.verified = False
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "volunteer_id": str,
            "event_id": str,
            "hours": float,
            "verified": bool
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, volunteer_hours.__dict__)
                self.assertIs(type(volunteer_hours.__dict__[attr]), typ)
        self.assertEqual(volunteer_hours.hours, 5.5)

    def test_hours_validation(self):
        """Test hours validation in VolunteerHours class"""
        volunteer_hours = VolunteerHours()
        volunteer_hours.volunteer_id = "volunteer-uuid"
        volunteer_hours.event_id = "event-uuid"
        with self.assertRaises(ValueError):
            volunteer_hours.hours = -5.0

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        volunteer_hours = VolunteerHours()
        volunteer_hours.volunteer_id = "volunteer-uuid"
        volunteer_hours.event_id = "event-uuid"
        volunteer_hours.hours = 5.5
        volunteer_hours.save()
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)
