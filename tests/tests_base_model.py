#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.base_model import BaseModel 
from datetime import datetime


class Base_Model_Tests(unittest.TestCase):
    """test attrubute """

    def test_attributes(self):
        """check attributes"""
        base0 = BaseModel()

        self.assertEqual(type(base0.id), str)