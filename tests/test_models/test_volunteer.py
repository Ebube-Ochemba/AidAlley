#!/usr/bin/python3
"""Test Volunteer for expected behavior and documentation"""
from datetime import datetime
from models.volunteer import Volunteer
import bcrypt
import models
from unittest import mock
import inspect
import pycodestyle
import unittest


class TestVolunteerDocs(unittest.TestCase):
    """Tests to check the documentation and style of Volunteer class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.volunteer_funcs = inspect.getmembers(Volunteer, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/volunteer.py conforms to PEP8."""
        with self.subTest(path='models/volunteer.py'):
            errors = pycodestyle.Checker('models/volunteer.py').check_all()
            self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(models.volunteer.__doc__, None,
                         "models/volunteer.py needs a docstring")
        self.assertTrue(len(models.volunteer.__doc__) > 1,
                        "models/volunteer.py needs a docstring")

    def test_class_docstring(self):
        """Test for the Volunteer class docstring"""
        self.assertIsNot(Volunteer.__doc__, None,
                         "Volunteer class needs a docstring")
        self.assertTrue(len(Volunteer.__doc__) >= 1,
                        "Volunteer class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in Volunteer methods"""
        for func in self.volunteer_funcs:
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


class TestVolunteer(unittest.TestCase):
    """Test the Volunteer class"""

    def test_instantiation(self):
        """Test that a Volunteer object is correctly created"""
        vol = Volunteer()
        self.assertIs(type(vol), Volunteer)
        vol.first_name = "Walter"
        vol.last_name = "White"
        vol.email = "walter@breakingbad.com"
        vol.phone = "555-123-4567"
        vol.availability = "Monday, Wednesday, Friday"
        vol.password = "Heisenberg"
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "first_name": str,
            "last_name": str,
            "email": str,
            "phone": str,
            "availability": str,
            "password": str
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, vol.__dict__)
                self.assertIs(type(vol.__dict__[attr]), typ)
        self.assertEqual(vol.first_name, "Walter")
        self.assertEqual(vol.last_name, "White")

    def test_password_hashing(self):
        """Test password hashing and verification"""
        vol = Volunteer()
        vol.password = "Heisenberg"
        hashed_password = vol.password
        self.assertTrue(bcrypt.checkpw("Heisenberg".encode('utf-8'),
                                       hashed_password.encode('utf-8')))
        self.assertFalse(bcrypt.checkpw("HeisenberG".encode('utf-8'),
                                        hashed_password.encode('utf-8')))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        vol = Volunteer()
        old_created_at = vol.created_at
        old_updated_at = vol.updated_at
        vol.save()
        new_created_at = vol.created_at
        new_updated_at = vol.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)
