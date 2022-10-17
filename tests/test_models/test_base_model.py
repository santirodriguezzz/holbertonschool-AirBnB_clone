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
        """set up new basemodel"""
        self.base = BaseModel()

    def test1(self):
        """test 1"""
        self.assertEqual(type(self.base.id), str, [])
        self.assertEqual(type(self.base.created_at), datetime.datetime)
        self.assertEqual(type(self.base.updated_at), datetime.datetime)

    def test_initt(self):
        """tests init"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save(self):
        """tests save"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)



if __name__ == '__main__':
    unittest.main()
