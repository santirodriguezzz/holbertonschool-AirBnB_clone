#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import datetime


class Base_Model_Tests(unittest.TestCase):
    """test attrubute """

    def setUp(self):
        base0 = BaseModel()
    def test_attributes(self):
        """check attributes"""
        self.assertEqual(type(base0.id), str, [])
        self.assertEqual(type(base0.created_at), datetime.datetime)
        self.assertEqual(type(base0.updated_at), datetime.datetime)

    def test_initt(self):
        """tests init"""
        self.assertTrue(isinstance(self.base0, BaseModel))

    def test_save(self):
        """tests save"""
        self.base0.save()
        self.assertNotEqual(self.base0.created_at, self.base0.updated_at)


if __name__ == '__main__':
    unittest.main()
