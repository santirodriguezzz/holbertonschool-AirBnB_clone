#!/usr/bin/python3
"""python interpreter"""
import unittest
# from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
from models.city import City


class City_Tests(unittest.TestCase):
    """tests attributes from city class"""

    def test_attributes(self):
        newCity = City()
        self.assertEquals(newCity.__class.__name__, "City")

    def test_1(self):
        newCity = City()
        self.assertEqual(type(newCity.name), str)
