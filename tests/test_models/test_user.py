#!/usr/bin/python3
"""testing"""
import unittest
from models import storage
import models
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class User_Test(unittest.TestCase):
    """tests user"""

    def test_0(self):
        newUser = User()
        self.assertEquals(newUser.__class__.__name__, "User")

    def test_1(self):
        newUser = User()
        self.assertEqual(type(newUser.email), str)
        self.assertEqual(type(newUser.password), str)
        self.assertEqual(type(newUser.first_name), str)
        self.assertEqual(type(newUser.last_name), str)
