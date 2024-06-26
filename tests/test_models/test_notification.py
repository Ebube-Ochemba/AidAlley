#!/usr/bin/python3
"""Test Volunteer for expected behavior and documentation"""
from datetime import datetime
from models.notification import Notification
import models
from unittest import mock
import inspect
import pycodestyle
import unittest


class TestNotificationDocs(unittest.TestCase):
    """Tests to check the documentation and style of Notification class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.notification_funcs = inspect.getmembers(Notification, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/notification.py conforms to PEP8."""
        with self.subTest(path='models/notification.py'):
            errors = pycodestyle.Checker('models/notification.py').check_all()
            self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(models.notification.__doc__, None,
                         "models/notification.py needs a docstring")
        self.assertTrue(len(models.notification.__doc__) > 1,
                        "models/notification.py needs a docstring")

    def test_class_docstring(self):
        """Test for the Notification class docstring"""
        self.assertIsNot(Notification.__doc__, None,
                         "Notification class needs a docstring")
        self.assertTrue(len(Notification.__doc__) >= 1,
                        "Notification class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in Notification methods"""
        for func in self.notification_funcs:
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


class TestNotification(unittest.TestCase):
    """Test the Notification class"""

    def test_instantiation(self):
        """Test that a Notification object is correctly created"""
        notification = Notification()
        self.assertIs(type(notification), Notification)
        notification.volunteer_id = "volunteer-uuid"
        notification.message = "You have a new message"
        notification.status = "unread"
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "volunteer_id": str,
            "message": str,
            "status": str
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, notification.__dict__)
                self.assertIs(type(notification.__dict__[attr]), typ)
        self.assertEqual(notification.status, "unread")

    @mock.patch('models.storage')
    def test_mark_as_read(self, mock_storage):
        """Test the mark_as_read method"""
        notification = Notification()
        notification.volunteer_id = "volunteer-uuid"
        notification.message = "You have a new message"
        notification.mark_as_read()
        self.assertEqual(notification.status, "read")
        self.assertTrue(mock_storage.save.called)

    @mock.patch('models.storage')
    def test_mark_as_dismissed(self, mock_storage):
        """Test the mark_as_dismissed method"""
        notification = Notification()
        notification.volunteer_id = "volunteer-uuid"
        notification.message = "You have a new message"
        notification.mark_as_dismissed()
        self.assertEqual(notification.status, "dismissed")
        self.assertTrue(mock_storage.save.called)