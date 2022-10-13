#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import datetime


class Base_Model_Tests(unittest.TestCase):
    """test attrubute """

    def test_attributes(self):
        """check attributes"""
        base0 = BaseModel()

        self.assertEqual(type(base0.id), str, [])
        self.assertEqual(type(base0.created_at), datetime)
        self.assertEqual(type(base0.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()
