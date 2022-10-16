"""python interpreter"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


class State_Tests(unittest.TestCase):
    """tests attributes from state class"""

    def test_attributes(self):
        newState = State()
        self.assertEquals(newState.__class__.__name__, "State")

    def test_1(self):
        newState = State()
        self.assertEqual(type(newState.name), str)
