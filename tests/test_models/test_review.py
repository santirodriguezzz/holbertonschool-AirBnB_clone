#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.review import Review


class Review_Tests(unittest.TestCase):
    """tests attributes from Review class"""

    def test_attributes(self):
        newReview = Review()
        self.assertEquals(newReview.__class__.__name__, "Review")

    def test_1(self):
        newReview = Review()
        self.assertEqual(type(newReview.place_id), str)
        self.assertEqual(type(newReview.user_id), str)
        self.assertEqual(type(newReview.text), str)
