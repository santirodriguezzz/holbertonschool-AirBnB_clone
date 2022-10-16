#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.amenity import Amenity


class Amenity_Tests(unittest.TestCase):
    """tests attributes from Amenity class"""

    def test_attributes(self):
        newAmenity = Amenity()
        self.assertEquals(newAmenity.__class__.__name__, "Amenity")

    def test_1(self):
        newAmenity = Amenity()
        self.assertEqual(type(newAmenity.name), str)
