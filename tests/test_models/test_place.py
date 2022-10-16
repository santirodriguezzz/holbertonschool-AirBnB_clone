#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.place import Place


class Place_Tests(unittest.TestCase):
    """tests attributes from Place class"""

    def test_attributes(self):
        newPlace = Place()
        self.assertEquals(newPlace.__class__.__name__, "Place")

    def test_1(self):
        newPlace = Place()
        self.assertEqual(type(newPlace.city_id), str)
        self.assertEqual(type(newPlace.user_id), str)
        self.assertEqual(type(newPlace.name), str)
        self.assertEqual(type(newPlace.description), str)
        self.assertEqual(type(newPlace.number_rooms), int)
        self.assertEqual(type(newPlace.number_bathrooms), int)
        self.assertEqual(type(newPlace.price_by_night), int)
        self.assertEqual(type(newPlace.latitude), float)
        self.assertEqual(type(newPlace.longitude), float)
        self.assertEqual(type(newPlace.amenity_ids), list)
