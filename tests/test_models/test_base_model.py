#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.base_model import BaseModel
import datetime


class Base_Model_Tests(unittest.TestCase):
    """test attrubute """

    def test_attributes(self):
        """check attributes"""
        base0 = BaseModel()

        self.assertEqual(type(base0.id), str, [])
        self.assertEqual(type(base0.created_at), datetime)
        self.assertEqual(type(base0.updated_at), datetime)

class File_Storage_Tests(unittest.TestCase):
    """tests file storage file"""

    def test0(self):
        """tests file storage methods"""
        file1 = FileStorage()

        self.assertEqual(file1.all(), {})

if __name__ == '__main__':
    unittest.main()
