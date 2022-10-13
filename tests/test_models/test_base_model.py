#!/usr/bin/python3
"""python interpreter"""
import unittest
import models
import datetime


class Base_Model_Tests(unittest.TestCase):
    """test attrubute """

    def test_attributes(self):
        """check attributes"""
        base0 = BaseModel()

        self.assertEqual(type(base0.id), str, [])
        self.assertEqual(type(base0.created_at), datetime)
        self.assertEqual(type(base0.updated_at), datetime)

    def file_storage(Self):
        """tests file storage methods"""
        file1 = FileStorage()