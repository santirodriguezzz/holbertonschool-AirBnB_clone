#!/usr/bin/python3
"""testing"""
import unittest
from models import storage
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class File_Storage_Tests(unittest.TestCase):
    """tests file storage file"""

    def test__FilePath(self):
        """tests attr file_path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test__Obj(self):
        """tests attr obj"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        """tests method all"""
        dictionary = storage.all()
        self.assertEqual(type(dictionary), dict)

    def test_new(self):
        """tests method new"""
        newobj = storage.all().copy()
        storage.new(BaseModel())
        self.assertNotEqual(newobj, storage.all())

    def test_reload(self):
        """tests reload"""
        self.assertRaises(FileNotFoundError, models.storage.reload())
